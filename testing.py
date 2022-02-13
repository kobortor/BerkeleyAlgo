import pandas as pd
from submodels import trapezoids

def retail_algorithm(pred_edge: float, stk: str, xchg: str, px: float, sz: int, dir: str, sm_naive: float) -> bool:
    trap = trapezoids[(xchg, stk)]

    real_pred_edge = pred_edge + trap.calc(sm_naive)
    if real_pred_edge > 0:
        return True
    else:
        return False

def algorithm(pred_edge: float, stk: str, xchg: str, px: float, sz: int, dir: str, cp_naive: str, sm_naive: float) -> bool:
    if cp_naive != 'R':
        return False
    
    return retail_algorithm(pred_edge, stk, xchg, px, sz, dir, sm_naive)

def yes_algorithm(pred_edge: float, stk: str, xchg: str, px: float, sz: int, dir: str, cp_naive: str, sm_naive: float) -> bool:
    return True

dev_df = None
def test_algo_pnl(algo, cp_naive: bool = True, sm_naive: bool = True) -> float:
    global dev_df
    if dev_df is None:
        dev_df = pd.read_csv("dev.csv")

    pnl = 0
    for _, row in dev_df.iterrows():
        cp = row.cp_naive if cp_naive else row.cp
        sm = row.sm_naive if sm_naive else row.sm
        if algo(row.pred_edge, row.stk, row.xchg, row.px, row.sz, row.dir, cp, sm):
            pnl += row.pnl

    return pnl

print(test_algo_pnl(yes_algorithm))
print(test_algo_pnl(algorithm, False, False))
print(test_algo_pnl(algorithm, False, True))
print(test_algo_pnl(algorithm, True, False))
print(test_algo_pnl(algorithm, True, True))