import requests
import shutil
import json
import os

# Replace with your actual APP_KEY and APP_SECRET
APP_KEY = "SkR668psw81VyLWixAo22g=="
APP_SECRET = "S5nnQ0fEdZl4YNnXqIk0Ub2nRGnR2-80VcI6pFYDMAg="

# Retrieve access token for authentication
payload = {
    'grant_type': 'client_credentials',
    'expires_in': 1800
}
response = requests.post('https://api.dolby.io/v1/auth/token', data=payload, auth=requests.auth.HTTPBasicAuth(APP_KEY, APP_SECRET))
body = json.loads(response.content)
access_token = body['access_token']

# Use the access_token for further API requests
print(access_token)

# Specify the file path of the input media file
file_path = "C:/Users/sanjay/Desktop/task/AC.mp3"

# Declare your dlb:// location
url = "https://api.dolby.com/media/input"
headers = {
    "Authorization": "Bearer {0}".format(access_token),
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Create the input media request
body = {
    "url": "dlb://new.mp3",
}

# Send the input media request
response = requests.post(url, json=body, headers=headers)
response.raise_for_status()
data = response.json()
presigned_url = data["url"]

# Upload the input media file to the pre-signed URL
print("Uploading {0} to {1}".format(file_path, presigned_url))
with open(file_path, "rb") as input_file:
    requests.put(presigned_url, data=input_file)

# Enhance the audio
body = {
  "input" : "dlb://new.mp3",
  "output" : "dlb://out/newaudio.mp3",
  "content" : {
      "type": "mobile_phone"
  }
}

url = "https://api.dolby.com/media/enhance"
headers = {
    "Authorization": "Bearer {0}".format(access_token),
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Send the audio enhancement request
response = requests.post(url, json=body, headers=headers)
response.raise_for_status()
print(response.json())

# Download the enhanced audio
output_dir = "C:/Users/sanjay/Desktop/task"
output_filename = "new.mp3"
output_path = os.path.join(output_dir, output_filename)

url = "https://api.dolby.com/media/output"
headers = {
    "Authorization": "Bearer {0}".format(access_token),
    "Content-Type": "application/json",
    "Accept": "application/json"
}

args = {
    "url": "dlb://new.mp3",
}

# Send the download request for the enhanced audio
with requests.get(url, params=args, headers=headers, stream=True) as response:
    response.raise_for_status()
    response.raw.decode_content = True
    print("Downloading from {0} into {1}".format(response.url, output_path))
    with open(output_path, "wb") as output_file:
        shutil.copyfileobj(response.raw, output_file)
