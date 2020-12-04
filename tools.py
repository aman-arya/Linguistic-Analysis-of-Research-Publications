#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 00:30:10 2020

@author: prithvi
"""

import numpy as np
import pandas as pd

def get_abstract_vocab_count(subject):
    vocab = [['bio', 'abstract_vocabulary.csv'],
             ['computer', 'abstract_vocabulary.csv'], 
             ['finance', 'abstract_vocabulary.csv'], 
             ['maths', 'abstract_vocabulary.csv'], 
             ['physics', 'abstract_vocabulary.csv'], 
             ['stats', 'abstract_vocabulary.csv']]
    
    if (subject == 'bio'):
        return sum(pd.read_csv('data/%s/%s' % (vocab[0][0], vocab[0][1]))['count'].to_list())
    elif (subject == 'computer'):
        return sum(pd.read_csv('data/%s/%s' % (vocab[1][0], vocab[0][1]))['count'].to_list())
    elif (subject == 'finance'):
        return sum(pd.read_csv('data/%s/%s' % (vocab[2][0], vocab[0][1]))['count'].to_list())
    elif (subject == 'maths'):
        return sum(pd.read_csv('data/%s/%s' % (vocab[3][0], vocab[0][1]))['count'].to_list())
    elif (subject == 'physics'):
        return sum(pd.read_csv('data/%s/%s' % (vocab[4][0], vocab[0][1]))['count'].to_list())
    elif (subject == 'stats'):
        return sum(pd.read_csv('data/%s/%s' % (vocab[5][0], vocab[0][1]))['count'].to_list())
    else:
        raise Exception("wrong subject or subject code entered")
    

def get_all_abstract_universal_tag_counts():
    dataset = [['bio', 'abstract_tags_universal_counts.csv'], 
           ['computer', 'abstract_tags_universal_counts.csv'], 
           ['finance', 'abstract_tags_universal_counts.csv'], 
           ['maths', 'abstract_tags_universal_counts.csv'], 
           ['physics', 'abstract_tags_universal_counts.csv'], 
           ['stats', 'abstract_tags_universal_counts.csv']]

    tags = pd.read_csv('data/%s/%s' % (dataset[0][0], dataset[0][1]))['Unnamed: 0'].to_list()
    bio = pd.read_csv('data/%s/%s' % (dataset[0][0], dataset[0][1])).set_index('Unnamed: 0')
    comp = pd.read_csv('data/%s/%s' % (dataset[1][0], dataset[0][1])).set_index('Unnamed: 0')
    fin = pd.read_csv('data/%s/%s' % (dataset[2][0], dataset[0][1])).set_index('Unnamed: 0')
    math = pd.read_csv('data/%s/%s' % (dataset[3][0], dataset[0][1])).set_index('Unnamed: 0')
    phy = pd.read_csv('data/%s/%s' % (dataset[4][0], dataset[0][1])).set_index('Unnamed: 0')
    stats = pd.read_csv('data/%s/%s' % (dataset[5][0], dataset[0][1])).set_index('Unnamed: 0')
    
    return tags, bio, comp, fin, math, phy, stats


def get_abstract_universal_tags_dictionary():
    
    tags, bio, comp, fin, math, phy, stats = get_all_abstract_universal_tag_counts()
    
    nouns = {'Biology': bio.at['NOUN','0']/get_abstract_vocab_count('bio'),
            'Computer Science': comp.at['NOUN','0']/get_abstract_vocab_count('computer'),
            'Finance': fin.at['NOUN','0']/get_abstract_vocab_count('finance'),
            'Maths': math.at['NOUN','0']/get_abstract_vocab_count('maths'),
            'Physics': phy.at['NOUN','0']/get_abstract_vocab_count('physics'),
            'Statistics': stats.at['NOUN','0']/get_abstract_vocab_count('stats')}

    verbs = {'Biology': bio.at['VERB','0']/get_abstract_vocab_count('bio'),
            'Computer Science': comp.at['VERB','0']/get_abstract_vocab_count('computer'),
            'Finance': fin.at['VERB','0']/get_abstract_vocab_count('finance'),
            'Maths': math.at['VERB','0']/get_abstract_vocab_count('maths'),
            'Physics': phy.at['VERB','0']/get_abstract_vocab_count('physics'),
            'Statistics': stats.at['VERB','0']/get_abstract_vocab_count('stats')}
    
    adpositions = {'Biology': bio.at['ADP','0']/get_abstract_vocab_count('bio'),
            'Computer Science': comp.at['ADP','0']/get_abstract_vocab_count('computer'),
            'Finance': fin.at['ADP','0']/get_abstract_vocab_count('finance'),
            'Maths': math.at['ADP','0']/get_abstract_vocab_count('maths'),
            'Physics': phy.at['ADP','0']/get_abstract_vocab_count('physics'),
            'Statistics': stats.at['ADP','0']/get_abstract_vocab_count('stats')}
    
    adjectives = {'Biology': bio.at['ADJ','0']/get_abstract_vocab_count('bio'),
            'Computer Science': comp.at['ADJ','0']/get_abstract_vocab_count('computer'),
            'Finance': fin.at['ADJ','0']/get_abstract_vocab_count('finance'),
            'Maths': math.at['ADJ','0']/get_abstract_vocab_count('maths'),
            'Physics': phy.at['ADJ','0']/get_abstract_vocab_count('physics'),
            'Statistics': stats.at['ADJ','0']/get_abstract_vocab_count('stats')}
    
    particles = {'Biology': bio.at['PRT','0']/get_abstract_vocab_count('bio'),
            'Computer Science': comp.at['PRT','0']/get_abstract_vocab_count('computer'),
            'Finance': fin.at['PRT','0']/get_abstract_vocab_count('finance'),
            'Maths': math.at['PRT','0']/get_abstract_vocab_count('maths'),
            'Physics': phy.at['PRT','0']/get_abstract_vocab_count('physics'),
            'Statistics': stats.at['PRT','0']/get_abstract_vocab_count('stats')}
    
    conjunctions = {'Biology': bio.at['CONJ','0']/get_abstract_vocab_count('bio'),
            'Computer Science': comp.at['CONJ','0']/get_abstract_vocab_count('computer'),
            'Finance': fin.at['CONJ','0']/get_abstract_vocab_count('finance'),
            'Maths': math.at['CONJ','0']/get_abstract_vocab_count('maths'),
            'Physics': phy.at['CONJ','0']/get_abstract_vocab_count('physics'),
            'Statistics': stats.at['CONJ','0']/get_abstract_vocab_count('stats')}
    
    punctuations = {'Biology': bio.at['.','0']/get_abstract_vocab_count('bio'),
            'Computer Science': comp.at['.','0']/get_abstract_vocab_count('computer'),
            'Finance': fin.at['.','0']/get_abstract_vocab_count('finance'),
            'Maths': math.at['.','0']/get_abstract_vocab_count('maths'),
            'Physics': phy.at['.','0']/get_abstract_vocab_count('physics'),
            'Statistics': stats.at['.','0']/get_abstract_vocab_count('stats')}
    
    adverbs = {'Biology': bio.at['ADV','0']/get_abstract_vocab_count('bio'),
            'Computer Science': comp.at['ADV','0']/get_abstract_vocab_count('computer'),
            'Finance': fin.at['ADV','0']/get_abstract_vocab_count('finance'),
            'Maths': math.at['ADV','0']/get_abstract_vocab_count('maths'),
            'Physics': phy.at['ADV','0']/get_abstract_vocab_count('physics'),
            'Statistics': stats.at['ADV','0']/get_abstract_vocab_count('stats')}
    
    determinants = {'Biology': bio.at['DET','0']/get_abstract_vocab_count('bio'),
            'Computer Science': comp.at['DET','0']/get_abstract_vocab_count('computer'),
            'Finance': fin.at['DET','0']/get_abstract_vocab_count('finance'),
            'Maths': math.at['DET','0']/get_abstract_vocab_count('maths'),
            'Physics': phy.at['DET','0']/get_abstract_vocab_count('physics'),
            'Statistics': stats.at['DET','0']/get_abstract_vocab_count('stats')}
    
    pronouns = {'Biology': bio.at['PRON','0']/get_abstract_vocab_count('bio'),
            'Computer Science': comp.at['PRON','0']/get_abstract_vocab_count('computer'),
            'Finance': fin.at['PRON','0']/get_abstract_vocab_count('finance'),
            'Maths': math.at['PRON','0']/get_abstract_vocab_count('maths'),
            'Physics': phy.at['PRON','0']/get_abstract_vocab_count('physics'),
            'Statistics': stats.at['PRON','0']/get_abstract_vocab_count('stats')}
    
    foreign_words = {'Biology': bio.at['X','0']/get_abstract_vocab_count('bio'),
            'Computer Science': comp.at['X','0']/get_abstract_vocab_count('computer'),
            'Finance': fin.at['X','0']/get_abstract_vocab_count('finance'),
            'Maths': math.at['X','0']/get_abstract_vocab_count('maths'),
            'Physics': phy.at['X','0']/get_abstract_vocab_count('physics'),
            'Statistics': stats.at['X','0']/get_abstract_vocab_count('stats')}
    
    cardinals = {'Biology': bio.at['NUM','0']/get_abstract_vocab_count('bio'),
            'Computer Science': comp.at['NUM','0']/get_abstract_vocab_count('computer'),
            'Finance': fin.at['NUM','0']/get_abstract_vocab_count('finance'),
            'Maths': math.at['NUM','0']/get_abstract_vocab_count('maths'),
            'Physics': phy.at['NUM','0']/get_abstract_vocab_count('physics'),
            'Statistics': stats.at['NUM','0']/get_abstract_vocab_count('stats')} 
    
    return nouns, verbs, adpositions, adjectives, particles, conjunctions, punctuations, adverbs, determinants, pronouns, foreign_words, cardinals 

def get_abstract_tags_default():
    dataset = [['bio', 'abstract_tags_default.csv'], 
           ['computer', 'abstract_tags_default.csv'], 
           ['finance', 'abstract_tags_default.csv'], 
           ['maths', 'abstract_tags_default.csv'], 
           ['physics', 'abstract_tags_default.csv'], 
           ['stats', 'abstract_tags_default.csv']]
    
    bio = pd.read_csv('data/%s/%s' % (dataset[0][0], dataset[0][1]))
    comp = pd.read_csv('data/%s/%s' % (dataset[1][0], dataset[0][1]))
    fin = pd.read_csv('data/%s/%s' % (dataset[2][0], dataset[0][1]))
    math = pd.read_csv('data/%s/%s' % (dataset[3][0], dataset[0][1]))
    phy = pd.read_csv('data/%s/%s' % (dataset[4][0], dataset[0][1]))
    stats = pd.read_csv('data/%s/%s' % (dataset[5][0], dataset[0][1]))
    
    return bio, comp, fin, math, phy, stats 