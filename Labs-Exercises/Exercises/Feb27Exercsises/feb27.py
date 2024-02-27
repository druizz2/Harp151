import requests 
import json
from base64 import b64encode

# OAUTH PARTS
# Special User ID -> Will have a client ID and a secret client code, pass both to the server
# Pass to API-> registered, API knows you, can start using API
# if something asks for redirect URL use localhost:8080

# Spotify API Example
client_id = "9d978f7ae3dd4f2bace272a48c18b1f5"
client_secret = "d4d4a0c1b4564754b999e2520ad3efd9"

auth_url = 'https://accounts.spotify.com/api/token'
auth_header = 'Basic ' + b64encode((client_id + ':' + client_secret).encode()).decode()

auth_data = {
    'grant_type': 'client_credentials'
}

#we are POSTING something to the server in order to RETURN the token
auth_response = requests.post(auth_url, headers={'Authorization': auth_header}, data=auth_data)

if auth_response.status_code == 200:
    token = auth_response.json().get('access_token')
    print('Token:', token)
else:
    print('Error:', auth_response.status_code)
    print(auth_response.text)

# Now we can try requesting information
track_id = "11dFghVXANMlKmJXsNCbNl"
url = f"https://api.spotify.com/v1/tracks/{track_id}/"

headers = {     # have to call every time run API
    "Authorization": "Bearer " + token
}

response = requests.get(url, headers=headers)

data = response.json()
print(json.dumps(data))


