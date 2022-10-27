import requests
import pandas
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY1 = "EW4VQ380ZJHR9WJD"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# getting yesterday's price
url1 = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK}&interval=5min&apikey={API_KEY1}"
r1 = requests.get(url1)
r1.raise_for_status()
stock_data1 = r1.json()
today = datetime.today()
yesterday = (today - timedelta(days=1))
yesterday = str(yesterday).split(" ")[0]

yest_price = float(stock_data1["Time Series (5min)"]
                   [f"{yesterday} 16:00:00"]["4. close"])


# getting today's price
url2 = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={STOCK}&interval=15min&slice=year1month1&apikey={API_KEY1}"
with requests.Session() as s:
    download = s.get(url2).content
    stock_data2 = pandas.read_csv(url2)
    print(stock_data2)


# today = str(today).split(" ")[0]

# yest_price = float(stock_data2["Time Series (15min)"]
#                    [f"{today} 9:00:00"]["1. open"])


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


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
