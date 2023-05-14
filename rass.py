import matplotlib.pyplot as plt
# import pandas as pd

# Постоение распределения
def rasse(df, x1, y1):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x=df[x1], y=df[y1])
    plt.xlabel(x1)
    plt.ylabel(y1)
    plt.show()
