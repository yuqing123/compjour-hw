from random import random

def find_first_VIRALFOODTWEET_tagged_mention(mentions):
    """
    Given a list of tweets, find the earliest one that has the #VIRALFOODTWEET hashtag in it
    Arguments:
        mentions (list): a list of Twitter tweet objects that are dicts
    Returns:
        if any such tweet is found, return that tweet (dict)
        else, return None
    """
    foodmentions = []
    for m in mentions:
        hashtags = m['entities']['hashtags']
        for tag in hashtags:
            if tag['text'].upper() == "VIRALFOODTWEET":
                foodmentions.append(m)

    if len(foodmentions) > 0:
        return foodmentions[0]
    else:
        return None

def keywords
    """
    from find_first_VIRALFOODTWEET_tagged_mention(mentions), get the keywords that will be used to
    search for tweets. Since people are asked to tweet in the fomart of "#VIRALFOODTWEET cupcake", 
    the keywords should just be the text of the tweets minus the hashtag #VIRALFOODTWEET
    Arguments:
        tweets (list): a list of keywords
    Returns:
        if any such keyword is found, return that keyword(dict)
        else, return None
    """


def search_results
    """
    Given a list of tweets, find the one that has the keyword (for example "cupcake") in it
    Arguments:
        tweets (list): a list of Twitter tweet objects that are dicts
    Returns:
        if any such tweet is found, return that tweet (dict)
        else, return None
    """
    #twitter search recipe(from the Internet, I don't know whether it actually works)
    import sysimport json
    import twitter
    Q = ' '.join(sys.argv[1])
    MAX_PAGES = 15
    RESULTS_PER_PAGE = 100
    twitter_search = twitter.Twitter(domain="search.twitter.com")
    search_results = []
    for page in range(1,MAX_PAGES+1):
        earch_results += \
            twitter_search.search(q=Q, rpp=RESULTS_PER_PAGE, page=page)['results']
    print json.dumps(search_results, indent=1)
    #---end of potential code



def latest_YOUWANTIT_reply(tweets):
    """
    Given a list of tweets, find the earliest one that has the #YOUWANTIT hashtag in it
    Arguments:
        tweets (list): a list of Twitter tweet objects that are dicts
    Returns:
        if any such tweet is found, return that tweet (dict)
        else, return None
    """
    for tweet in tweets:
        tags = [tag for tag in tweet['entities']['hashtags'] if tag['text'].upper() == 'YOUWANTIT']
        if len(tags) > 0:
            return tweet



def make_YOUWANTIT_text():
    """
    Create a custom #YOUWANTIT message
    Arguments:
        None
    Returns:
        A text string with the name of the user, the #YOUWANTIT hashtag, and content of the tweet 
    """
    #Step 1. from search_result, select the tweet that has the largest retweet_count
    
    #Step 2. print the text of the tweet

    #Step 3. create YOUWANTIT text in the format: @user #YOUWANTIT tweet_text 




