import requests
import shutil
import json
import os
import openai

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
file_path = "C:/Users/sanjay/Desktop/task/Raw Audio.mp3"

# Declare your dlb:// location
url = "https://api.dolby.com/media/input"
headers = {
    "Authorization": "Bearer {0}".format(access_token),
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Create the input media request
body = {
    "url": "dlb://Enhanced Audio.mp3",
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
output_filename = "Enhanced Audio.mp3"
output_path = os.path.join(output_dir, output_filename)

url = "https://api.dolby.com/media/output"
headers = {
    "Authorization": "Bearer {0}".format(access_token),
    "Content-Type": "application/json",
    "Accept": "application/json"
}

args = {
    "url": "dlb://Enhanced Audio.mp3",
}

# Send the download request for the enhanced audio
with requests.get(url, params=args, headers=headers, stream=True) as response:
    response.raise_for_status()
    response.raw.decode_content = True
    print("Downloading from {0} into {1}".format(response.url, output_path))
    with open(output_path, "wb") as output_file:
        shutil.copyfileobj(response.raw, output_file)

# Transcribe the audio
openai.api_key = "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"
audio_file = open("C:/Users/sanjay/Desktop/task/Enhanced Audio.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript.text)

# Write the output text to a file
file = open("Audio Transcription.txt", "w")
file.write(transcript.text)
file.close()

# Perform chat completion using GPT-3.5 Turbo model
text_file = open("C:/Users/sanjay/Desktop/task/Audio Transcription.txt", "rb")
Fcontents = text_file.read().decode('utf-8')

# List available models
models = openai.Model.list()

# Print the ID of the first model
print(models.data[0].id)

# Create a chat completion
chat_completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "The Raw form is the original audio as spoken by the speaker. The Cleaned up form is an optimized version of the text, where ChatGPT removes unnecessary words or parts that do not contribute to the conversation. The Summary form is a shortened version of the cleaned-up text that retains the essential information. According to the instruction can you print the cleaned up and summary of this speech "},
    {"role": "user", "content": Fcontents},
  ]
)

# Get the summary from the chat completion response
summary = chat_completion.choices[0].message.content
print(summary)

# Write the summary text to a file
file = open("summary.txt", "w")
file.write(summary)
file.close()
