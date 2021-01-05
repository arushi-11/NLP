import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import re
import glob
import random
import seaborn as sns
import string

#taking text corpus and working with real movie review dataset have 50k lines! 
train_data_sent = pd.read_csv('/content/drive/MyDrive/MOVIE_REVIEWS/movie_review.csv')

#data preprocessing
train_data_sent['sentence_clean'] = train_data_sent['text'].str.replace('[{}]'.format(string.punctuation), '')
train_data_sent['sentence_clean'] = train_data_sent['sentence_clean'].str.lower()
train_data_senti=train_data_sent
train_data_sent=train_data_sent.head(1000)
#printing text with sentence_clean
print(train_data_sent.head())
