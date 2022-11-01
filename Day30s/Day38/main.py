import requests
import os
from datetime import datetime

api_key = os.environ["API_NUTRI"]
api_id = os.environ["API_ID"]
CONTENT_TYPE = "application/json"

xr6_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": api_id,
    "x-app-key": api_key,
    "Content-Type": CONTENT_TYPE
}

body = {
    "query": input("Tell us what activities you performed: "),
    "gender": "male",
    "weight_kg": 71.2,
    "height_cm": 170,
    "age": 23
}

response = requests.post(url=xr6_endpoint, json=body, headers=headers)
response.raise_for_status()

duration = (response.json())["exercises"][0]["duration_min"]
calories = (response.json())["exercises"][0]["nf_calories"]
activity = response.json()["exercises"][0]["name"]

exercises = response.json()["exercises"]

print(duration, calories, activity)

SHEETY_ENDPOINT = "https://api.sheety.co/36536736de4e7c60b867b15e344d3cbc/copieDeMyWorkouts/workouts"

bearer_headers = {
    "Authorization": "Bearer qwerqwerqwer"}

today = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")

print(today, current_time)

for exercise in exercises:
    body = {"workout":
            {
                "date": today,
                "time": current_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            },

            }

    r2 = requests.post(url=SHEETY_ENDPOINT, json=body, headers=bearer_headers)
    r2.raise_for_status()
    print(r2.text)
