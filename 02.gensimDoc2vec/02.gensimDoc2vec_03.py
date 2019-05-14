#!/usr/bin/env python
# -*- coding: utf-8 -*-

# load
from konlpy.corpus import kobill
docs_ko = [kobill.open(i).read() for i in kobill.fileids()]

# Tokenize
from konlpy.tag import Twitter;
t = Twitter()
pos = lambda d: ['/'.join(p) for p in t.pos(d)]
texts_ko = [pos(doc) for doc in docs_ko]


# 3.2 word2vec 을 이용한 word embedding

#train
from gensim.models import word2vec

wv_model_ko = word2vec.Word2Vec(texts_ko)
wv_model_ko.init_sims(replace=True)

wv_model_ko.save('ko_words2vec_e.model')

#test
print(wv_model_ko.most_similar(pos('트럼프')))