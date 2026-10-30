import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:

    # return pd.concat([df1, df2], ignore_index = True)
    # return pd.concat([df1, df2], axis=0)
    # return pd.merge(df1, df2, how='outer')
    # return df1.merge(df2, how='outer')
    return df1._append(df2)