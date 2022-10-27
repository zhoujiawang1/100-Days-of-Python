import smtplib
import datetime as dt
import pandas
from random import choice
# credentials
my_email = "topjeutony@hotmail.fr"
password = "Lawlxd12345!"

email = []

# text for letter
letters = [1, 2, 3]
file_letter = open(
    f"Day30s/Day32/letter_templates/letter_{choice(letters)}.txt")
letter = file_letter.read()

# get day and month
day = dt.datetime.now().day
month = dt.datetime.now().month


data_bd = pandas.read_csv("Day30s/Day32/birthdays.csv")
name = []

for (index, row) in data_bd.iterrows():
    print(row)
    temp = row["name"]
    if int(row.month) == month and int(row.day) == day:

        name.append(temp)
        email.append(row.email)


print(name, email)
letter = letter.replace("[NAME]", name[0])
print(letter)

with smtplib.SMTP("smtp.outlook.com", port=587) as connection:
    connection.starttls()  # makes connection secured
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=email[0],
                        msg=f"Subject: Happy Birthday\n\n{letter}"
                        )
