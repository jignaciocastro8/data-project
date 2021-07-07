
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import gensim


import pyLDAvis.gensim
import chart_studio
import chart_studio.plotly as py 
import chart_studio.tools as tls

plt.style.use('seaborn')

#data_path = "data/santiago_covid_2020.csv"
#data_path = "data/santiago_enero.csv"
data_path = "data/gabrielboric.csv"



# spanish stop words
stop_words = set(stopwords.words('spanish'))
stop_words = ['t', 'si', 'q', 'https', 'co', 'solo', 'ser', 'bien', 
            'así', 'ma', 'mas', 'igual', 'va', 'después',
            'hacer', 'hace', 'creo'] + list(stop_words)


def delete_chars(text, unwanted_chars):
    """
    useful method to replace a list of chars on text.
    return:
        (str) the same str without the chars in chars.
    """
    for char in unwanted_chars:
        text = text.replace(char, '')
    return text

def preprocess_tweet(tweet):
    """
    Replaces unwanted characters and performs
    a preprocessing.
    input: 
        (str) tweet.
    return:
        (str[]) final: list of words.
    """
    unwanted = ['#', ',', '.', '!', '?', '¿', '¡', '()',                ')', '-', '=', 'jaja', 'jajaja']
    final = delete_chars(tweet, unwanted).split()
    final = [w.lower() for w in final]
    final = [w for w in final if w not in stop_words and len(w) > 3]
    # Se eliminan links y @users
    final = [w for w in final if w[:4] != 'http']
    final = [w for w in final if w[:1] != '@']
    return final
    



# Se pre-procesan los tweets: Esto transforma cada
# tweet en una colección de palabras.
# processed_tweets corresponde a una lista de listas de palabras.

data = pd.read_csv(data_path)[['date', 'tweet']]
processed_tweets = data['tweet'].map(preprocess_tweet)
processed_tweets.head()

# Se van a eliminar tweets pequeños: con menos de 5 palabras después
# del preprocessing.
dropers = []
for ind, tweet in enumerate(processed_tweets):
    if len(tweet) < 5:
        dropers.append(ind) 

processed_tweets = processed_tweets.drop(dropers)
processed_tweets.sample(5)


# Se crea el vocabulario. 
# Corresponde a crear una lista con todas las palabras involucrada 
# en el corpus asignando un índice único a cada una.

dictionary = gensim.corpora.Dictionary(processed_tweets)


# Se transforman las palabras a vectores con el dictionary.
# bow = "bag of words"

bow_corpus = [dictionary.doc2bow(doc) for doc in processed_tweets]

# Con esto cada tweet se representa como una colección de tuplas (w, a) 
# donde w es el índice de la palabra y a la cantidad de apariciones en ese
# tweet.



# Se crea y usa el lda model
# Running LDA using Bag of Words
lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=5, id2word=dictionary, passes=2, workers=2)


# Los hiperparámetros serán calibrados más adelante.



for idx, topic in lda_model.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx, topic))

print('hola')

# Visualizar:

#pyLDAvis.enable_notebook()
#pyLDAvis.gensim.prepare(lda_model, bow_corpus, dictionary)



#from gensim.models import CoherenceModel
# Compute Coherence Score
#coherence_model_lda = CoherenceModel(model=lda_model, texts=processed_tweets, dictionary=dictionary, coherence='c_v')
#coherence_model_lda.get_coherence()






