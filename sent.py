# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 13:28:25 2018

@author: Arun Vajrapu
"""

'''
uses TextBlob to obtain sentiment for unique tweets
'''


from textblob import TextBlob
import sys
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
rev_positive = 0
rev_negitive = 0
rev_nuteral = 0

pro_positive = 0
pro_negitive = 0
pro_nuteral = 0


con_positive = 0
con_negitive = 0
con_nuteral = 0

alltweets = pd.read_csv("test.csv")
#sntTweets = pd.read_csv("test.csv")
#print(alltweets['summary'])
for row in alltweets['summary']:
    #print(row)
    blob = TextBlob(str(row))
    #print blob.sentiment.polarity
    if blob.sentiment.polarity > 0:
        rev_positive = rev_positive + 1
    elif blob.sentiment.polarity < 0:
        rev_negitive = rev_negitive + 1 
    elif blob.sentiment.polarity == 0.0:
        rev_nuteral = rev_nuteral + 1
        
        
        
for row in alltweets['pro']:
    #print(row)
    blob = TextBlob(str(row))
    #print blob.sentiment.polarity
    if blob.sentiment.polarity > 0:
        pro_positive = rev_positive + 1
    elif blob.sentiment.polarity < 0:
        pro_negitive = rev_negitive + 1 
    elif blob.sentiment.polarity == 0.0:
        pro_nuteral = rev_nuteral + 1
        
        


for row in alltweets['con']:
    #print(row)
    blob = TextBlob(str(row))
    #print blob.sentiment.polarity
    if blob.sentiment.polarity > 0:
        con_positive = rev_positive + 1
    elif blob.sentiment.polarity < 0:
        con_negitive = rev_negitive + 1 
    elif blob.sentiment.polarity == 0.0:
        con_nuteral = rev_nuteral + 1
        
        
        
        


explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

labels = ['pro_positive','pro_nuteral','pro_negitive']
values = [pro_positive,pro_nuteral,pro_negitive]

fig1, ax1 = plt.subplots()
ax1.pie(values, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()