

import bisect
import itertools
import random
import re

import nltk
from konlpy.corpus import kolaw
from konlpy.tag import Mecab 


def generate_sentence(cfdist, word, num=5):
    sentence = []

    while word!='.':
        sentence.append(word)

        choices, weights = zip(*cfdist[word].items())
        cumdist = list(itertools.accumulate(weights))
        x = random.random() * cumdist[-1]
        word = choices[bisect.bisect(cumdist, x)]

    regEx = re.compile('^J|^E|^X')
    res = ''
    for i in sentence:
        if regEx.match(Mecab.pos(i)==None):
            res += i

        else:
            res += ' '
            res += i
        

    return res


def calc_cfd(doc):
    words = [w for w, t in Mecab().pos(doc)]
    ngrams = nltk.ngrams(words, n=2)
    #condition_pairs = (((w0, w1), w2) for w0, w1, w2 in ngrams)
    return nltk.ConditionalFreqDist(ngrams)

'''def calc_cfd(doc):
    words = [w for w, t in Mecab().pos(doc)]
    ngrams = nltk.ngrams(words, n=3)
    condition_pairs = (((w0, w1), w2) for w0, w1, w2 in ngrams)
    return nltk.ConditionalFreqDist(condition_pairs)
'''

if __name__=='__main__':
    nsents = 5 
    initstr = u'나' 

    doc = open('4294967295.txt', 'rt', encoding='UTF8').read()
    cfd = calc_cfd(doc)

    for i in range(nsents):
        print('%d. %s' % (i, generate_sentence(cfd, initstr)))