import json
from collections import Counter 

def main(): 
    freq = {}

    data = json.loads(open('./random.json').read())
    users = json.loads(open('./users.json').read())

    for message in data['messages']:
        if (message['user'] in freq):
            freq[message['user']] += 1
        else: 
            freq[message['user']] = 1

    k = Counter(freq)
    high = k.most_common(10) 

    for i in high:
        print(i[0]," :",i[1]," ") 

    

main()



