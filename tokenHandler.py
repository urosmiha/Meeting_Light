import json
import requests

def renewAccessToken():
    # TODO: Error handling

    parameters = getParameters()

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


def getParameters():
    json_file = open('parameters.json', 'r')
    parameters = json.load(json_file)
    json_file.close()

    return parameters


def getPersonalToken():

    parameters = getParameters()
    return parameters['access_token']


def getRefreshToken():

    parameters = getParameters()
    return parameters['refresh_token']


def getBotToken():

    parameters = getParameters()
    return parameters['bot_token']


if __name__ == "__main__":
    print("\n Note You are about to renew your token \n")
    user_input = input("Continue (Y/n): ")

    if user_input in "Y" or user_input in "y":
        print("\n")
        print("Old Token: {}".format(getPersonalToken()))
        print("Old Refresh Token: {}".format(getPersonalToken()))

        renewAccessToken()

        print("\n")
        print("New Token: {}".format(getPersonalToken()))
        print("New Refresh Token: {}".format(getPersonalToken()))
    else:
        print("Bye Bye then")
        pass