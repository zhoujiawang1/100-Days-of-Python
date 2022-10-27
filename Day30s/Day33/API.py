from urllib import request
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json#")
response = requests.get(url="https://kanye.rest/")

print(response.status_code)  # we get 200, response code
response.raise_for_status()

data = response.json()

print(data)

# Too long for too many errors
# if response.status_code == 404:
#     raise Exception("Resource doesnt exist")
# elif response.status_code == 401:
#     raise Exception("No authorized to access data")

# Code 1XX : hold on
# Code 2XX : You got it
# Code 3XX : No permission
# Code 4XX : You screwed up
# Code 5XX : Server screwed up
