import requests
# from config import AUTH_TOKEN
import config
# import datadog
import datetime

# help(datadog)

BASE_URL = 'enter base url'
PIXELA_CREATE_USER_POST_ENDPOINT = 'enter endpoint'

# ---
# 1. create user account

# how to do: POST request
url = BASE_URL + PIXELA_CREATE_USER_POST_ENDPOINT

create_user_parameters = {
    'token': config.AUTH_TOKEN,
    'username': 'enter username',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=url, json=parameters)
# # response.raise_for_status()
# # print(response)
# # print(response.status_code)
# print(response.text)
# ---

# ---
# 2. create graph definition
USERNAME = 'enter username'
AUTH_TOKEN = config.AUTH_TOKEN

PIXELA_CREATE_GRAPH_DEFINITION_ENDPOINT = '{pixela_create_user_endpoint}/{username}/graphs'.format(
    pixela_create_user_endpoint=PIXELA_CREATE_USER_POST_ENDPOINT,
    username=USERNAME
)

graph_definition_url = f'{BASE_URL}{PIXELA_CREATE_GRAPH_DEFINITION_ENDPOINT}'
graph_definition_parameters = {
    'id': 'graph1',
    'name': 'projects_per_day_tracker',
    'unit': 'project(s)',
    'type': 'int',
    'color': 'sora',
}

# response = requests.post(url=graph_definition_url, json=graph_definition_parameters)
# print(response.text)
# how to do: HTTP HEADER (for authentication) aka authentication headers
headers = {
    'X-USER-TOKEN': AUTH_TOKEN,
}

# response = requests.post(url=graph_definition_url, json=graph_definition_parameters, headers=headers)
# print(response.text)
# ---

# ---
# 3. get the graph
# ---

# ---
# 4. post pixel to the graph
PIXELA_GRAPH_ID = 'enter graph id'

PIXELA_POST_PIXEL_ENDPOINT = BASE_URL + '{pixela_create_graph_definition}/{graph_id}'.format(
    pixela_create_graph_definition=PIXELA_CREATE_GRAPH_DEFINITION_ENDPOINT,
    graph_id=PIXELA_GRAPH_ID,
)

post_pixel_url = PIXELA_POST_PIXEL_ENDPOINT

# print(datetime.datetime.now().strftime('%Y/%m/%d'))
post_pixel_parameters = {
    'date': datetime.datetime.now().strftime('%Y%m%d'),
    'quantity': '2',
}

# headers = {
#     'X-USER-TOKEN': AUTH_TOKEN,
# }

# response = requests.post(url=post_pixel_url, json=post_pixel_parameters, headers=headers)
# print(response.text)
# ---

# ---
# how to do: PUT (i.e. update) request
date = datetime.date(year=2021, month=7, day=30).strftime('%Y%m%d')

PIXELA_UPDATE_PIXEL_ENDPOINT = f'{PIXELA_POST_PIXEL_ENDPOINT}/{date}'

put_pixel_url = PIXELA_UPDATE_PIXEL_ENDPOINT

put_pixel_parameters = {
    'quantity': '2',
}

# headers = {
#     'X-USER-TOKEN': AUTH_TOKEN,
# }

# response = requests.put(url=put_pixel_url, json=put_pixel_parameters, headers=headers)
# print(response.text)
# ---

# ---
# how to do: DELETE request
date = datetime.date(year=2021, month=7, day=30).strftime('%Y%m%d')

PIXELA_DELETE_PIXEL_ENDPOINT = PIXELA_UPDATE_PIXEL_ENDPOINT

delete_pixel_url = PIXELA_DELETE_PIXEL_ENDPOINT

headers = {
    'X-USER-TOKEN': AUTH_TOKEN,
}

response = requests.delete(url=delete_pixel_url, headers=headers)
print(response.text)
# ---
