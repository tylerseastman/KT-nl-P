import requests 

token = "???"

def makeRequestURL(method, parametersList):
    url = "https://slack.com/api/" + method + "token=" + token

    parametersList = map(lambda param: "&" + param, parametersList)

    for parameters in parametersList:
        url = url + parameters

    url = url + "&pretty=1"

    return url

def main(): 
    parametersList = ["count=1000"]

    method = "channels.list"

    url = makeRequestURL(method, parametersList)

    html = requests.get(url)

    print(html)

main()



