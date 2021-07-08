import pandas as pd
import datetime
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud

# spanish stop words
stop_words = set(stopwords.words('spanish'))
forbidden_words = ['t', 'si', 'q', 'https', 'co', 'solo', 'ser', 'bien', 
                        'así', 'ma', 'igual', 'va', 'después', 'hacer',
                        'hace', 'creo'] + list(stop_words)


def preprocess_tweet(tweet):
    """
    Replaces unwanted characters and performs
    a preprocessing.
    input: 
        (str) tweet.
    return:
        (str[]) final: list of words.
    """
    unwanted = ['#', ',', '.', '!', '?', '¿', '¡', '(',\
                ')', '-', '=', 'jaja', 'jajaja',' 1','2',\
                '3', '4', '5', '6', '7', '8', '9', '0',\
                '"', ':']
    final = delete_chars(tweet, unwanted).split()
    final = [w.lower() for w in final]
    final = [w for w in final if w not in stop_words and len(w) > 3]
    # Se eliminan links y @users
    final = [w for w in final if w[:4] != 'http']
    final = [w for w in final if w[:1] != '@']
    return final



def delete_chars(text, unwanted_chars):
    """
    useful method to replace a list of chars on text.
    return:
        (str) the same str without the chars in chars.
    """
    for char in unwanted_chars:
        text = text.replace(char, '')
    return text


def wordcloud_tweets(df, file_name = '', save = True, forbidden_words = []):
    """Create a wordcloud from a collection of tweets. For this purpose we put all the tweets together

    Args:
        df (pandas Dataframe): Must has column 'tweet' with tweets.
        file_name (str): Directory to save the .png.
    """
    # Possible problematic words to add.
    forbidden_words = ['t', 'si', 'q', 'https', 'co', 'solo', 'ser', 'bien', 
                        'así', 'ma', 'igual', 'va', 'después', 'hacer',
                        'hace', 'creo'] + forbidden_words
    # Join tweets by ' '.
    tweets_str = ' '.join([t for t in df['tweet']])
    # Get a list with all the words.
    word_list = tweets_str.split()
    # Lowercase
    word_list = [w.lower() for w in word_list]
    # Delete stop words.   
    word_list = [w for w in word_list if not w in stop_words]
    # Final list of words.
    final_data = []
    # Delete unwanted words.
    for w in word_list:
        flag = False
        for forbidden in forbidden_words:
            if forbidden in w:
                flag = True
        if not flag: final_data.append(w)
    # Join the processed words.
    final_data = ' '.join(final_data)
    # Wordcloud process.
    wordcloud = WordCloud(width=1600, height=800, max_font_size=200, background_color="black").generate(final_data)
    #plt.figure(figsize=(12,10))
    plt.imshow(wordcloud)
    plt.axis("off")
    if save: plt.savefig('imgs/' + file_name + '.png')
    plt.show()

def df_to_datetime(df):
    """Transform the 'date' column from str to datetime format.

    Args:
        df (pandas dataframe): Dataframe with 'date' column.
    Return:
        same df with dates in datetime format.
    """
    df['date'] = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in df['date']]
    return df


def f(): print('hola')

# test:

tweet = 'BUenas BUENas, hola @hola #HOla'
print(preprocess_tweet(tweet))