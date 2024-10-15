import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv("C:/Users/peter/EnvironmentVariables/.env")
# Longitude and latitude location info
CELJE_LAT = 46.239750
CELJE_LON = 15.267706
BRUSEL_LAT = 50.850346
BRUSSEL_LON = 4.351721

# openweather my API key, API endpoint, requesting data from openweather
API_KEY = os.getenv("OWM_API_KEY")

parameters = {
    "lat": 40.030499,
    "lon": -6.088250,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
data = data["list"]

# Twilio client setup
account_sid = "ACb14275426dc74749c9ee664cde21912c"
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

# geting the information I need, in this case if it will rain in the next 12 hours.
rain = False
for item in data:
    if item["weather"][0]["id"] < 601:
        rain = True
        print(item["weather"][0]["description"])
if rain:
    print("Bring an umbrella!")
    message = client.messages.create(
        body="It will rain sometime in the next 12 hours! Bring an umbrella ☂️!",
        from_="+12028048453",
        to="ENTERPHONENUMBER",
    )

    print(message.status)

else:
    print("No rain!")
