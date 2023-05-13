import requests
import json
import os

APP_KEY = "EPSZxWoWRjwpA_sjLDdUCg=="  # Replace with your actual APP_KEY
APP_SECRET = "CivfNY0S34av6ESwk34NjRIzO7N7955a4W8v8ojb0Zo="  # Replace with your actual APP_SECRET

payload = {
    'grant_type': 'client_credentials',
    'expires_in': 1800
}

response = requests.post('https://api.dolby.io/v1/auth/token', data=payload, auth=requests.auth.HTTPBasicAuth(APP_KEY, APP_SECRET))
body = json.loads(response.content)
access_token = body['access_token']

# Use the access_token for further API requests
print(access_token)
