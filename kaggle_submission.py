import pandas as pd
from algorithm import *

if __name__ == "__main__":
    df = pd.read_csv("split/test.csv")

    df_cp = pd.read_csv("test_counterparty.csv")
    df_sm = pd.read_csv("test_sentiment.csv")

    df.cp_naive = df_cp.counterparty.values
    df.sm_naive = df_sm['sm sentiment'].values

    # result = pd.DataFrame([], columns=['trade id', 'pred edge']).set_index('trade id')
    results = {}
    for idx, row in df.iterrows():
        if idx % 1000 == 0:
            print(f"{idx} / {len(df)}")
        pred_edge = algorithm(row.pred_edge, row.stk, row.xchg, row.px, row.sz, row.dir, row.cp_naive, row.sm_naive)
        # result.loc[idx] = {'pred edge': pred_edge}
        results[idx] = pred_edge

    df = pd.DataFrame.from_dict(results, orient='index', columns=['realized edge'])
    df.index = df.index.rename('trade id')
    df.to_csv("kaggle.csv")