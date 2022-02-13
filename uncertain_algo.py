import numpy as np
from typing import *
from constants import *

# returns the probability that the algorithm will return true
def make_uncertain(
        normal_algo: Callable[[float, str, str, float, int, str, str, float], bool], 
        pred_edge: float, stk: str, xchg: str, px: float, sz: int, dir: str, cp_naive: str, sm_naive: float, ls_cnt: int = 100) -> float:

    yes_total = 0.0
    weight_total = 0.0

    for cp_real in parties:
        for sm_real in np.linspace(-100, 100, ls_cnt):
            wt = real_probs_given[(cp_real, cp_naive)] * intern_error_rate / ls_cnt

            weight_total += wt
            if normal_algo(pred_edge, stk, xchg, px, sz, dir, cp_real, sm_real):
                yes_total += wt
        
        wt = real_probs_given[(cp_real, cp_naive)] * (1 - intern_error_rate)
        weight_total += wt

        if normal_algo(pred_edge, stk, xchg, px, sz, dir, cp_real, sm_naive):
            yes_total += wt
        
    return yes_total / weight_total

