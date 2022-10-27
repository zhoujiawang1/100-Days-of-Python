import smtplib
import getpass
import datetime as dt
from random import choice

my_email = "topjeutony@hotmail.fr"
password = "Lawlxd12345!"
# password = getpass.getpass("Password: ")

with open("Day30s/Day32/quotes.txt", "r") as file:
    lines = file.readlines()
    quotes = []
    for line in lines:
        quotes.append(line)


if dt.datetime.now().weekday() == 0:
    with smtplib.SMTP("smtp.outlook.com", port=587) as connection:
        connection.starttls()  # makes connection secured
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="zhoujiawang1@gmail.com",
                            msg=f"Subject:Inspirational Quote of the Week\n\n.{choice(quotes)}"
                            )
