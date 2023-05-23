import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
my_phone = os.environ.get("MY_PHONE")
her_phone = os.environ.get("HER_PHONE")
owm_phone = os.environ.get("OWM_PHONE")

#LAT/LONG set for a specific location (Palm Harbor, FL)
weather_params = {
    "appid": api_key,
    "lat": 	28.078072,
    "lon": -82.763710,
    "exclude": "current,minutely,daily"
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

### My version without slicing
rain = False
for x in range(12):
    weather = weather_data["hourly"][x]["weather"][0]["id"]
    if weather < 700:
        rain = True

if rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain in the next 12 hours in Palm Harbor, FL! Hugs and kisses, bring an umbrella ☂️",
        from_=owm_phone,
        to=my_phone,
    )
    message2 = client.messages \
        .create(
        body="It's going to rain in the next 12 hours in Palm Harbor, FL! Hugs and kisses, bring an umbrella ☂️",
        from_=owm_phone,
        to=her_phone,
    )

    print(message.status)
    print(message2.status)
