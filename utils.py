import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud

# spanish stop words
stop_words = set(stopwords.words('spanish'))
problematic_words = ['t', 'si', 'q']

def wordcloud_tweets(df, file_name):
    """Create a wordcloud from a collection of tweets. For this purpose we put all the tweets together

    Args:
        df (pandas Dataframe): Must has column 'tweet' with tweets.
        file_name (str): Directory to save the .png.
    """
    # Join tweets by ' '.
    tweets_str = ' '.join([t for t in df['tweet']])
    # Get a list with all the words.
    word_list = tweets_str.split()
    # Lowercase
    word_list = [w.lower() for w in word_list]
    # Delete @account, stop words and 'https...'   
    word_list = [w for w in word_list if not w in stop_words and not w in problematic_words]
    # Final list of words.
    final_data = []
    for w in word_list:
        if not (len(w)>=5 and w[:5] == 'https') :
            final_data.append(w)
    # Join the processed words.
    final_data = ' '.join(final_data)
    # Wordcloud process.
    wordcloud = WordCloud(width=1600, height=800, max_font_size=200, background_color="black").generate(final_data)
    plt.figure(figsize=(12,10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(file_name)
    plt.show()

