import requests
from datetime import datetime

USERNAME = "raghvendra2994"
TOKEN = "qwerty123!@#keyboard"
GRAPH_ID = "graph"

pixela_endpoint = "https://pixe.la/v1/users"

api_header = {
    "X-USER-TOKEN": TOKEN
}


def create_user():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)


def create_graph():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    graph_params = {
        "id": GRAPH_ID,
        "name": "Coding Graph",
        "unit": "Minutes",
        "type": "float",
        "color": "sora",
    }

    response = requests.post(url=graph_endpoint, json=graph_params, headers=api_header)
    print(response.text)


def create_pixel(update_time):
    pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_params = {
        'date': update_time,
        'quantity': input("Enter the number of minutes: "),
    }
    response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=api_header)
    print(response.text)


def update_pixel_ep():
    endpoint = (f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/"
                f"{input('Enter the date for the changes need to be done in yyyyMMdd format: ')}")
    return endpoint


def update_pixel():
    pixela_changes_endpoint = update_pixel_ep()
    pixela_update_params = {
        "quantity": input("Enter the number of minutes that need to be updated: "),
    }
    response = requests.put(url=pixela_changes_endpoint, json=pixela_update_params, headers=api_header)
    print(response.text)


def delete_pixel():
    pixela_changes_endpoint = update_pixel_ep()
    response = requests.delete(url=pixela_changes_endpoint, headers=api_header)
    print(response.text)


user_choice = input(
    """Enter your choice
    1. Create a User(Create).
    2. Enter study time details(New detail).
    3. Update study time details(Update).
    4. Delete older details(Delete).
    """).lower()
if user_choice == 'create':
    create_user()
    create_graph()
elif user_choice == 'new detail':
    current_time = str(datetime.now()).split()[0].split('-')
    str_time = ''
    for item in current_time:
        str_time += item
    create_pixel(str_time)
elif user_choice == 'update':
    update_pixel()
elif user_choice == 'delete':
    delete_pixel()
else:
    print("Wrong input")