import pandas as pd
import week
import numpy as np
from datetime import datetime, timedelta
#

# def random_dates(start, end, n=10):
#
#     start_u = start.value//10**9
#     end_u = end.value//10**9
#
#     return pd.to_datetime(np.random.randint(start_u, end_u, n), unit='s')
#
# start = pd.to_datetime('2015-01-01')
# end = pd.to_datetime('2018-01-01')



# df = pd.read_csv("newd.csv")
# date_today = datetime.now()
# days = pd.date_range(date_today, date_today + timedelta(int(43)), freq='D')
# df.datetime = days
# # print(df)
# df.info()
# df.to_csv("d.csv")
#
# df = pd.read_csv("d.csv")
# df.info()
# print(df)

df = pd.read_csv("d.csv")
# print(df)
# for col in df:
#     try:
#         print(col)
#         df[f'{col}'] = pd.to_datetime(df[f'{col}'], format="%Y-%m-%d %H:%M:%S.%f")
#         print(df[f'{col}'])
#     except:
#         print("NOOOPE")

week.week(df, "ale", "datetime", "datetime")