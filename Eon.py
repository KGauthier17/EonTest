from pytrends.request import TrendReq
import pandas as pd
import pathlib


pytrend = TrendReq(hl='en-GB', tz=360)
dataset = []

keywords = ["bitcoin"]
pytrend.build_payload(
kw_list=keywords,
cat=0,
timeframe='2015-01-01 2022-09-13',
geo='GB')
data = pytrend.interest_over_time()
if not data.empty:
    data = data.drop(labels=['isPartial'],axis='columns')
    dataset.append(data)

result = pd.concat(dataset, axis=1)
p = str(pathlib.Path(__file__).parent.resolve()) + "/search_trends.csv"
result.to_csv(p)
