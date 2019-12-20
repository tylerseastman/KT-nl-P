# KT-nl-P

A Naive Bayes Classifier for the Kappa Theta Pi fraternity's Slack channel messages. The dataset used are the most recent 1000 messages from all the channels when we first commenced the project. The project initially started at the KTP Hackathon and continued outside afterwards. 

### Installing

Download all needed dependencies via the below command:

```
pip install -r requirements.txt
```

## Deployment

```
$ python3 transformData.py
```

## Running tests on current data

By running the command
```
$ python3 transformData.py
```

3 sections will be printed to the terminal. The first section is the actual dataframe generated from all the json files of the 1000 Slack messages (stored under the ```data``` folder as json files) gathered across all the channels in the KTP Slack Workspace. The second and third are the prediction accuracies of using a [Multinomial Naive Bayes classifier](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html) and a [Decision Tree classifier](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html) on the first 600 messages as training data, and the last 400 messages as testing data. 

## Built With

* [Slack API](https://api.slack.com/) - Used to gather Slack Workspace and channel data
* [ScKit](https://scikit-learn.org/stable/index.html) - Machine Learning Library used
* [Natural Language Toolkit](https://www.nltk.org/) - Toolkit used to process the data, including lemmatization and removing stop-words

## Authors

* **Tyler Eastman** - [tylerseastman](https://github.com/tylerseastman)
* **Shan Jiang** - [shanjng](https://github.com/shanjng)
* **Rea Parocaran**
