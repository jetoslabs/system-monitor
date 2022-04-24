import tweepy

from client.schemas.schema_twitter import TweetReqSchema, TweetResSchema
from client.core.settings import settings


class Twitter:

    @staticmethod
    def create_tweet(tweet: TweetReqSchema) -> TweetResSchema:
        client = tweepy.Client(
            consumer_key=settings.TWITTER_CONSUMER_KEY,
            consumer_secret=settings.TWITTER_CONSUMER_SECRET,
            access_token=settings.TWITTER_ACCESS_TOKEN,
            access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET
        )

        response = client.create_tweet(
            text=tweet.text
        )

        resp = TweetResSchema(**response.data)
        resp.link = f"https://twitter.com/user/status/{response.data['id']}"

        return resp
