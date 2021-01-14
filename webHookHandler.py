import requests
import json

from apiHandler import apiCallReturnJSON
from tokenHandler import getPersonalToken, getBotToken

def getHookConfig():

    json_file = open('webhook_config.json', 'r')
    config = json.load(json_file)
    json_file.close()

    return config


def createWebHook():

    api_url = "webhooks"
    payload = json.dumps(getHookConfig())

    return apiCallReturnJSON(getBotToken(), "POST", api_url, payload)


def updateWebHook(webhook_id, targetUrl):

    # TODO: There is a bug here, it won't update - investigate later
    # ISSUE #400-01:

    webhook = getWebHook(webhook_id)

    api_url = "webhooks"
    body = {
        "name": "{}".format(webhook["name"]),
        "targetUrl" : "{}".format(targetUrl)
    }
    
    payload = json.dumps(body)

    response = apiCallReturnJSON(getBotToken(), "PUT", api_url, payload)
    print(json.dumps(response, indent=4, sort_keys=True))


def listWebHooks():

    api_url = "webhooks"
    payload = {}
    response = apiCallReturnJSON(getBotToken(), "GET", api_url, payload)

    print(json.dumps(response, indent=4, sort_keys=True))


def getWebHook(webhook_id):

    api_url = "webhooks/{}".format(webhook_id)
    payload = {}
    return apiCallReturnJSON(getBotToken(), "GET", api_url, payload)


def deleteWebHook(webhook_id):

    api_url = "webhooks/{}".format(webhook_id)
    payload = {}
    response = apiCallReturnJSON(getBotToken(), "DELETE", api_url, payload)

    print(json.dumps(response, indent=4, sort_keys=True))


if __name__ == "__main__":

    # TODO: Features
        # Feature #300-01: Add option to select the access token and/or use token stored locally. This is to differentiate if using a token for Bot or personal/integration hooks.
        # Feature #300-02: Allow to either enter hook ID or use config file to read it

    print("\n Welcome to Web Hook Handler... What would you like to do?\n")
    print("1 - Create Web Hook\n")
    print("2 - Update Web Hook Target URL\n")
    print("3 - List all Web Hooks\n")
    print("4 - Get Info about specific Web Hook\n")
    print("5 - Delete a Web Hook\n")
    user_input = input("Enter appropriate number: ")
    choice = int(user_input)

    if choice == 1:
        print("\n Note You are about to create a new Web Hook. webhook_config.json will be used to config the web hook. \n")
        user_input = input("Continue (Y/n): ")

        if user_input in "Y" or user_input in "y":

            print("\n")
            response = createWebHook()
            print(json.dumps(response, indent=4, sort_keys=True))

        else:
            print("Bye Bye then")

    elif choice == 2:
        webhook_id = input("Enter Hook ID: ")
        target_url = input("Enter New TargetUrl: ")
        updateWebHook(webhook_id, target_url)

    elif choice == 3:
        listWebHooks()

    elif choice == 4:
        webhook_id = input("Enter Hook ID: ")
        response = getWebHook(webhook_id)
        print(json.dumps(response, indent=4, sort_keys=True))
    
    elif choice == 5:
        webhook_id = input("Enter Hook ID: ")
        print("\n Note You are about to DELETE {} \n".format(webhook_id))
        confirm = input("You sure? (Y/n): ")

        if confirm in "Y" or confirm in "y":
            deleteWebHook(webhook_id)
            print("Deleting...")
        else:
            print("hmmm don't think so. Bye Bye then.")
            pass
    else:
        print("Sorry but that ain't one of the options.")