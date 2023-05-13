import os
import requests

# Set or replace these values
api_token="eyJ0eXAiOiJKV1QiLCJraWQiOiI1ODExQjE0RS1DQzVCLTQ4QkQtQTNEOC1DREQxQzUzQ0ZDNUMiLCJhbGciOiJSUzUxMiJ9.eyJpc3MiOiJkb2xieS5pbyIsImlhdCI6MTY4MzgwMDIxMSwic3ViIjoiRVBTWnhXb1dSandwQV9zakxEZFVDZz09IiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9DVVNUT01FUiJdLCJ0YXJnZXQiOiJhcGkiLCJvaWQiOiI3ZDU5NjYzZi1lOWQ4LTQ2YjgtOGY5OS1kOWU3MDk3MTczNTkiLCJhaWQiOiI0OTQ2NzgwMS01MWMzLTRmNjUtOGYxYy1kMWYzYjYyMGQ4MDQiLCJiaWQiOiI4YTM2ODdiYzg4MDVjNzVjMDE4ODA5YzI1ZGI5NWM2MyIsImV4cCI6MTY4MzgwMjAxMX0.uQY_NuQUCYI4dQf9-YZLFgVORZjNuhy6baacDR5L_KtxCKwePjpwXUmn-OMKyz3vFyMKpHX3LuVu_6rb_xvOQ_nr3li285kMtX0eB1BXxDSCk0ZK65KNIGEG40otbOfu1rcI9Dpfh3WJXSUDyRfHf2wjaAp4bAV3avwaQJ3vOEWYZbTSb8Sthm_wTDIYwT502O81lus60QWIdTaeZAHf53jFMVSezS7EySJ4Oi3W3RBJ8yHxbQR2Qd5cC2e4hCs5q9HXoMwm7587jTPlrIcKClGzgrdYtkMPAm4R4d04Sn-MxpTVNdkiPOI8gHk1U5F3iGkoA9FBbSSddUsv7njNi6Nlm9GBRB42SJyA1clNgCACDm3fsPgrhLxcj-0CaM4-lb8mZ4Z1P_sa-3HuZd1n29do1TTGG4GvLgtvNdsrS3_x0poCEXvVc830eWiDAPFXB-cm7XZniNFjiI0Rt2tgteVKy_60RgxHZG_16WXtEgadexV0O0qDtIU_Af1HuT9xRUnc6ZU2j-MSo2e_yi6SQr6aoClOTW2SIj7REDxw3o7mn2qmtvTM86Y6lYsPPEmjKzujPsufm7eVQ6Qv7H1Lsnw_7KSth2-8beoak_KtbCViehLrJ_XDv2I9iKAAdqXn7ruAgBR6fM1ehYcdmeHcW78jSJBKsSSu8j8NKemPzus"

file_path = "C:/Users/sanjay/Desktop/task/AC.mp3"

# Declare your dlb:// location

url = "https://api.dolby.com/media/input"
headers = {
    "Authorization": "Bearer {0}".format(api_token),
    "Content-Type": "application/json",
    "Accept": "application/json"
}

body = {
    "url": "dlb://Cleaned.mp3",
}

response = requests.post(url, json=body, headers=headers)
response.raise_for_status()
data = response.json()
presigned_url = data["url"]

# Upload your media to the pre-signed url response

print("Uploading {0} to {1}".format(file_path, presigned_url))
with open(file_path, "rb") as input_file:
  requests.put(presigned_url, data=input_file)