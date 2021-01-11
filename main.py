import requests
import json

def apiCallReturnJSON(method, api_url):

    # TODO: Check if the token is still valid

    url = "https://webexapis.com/v1/{}".format(api_url)
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(getAccessToken())
    }
    payload = {}

    response = requests.request(method, url, headers=headers, data=payload)
    print("Response Status: {} \n".format(response))
    return json.loads(response.text)


def renewAccessToken():
    # TODO: Error handling

    json_file = open('parameters.json', 'r')
    parameters = json.load(json_file)
    json_file.close()

    base_url = "https://webexapis.com/v1/access_token"
    grant_type = "refresh_token"
    client_id = parameters['client_id']
    client_secret = parameters['client_secret']
    refresh_token = parameters['refresh_token']

    url = "{}?grant_type={}&client_id={}&client_secret={}&refresh_token={}".format(base_url, grant_type, client_id, client_secret, refresh_token)
    headers = {
        'Accept':'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
        }
    payload = {}

    response = requests.request("POST", url, headers=headers, data=payload)
    print("Response Status: {} \n".format(response))
    response_json = json.loads(response.text)

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
    json_file = open('parameters.json', 'r')
    parameters = json.load(json_file)
    json_file.close()

    print("Access Token: {} \n".format(parameters['access_token']))

    return parameters['access_token']


def getAllMeetings():

    print(apiCallReturnJSON("GET", "meetings"))


if __name__ == "__main__":
    getAllMeetings()