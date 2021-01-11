import requests
import json

def renewAccessToken():
    # TODO: Error handling

    json_file = open('parameters.json', 'r')
    parameters = json.load(json_file)
    json_file.close()

    base_url = "https://webexapis.com/v1/access_token"
    grant_type = "authorization_code"
    client_id = parameters['client_id']
    client_secret = parameters['client_secret']
    refresh_token = parameters['refresh_token']

    url = "{}?grant_type={}&client_id={}&client_secret={}&refresh_token={}".format(base_url, grant_type, client_id, client_secret, refresh_token)

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }

    payload = {}

    response_json = apiCallReturnJSON("POST", url, headers, payload)

    print(response_json)

    access_token = response_json['access_token']
    refresh_token = response_json['refresh_token']

    # # TODO: Logging of the token request

    json_file =  open('parameters.json', 'w')

    parameters['access_token'] = access_token
    parameters['refresh_token'] = refresh_token

    json.dump(parameters, json_file)
    json_file.close()


def getAccessToken():
    with open('parameters.json', 'r') as json_file:
        parameters = json.load(json_file)

    return parameters['access_token']


def apiCallReturnJSON(method, url, headers, payload):
    response = requests.request(method, url, headers=headers, data=payload)
    print("Response Status: {} \n".format(response))
    return json.loads(response.text)


if __name__ == "__main__":
    renewAccessToken()