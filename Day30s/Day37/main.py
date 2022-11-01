from tokenize import Token
import requests
import json
from datetime import datetime

USER_TOKEN = "sadfpokqwe12563poi"
USERNAME = "zhoujiawang"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": USER_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# creating user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": USER_TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Days",
    "type": "int",
    "color": "momiji"
}

# creating graph
# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

optionalData = {
    "language": "Python",
    "duration": "1 hour",
    "day": "37"
}

add_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

pixel_config = {
    "date": "20221030",
    "quantity": "1",
    "optionalData": json.dumps(optionalData)
}

# creating pixel
# response = requests.post(url=add_pixel_endpoint,
#                          json=pixel_config, headers=headers)
# print(response.text)

pixel_config2 = {
    "quantity": "100"
}

today = datetime.now().strftime("%Y%m%d")

mod_pixela_endpoint = f"{add_pixel_endpoint}/{today}"

response = requests.delete(url=mod_pixela_endpoint, headers=headers)
print(response.text)
