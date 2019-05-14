#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
from konlpy.corpus import kobill
from konlpy.tag import Twitter
from gensim import models
from gensim import corpora
import numpy as np



docs_ko = [kobill.open(i).read() for i in kobill.fileids()]

#tokenize
t=Twitter()
pos = lambda d: ['/'.join(p)for p in t.pos(d)]
texts_ko = [pos(doc) for doc in docs_ko]



#e.g.
#3.1 topic modeling(LSI, LDA, HDP algorithm)

#encode tokens to integers
dictionary_ko = corpora.Dictionary(texts_ko)
dictionary_ko.save('ko.dict') #save dictionary to file for futre use

# calculate Tf-IDF
tf_ko = [dictionary_ko.doc2bow(text) for text in texts_ko]
tfidf_model_ko = models.TfidfModel(tf_ko)
tfidf_ko = tfidf_model_ko[tf_ko]
corpora.MmCorpus.serialize('ko.mm', tfidf_ko) #save corpus to file for future use


#train topic model
#LSI
ntopics, nwords = 3, 5
lsi_ko = models.lsimodel.LsiModel(tfidf_ko, id2word=dictionary_ko, num_topics=ntopics)
print(lsi_ko.print_topics(num_topics=ntopics, num_words=nwords))

#LDA
np.random.seed(42) # optional
lda_ko = models.ldamodel.LdaModel(tfidf_ko, id2word=dictionary_ko, num_topics=ntopics)
print(lda_ko.print_topics(num_topics=ntopics, num_words=nwords))

#HDP
np.random.seed(42)
hdp_ko = models.hdpmodel.HdpModel(tfidf_ko, id2word=dictionary_ko)
print(hdp_ko.print_topics(num_topics=ntopics, num_words = nwords))


#scoreing document
bow = tfidf_model_ko[dictionary_ko.doc2bow(texts_ko[0])]
sorted(lsi_ko[bow], key=lambda x: x[1], reverse=True)
sorted(lda_ko[bow], key=lambda x: x[1], reverse=True)
sorted(hdp_ko[bow], key=lambda x: x[1], reverse=True)

bow = tfidf_model_ko[dictionary_ko.doc2bow(texts_ko[1])]
sorted(lsi_ko[bow], key=lambda x: x[1], reverse=True)
sorted(lda_ko[bow], key=lambda x: x[1], reverse=True)
sorted(hdp_ko[bow], key=lambda x: x[1], reverse=True)


