import requests 

token = "xoxp-167865381525-250932508468-800973847204-0713bfc64add0a47ba8ea64f1d90a221"

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



