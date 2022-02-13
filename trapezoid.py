import numpy as np
import scipy 

class Trapezoid:
    def __init__(self, x1, x2, yl, ymid, yr):
        self.x1 = x1
        self.x2 = x2
        self.yl = yl
        self.ymid = ymid
        self.yr = yr

    def calc(self, x: float) -> float:
        if x < self.x1:
            return self.ymid + (x - self.x1) * (self.ymid - self.yl) / (self.x1 + 100)
        elif x > self.x2:
            return self.ymid + (x - self.x2) * (self.yr - self.ymid) / (100 - self.x2)
        else:
            return self.ymid

def learn_trapezoid(xs, ys, yerrs):
    xs = np.array(xs)
    ys = np.array(ys)
    assert(len(xs) == len(ys))
    mean = np.mean(ys)
    x0 = [-75, 75, mean, mean, mean]

    def helper(x):
        trap = Trapezoid(*x)
        errs = [(ys[i] - trap.calc(xs[i])) for i in range(len(xs))]
        retval = np.square(errs).sum()

        too_far_penalty = 0
        too_far_penalty += max(0, -x[0] - 90)*100
        too_far_penalty += max(0, x[1] - 90)*100
        return retval + too_far_penalty

    return Trapezoid(*scipy.optimize.minimize(helper, x0).x)