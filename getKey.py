import requests
import json

# Read the client parameters that are needed for generating the token key
with open('parameters.json', 'r') as json_file:
    parameters = json.load(json_file)

base_url = "https://webexapis.com/v1/access_token"
grant_type = "authorization_code"
client_id = parameters['client_id']
client_secret = parameters['client_secret']
code = parameters['code']
redirect_uri = parameters['redirect_uri']

# Ensure that content type if the right one
headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }

payload = {}

url = "{}?grant_type={}&client_id={}&client_secret={}&code={}&redirect_uri={}".format(base_url, grant_type, client_id, client_secret, code, redirect_uri)
print (url)

# You need to do a post method
response = requests.request("POST", url, headers=headers, data=payload)

# Just print the response no need to be fancy or easy to read since only use once
print(response)
print(response.text)
