from pydantic import BaseModel


class TweetReqSchema(BaseModel):
    text: str


class TweetResSchema(BaseModel):
    id: str
    text: str
    link: str
