import requests
import json

# Read the client parameters that are needed for generating the token key
json_file = open('parameters.json', 'r')
parameters = json.load(json_file)
json_file.close()

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
response_json = json.loads(response.text)

print(response)
print(response_json)

json_file =  open('parameters.json', 'w')

parameters['access_token'] = response_json['access_token']
parameters['refresh_token'] = response_json['refresh_token']

json.dump(parameters, json_file)
json_file.close()
