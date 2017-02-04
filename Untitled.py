
# coding: utf-8

# In[1]:

import pandas


# In[2]:

ls


# In[3]:

data = pandas.read_csv("movie-pang02.csv")


# In[4]:

data


# In[ ]:




# In[5]:

type(data)


# In[6]:

import nltk


# In[7]:

from nltk.tokenize import sent_tokenize,word_tokenize


# In[8]:

from collections import Counter


# In[9]:

a=Counter([1,2,3,4,5])


# In[10]:

print(a)


# In[11]:

data_pos = data[data["class"] == 'Pos']
data_neg = data[data["class"] == 'Neg']


# In[12]:

print(data_pos)


# In[13]:

positive=[]
negative=[]


# In[15]:

for text in data_pos["text"]:
    sentences=sent_tokenize(text)
    for s in sentences:
        word = word_tokenize(s)
        positive.extend(word)


# In[16]:

positive


# In[17]:

for text in data_neg["text"]:
    sentences=sent_tokenize(text)
    for s in sentences:
        word = word_tokenize(s)
        negative.extend(word)


# In[18]:

negative


# In[20]:

pos_ctr=Counter(positive)


# In[21]:

pos_ctr


# In[22]:

neg_ctr=Counter(negative)


# In[23]:

neg_ctr


# In[24]:

prob = len(positive)+len(negative)


# In[25]:

prob


# In[26]:

len(positive)/prob


# In[27]:

len(negative)/prob


# In[31]:

len(positive)


# In[32]:

len(negative)


# In[37]:

import nltk
stop_words = set(nltk.corpus.stopwords.words('english'))
filtered_pos = [w for w in positive if w not in stop_words]
filtered_neg = [w for w in negative if w not in stop_words]


# In[34]:

filtered_pos


# In[36]:

len(filtered_pos)


# In[38]:

filtered_neg


# In[39]:

negative


# In[40]:

x=Counter(filtered_pos)


# In[41]:

x


# In[43]:

y=Counter(filtered_neg)


# In[46]:

prob_pos=len(filtered_pos)/(len(filtered_pos)+len(filtered_neg))


# In[47]:

prob_pos

prob_neg=len(filtered_neg)/((len(filtered_pos)+len(filtered_neg))
# In[49]:

prob_neg=len(filtered_neg)/(len(filtered_pos)+len(filtered_neg))


# In[50]:

prob_neg


# In[ ]:



