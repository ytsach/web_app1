import pandas as pd


def get_relevant_data_compare(dataf):
    df = pd.DataFrame(dataf)
    return df.drop(columns=['Player','Pos','Age','Tm','PF'])