from flask import Flask, request
import json

app = Flask(__name__)

from apiHandler import apiCallReturnJSON
from tokenHandler import getBotToken


@app.route("/", methods=["GET"])
def get_click():

    print("Here")


@app.route("/", methods=["POST"])
def get_login():

    print("Here instead")
    print(request.method)
    hook = request.json
    print(json.dumps(hook, indent=4, sort_keys=True))

    message = getMsgInfo(hook["data"]["id"])

    print("Bot Said: {}".format(message["text"]))

    return "Hello"

    # return redirect("{}?continue_url={}".format(success_url,base_grant_url), code=302)


@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    return response


def getMsgInfo(message_id):
    
    api_url = "messages/{}".format(message_id)
    payload = {}

    return apiCallReturnJSON(getBotToken(), "GET", api_url, payload)


if __name__ == "__main__":
    # Hosted on localhost port 5004 - Remember to run "ngrok http 5004"
    app.run(host="0.0.0.0", port=8000, debug=False)