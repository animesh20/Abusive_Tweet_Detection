
# coding: utf-8

# In[1]:


import sys
sys.path.append('../src')
import data_io, params, SIF_embedding
import numpy as np


# In[2]:


# input
wordfile = '../data/glove.840B.300d.txt' # word vector file, can be downloaded from GloVe website
weightfile = '../auxiliary_data/enwiki_vocab_min200.txt' # each line is a word and its frequency
weightpara = 1e-3 # the parameter in the SIF weighting scheme, usually in the range [3e-5, 3e-3]
rmpc = 1 # number of principal components to remove in SIF weighting scheme

# Load sentences
sentences = []
with open('sentences.txt') as f:
    for line in f:
        sentences.append(line.strip())
print(len(sentences))


# In[ ]:


# load word vectors
(words, We) = data_io.getWordmap(wordfile)
# load word weights
word2weight = data_io.getWordWeight(weightfile, weightpara) # word2weight['str'] is the weight for the word 'str'
weight4ind = data_io.getWeight(words, word2weight) # weight4ind[i] is the weight for the i-th word
# load sentences
x, m, _ = data_io.sentences2idx(sentences, words) # x is the array of word indices, m is the binary mask indicating whether there is a word in that location
w = data_io.seq2weight(x, m, weight4ind) # get word weights


# In[ ]:


# set parameters
params = params.params()
params.rmpc = rmpc
# get SIF embedding
embeddings = SIF_embedding.SIF_embedding(We, x, w, params) # embedding[i,:] is the embedding for sentence i


# In[ ]:


np.save('embeddings',embeddings)
loaded_embeddings = np.load('embeddings.npy')
print(len(loaded_embeddings))
print(loaded_embeddings[0])

