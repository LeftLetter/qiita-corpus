import pprint
from gensim.models.fasttext import FastText
from gensim.models import Word2Vec


# 単語
positive = []
negative = []

# データ読み込み
sg_model = Word2Vec.load('model/sg.model')
cbow_model = Word2Vec.load('model/cbow.model')
ft_sg_model = FastText.load('model/ft_sg.model')
ft_cbow_model = FastText.load('model/ft_cbow.model')

# Word2Vec (Skip-gram)
similar_words = sg_model.wv.most_similar(
    positive=positive, negative=negative, topn=5)
print('Word2Vec (Skip-gram)')
pprint.pprint(similar_words)
print()

# Word2Vec (CBOW)
similar_words = cbow_model.wv.most_similar(
    positive=positive, negative=negative, topn=5)
print('Word2Vec (CBOW)')
pprint.pprint(similar_words)
print()

# fastText (Skip-gram)
similar_words = ft_sg_model.wv.most_similar(
    positive=positive, negative=negative, topn=5)
print('fastText (Skip-gram)')
pprint.pprint(similar_words)
print()

# fastText (CBOW)
similar_words = ft_cbow_model.wv.most_similar(
    positive=positive, negative=negative, topn=5)
print('fastText (CBOW)')
pprint.pprint(similar_words)
print()
