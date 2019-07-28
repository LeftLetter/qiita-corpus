from gensim.models.fasttext import FastText
from gensim.models import word2vec, Word2Vec

sentences = word2vec.LineSentence('data/qiita_corpus.txt')

# Word2Vec (Skip-gram)
sg_model = Word2Vec(sentences=sentences, size=200, workers=6,
                    min_count=20, window=15, sg=1, iter=5)
sg_model.save('model/sg.model')
print('Finish Skip-gram')

# Word2Vec (CBOW)
cbow_model = Word2Vec(sentences=sentences, size=200, workers=6,
                      min_count=20, window=15, sg=0, iter=5)
cbow_model.save('model/cbow.model')
print('Finish CBOW')

# fastText (Skip-gram)
ft_sg_model = FastText(sentences=sentences, size=200, workers=6,
                       min_count=20, window=15, sg=1, iter=5)
ft_sg_model.save('model/ft_sg.model')
print('Finish fastText Skip-gram')

# fastText (CBOW)
ft_cbow_model = FastText(sentences=sentences, size=200, workers=6,
                         min_count=20, window=15, sg=0, iter=5)
ft_cbow_model.save('model/ft_cbow.model')
print('Finish fastText CBOW')
