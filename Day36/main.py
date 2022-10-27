import requests
import pandas
from datetime import datetime, timedelta
from newsapi import NewsApiClient
import html

STOCK = "BITO"
COMPANY_NAME = "Tesla Inc"
API_KEY1 = "EW4VQ380ZJHR9WJD"
API_KEY2 = "54da6dce5a454b889681940d67349ff0"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# getting yesterday's price
url1 = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK}&interval=30min&apikey={API_KEY1}"
r1 = requests.get(url1)
r1.raise_for_status()
stock_data1 = r1.json()
today = datetime.today()
day_open = (today - timedelta(days=1))

day_open = str(day_open).split(" ")[0]

today_price = float(stock_data1["Time Series (30min)"]
                    [f"{day_open} 09:30:00"]["1. open"])
print(f"Current Bitcoin {STOCK} Price Open: {today_price}")

# getting today's price
url2 = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={STOCK}&interval=15min&slice=year1month1&apikey={API_KEY1}"

prev_day_close = (today - timedelta(days=2))
prev_day_close = str(prev_day_close).split(" ")[0]
with requests.Session() as s:
    download = s.get(url2).content
    stock_data2 = pandas.read_csv(url2)
    yest_price = float(stock_data2.loc[stock_data2['time']
                                       == f"{prev_day_close} 16:00:00"]["close"].values[0])
    print(f"Yesterday's Close {STOCK} Price: {yest_price}")

if abs((today_price-yest_price)/yest_price) >= 0.05:
    print("Get NEWS")

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


# Init
newsapi = NewsApiClient(api_key=API_KEY2)

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q="Tesla",
                                          language='en'
                                          )
all_articles = newsapi.get_everything(q="bitcoin",
                                      from_param=day_open,
                                      to=day_open,
                                      language='en',
                                      sort_by='popularity',
                                      page=1)


titles = []
descriptions = []
# print(top_headlines)
for num_article in range(2):
    title = all_articles["articles"][num_article]["title"]
    desc = all_articles["articles"][num_article]["description"]
    # titles.append(title)
    # descriptions.append(desc)
    print(f"Headline: {title}\nDescription: {html.unescape(desc)}")


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
