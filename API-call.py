import requests 
import json

token = "???"

def makeRequestURL(method, parametersList):
    url = "https://slack.com/api/" + method + "?token=" + token

    parametersList = map(lambda param: "&" + param, parametersList)

    for parameters in parametersList:
        url = url + parameters

    url = url + "&pretty=1"

    return url

def main(): 
    parametersList = ["count=1000"]

    method = "channels.list"

    url = makeRequestURL(method, parametersList)

    response = requests.get(url)

    channels = json.loads(response.content)['channels']
    channelIds = []

    for channel in channels:
        channelIds.append(channel['id'])

    messages = {}
    method = "channels.history"
    for channel in channelIds:
        parametersList = ["channel=" + channel]
        url = makeRequestURL(method, parametersList)
        responseJSON = json.loads(requests.get(url).content)
        for message in responseJSON['messages']:
            if("client_msg_id" in message and 'text' in message and 'user' in message):
                messages[message["client_msg_id"]] = (message['text'], message['user'])

    print(messages)

# TODO: add time wait before refreshing inventory of messages
# TODO: check to see if message is already in dictionary

main()



