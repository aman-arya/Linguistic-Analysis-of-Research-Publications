#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 09:43:48 2020

@author: prithvi
"""

import numpy as np
import pandas as pd 
import nltk
from nltk.tag import pos_tag, map_tag
from nltk.tokenize import word_tokenize


def plot_confusion_matrix(folder, cm, target_names, title='POS_Tags_confusion_matrix', cmap=None, normalize=True):
    
    import matplotlib.pyplot as plt
    import numpy as np
    import itertools

    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure(figsize=(12, 12))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45)
        plt.yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    plt.tight_layout()
    plt.ylabel('True POS Tags')
    plt.xlabel('Predicted POS Tags\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
    plt.show()
    plt.savefig('data/%s/%s.png' % (folder, title)) 


d = [['bio', 'QuantitativeBiology.csv'], 
           ['computer', 'ComputerScience.csv'], 
           ['finance', 'QuantitativeFinance.csv'], 
           ['maths', 'Mathematics.csv'], 
           ['physics', 'Physics.csv'], 
           ['stats', 'Statistics.csv']]


data = pd.read_csv('data/%s' %d[5][1])
abstracts = data['Abstract'].tolist()
test_tags = []
true_tags = []
tags = []

for sent in abstracts:
    tag_a = pos_tag(nltk.word_tokenize(sent))
    for i in range(len(tag_a)):
        test_tags.append(tag_a[i][1])
        if (test_tags[-1] not in tags):
            tags.append(test_tags[-1])
        true_tags.append(pos_tag([tag_a[i][0]])[0][1])
        
mat = nltk.ConfusionMatrix(true_tags, test_tags)
plot_confusion_matrix(folder = d[5][0], cm = np.array(mat._confusion),
                      normalize = False,
                      target_names = tags,
                      title = "%s_POS_Tags_confusion_matrix" % d[5][1])








    
    
    
