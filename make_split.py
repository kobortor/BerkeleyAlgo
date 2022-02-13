import pandas as pd
import numpy as np

if __name__ == "__main__":
    df_all = pd.read_csv('raw/train.csv')
    train_mask = (np.random.random(len(df_all)) < 0.9)
    df_all[train_mask].to_csv('split/train.csv')
    df_all[~train_mask].to_csv('split/dev.csv')

    df_test = pd.read_csv('raw/test.csv')
    df_test.to_csv('split/test.csv')
else:
    raise Exception("Only call this in main!")