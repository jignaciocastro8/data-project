import pandas as pd
import time
import twint
import nest_asyncio
nest_asyncio.apply()


def search_user_tweets(id):
    ini = time.time()

    # Define c object
    c = twint.Config()
    # Parameters
    c.Username = id
    c.Store_csv = True
    c.Output = 'data/'+ id +'.csv'
    # Run search
    twint.run.Search(c)

    print('time (min): ', (time.time() - ini) / 60 ) 

def search_tweets_santiago(since, until, word, file_name):
    """Search for tweets and saves them into a csv file.

    Args:
        since (str): Date to start the search. Ex: '2019-10-16'.
        until ([type]): Date to start the search. Ex: '2019-10-22'.
        file_name ([type]): Name to save the csv with tweets.
    """
    ini =  time.time()

    
    # Custom config
    #c.Min_likes = 10
    #c.Min_retweets = 10

    # Hide output
    #c.Hide_output = False
    #c.Geo = "-33.45776872061534,-70.66448325142338,15km"

    # Define c object
    c = twint.Config()
    # Parameters
    c.Search = word
    c.Near = 'Santiago, Chile'
    c.Since = since
    c.Until = until
    c.Store_csv = True
    c.Output = 'data/'+ file_name +'.csv'
    # Run search
    twint.run.Search(c)

    print('time (min): ', (time.time() - ini) / 60 ) 

if __name__ == "__main__":
    #search_tweets_santiago('2020-01-01', '2021-05-31', 'jadue', 'santiago_jadue_2020')
    #search_tweets_santiago('2020-01-01', '2021-05-31', 'covid', 'santiago_covid_2020')
    search_user_tweets('gabrielboric')


