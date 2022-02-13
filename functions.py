import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def bin_helper(xs, ys, nbins: int = 10):
    assert(isinstance(xs, pd.Series))
    assert(isinstance(ys, pd.Series))
    assert(len(xs) == len(ys))

    N = len(xs)

    argsort = xs.rank() // ((N + nbins - 1) // nbins)

    x_points = xs.groupby(argsort).mean()
    y_points = ys.groupby(argsort).mean()
    y_errs = ys.groupby(argsort).std() / np.sqrt(ys.groupby(argsort).count()) * 2

    return x_points, y_points, y_errs


def binned_plot(xs: pd.Series, ys: pd.Series, nbins: int = 10, ax = None):
    xs = pd.Series(xs)
    ys = pd.Series(ys)
    
    if ax is None:
        ax = plt.gca()

    x_points, y_points, y_errs = bin_helper(xs, ys, nbins)
    ax.errorbar(x_points, y_points, y_errs)