import requests
from datetime import datetime

USERNAME = 'USERNAME'
TOKEN = "TOKEN"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# r = requests.post(url=pixela_endpoint, json=user_params)
# print(r.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "rishicode",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# r = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(r.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/rishicode"

today = datetime.now().strftime("%Y%m%d")

pixel_config = {
    "date": today,
    "quantity": input("Enter hours: "),
}

r = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(r.text)
