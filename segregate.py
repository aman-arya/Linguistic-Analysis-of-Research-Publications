#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:12:30 2020

@author: prithvi
"""

import pandas as pd 
import nltk
from pycontractions import Contractions

train = pd.read_csv("train.csv")

computer = []
physics = []
maths = []
stats = []
bio = []
finance = []

for i in range(len(train)):
    if (train.at[i, "Computer Science"] == 1):
        computer.append([train.at[i, "TITLE"], train.at[i, "ABSTRACT"]])
        
    if (train.at[i, "Physics"] == 1):
        physics.append([train.at[i, "TITLE"], train.at[i, "ABSTRACT"]])
        
    if (train.at[i, "Mathematics"] == 1):
        maths.append([train.at[i, "TITLE"], train.at[i, "ABSTRACT"]])
        
    if (train.at[i, "Statistics"] == 1):
        stats.append([train.at[i, "TITLE"], train.at[i, "ABSTRACT"]])
        
    if (train.at[i, "Quantitative Biology"] == 1):
        bio.append([train.at[i, "TITLE"], train.at[i, "ABSTRACT"]])
        
    if (train.at[i, "Quantitative Finance"] == 1):
        finance.append([train.at[i, "TITLE"], train.at[i, "ABSTRACT"]])
        
del i

bio = pd.DataFrame(bio, columns=['Title', 'Abstract'])
bio.to_csv('data/bio/QuantitativeBiology.csv', index=False)
computer = pd.DataFrame(computer, columns=['Title', 'Abstract'])
computer.to_csv('data/computer/ComputerScience.csv', index=False)
finance = pd.DataFrame(finance, columns=['Title', 'Abstract'])
finance.to_csv('data/finance/QuantitativeFinance.csv', index=False)
maths = pd.DataFrame(maths, columns=['Title', 'Abstract'])
maths.to_csv('data/maths/Mathematics.csv', index=False)
physics = pd.DataFrame(physics, columns=['Title', 'Abstract'])
physics.to_csv('data/physics/Physics.csv', index=False)
stats = pd.DataFrame(stats, columns=['Title', 'Abstract'])
stats.to_csv('data/stats/Statistics.csv', index=False)


# =============================================================================
# cont = Contractions('GoogleNews-vectors-negative300.bin')
# for i in range(len(lower_text)):
#     lower_text[i] = list(cont.expand_texts([lower_text[i]], precise=True))[0]
# =============================================================================
