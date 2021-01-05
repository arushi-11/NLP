import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

text = "Hello Everyone we can start the assingment with printing simple things\
so thst it becomes easy to understand what actually we want to achieve using this\
assingment. Hope you enjoy the practical session of today and if you have any\
doubts you can always reach out to me"
token = nltk.word_tokenize(text)
bigrams = ngrams(token,2)
trigrams = ngrams(token,3)
fourgrams = ngrams(token,4)
fivegrams = ngrams(token,5)

#to calculate the tokens of a sentence of sequence of words

print(Counter(bigrams)) #it will print 2 consecutive tokens from the text that we've provided! eg. ('Hello', 'Everyone') and so on ..
print(Counter(trigrams))  #it will print 3 consecutive tokens.
print(Counter(fourgrams))  #it will print 4 consecutive tokens.
print(Counter(fivegrams))   #it will print 5 consecutive tokens.


