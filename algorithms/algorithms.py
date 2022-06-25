import os
import nltk
import re
import pandas as pd
import string
import math
import numpy as np
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .nlp import model


def stopwords(text):
    # download english stop words from the nltk library
    stopWords = nltk.corpus.stopwords.words('english')
    str = ""
    # splits the input into individual words the check them to see if they exist in the stopword list | if the dont they add them to the words array
    words = [word for word in text.split() if word not in stopWords]
    # iterate through the words in the words array and make them a sentence by adding a space after each word
    for i in words:
        str += i
        str += " "
    return str


# converts capital letters to lowercase in text
def text_lowercase(text):
    return text.lower()


# removing numbers from text
def remove_numbers(text):
    # \d+ \d=digit \d+=one or more digits
    result = re.sub(r'\d+', '', text)
    return result


# removing punctuations in text
def remove_punctuations(text):
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)


# removing whitespace in text
def remove_whitespace(text):
    return " ".join(text.split())


def tokenizer(text):
    # to remove non asci character =  character that are not(^) in the range \x20-\x7E
    text = re.sub('^^\x20-\x7E', '', text)
    return word_tokenize(text)
    # change the text into a bag of words(array of words)
    # "hello there! i won." => ['hello', 'there', '!', 'i', 'won']


def document_vector(doc):
    doc = [word for word in doc if word in model.vocab]
    a = model[doc]
    return np.mean(model[doc], axis=0)

def preprocessing(cleaned):
    cleaned = remove_whitespace(cleaned)
    cleaned = remove_numbers(cleaned)
    cleaned = remove_punctuations(cleaned)
    valid_characters = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890'
    cleaned = ''.join([x for x in cleaned if x in valid_characters])
    cleaned = text_lowercase(cleaned)
    cleaned = stopwords(cleaned)
    cleaned = tokenizer(cleaned)
    return cleaned

def preprocessing_(doc):
    cleaned = doc
    cleaned = remove_whitespace(cleaned)
    cleaned = remove_numbers(cleaned)
    cleaned = remove_punctuations(cleaned)
    cleaned = text_lowercase(cleaned)
    cleaned = stopwords(cleaned)
    return cleaned

def alldocclean(alldocuments):
    predocs = []
    for i in alldocuments:
        predoc = preprocessing(i)
        predocs.append(predoc)
    return predocs  # predocs contains all cleared texts

def alldocclean_(alldocuments):
    predocs = []
    for i in alldocuments:
        predoc = preprocessing_(i)
        predocs.append(predoc)
    return predocs  # predocs contains all cleared texts

def TFIDFCosineSimilarity(doc, alldoc):
    cleantext = alldocclean_(alldoc)
    tfidf = TfidfVectorizer()  # instantiate tfidf vectorizer
    tfs = tfidf.fit_transform(cleantext)
    # DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table
    df = pd.DataFrame(tfs.toarray(), columns=tfidf.get_feature_names())
    cossim = cosine_similarity(df)
    cossimdf = pd.DataFrame(cossim)
    cossimpair = []
    for index in range(len(alldoc)):
        if (doc != index):
            temp = []
            temp.append(index)
            temp.append(cossimdf.at[index, doc])
            cossimpair.append(temp)
    return cossimpair

def cosine_similarity_(vector1, vector2):
    dot_product = sum(p * q for p, q in zip(vector1, vector2))
    magnitude = math.sqrt(sum([val ** 2 for val in vector1])) * \
        math.sqrt(sum([val ** 2 for val in vector2]))
    if not magnitude:
        return 0
    return dot_product / magnitude

def word2VecCosineSimilarity(doc, alldoc):
    if model is None:
        return None
    arr = alldocclean(alldoc)
    simArr = []
    doc_text = document_vector(arr[doc])
    for i in range(len(arr)):
        if doc != i:
            temp = [i, cosine_similarity_(doc_text, document_vector(arr[i]))]
            simArr.append(temp)
    return simArr
