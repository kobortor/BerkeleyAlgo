from submodels import *

def retail_algorithm(pred_edge: float, stk: str, xchg: str, px: float, sz: int, dir: str, sm_naive: float) -> bool:
    trap = trapezoids[(xchg, stk, dir)]

    real_pred_edge = pred_edge + trap.calc(sm_naive)

    offset = retail_lines['offset'][(xchg, stk, dir)]
    slope = retail_lines['slope'][(xchg, stk, dir)]

    real_pred_edge += sz * slope + offset
    return real_pred_edge

def mutual_fund_algorithm(pred_edge: float, stk: str, xchg: str, px: float, sz: int, dir: str, sm_naive: float) -> bool:
    if sz == 8 and stk == "D":
        if xchg == "CSE":
            return pred_edge - 22
        else:
            return pred_edge - 17.5

    pred_edge_slope = mutual_fund_lines['pred_edge_slope'][(xchg, stk)]
    px_slope = mutual_fund_lines['px_slope'][(xchg, stk)]
    sz_slope = mutual_fund_lines['sz_slope'][(xchg, stk)]
    # sm_slope = mutual_fund_lines['sm_slope'][(xchg, stk)]
    offset = mutual_fund_lines['offset'][(xchg, stk)]
    real_pred_edge = pred_edge
    real_pred_edge += pred_edge * pred_edge_slope
    real_pred_edge += px * px_slope
    real_pred_edge += sz * sz_slope
    # real_pred_edge += sm_naive * sm_slope
    real_pred_edge += offset

    return real_pred_edge

def hedge_fund_algorithm(pred_edge: float, stk: str, xchg: str, px: float, sz: int, dir: str, sm_naive: float) -> bool:
    if sz == 2000 and stk == "C":
        if xchg == "CSE":
            return pred_edge - 27
        else:
            return pred_edge - 22
        
    if sz == 450 and stk == "A":
        if xchg == "CSE":
            return pred_edge - 27
        else:
            return pred_edge - 22
        
    pred_edge_slope = hedge_fund_lines['pred_edge_slope'][(xchg, stk)]
    px_slope = hedge_fund_lines['px_slope'][(xchg, stk)]
    sz_slope = hedge_fund_lines['sz_slope'][(xchg, stk)]
    # sm_slope = hedge_fund_lines['sm_slope'][(xchg, stk)]
    offset = hedge_fund_lines['offset'][(xchg, stk)]
    real_pred_edge = pred_edge
    real_pred_edge += pred_edge * pred_edge_slope
    real_pred_edge += px * px_slope
    real_pred_edge += sz * sz_slope
    # real_pred_edge += sm_naive * sm_slope
    real_pred_edge += offset

    return real_pred_edge


def algorithm(pred_edge: float, stk: str, xchg: str, px: float, sz: int, dir: str, cp_naive: str, sm_naive: float) -> bool:
    if cp_naive == 'R':
        return retail_algorithm(pred_edge, stk, xchg, px, sz, dir, sm_naive)
    elif cp_naive == 'MF':
        return mutual_fund_algorithm(pred_edge, stk, xchg, px, sz, dir, sm_naive)
    else:
        return hedge_fund_algorithm(pred_edge, stk, xchg, px, sz, dir, sm_naive)

def binary_algorithm(pred_edge: float, stk: str, xchg: str, px: float, sz: int, dir: str, cp_naive: str, sm_naive: float) -> bool:
    return algorithm(pred_edge, stk, xchg, px, sz, dir, cp_naive, sm_naive) > 0