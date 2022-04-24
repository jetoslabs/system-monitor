from fastapi import APIRouter

from client.controllers.twitter import Twitter
from client.schemas.schema_twitter import TweetReqSchema

router = APIRouter()


@router.post("/tweet")
async def tweet(tweet: TweetReqSchema):
    data = Twitter.create_tweet(tweet)
    return data
