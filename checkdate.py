import pandas as pd
def check_date(df):
    flag = 0
    for col in df:
        try:
            df[f'{col}'] = pd.to_datetime(df[f'{col}'], format="%Y-%m-%d %H:%M:%S.%f")
            flag = 1
            return flag, col
        except:
            pass
    return flag, ""