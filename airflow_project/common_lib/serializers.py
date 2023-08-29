from pydantic import BaseModel


class TemperatureModel(BaseModel):
    datetime: str
    tempmax: float
    tempmin: float
    temp: float


class TwitterModel(BaseModel):
    id: str
    edit_history_tweet_ids: list
    author_id: str
    created_at: str
    text: str
    public_metrics: dict
    in_reply_to_user_id: str
    conversation_id: str
    lang: str
