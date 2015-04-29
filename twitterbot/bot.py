import foo
import twit_utils
CREDS_FILE = "~/.creds/me.json"

def make_it_so():
    # Step 1. Get my latest tweets
    tweets = twit_utils.get_latest_tweets_from_me(CREDS_FILE)
    print("Found", len(tweets), "tweets")

    # Step 2. From my tweets, get the last time I did a YOUWANTIT reply
    foodreply = foo.latest_YOUWANTIT_reply(tweets)
    if foodreply:
        xid = foodreply['in_reply_to_status_id']
    else:
        xid = 1
    print("Searching for mentions with an id later than", xid)

    # Step 3. Get the most recent mentions since my last YOUWANTIT reply
    mentions = twit_utils.get_mentions(CREDS_FILE, {"since_id": xid})
    print("Found", len(mentions), "mentions")

    # Step 4. from the mentions, see if anyone has used the hashtag #VIRALFOODTWEET
    foodtweet = foo.find_first_VIRALFOODTWEET_tagged_mention(mentions)

    # Step 5. Get the most search_results 
    keywordresult = foo.search_results

    if foodtweet == None:
        print("No #VIRALFOODTWEET tweet to reply to")
        return None
    else:
        # Step 6. see if there's tweet with the keyword
        if keywordresult == None:
            print("No tweet with the keyword exist")
            return None
        else:
            # Step 7. Create the custom YOUWANTIT message
            print("About to send a message to", foodtweet['user']['screen_name'])
            txt = foo.make_YOUWANTIT_text()

            # Step 8. Send the message
            resp = twit_utils.reply(CREDS_FILE, txt, foodtweet)
            return resp



import time
print('what')
while True:
    make_it_so()
    time.sleep(10)