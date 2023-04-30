import pandas as pd
link = "https://en.wikipedia.org/wiki/Boxing_pound_for_pound_rankings"
dfw = pd.read_html(link)
print(len(dfw))
dfw[0].head(10)