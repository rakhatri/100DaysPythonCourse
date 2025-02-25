import requests
import datetime

STOCK = "BRK-B"
COMPANY_NAME = "Berkshire Hathaway Inc."
STOCK_API_KEY = ""
NEWS_API_KEY = ""

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()
current_date = datetime.datetime.now().date()
prev_date = datetime.datetime.now().date() - datetime.timedelta(3)

current_date_stock_price = float(stock_response.json()["Time Series (Daily)"][str(current_date)]["4. close"])
prev_date_stock_price = float(stock_response.json()["Time Series (Daily)"][str(prev_date)]["4. close"])
percentage_change = round(((current_date_stock_price - prev_date_stock_price) / current_date_stock_price) * 100, 2)
if abs(percentage_change) > 2.5:
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    news_parameters = {
        "q": STOCK,
        "from": str(prev_date),
        "to": str(current_date),
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    for article in news_response.json()["articles"]:
        print(article["title"])
        print(article["description"])


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

