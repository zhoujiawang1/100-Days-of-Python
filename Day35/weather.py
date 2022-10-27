import requests
from datetime import datetime
from twilio.rest import Client

API_KEY = "bd1d598397285ba0ac44437390b7ea3c"

# response1 = requests.get(
#     url=f"http://api.openweathermap.org/geo/1.0/direct?q=Montreal,Quebec,Canada&limit={2}&appid={API_KEY}")
# response1.raise_for_status()
# # print(response1.json())

MY_LAT = 45.5031824
MY_LONG = -73.5698065


parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "appid": API_KEY
}
response = requests.get(
    url=f"https://api.openweathermap.org/data/2.5/weather?lat={MY_LAT}&lon={MY_LONG}&appid={API_KEY}", params=parameters)
response.raise_for_status()

data = response.json()
print(data["weather"][0]["id"])
weather_id = data["weather"][0]["id"]

bad_weather = []
bad_weather.append(range(500, 532))

time_now = datetime.now().hour
print(time_now)

if weather_id < 700 and time_now == 7:
    print("Its raining! Stay under the umbrella")
