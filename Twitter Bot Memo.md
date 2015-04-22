#Pitch
Everyone who tweets at my bot with the name of a food will be tweeted back the most retweeted tweet with the food and a picture in it.

Example:
 @foodbot cupcake #viralfoodtweet

@user Choc Strawberry Cupcake #F00DP0RN from @foodporn
![alt tag](http://i.imgur.com/2gPu6g6.png)

#Steps
- Bot checks Twitter API endpoint of statuses/mentions_timeline
- For each Tweet, the bot to see if the #viralfoodtweet hashtag was used. Also, note the user's screen name and the ID of the tag.
- Scrape the twitter api using the keyword given, get the tweet with picture with the most retweets.
- Extract the image's web link
- Use Twitter's statuses/update endpoint and reply back to the user with the text, the original account, and the image URL.
