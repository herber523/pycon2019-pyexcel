import pandas as pd
from itertools import islice

def convert_ws_df(ws, keep_formula):
    df = None
    data = ws.values
    if keep_formula:
        cols = next(data)
        data = list(data)
        data = (islice(r, 0, None) for r in data)
        df = pd.DataFrame(data, columns=cols)
    else:
        df = pd.DataFrame(data)
        
    return df


def refresh_pv(ws):
    pivot = ws._pivots[0]
    pivot.cache.refreshOnload = True

