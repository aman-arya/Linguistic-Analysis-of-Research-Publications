#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 01:22:08 2020

@author: prithvi
"""

import pandas as pd 
import nltk

# =============================================================================
# NOUN (nouns)
# VERB (verbs)
# ADJ (adjectives)
# ADV (adverbs)
# PRON (pronouns)
# DET (determiners and articles)
# ADP (prepositions and postpositions)
# NUM (numerals)
# CONJ (conjunctions)
# PRT (particles)
# . (punctuation marks)
# X (a catch-all for other categories such as abbreviations or foreign words)
# =============================================================================

def gen_abstract_universal_count(folder, file):
    data = pd.read_csv('data/%s/%s' % (folder, file))
    data = data['0'].tolist()
    tags = {}
    
    for i in range(len(data)):
        sent = data[i].split()
        for tag in sent:
            if (tag not in tags.keys()):
                tags[tag] = 1
            else:
                tags[tag] += 1
    
        
    tags = pd.DataFrame.from_dict(tags, orient='index')
    tags.to_csv('data/%s/abstract_tags_universal_counts.csv' % folder, index=True)
    

dataset = [['bio', 'abstract_tags_universal.csv'], 
           ['computer', 'abstract_tags_universal.csv'], 
           ['finance', 'abstract_tags_universal.csv'], 
           ['maths', 'abstract_tags_universal.csv'], 
           ['physics', 'abstract_tags_universal.csv'], 
           ['stats', 'abstract_tags_universal.csv']]

for data in dataset:
    gen_abstract_universal_count(data[0], data[1])
    print(data[1]+" done")
    
    
def gen_title_universal_count(folder, file):
    data = pd.read_csv('data/%s/%s' % (folder, file))
    data = data['0'].tolist()
    tags = {}
    
    for i in range(len(data)):
        sent = data[i].split()
        for tag in sent:
            if (tag not in tags.keys()):
                tags[tag] = 1
            else:
                tags[tag] += 1
    
        
    tags = pd.DataFrame.from_dict(tags, orient='index')
    tags.to_csv('data/%s/title_tags_universal_counts.csv' % folder, index=True)
    

dataset = [['bio', 'title_tags_universal.csv'], 
           ['computer', 'title_tags_universal.csv'], 
           ['finance', 'title_tags_universal.csv'], 
           ['maths', 'title_tags_universal.csv'], 
           ['physics', 'title_tags_universal.csv'], 
           ['stats', 'title_tags_universal.csv']]

for data in dataset:
    gen_title_universal_count(data[0], data[1])
    print(data[1]+" done")