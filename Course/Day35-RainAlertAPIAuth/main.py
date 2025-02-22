import requests
from twilio.rest import Client

api_key = ""
account_sid = ""
auth_token = ""


parameters = {
    "lat": 49.234669,
    "lon": -124.807587,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]
will_rain = False

for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain. Bring an Umbrella",
        from_="whatsapp:+14155238886",
        to="whatsapp:+",
    )
    print(message.status)
