from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

'''
Eli Miller

Uses scikit-learn to classify strings of text.

To do:
- collect/label the training data (all the lines) and turn it into training tuples
- add a process for turning the test data into the correct format
- incorporate the metamap UMLS information into the data
- decide what classifier(s) to use - do some testing on dev data
- implement a voting system if I decide to use an ensemble
'''

def train(text):
    '''
    Takes a list of (string, label) tuples.
    Returns a fitted vectorizer and a trained classifier.
    Currently returns a multinominal naive bayes classifier
    '''
    count_vect = CountVectorizer()
    labels = [x[1] for x in text]
    lines = [x[0] for x in text]
    train_counts = count_vect.fit_transform(lines)
    print(train_counts.shape)
    mnb = MultinomialNB().fit(train_counts, labels)
    return count_vect, mnb

def test(model, count_vect, text):
    '''
    Takes a trained classifier, a fitted vectorizer, and a list of strings to classify.
    Returns a list containing the classification of each string, in the same order as
    the given list of strings.
    '''
    counts = count_vect.transform(text)
    pred = model.predict(counts)
    return list(pred)

if __name__ == "__main__":
    import sys
    text = [("presidents senators vote bill law", "1"), ("keyboard RAM memory CPU", "0")]
    count_vect, model = train(text)
    unktext = ["presidents and senators are people", "I need more memory in my keyboard"]
    ans = test(model, count_vect, unktext)
    print(ans)
