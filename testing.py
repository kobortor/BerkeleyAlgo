import pandas as pd
from submodels import *
from uncertain_algo import *

from algorithm import *

def yes_algorithm(pred_edge: float, stk: str, xchg: str, px: float, sz: int, dir: str, cp_naive: str, sm_naive: float) -> bool:
    return True

dev_df = None
def test_algo_pnl(algo, cp_naive: bool = True, sm_naive: bool = True) -> float:
    global dev_df
    if dev_df is None:
        dev_df = pd.read_csv("split/dev.csv")

    pnl = 0
    for _, row in dev_df.iterrows():
        cp = row.cp_naive if cp_naive else row.cp
        sm = row.sm_naive if sm_naive else row.sm
        if algo(row.pred_edge, row.stk, row.xchg, row.px, row.sz, row.dir, cp, sm):
            pnl += row.pnl

    return pnl

def test_algo_uncertain(algo, cp_naive: bool = True, sm_naive: bool = True) -> float:
    global dev_df
    if dev_df is None:
        dev_df = pd.read_csv("split/dev.csv")

    pr_pnls = []
    for i, row in dev_df.iterrows():
        if i % 1000 == 0:
            print("{} / {}".format(i, len(dev_df)))
        cp = row.cp_naive if cp_naive else row.cp
        sm = row.sm_naive if sm_naive else row.sm
        pr_exec = make_uncertain(algo, row.pred_edge, row.stk, row.xchg, row.px, row.sz, row.dir, cp, sm, ls_cnt=1000)
        pr_pnls.append((pr_exec, row.pnl))

    return pr_pnls

"""
pr_pnls = list(sorted(test_algo_uncertain(binary_algorithm)))
prs = [pr for (pr, pnl) in pr_pnls]
pnls = [pnl for (pr, pnl) in pr_pnls]

import matplotlib.pyplot as plt
plt.plot(prs, np.cumsum(pnls[::-1])[::-1])
plt.show()
"""

print(test_algo_pnl(yes_algorithm))
print(test_algo_pnl(binary_algorithm, False, False))
print(test_algo_pnl(binary_algorithm, False, True))
print(test_algo_pnl(binary_algorithm, True, False))
print(test_algo_pnl(binary_algorithm, True, True))