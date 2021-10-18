import os

# set environment variable
os.environ['PIXELA_AUTH_TOKEN'] = 'enter auth token'

# get environment variable
AUTH_TOKEN = os.environ.get('PIXELA_AUTH_TOKEN')
