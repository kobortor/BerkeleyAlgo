from typing import *
from constants import *
import pandas as pd

from trapezoid import Trapezoid

def load_trapezoids() -> Dict[Tuple[str, str], Trapezoid]:
    traps = {}

    loaded = pd.read_csv("trapezoids.csv")

    for xchg, stk in itertools.product(exchanges, stocks):
        rows = loaded[(loaded.xchg == xchg) & (loaded.stk == stk)]
        if len(rows) != 1:
            raise Exception()

        row = rows.iloc[0]
        traps[(xchg, stk)] = Trapezoid(row.x1, row.x2, row.yl, row.ymid, row.yr)        
    
    return traps

trapezoids = load_trapezoids()