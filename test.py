import pandas as pd
link = "https://en.wikipedia.org/wiki/Boxing_pound_for_pound_rankings"
link = "https://en.wikipedia.org/wiki/Wikipedia:List_of_Wikipedians_by_number_of_edits"
link = "https://stats.wikimedia.org/EN/TablesWikipediaEN.htm"
link = "https://en.m.wikipedia.org/wiki/List_of_masters_world_records_in_road_running"
dfw = pd.read_html(link)
print(len(dfw))
print(dfw[0])