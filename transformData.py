import pandas as pd
import nltk
import json
import os
import string
import numpy as np
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
nltk.download('stopwords')
stopwords.words('english')
lemmatizer = WordNetLemmatizer()
dirs = os.listdir("data")
print(dirs)
# nltk.download('wordnet') Download Once
# nltk.download('averaged_perceptron_tagger') Download Once

def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wn.ADJ,
                "N": wn.NOUN,
                "V": wn.VERB,
                "R": wn.ADV}

    return tag_dict.get(tag, wn.NOUN)

dfs = []
userMessages = []
count = 0
for fileName in dirs:
    data = json.loads(open('./data/' + fileName).read())
   

    for message in data['messages']:
        if('user' not in message):
                continue
        # Strip punction and numbers from text
        for punctuation in string.punctuation:
            message['text'] = message['text'].replace(punctuation, ' ')
        for digit in string.digits:
            message['text'] = message['text'].replace(digit, ' ')
        # Split text into lowercase tokens and remove stopwords
        token_list = word_tokenize(message['text'].lower())
        clean_tokens = token_list
        sr = stopwords.words('english')
        for token in token_list:
            if token in stopwords.words('english'):
                clean_tokens.remove(token)
        lemmatized_output = ' '.join([lemmatizer.lemmatize(token, get_wordnet_pos(token)) for token in clean_tokens])

        if(lemmatized_output == ""):
             count += 1

        # for word in lemmatized_output:
        #     wn.synset(word + '.' + get_wordnet_pos(word) + '.01').hyponyms[0]

        userMessages.append([message['user'], lemmatized_output])
    

df = pd.DataFrame(userMessages, columns = ['User ID', 'Text']) 

print(df)

print("count: " + str(count))

count_vect = CountVectorizer()
X_counts = count_vect.fit_transform(df['Text'])
# print(count_vect.get_feature_names())
# print(X_counts.toarray())
# print(X_counts.shape) # (n_samples, n_features)
# print(count_vect.vocabulary_.get(u'zw')) # gets Index

clf = MultinomialNB()
print(X_counts[0:2250])
buildModel= clf.fit(X_counts[0:2250], df['User ID'][0:2250])
y_pred = buildModel.predict(X_counts[2250:])
print(np.mean(y_pred == df['User ID'][2250:]))


# print("Number of mislabeled points out of a total %d points : %d"
#     % (trainingData['Text'].shape[0],(trainingData['User ID'] != y_pred).sum()))