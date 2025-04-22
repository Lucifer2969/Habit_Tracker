import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "raghvendra2994"
TOKEN = "qwerty123!@#keyboard"
GRAPH_ID = "graph"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

api_header = {
    "X-USER-TOKEN": TOKEN
}

graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Minutes",
    "type": "float",
    "color": "sora",
}

# response = requests.post(url= graph_endpoint,json=graph_params,headers=api_header)
# print(response.text)

current_time = str(datetime.now()).split()[0].split('-')
str_time = ''
for item in current_time:
    str_time += item

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# pixel_params = {
#     'date': str_time,
#     'quantity': input("Enter the number of minutes: "),
# }

# response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=api_header)
# print(response.text)

pixela_changes_endpoint = (f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/"
                           f"{input('Enter the date for the changes need to be done in yyyyMMdd format: ')}")

# pixela_update_params = {
#     "quantity" : input("Enter the number of minutes that need to be updated: "),
# }

# response = requests.put(url=pixela_changes_endpoint,json=pixela_update_params,headers=api_header)
# print(response.text)

response = requests.delete(url=pixela_changes_endpoint,headers=api_header)
print(response.text)