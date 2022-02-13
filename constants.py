import itertools 
# CONSTANTS

# This way we type far less, and you can do something like `df_train.real_edge`
# whereas before you cannot do `df_train.realized edge`
name_remap = {
    "trade id": "id",
    "pred edge": "pred_edge",
    "stock": "stk",
    "location": "xchg",  # Not naming `loc` because it's used for something else
    "price": "px",
    "size": "sz",
    "dir": "dir",

    "counterparty": "cp",
    "counterparty (naive)": "cp_naive",
    "sm sentiment": "sm",
    "sm sentiment (naive)": "sm_naive",

    "realized edge": "real_edge",
    "pnl": "pnl"
}

# Lists you can iterate over
exchanges = ["CSE", "NYSE", "NASDAQ"]
stocks = ["A", "B", "C", "D"]
parties = ["HF", "R", "MF"]  # Hedge Fund, Retail, Mutual Fund

intern_error_rate = 0.4
party_probs = {"HF": 0.2, "R": 0.35, "MF": 0.45}

real_probs_given = {}
for x, y in itertools.product(parties, repeat=2):
    if x == y:
        real_probs_given[(x, y)] = (party_probs[x] * ((1 - intern_error_rate) + intern_error_rate * party_probs[y])) / party_probs[y]
    else:
        real_probs_given[(x, y)] = (party_probs[x] * intern_error_rate * party_probs[y]) / party_probs[y]