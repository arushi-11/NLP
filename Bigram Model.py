#IMPLEMENTATION OF TRIGRAM
#where tokens = 2

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import re
import glob
import random
import seaborn as sns
import string

train_data_sent = pd.read_csv(r'C:\Users\HP\Documents\Arushi\NLP\movie_review.csv')
train_data_sent['sentence_clean'] = train_data_sent['text'].str.replace('[{}]'.format(string.punctuation), '')
train_data_sent['sentence_clean'] = train_data_sent['sentence_clean'].str.lower()
train_data_senti=train_data_sent
train_data_sent=train_data_sent.head(1200) #here, I'am considering my data till 1200 heads out of 50k.
train_data_sent.head()

from collections import defaultdict
from nltk import bigrams, trigrams
from collections import Counter
model = defaultdict(lambda: defaultdict(lambda: 0))



#here, I'm finding the number of occurence of tokens in trigram

for sentence in train_data_sent['sentence_clean']:
    
#Split the sentence into trigrams inorder to count the frequencies of the trigrams
  for w1, w2, w3 in trigrams(sentence.split(), pad_right=True, pad_left=True):       #checking padding of the tokens
    model_2[(w1, w2)][w3] += 1

print("The Number of times *america after* bigram has existed is ",model_2['america']['after'])

for w1 in model_2:
    total_count = float(sum(model_2[w1].values()))
    for w2 in model_2[w1]:
# To calculate the probability of the model
        model_2[w1][w2] /= total_count
print(model_2[w1][w2])
