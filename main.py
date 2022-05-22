import requests

from twilio.rest import Client   # install, client is a class



API_KEY =  os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("sid")
auth_token = os.environ.get("AUTH_TOKEN")
MY_LAT = 10.56
MY_LONG = 78.48

parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "exclude" : "current,minutely,daily,alerts",
    "appid" : API_KEY
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
print(data["timezone"])
will_rain = False
# TODO extracting weather_Code for next 12 hours so range(0,12)
for i in range(0,12):
    weather_condition = data["hourly"][i]["weather"][0]["id"]
    if weather_condition < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Today Its gonna Rain...Grab an Umbrella",
        from_=from_num,
        to=to_num
    )

    print(message.status)
