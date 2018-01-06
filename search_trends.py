#coding:utf-8

from pytrends.request import TrendReq

pytrend = TrendReq(hl='en-US', tz=360)
pytrend.build_payload(kw_list, timeframe='today 5-y', geo='800')



kw_list = ["tax",'entrepreneur']

interest_over_time_df = pytrend.interest_over_time()
interest_over_time_df.to_csv('800.csv')