#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:52:35 2020

@author: prithvi
"""

import pandas as pd
import numpy as np
from tools import *
from matplotlib import pyplot as plt
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

tags, bio, comp, fin, math, phy, stats = get_all_abstract_universal_tag_counts()

# =============================================================================
# Ratios to find:
#     ADV-ADJ
#     ADV-NOUN
#     ADV-PRON
#     ADJ-VERB
#     ADJ-PRON
#     NOUN-PRON
#     VERB-PRON
#     X-NOUNS
# =============================================================================

""" ADV-ADJ """

adv_adj = {'Biology': bio.at['ADV','0']/bio.at['ADJ','0'],
           'Computer Science': comp.at['ADV','0']/comp.at['ADJ','0'],
            'Finance': fin.at['ADV','0']/fin.at['ADJ','0'],
            'Maths': math.at['ADV','0']/math.at['ADJ','0'],
            'Physics': phy.at['ADV','0']/phy.at['ADJ','0'],
            'Statistics': stats.at['ADV','0']/stats.at['ADJ','0']}

subject = list(adv_adj.keys())
counts = list(adv_adj.values())
  

# Figure Size 
fig, ax = plt.subplots(figsize =(20, 10)) 
  
# Horizontal Bar Plot 
ax.barh(subject, counts) 
  
# Remove axes splines 
for s in ['top', 'bottom', 'left', 'right']: 
    ax.spines[s].set_visible(False) 
  
# Remove x, y Ticks 
ax.xaxis.set_ticks_position('none') 
ax.yaxis.set_ticks_position('none') 
  
# Add padding between axes and labels 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 10) 
  
# Add x, y gridlines 
ax.grid(b = True, color ='grey', 
        linestyle ='-.', linewidth = 0.5, 
        alpha = 0.2) 
  
# Show top values  
ax.invert_yaxis() 
  
# Add annotation to bars 
for i in ax.patches: 
    plt.text(i.get_width()+0.2, i.get_y()+0.5,  
             str(round((i.get_width()), 2)), 
             fontsize = 10, fontweight ='bold', 
             color ='grey') 
  
# Add Plot Title 
ax.set_title('Adverbs to Adjective ratios in different classes', 
             loc ='left', ) 
  
# Add Text watermark 
fig.text(0.9, 0.15, 'Linguistics Final Project\nby Prithvi and Aman', fontsize = 12, 
         color ='grey', ha ='right', va ='bottom', 
         alpha = 0.5) 
  
# Show Plot 
plt.savefig('Adverbs_to_Adjective_ratios.png') 


""" ADV-NOUN """

adv_noun = {'Biology': bio.at['ADV','0']/bio.at['NOUN','0'],
           'Computer Science': comp.at['ADV','0']/comp.at['NOUN','0'],
            'Finance': fin.at['ADV','0']/fin.at['NOUN','0'],
            'Maths': math.at['ADV','0']/math.at['NOUN','0'],
            'Physics': phy.at['ADV','0']/phy.at['NOUN','0'],
            'Statistics': stats.at['ADV','0']/stats.at['NOUN','0']}

subject = list(adv_noun.keys())
counts = list(adv_noun.values())
  

# Figure Size 
fig, ax = plt.subplots(figsize =(20, 10)) 
  
# Horizontal Bar Plot 
ax.barh(subject, counts) 
  
# Remove axes splines 
for s in ['top', 'bottom', 'left', 'right']: 
    ax.spines[s].set_visible(False) 
  
# Remove x, y Ticks 
ax.xaxis.set_ticks_position('none') 
ax.yaxis.set_ticks_position('none') 
  
# Add padding between axes and labels 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 10) 
  
# Add x, y gridlines 
ax.grid(b = True, color ='grey', 
        linestyle ='-.', linewidth = 0.5, 
        alpha = 0.2) 
  
# Show top values  
ax.invert_yaxis() 
  
# Add annotation to bars 
for i in ax.patches: 
    plt.text(i.get_width()+0.2, i.get_y()+0.5,  
             str(round((i.get_width()), 2)), 
             fontsize = 10, fontweight ='bold', 
             color ='grey') 
  
# Add Plot Title 
ax.set_title('Adverbs to Nouns ratios in different classes', 
             loc ='left', ) 
  
# Add Text watermark 
fig.text(0.9, 0.15, 'Linguistics Final Project\nby Prithvi and Aman', fontsize = 12, 
         color ='grey', ha ='right', va ='bottom', 
         alpha = 0.5) 
  
# Show Plot 
plt.savefig('Adverbs_to_Nouns_ratios.png') 


""" ADV-PRON """

adv_pron = {'Biology': bio.at['ADV','0']/bio.at['PRON','0'],
           'Computer Science': comp.at['ADV','0']/comp.at['PRON','0'],
            'Finance': fin.at['ADV','0']/fin.at['PRON','0'],
            'Maths': math.at['ADV','0']/math.at['PRON','0'],
            'Physics': phy.at['ADV','0']/phy.at['PRON','0'],
            'Statistics': stats.at['ADV','0']/stats.at['PRON','0']}

subject = list(adv_pron.keys())
counts = list(adv_pron.values())
  

# Figure Size 
fig, ax = plt.subplots(figsize =(20, 10)) 
  
# Horizontal Bar Plot 
ax.barh(subject, counts) 
  
# Remove axes splines 
for s in ['top', 'bottom', 'left', 'right']: 
    ax.spines[s].set_visible(False) 
  
# Remove x, y Ticks 
ax.xaxis.set_ticks_position('none') 
ax.yaxis.set_ticks_position('none') 
  
# Add padding between axes and labels 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 10) 
  
# Add x, y gridlines 
ax.grid(b = True, color ='grey', 
        linestyle ='-.', linewidth = 0.5, 
        alpha = 0.2) 
  
# Show top values  
ax.invert_yaxis() 
  
# Add annotation to bars 
for i in ax.patches: 
    plt.text(i.get_width()+0.2, i.get_y()+0.5,  
             str(round((i.get_width()), 2)), 
             fontsize = 10, fontweight ='bold', 
             color ='grey') 
  
# Add Plot Title 
ax.set_title('Adverbs to Pronouns ratios in different classes', 
             loc ='left', ) 
  
# Add Text watermark 
fig.text(0.9, 0.15, 'Linguistics Final Project\nby Prithvi and Aman', fontsize = 12, 
         color ='grey', ha ='right', va ='bottom', 
         alpha = 0.5) 
  
# Show Plot 
plt.savefig('Adverbs_to_Pronouns_ratios.png') 


""" ADJ-VERB """

adj_verb = {'Biology': bio.at['ADJ','0']/bio.at['VERB','0'],
           'Computer Science': comp.at['ADJ','0']/comp.at['VERB','0'],
            'Finance': fin.at['ADJ','0']/fin.at['VERB','0'],
            'Maths': math.at['ADJ','0']/math.at['VERB','0'],
            'Physics': phy.at['ADJ','0']/phy.at['VERB','0'],
            'Statistics': stats.at['ADJ','0']/stats.at['VERB','0']}

subject = list(adj_verb.keys())
counts = list(adj_verb.values())
  

# Figure Size 
fig, ax = plt.subplots(figsize =(20, 10)) 
  
# Horizontal Bar Plot 
ax.barh(subject, counts) 
  
# Remove axes splines 
for s in ['top', 'bottom', 'left', 'right']: 
    ax.spines[s].set_visible(False) 
  
# Remove x, y Ticks 
ax.xaxis.set_ticks_position('none') 
ax.yaxis.set_ticks_position('none') 
  
# Add padding between axes and labels 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 10) 
  
# Add x, y gridlines 
ax.grid(b = True, color ='grey', 
        linestyle ='-.', linewidth = 0.5, 
        alpha = 0.2) 
  
# Show top values  
ax.invert_yaxis() 
  
# Add annotation to bars 
for i in ax.patches: 
    plt.text(i.get_width()+0.2, i.get_y()+0.5,  
             str(round((i.get_width()), 2)), 
             fontsize = 10, fontweight ='bold', 
             color ='grey') 
  
# Add Plot Title 
ax.set_title('Adjectives to Verbs ratios in different classes', 
             loc ='left', ) 
  
# Add Text watermark 
fig.text(0.9, 0.15, 'Linguistics Final Project\nby Prithvi and Aman', fontsize = 12, 
         color ='grey', ha ='right', va ='bottom', 
         alpha = 0.5) 
  
# Show Plot 
plt.savefig('Adjectives_to_Verbs_ratios.png') 


""" ADJ-PRON """

adj_pron = {'Biology': bio.at['ADJ','0']/bio.at['PRON','0'],
           'Computer Science': comp.at['ADJ','0']/comp.at['PRON','0'],
            'Finance': fin.at['ADJ','0']/fin.at['PRON','0'],
            'Maths': math.at['ADJ','0']/math.at['PRON','0'],
            'Physics': phy.at['ADJ','0']/phy.at['PRON','0'],
            'Statistics': stats.at['ADJ','0']/stats.at['PRON','0']}

subject = list(adj_pron.keys())
counts = list(adj_pron.values())
  

# Figure Size 
fig, ax = plt.subplots(figsize =(20, 10)) 
  
# Horizontal Bar Plot 
ax.barh(subject, counts) 
  
# Remove axes splines 
for s in ['top', 'bottom', 'left', 'right']: 
    ax.spines[s].set_visible(False) 
  
# Remove x, y Ticks 
ax.xaxis.set_ticks_position('none') 
ax.yaxis.set_ticks_position('none') 
  
# Add padding between axes and labels 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 10) 
  
# Add x, y gridlines 
ax.grid(b = True, color ='grey', 
        linestyle ='-.', linewidth = 0.5, 
        alpha = 0.2) 
  
# Show top values  
ax.invert_yaxis() 
  
# Add annotation to bars 
for i in ax.patches: 
    plt.text(i.get_width()+0.2, i.get_y()+0.5,  
             str(round((i.get_width()), 2)), 
             fontsize = 10, fontweight ='bold', 
             color ='grey') 
  
# Add Plot Title 
ax.set_title('Adjectives to Pronouns ratios in different classes', 
             loc ='left', ) 
  
# Add Text watermark 
fig.text(0.9, 0.15, 'Linguistics Final Project\nby Prithvi and Aman', fontsize = 12, 
         color ='grey', ha ='right', va ='bottom', 
         alpha = 0.5) 
  
# Show Plot 
plt.savefig('Adjectives_to_Pronouns_ratios.png') 


""" NOUN-PRON """

noun_pron = {'Biology': bio.at['NOUN','0']/bio.at['PRON','0'],
           'Computer Science': comp.at['NOUN','0']/comp.at['PRON','0'],
            'Finance': fin.at['NOUN','0']/fin.at['PRON','0'],
            'Maths': math.at['NOUN','0']/math.at['PRON','0'],
            'Physics': phy.at['NOUN','0']/phy.at['PRON','0'],
            'Statistics': stats.at['NOUN','0']/stats.at['PRON','0']}

subject = list(noun_pron.keys())
counts = list(noun_pron.values())
  

# Figure Size 
fig, ax = plt.subplots(figsize =(20, 10)) 
  
# Horizontal Bar Plot 
ax.barh(subject, counts) 
  
# Remove axes splines 
for s in ['top', 'bottom', 'left', 'right']: 
    ax.spines[s].set_visible(False) 
  
# Remove x, y Ticks 
ax.xaxis.set_ticks_position('none') 
ax.yaxis.set_ticks_position('none') 
  
# Add padding between axes and labels 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 10) 
  
# Add x, y gridlines 
ax.grid(b = True, color ='grey', 
        linestyle ='-.', linewidth = 0.5, 
        alpha = 0.2) 
  
# Show top values  
ax.invert_yaxis() 
  
# Add annotation to bars 
for i in ax.patches: 
    plt.text(i.get_width()+0.2, i.get_y()+0.5,  
             str(round((i.get_width()), 2)), 
             fontsize = 10, fontweight ='bold', 
             color ='grey') 
  
# Add Plot Title 
ax.set_title('Nouns to Pronouns ratios in different classes', 
             loc ='left', ) 
  
# Add Text watermark 
fig.text(0.9, 0.15, 'Linguistics Final Project\nby Prithvi and Aman', fontsize = 12, 
         color ='grey', ha ='right', va ='bottom', 
         alpha = 0.5) 
  
# Show Plot 
plt.savefig('Nouns_to_Pronouns_ratios.png') 


""" VERB-PRON """

verb_pron = {'Biology': bio.at['VERB','0']/bio.at['PRON','0'],
           'Computer Science': comp.at['VERB','0']/comp.at['PRON','0'],
            'Finance': fin.at['VERB','0']/fin.at['PRON','0'],
            'Maths': math.at['VERB','0']/math.at['PRON','0'],
            'Physics': phy.at['VERB','0']/phy.at['PRON','0'],
            'Statistics': stats.at['VERB','0']/stats.at['PRON','0']}

subject = list(verb_pron.keys())
counts = list(verb_pron.values())
  

# Figure Size 
fig, ax = plt.subplots(figsize =(20, 10)) 
  
# Horizontal Bar Plot 
ax.barh(subject, counts) 
  
# Remove axes splines 
for s in ['top', 'bottom', 'left', 'right']: 
    ax.spines[s].set_visible(False) 
  
# Remove x, y Ticks 
ax.xaxis.set_ticks_position('none') 
ax.yaxis.set_ticks_position('none') 
  
# Add padding between axes and labels 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 10) 
  
# Add x, y gridlines 
ax.grid(b = True, color ='grey', 
        linestyle ='-.', linewidth = 0.5, 
        alpha = 0.2) 
  
# Show top values  
ax.invert_yaxis() 
  
# Add annotation to bars 
for i in ax.patches: 
    plt.text(i.get_width()+0.2, i.get_y()+0.5,  
             str(round((i.get_width()), 2)), 
             fontsize = 10, fontweight ='bold', 
             color ='grey') 
  
# Add Plot Title 
ax.set_title('Verbs to Pronouns ratios in different classes', 
             loc ='left', ) 
  
# Add Text watermark 
fig.text(0.9, 0.15, 'Linguistics Final Project\nby Prithvi and Aman', fontsize = 12, 
         color ='grey', ha ='right', va ='bottom', 
         alpha = 0.5) 
  
# Show Plot 
plt.savefig('Verbs_to_Pronouns_ratios.png') 


""" X-NOUN """

x_noun = {'Biology': bio.at['X','0']/bio.at['NOUN','0'],
           'Computer Science': comp.at['X','0']/comp.at['NOUN','0'],
            'Finance': fin.at['X','0']/fin.at['NOUN','0'],
            'Maths': math.at['X','0']/math.at['NOUN','0'],
            'Physics': phy.at['X','0']/phy.at['NOUN','0'],
            'Statistics': stats.at['X','0']/stats.at['NOUN','0']}

subject = list(x_noun.keys())
counts = list(x_noun.values())
  

# Figure Size 
fig, ax = plt.subplots(figsize =(20, 10)) 
  
# Horizontal Bar Plot 
ax.barh(subject, counts) 
  
# Remove axes splines 
for s in ['top', 'bottom', 'left', 'right']: 
    ax.spines[s].set_visible(False) 
  
# Remove x, y Ticks 
ax.xaxis.set_ticks_position('none') 
ax.yaxis.set_ticks_position('none') 
  
# Add padding between axes and labels 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 10) 
  
# Add x, y gridlines 
ax.grid(b = True, color ='grey', 
        linestyle ='-.', linewidth = 0.5, 
        alpha = 0.2) 
  
# Show top values  
ax.invert_yaxis() 
  
# Add annotation to bars 
for i in ax.patches: 
    plt.text(i.get_width()+0.2, i.get_y()+0.5,  
             str(round((i.get_width()), 2)), 
             fontsize = 10, fontweight ='bold', 
             color ='grey') 
  
# Add Plot Title 
ax.set_title('Cardinals to Nouns ratios in different classes', 
             loc ='left', ) 
  
# Add Text watermark 
fig.text(0.9, 0.15, 'Linguistics Final Project\nby Prithvi and Aman', fontsize = 12, 
         color ='grey', ha ='right', va ='bottom', 
         alpha = 0.5) 
  
# Show Plot 
plt.savefig('Cardinals_to_Nouns_ratios.png') 