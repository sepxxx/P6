import matplotlib.pyplot as plt
import pandas as pd
def week(df, x1, y1, z1):
    plt.figure()
    dfz = df.copy()
    dfz[z1] = pd.to_datetime(dfz[z1])
    dfz['weekday'] = dfz[z1].dt.day_name()
    if x1 == z1:
        res = dfz.groupby('weekday').aggregate({f'{y1}': 'mean'})
        plt.bar(res.index, res[f'{y1}'])
        plt.show()
    else:
        if y1 == z1:
            res = dfz.groupby('weekday').aggregate({f'{x1}': 'mean'})
            plt.bar(res.index, res[f'{x1}'])
            plt.show()