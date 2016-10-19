from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import os
import logging

class TopicExtrator(object):

	def __init__(self, path):
		self.tokens = []
		self.take = path
		a = path.split('/')
		b = a[-1].split('.')
		self.name = b[0]

	def makeTokens(self):
		en_stop = stopwords.words('english')
		tokenizer = RegexpTokenizer(r'\w+')
		p_stemmer = PorterStemmer()
		sentences = self.readFile()

		for i in sentences:
			i = i.lower().replace("\n","")
			token =  tokenizer.tokenize(i)
			stopped_tokens = [i for i in token if not i in en_stop]
			stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
			self.tokens.append(stemmed_tokens)

	def readFile(self):
		f = open("{}".format(self.take), "r")
		vocab = f.readlines()
		return vocab

	def ldaModel(self):
		dictionary = corpora.Dictionary(self.tokens)
		dictionary.save('{}.dict'.format(self.name))
		#logging.basicConfig(format = '%(asctime)s : %(levelname)s : %(message)s', level = logging.INFO)
		corpus = [dictionary.doc2bow(text) for text in self.tokens]
		corpora.MmCorpus.serialize('{}.mm'.format(self.name), corpus)
		mm = corpora.MmCorpus('{}.mm'.format(self.name))
		
		lda = gensim.models.ldamodel.LdaModel(corpus = mm, num_topics=8, id2word = dictionary, passes=20)
		#save(fname, ignore=['state', 'dispatcher'], *args, **kwargs)
		print(lda.print_topics(50))

if __name__ == "__main__":
	k = TopicExtrator("test_file.txt")
	k.makeTokens()
	k.ldaModel()





