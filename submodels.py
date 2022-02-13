from typing import *
from constants import *
import pandas as pd

from trapezoid import Trapezoid

def load_trapezoids() -> Dict[Tuple[str, str, str], Trapezoid]:
    traps = {}

    loaded = pd.read_csv("trapezoids.csv")

    for xchg, stk, drct in itertools.product(exchanges, stocks, directions):
        rows = loaded[(loaded.xchg == xchg) & (loaded.stk == stk) & (loaded.dir == drct)]
        if len(rows) != 1:
            raise Exception()

        row = rows.iloc[0]
        traps[(xchg, stk, drct)] = Trapezoid(row.x1, row.x2, row.yl, row.ymid, row.yr)        
    
    return traps

trapezoids = load_trapezoids()
retail_lines = pd.read_csv("retail_line.csv").set_index(['xchg', 'stk', 'dir']).to_dict()
mutual_fund_lines = pd.read_csv("mutual_fund_lines.csv").set_index(['xchg', 'stk']).to_dict()
hedge_fund_lines = pd.read_csv("hedge_fund_lines.csv").set_index(['xchg', 'stk']).to_dict()