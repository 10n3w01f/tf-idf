# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory
#
# import os


import nltk
#from bs4 import BeautifulSoup
import string
import os, glob
import re
import math
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer, word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer


#
# def  discard_html(text):
#    data=BeautifulSoup(text,html)
#    html_free= data.get_text()
#    print(html_free)
text_data = []


def file_read():
    for directory in os.listdir("C:/Users/sampa/Documents/dataset/movie-reviews/Dataset_Copy"):
        text_dict = {}
        i=0
        filename=("C:/Users/sampa/Documents/dataset/movie-reviews/Dataset_Copy/"+directory+"/")
    #    print("**********************"+directory+"*******************")
        os.chdir(filename)
        for file in glob.glob("*.txt"):
          i+=1
          with open(file) as infile:
               text_dict={'doc_id':i,
                      'doc_data':infile.read()}
               text_data.append(text_dict)
    return text_data


def remove_all_special_character(text):
    parsed_string = re.sub('[^\w\s]', ' ', text)
    parsed_string = re.sub('_', ' ', parsed_string)
    parsed_string = re.sub('\s+', ' ', parsed_string)
    parsed_string = parsed_string.strip()
    return parsed_string


def read_data():
    for directory in os.listdir("F:/TTU/Spring 2020-1st sem/Information retrieval/data_set/Reviews"):
        text_data = []
        filename = "F:/TTU/Spring 2020-1st sem/Information retrieval/data_set/Reviews/" + directory + "/"
        #    print("**********************"+directory+"*******************")
        os.chdir(filename)
        for file in glob.glob("*.txt"):
            with open(file) as infile:
                text_data.append(infile.read())
        print(text_data)


def discard_punctuation(text):
    data = "".join([c for c in text if c not in string.punctuation])
    return data


def tokenize_data(text):
    tokenizer = RegexpTokenizer(r'\w+')
    data = tokenizer.tokenize(text.lower())
    return data


def remove_stopwords(text):
    words = [w for w in text if w not in stopwords.words('english')]
    return words


def remove_apostrope(text):
    data = np.char.replace(text, "'", "")
    return data


def remove_a_character(text):
    data = ""
    for words in text:
        if len(words) > 1:
            data = data + " " + words
    return data


def lemmatize_data(text):
    lemmatizer = WordNetLemmatizer()
    #    data=[lemmatizer.lemmatize(word) for word in text]
    data = " ".join([lemmatizer.lemmatize(word) for word in text])
    return data


def stemming_data(text):
    stemmer = PorterStemmer()
    data = " ".join([stemmer.stem(word) for word in text])
    return data


def count_words(text):
    count = 0
    words = word_tokenize(text)
    for word in words:
        count += 1
    return count


def get_doc_info(text_data):
    doc_info = []
    i = 0
    for text in text_data:
        i += 1
        count = count_words(text)
        temp = {'doc_id': i, 'doc_length': count}
        doc_info.append(temp)
    return doc_info


def create_freq(text):
    i = 0
    freq_list = []
    for data in text:
        i += 1
        freq_dict = {}
        words = word_tokenize(data)
        for word in words:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
            temp = {'doc_id': i,
                    'freq_dict': freq_dict}
        freq_list.append(temp)
    return freq_list


def computeTF(doc_info, freq_list):
    tf_score = []
    for tempdict in freq_list:
        id = tempdict['doc_id']
        for num in tempdict['freq_dict']:
            temp = {'key': num, 'doc_id': id,
                    'tf_score': tempdict['freq_dict'][num] / doc_info[id - 1]['doc_length']}
            tf_score.append(temp)
    return tf_score


def computeIDF(doc_info, freq_list):
    Idf_score = []
    counter = 0
    for tempdict in freq_list:
        counter += 1
        for num in tempdict['freq_dict'].keys():
            count = sum([num in tDict['freq_dict'] for tDict in freq_list])
            temp = {'key': num, 'doc_id': counter,
                    'Idf_score': math.log(len(doc_info) / count)}
            Idf_score.append(temp)
    return Idf_score


class preprocess:
    # text = "I have to say this movie is very \n tense. The disasters in // it make you think, will the/n world's really end this /n way? It's one of those films " \
    #        "where //it gets your mind thinking about // the world around us and how natural disasters can and will happen."
    # #     discard_html(text)
    text=file_read()
    for dict in text:
        text= dict['doc_data']
        parsed_data = discard_punctuation(text)
        parsed_data = tokenize_data(parsed_data)
        parsed_data = remove_stopwords(parsed_data)
        parsed_data = remove_apostrope(parsed_data)
        parsed_data = remove_a_character(parsed_data)
        parsed_data = tokenize_data(parsed_data)
        parsed_data = lemmatize_data(parsed_data)
        parsed_data = sent_tokenize(parsed_data)
        parsed_data = [remove_all_special_character(data) for data in parsed_data]
        doc_info = get_doc_info(parsed_data)
        freq_info = create_freq(parsed_data)
        tf_score = computeTF(doc_info, freq_info)
        idf_score = computeIDF(doc_info, freq_info)
        print(tf_score)
        print("\n")
        print(idf_score)

    #    print(parsed_data)

#    parsed_data=stemming_data(parsed_data)
#    print(parsed_data)

