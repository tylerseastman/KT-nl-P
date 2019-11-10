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
    responses = []
    for channel in channels:
        channelIds.append(channel['id'])
    method = "channels.history"
    for channel in channelIds:
        parametersList = ["channel=" + channel]
        url = makeRequestURL(method, parametersList)
        response = requests.get(url)
        print(response.content)



    

    print(responses)



main()



