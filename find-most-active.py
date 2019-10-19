import json
import numpy as np
import os
from collections import Counter 

def main(): 
    freq = {}

    dirs = os.listdir("data")
    print(dirs)
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
    n = 10
    high = k.most_common(10) 

    print("Top " + str(n) + " Posters in Random")
    for i in high:
        print(i[0]," :",i[1]," ") 

    ids = []
    for i in high:
        ids.append(i[0])


    for i in range(len(ids)):
        for user in users['members']:
            if (ids[i] ==  user['id']):
                ids[i] = user['real_name']

    for x in ids:
        print(x)

main()



