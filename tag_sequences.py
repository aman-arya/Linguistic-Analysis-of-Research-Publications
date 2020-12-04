#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:30:43 2020

@author: prithvi
"""
import nltk
import pandas as pd
import numpy as np
from tools import *
from matplotlib import pyplot as plt
from nltk import ngrams

bio, comp, fin, math, phy, stats = get_abstract_tags_default() 

bio = bio['0'].to_list()
comp = comp['0'].to_list()
fin = fin['0'].to_list()
math = math['0'].to_list()
phy = phy['0'].to_list()
stats = stats['0'].to_list()

file = open("data/bio/bio_tags.txt", 'w')
for line in bio:
    file.write(line+"\n")
file.close()

file = open("data/computer/computer_tags.txt", 'w')
for line in comp:
    file.write(line+"\n")
file.close()

file = open("data/finance/finance_tags.txt", 'w')
for line in fin:
    file.write(line+"\n")
file.close()

file = open("data/maths/math_tags.txt", 'w')
for line in math:
    file.write(line+"\n")
file.close()

file = open("data/physics/physics_tags.txt", 'w')
for line in phy:
    file.write(line+"\n")
file.close()

file = open("data/stats/statistics_tags.txt", 'w')
for line in stats:
    file.write(line+"\n")
file.close()




file = open("data/bio/bio_tags.txt", 'r')
bio = file.read()
file.close()

file = open("data/computer/computer_tags.txt", 'r')
comp = file.read()
file.close()

file = open("data/finance/finance_tags.txt", 'r')
fin = file.read()
file.close()

file = open("data/maths/math_tags.txt", 'r')
math = file.read()
file.close()

file = open("data/physics/physics_tags.txt", 'r')
phy = file.read()
file.close()

file = open("data/stats/statistics_tags.txt", 'r')
stats = file.read()
file.close()


bio_bigram = nltk.FreqDist(ngrams(bio.split(), 2))
total = bio_bigram.N()
for word in bio_bigram:
    bio_bigram[word] /= float(total)
commonbio = bio_bigram.most_common(100)
pd.DataFrame(commonbio, columns=['bigram', 'count']).to_csv('data/bio/tag_bigrams.csv', index=False)

comp_bigram = nltk.FreqDist(ngrams(comp.split(), 2))
total = comp_bigram.N()
for word in comp_bigram:
    comp_bigram[word] /= float(total)
commoncomp = comp_bigram.most_common(100)
pd.DataFrame(commoncomp, columns=['bigram', 'count']).to_csv('data/computer/tag_bigrams.csv', index=False)

fin_bigram = nltk.FreqDist(ngrams(fin.split(), 2))
total = fin_bigram.N()
for word in fin_bigram:
    fin_bigram[word] /= float(total)
commonfin = fin_bigram.most_common(100)
pd.DataFrame(commonfin, columns=['bigram', 'count']).to_csv('data/finance/tag_bigrams.csv', index=False)

math_bigram = nltk.FreqDist(ngrams(math.split(), 2))
total = math_bigram.N()
for word in math_bigram:
    math_bigram[word] /= float(total)
commonmath = math_bigram.most_common(100)
pd.DataFrame(commonmath, columns=['bigram', 'count']).to_csv('data/maths/tag_bigrams.csv', index=False)

phy_bigram = nltk.FreqDist(ngrams(phy.split(), 2))
total = phy_bigram.N()
for word in phy_bigram:
    phy_bigram[word] /= float(total)
commonphy = phy_bigram.most_common(100)
pd.DataFrame(commonphy, columns=['bigram', 'count']).to_csv('data/physics/tag_bigrams.csv', index=False)



stats_bigram = nltk.FreqDist(ngrams(stats.split(), 2))
total = stats_bigram.N()
for word in stats_bigram:
    stats_bigram[word] /= float(total)
commonstats = stats_bigram.most_common(100)
pd.DataFrame(commonstats, columns=['bigram', 'count']).to_csv('data/stats/tag_bigrams.csv', index=False)

bio_trigram = nltk.FreqDist(ngrams(bio.split(), 3))
total = bio_trigram.N()
for word in bio_trigram:
    bio_trigram[word] /= float(total)
commonbio = bio_trigram.most_common(100)
pd.DataFrame(commonbio, columns=['trigram', 'count']).to_csv('data/bio/tag_trigrams.csv', index=False)

comp_trigram = nltk.FreqDist(ngrams(comp.split(), 3))
total = comp_trigram.N()
for word in comp_trigram:
    comp_trigram[word] /= float(total)
commoncomp = comp_trigram.most_common(100)
pd.DataFrame(commoncomp, columns=['trigram', 'count']).to_csv('data/computer/tag_trigrams.csv', index=False)

fin_trigram = nltk.FreqDist(ngrams(fin.split(), 3))
total = fin_trigram.N()
for word in fin_trigram:
    fin_trigram[word] /= float(total)
commonfin = fin_trigram.most_common(100)
pd.DataFrame(commonfin, columns=['trigram', 'count']).to_csv('data/finance/tag_trigrams.csv', index=False)

math_trigram = nltk.FreqDist(ngrams(math.split(), 3))
total = math_trigram.N()
for word in math_trigram:
    math_trigram[word] /= float(total)
commonmath = math_trigram.most_common(100)
pd.DataFrame(commonmath, columns=['trigram', 'count']).to_csv('data/maths/tag_trigrams.csv', index=False)

phy_trigram = nltk.FreqDist(ngrams(phy.split(), 3))
total = phy_trigram.N()
for word in phy_trigram:
    phy_trigram[word] /= float(total)
commonphy = phy_trigram.most_common(100)
pd.DataFrame(commonphy, columns=['trigram', 'count']).to_csv('data/physics/tag_trigrams.csv', index=False)

stats_trigram = nltk.FreqDist(ngrams(stats.split(), 3))
total = stats_trigram.N()
for word in stats_trigram:
    stats_trigram[word] /= float(total)
commonstats = stats_trigram.most_common(100)
pd.DataFrame(commonstats, columns=['trigram', 'count']).to_csv('data/stats/tag_trigrams.csv', index=False)



bio_4gram = nltk.FreqDist(ngrams(bio.split(), 4))
total = bio_4gram.N()
for word in bio_4gram:
    bio_4gram[word] /= float(total)
commonbio = bio_4gram.most_common(100)
pd.DataFrame(commonbio, columns=['4gram', 'count']).to_csv('data/bio/tag_4grams.csv', index=False)

comp_4gram = nltk.FreqDist(ngrams(comp.split(), 4))
total = comp_4gram.N()
for word in comp_4gram:
    comp_4gram[word] /= float(total)
commoncomp = comp_4gram.most_common(100)
pd.DataFrame(commoncomp, columns=['4gram', 'count']).to_csv('data/computer/tag_4grams.csv', index=False)

fin_4gram = nltk.FreqDist(ngrams(fin.split(), 4))
total = fin_4gram.N()
for word in fin_4gram:
    fin_4gram[word] /= float(total)
commonfin = fin_4gram.most_common(100)
pd.DataFrame(commonfin, columns=['4gram', 'count']).to_csv('data/finance/tag_4grams.csv', index=False)

math_4gram = nltk.FreqDist(ngrams(math.split(), 4))
total = math_4gram.N()
for word in math_4gram:
    math_4gram[word] /= float(total)
commonmath = math_4gram.most_common(100)
pd.DataFrame(commonmath, columns=['4gram', 'count']).to_csv('data/maths/tag_4grams.csv', index=False)

phy_4gram = nltk.FreqDist(ngrams(phy.split(), 4))
total = phy_4gram.N()
for word in phy_4gram:
    phy_4gram[word] /= float(total)
commonphy = phy_4gram.most_common(100)
pd.DataFrame(commonphy, columns=['4gram', 'count']).to_csv('data/physics/tag_4grams.csv', index=False)

stats_4gram = nltk.FreqDist(ngrams(stats.split(), 4))
total = stats_4gram.N()
for word in stats_4gram:
    stats_4gram[word] /= float(total)
commonstats = stats_4gram.most_common(100)
pd.DataFrame(commonstats, columns=['4gram', 'count']).to_csv('data/stats/tag_4grams.csv', index=False)



bio_5gram = nltk.FreqDist(ngrams(bio.split(), 5))
total = bio_5gram.N()
for word in bio_5gram:
    bio_5gram[word] /= float(total)
commonbio = bio_5gram.most_common(100)
pd.DataFrame(commonbio, columns=['5gram', 'count']).to_csv('data/bio/tag_5grams.csv', index=False)

comp_5gram = nltk.FreqDist(ngrams(comp.split(), 5))
total = comp_5gram.N()
for word in comp_5gram:
    comp_5gram[word] /= float(total)
commoncomp = comp_5gram.most_common(100)
pd.DataFrame(commoncomp, columns=['5gram', 'count']).to_csv('data/computer/tag_5grams.csv', index=False)

fin_5gram = nltk.FreqDist(ngrams(fin.split(), 5))
total = fin_5gram.N()
for word in fin_5gram:
    fin_5gram[word] /= float(total)
commonfin = fin_5gram.most_common(100)
pd.DataFrame(commonfin, columns=['5gram', 'count']).to_csv('data/finance/tag_5grams.csv', index=False)

math_5gram = nltk.FreqDist(ngrams(math.split(), 5))
total = math_5gram.N()
for word in math_5gram:
    math_5gram[word] /= float(total)
commonmath = math_5gram.most_common(100)
pd.DataFrame(commonmath, columns=['5gram', 'count']).to_csv('data/maths/tag_5grams.csv', index=False)

phy_5gram = nltk.FreqDist(ngrams(phy.split(), 5))
total = phy_5gram.N()
for word in phy_5gram:
    phy_5gram[word] /= float(total)
commonphy = phy_5gram.most_common(100)
pd.DataFrame(commonphy, columns=['5gram', 'count']).to_csv('data/physics/tag_5grams.csv', index=False)

stats_5gram = nltk.FreqDist(ngrams(stats.split(), 5))
total = stats_5gram.N()
for word in stats_5gram:
    stats_5gram[word] /= float(total)
commonstats = stats_5gram.most_common(100)
pd.DataFrame(commonstats, columns=['5gram', 'count']).to_csv('data/stats/tag_5grams.csv', index=False)



bio_6gram = nltk.FreqDist(ngrams(bio.split(), 6))
total = bio_6gram.N()
for word in bio_6gram:
    bio_6gram[word] /= float(total)
commonbio = bio_6gram.most_common(100)
pd.DataFrame(commonbio, columns=['6gram', 'count']).to_csv('data/bio/tag_6grams.csv', index=False)

comp_6gram = nltk.FreqDist(ngrams(comp.split(), 6))
total = comp_6gram.N()
for word in comp_6gram:
    comp_6gram[word] /= float(total)
commoncomp = comp_6gram.most_common(100)
pd.DataFrame(commoncomp, columns=['6gram', 'count']).to_csv('data/computer/tag_6grams.csv', index=False)

fin_6gram = nltk.FreqDist(ngrams(fin.split(), 6))
total = fin_6gram.N()
for word in fin_6gram:
    fin_6gram[word] /= float(total)
commonfin = fin_6gram.most_common(100)
pd.DataFrame(commonfin, columns=['6gram', 'count']).to_csv('data/finance/tag_6grams.csv', index=False)

math_6gram = nltk.FreqDist(ngrams(math.split(), 6))
total = math_6gram.N()
for word in math_6gram:
    math_6gram[word] /= float(total)
commonmath = math_6gram.most_common(100)
pd.DataFrame(commonmath, columns=['6gram', 'count']).to_csv('data/maths/tag_6grams.csv', index=False)

phy_6gram = nltk.FreqDist(ngrams(phy.split(), 6))
total = phy_6gram.N()
for word in phy_6gram:
    phy_6gram[word] /= float(total)
commonphy = phy_6gram.most_common(100)
pd.DataFrame(commonphy, columns=['6gram', 'count']).to_csv('data/physics/tag_6grams.csv', index=False)

stats_6gram = nltk.FreqDist(ngrams(stats.split(), 6))
total = stats_6gram.N()
for word in stats_6gram:
    stats_6gram[word] /= float(total)
commonstats = stats_6gram.most_common(100)
pd.DataFrame(commonstats, columns=['6gram', 'count']).to_csv('data/stats/tag_6grams.csv', index=False)


