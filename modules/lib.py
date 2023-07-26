import pandas as pd 

def read_csv(path):
    df = pd.read_csv(path)
    return df

def rename_columns(df, columns_dict):
    df = df.rename(columns=columns_dict)
    return df