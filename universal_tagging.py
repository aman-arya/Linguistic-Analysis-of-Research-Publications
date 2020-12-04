#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:00:42 2020

@author: prithvi
"""

import pandas as pd 
import nltk
from nltk.tag import pos_tag, map_tag
from nltk.tokenize import word_tokenize



def universal_tagger(folder, file):
    data = pd.read_csv('data/%s' % file)

    titles = data['Title'].tolist()
    abstracts = data['Abstract'].tolist()
    
    del data
    
    """ For sequencing, we use the Stanford POS Tagger"""
    
    title_tags = []
    abstract_tags = []
    
    for i in range(len(titles)):
        sent_t = titles[i]
        sent_a = abstracts[i]
        
        tag_t = pos_tag(nltk.word_tokenize(sent_t))
        tag_a = pos_tag(nltk.word_tokenize(sent_a))
        
        tag_t = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in tag_t]
        tag_a = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in tag_a]
        
        sentence = tag_t[0][1]
        for j in range(1, len(tag_t)):
            sentence += ' '+tag_t[j][1]
        
        title_tags.append(sentence)
        
        sentence = tag_a[0][1]
        for j in range(1, len(tag_a)):
            sentence += ' '+tag_a[j][1]
        
        abstract_tags.append(sentence)
        
        
    title_tags = pd.DataFrame(title_tags)
    abstract_tags = pd.DataFrame(abstract_tags)
    title_tags.to_csv('data/%s/title_tags_universal.csv' % folder, index=False)
    abstract_tags.to_csv('data/%s/abstract_tags_universal.csv' % folder, index=False)


dataset = [['bio', 'QuantitativeBiology.csv'], 
           ['computer', 'ComputerScience.csv'], 
           ['finance', 'QuantitativeFinance.csv'], 
           ['maths', 'Mathematics.csv'], 
           ['physics', 'Physics.csv'], 
           ['stats', 'Statistics.csv']]

for data in dataset:
    universal_tagger(data[0], data[1])
    print(data[1]+" done")
        


