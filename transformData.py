import pandas as pd
import nltk
import json
import os
from nltk.tokenize import word_tokenize

dirs = os.listdir("data")
print(dirs)

dfs = []
userMessages = []
for fileName in dirs:
    data = json.loads(open('./data/' + fileName).read())
   

    for message in data['messages']:
        if('user' not in message):
                continue
        userMessages.append([message['user'], message['text']])
    
    # df = pd.DataFrame(userMessages, columns = ['User ID', 'Text']) 
    # dfs.append(df)

df = pd.DataFrame(userMessages, columns = ['User ID', 'Text']) 

print(df)

# Preprocessing 

#NLTK Tokenizing



