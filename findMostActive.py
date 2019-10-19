import json
import numpy as np
import os
from collections import Counter 

def mostActive(n): 
    freq = {}

    dirs = os.listdir("data")
    users = json.loads(open('./users.json').read())

    for fileName in dirs:
        data = json.loads(open('./data/' + fileName).read())
        print(fileName)
        for message in data['messages']:
            if('user' not in message):
                continue
            if (message['user'] in freq):
                freq[message['user']] += 1
            else: 
                freq[message['user']] = 1

    k = Counter(freq)
    high = k.most_common(n) 

    # print("Top " + str(n) + " Posters in Random")
    # for i in high:
    #     print(i[0]," :",i[1]," ") 

    userIds = []
    for i in high:
        userIds.append(i[0])

    print(userIds)
    
    for i in range(len(userIds)):
        for user in users['members']:
            if (userIds[i] ==  user['id']):
                userIds[i] = user['real_name']


    return userIds


