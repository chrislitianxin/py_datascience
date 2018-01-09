# Python 3

# Be sure you have followed the instructions to download the 98-0.txt,
# the text of A Tale of Two Cities, by Charles Dickens

import collections

file=open('98-0.txt')

# if you want to use stopwords, here's an example of how to do this
stopwords = set(line.strip() for line in open('stopwords'))

# create your data structure here.  F
wordcount={}

# Instantiate a dictionary, and for every word in the file, add to 
# the dictionary if it doesn't exist. If it does, increase the count.
for word in file.read().lower().split():
    word = word.replace(".", "").replace(",", "").replace("\"","")

    if word in stopwords:
        continue
    
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1



# after building your wordcount, you can then sort it and return the first
# n words.  If you want, collections.Counter may be useful.

d = collections.Counter(wordcount)

print(d.most_common(10))

