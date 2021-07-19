import tweepy
import twitter_auth as tw

class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = tweepy.OAuthHandler(tw.API_KEY, tw.API_SECRET_KEY)
        auth.set_access_token(tw.ACCESS_TOKEN, tw.ACCESS_TOKEN_SECRET)
        return auth