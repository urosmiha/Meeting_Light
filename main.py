import requests
import json

def apiCallReturnJSON(token, method, api_url, payload):

    # TODO: Check if the token is still valid

    url = "https://webexapis.com/v1/{}".format(api_url)
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(token)
    }

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


def getPersonalToken():
    json_file = open('parameters.json', 'r')
    parameters = json.load(json_file)
    json_file.close()

    print("Access Token: {} \n".format(parameters['access_token']))

    return parameters['access_token']

def getBotToken():
    json_file = open('parameters.json', 'r')
    parameters = json.load(json_file)
    json_file.close()

    print("Access Token: {} \n".format(parameters['bot_token']))

    return parameters['bot_token']


def getAllMeetings():

    api_url = "meetings?meetingType=meeting"
    meetings = apiCallReturnJSON(getPersonalToken(), "GET", api_url, {})
    print(json.dumps(meetings, indent=4, sort_keys=True))
    
    api_url = "meetings?meetingType=scheduledMeeting"
    meetings = apiCallReturnJSON(getPersonalToken(), "GET", api_url, {})
    print(json.dumps(meetings, indent=4, sort_keys=True))


def sendBotMsg(message):

    # TODO: Think how to obtain the BOT room ID easily or when the room has been deleted.

    api_url = "messages/"

    # TODO: REMOVE HARD-CODED Value
    payload = {
        "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGU3MjE3NGItOTQ5Yy0zZmQ4LWFmMjgtNmE3MDc1ZjY4OWJh",
        "text": "{}".format(message)
    }
    payload = json.dumps(payload)

    response = apiCallReturnJSON(getBotToken(), "POST", api_url, payload)
    print(json.dumps(response, indent=4, sort_keys=True))


if __name__ == "__main__":
    # sendBotMsg("Hello")
    getAllMeetings()
    