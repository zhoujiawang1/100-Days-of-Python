from symbol import parameters
from urllib import response
import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351
MY_LONG = -0.157758

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

# ISS


def iss_overhead():
    response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
    response1.raise_for_status()
    data1 = response1.json()
    lat = float(data1["iss_position"]["latitude"])
    long = float(data1["iss_position"]["longtitude"])

    if MY_LAT - 5 <= lat <= MY_LAT+5 and MY_LONG - 5 <= long <= MY_LONG+5:
        return True
    return False


def is_night():
    response = requests.get(
        url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    sunrise = int(sunrise.split("T")[1].split(":")[0])
    sunset = int(sunset.split("T")[1].split(":")[0])

    time_now = datetime.now().split(" ")[1].split(":")[0]

    if sunset < time_now or time_now < sunrise:
        return True
    return False


if is_night() and iss_overhead():
    connection = smtplib.SMTP("smtp.outlook.com")
    connection.starttls()
    connection.login(user="topjeutony@hotmail.fr", password="Lawlxd12345")
    connection.send_message(
        from_addr="topjeutony@hotmail.fr",
        to_addrs="topjeutony@hotmail.fr",
        msg="Subject:Look Up!\n\nThe ISS is overhead!"
    )
