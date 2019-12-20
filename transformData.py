import pandas as pd
import nltk
import json
import os
import string
import numpy as np
from nltk.stem import PorterStemmer
from sklearn.neural_network import MLPClassifier
from sklearn import tree
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from sklearn import svm
from nltk.stem import WordNetLemmatizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from findMostActive import mostActive as mostActiveFunc

stopwords.words('english')
lemmatizer = WordNetLemmatizer()
dirs = os.listdir("data")
# print(dirs)
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

mostActive = ['UFZ4ZBEDS', 'U7CFFQACR', 'U7EKJT35Y', 'U9628B2GP', 'U7F1RLY2C']

for fileName in sorted(dirs):
    data = json.loads(open('./data/' + fileName).read())
   

    for message in data['messages']:
        if('user' not in message):
            continue
        elif (message['user'] not in mostActive):
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

        userMessages.append([message['user'], lemmatized_output])
    

df = pd.DataFrame(userMessages, columns = ['User ID', 'Text']) 

print("Dataframe: \n", df, "\n\n")

# print("count: " + str(count))

count_vect = CountVectorizer()
X_counts = count_vect.fit_transform(df['Text'])
tf_transformer = TfidfTransformer(use_idf=False).fit(X_counts)
X_train_tf = tf_transformer.transform(X_counts)
# print(count_vect.get_feature_names())
# print(X_counts.toarray())
# print(X_counts.shape) # (n_samples, n_features)
# print(count_vect.vocabulary_.get(u'zw')) # gets Index



clf = MultinomialNB()
buildModel= clf.fit(X_train_tf[0:600], df['User ID'][0:600])
y_pred = buildModel.predict(X_train_tf[600:])
print("Multinomial Naive Bayes Accuracy:", np.mean(y_pred == df['User ID'][600:]), "\n")
# print(y_pred)
# clf = svm.SVC(gamma='scale', decision_function_shape='ovo')
# buildModel= clf.fit(X_counts[0:2250], df['User ID'][0:2250])
# y_pred = buildModel.predict(X_counts[2250:])
# print(y_pred)
# print("SVM Accuracy:", np.mean(y_pred == df['User ID'][2250:]))

clf = tree.DecisionTreeClassifier()
buildModel= clf.fit(X_train_tf[0:600], df['User ID'][0:600])
y_pred = buildModel.predict(X_train_tf[600:])
# print(y_pred)
print("Decision Tree Accuracy:", np.mean(y_pred == df['User ID'][600:]), "\n")
# clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
#                     hidden_layer_sizes=(5, 2), random_state=1)
# buildModel= clf.fit(X_counts[0:2250], df['User ID'][0:2250])
# y_pred = buildModel.predict(X_counts[2250:])
# print("Neural Network Accuracy:", np.mean(y_pred == df['User ID'][2250:]))

# 

# print("Number of mislabeled points out of a total %d points : %d"
#     % (trainingData['Text'].shape[0],(trainingData['User ID'] != y_pred).sum()))