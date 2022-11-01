import requests
from datetime import datetime
from twilio.rest import Client

API_KEY = "bd1d598397285ba0ac44437390b7ea3c"
MY_LAT = 45.5031824
MY_LONG = -73.5698065
AUTH_TOKEN = "936429a4725bfcf075efa52947da5226"
ACC_SID = "AC06d7be443edfe6733cc71a105e6af89c"
TWILIO_PHONE = "+16614435928"

# response1 = requests.get(
#     url=f"http://api.openweathermap.org/geo/1.0/direct?q=Montreal,Quebec,Canada&limit={2}&appid={API_KEY}")
# response1.raise_for_status()
# # print(response1.json())


parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "appid": API_KEY
}

# getting API
response = requests.get(
    url=f"https://api.openweathermap.org/data/2.5/weather?lat={MY_LAT}&lon={MY_LONG}&appid={API_KEY}", params=parameters)
response.raise_for_status()

# retrieving data
data = response.json()
print(data["weather"][0]["id"])
weather_id = data["weather"][0]["id"]

# getting time
time_now = datetime.now().hour
print(time_now)

# verifying condition and sending text if rain
if weather_id < 700 and time_now == 7:
    client = Client(ACC_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain. Bring an umbrella ☔!",
        from_=TWILIO_PHONE,
        to="+15146381668"
    )
    print(message.sid, message.status)
