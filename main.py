import requests

from twilio.rest import Client   # install, client is a class


# TODO Send a sms from twilio
#  get weather report from openweather api
#  get twilio trail account
#  to run in  python anywhere, some changes in code
#  "https://www.udemy.com/course/100-days-of-code/learn/lecture/21326812#questions"

# TODO Environment variables
#  It is shown using "env" in mac or pythonanywhere and "set" in windows
#  export OWM_API_KEY=286ae0ceeb0ecf40cf8866783b83c922 and set OWM_API_LEY=286ae0ceeb0ecf40cf8866783b83c922

API_KEY =  "286ae0ceeb0ecf40cf8866783b83c922" #os.environ.get("OWM_API_KEY")
account_sid = "ACe96dae203aa3443275c0f123e645e3bf"
auth_token = "65e6e653e6e504de8059a14b58214d70" #os.environ.get("AUTH_TOKEN")
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
        from_='+19036627947',
        to='+919952783610'
    )

    print(message.status)