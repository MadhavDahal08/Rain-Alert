import requests
from twilio.rest import Client
import os

API_URL = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "AC448ca51a033720f3e0a040ebc504edd8"
auth_token = os.environ.get("TWILIO_AUTH_KEY")
my_twilio_number = "+18144731588"


PARAMETERS = {
    "lat":  27.42,
    "lon": 85.18,
    "appid": api_key,
    "cnt": 4
}
response = requests.get(url=API_URL, params=PARAMETERS)
weather_data = response.json()["list"]
weather_list = [item["weather"][0] for item in weather_data]
raining_id = [item["id"] for item in weather_list if item["id"] < 700]
will_rain = False
for item in weather_list:
    if item["id"] < 700:
        will_rain = True

if will_rain:

    account_sid = account_sid
    auth_token = auth_token
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring and umbrella.",
        from_='+18144731588',
        to='+9779860911131'
    )
    print(message.status)
