import requests  # type: ignore
from airflow.models import BaseOperator

from airflow_project.common_lib.serializers import TwitterModel


class TwitterOperator(BaseOperator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self, context):
        url = "https://labdados.com/2/tweets/search/recent?query=cama&tweet.fields=author_id," \
              "conversation_id,created_at,id,in_reply_to_user_id,public_metrics,lang,text&expansions=author_id&" \
              "user.fields=id,name,username,created_at&start_time=2023-06-08T00:00:00.00Z&end_time=2023-06-07T16:53:45.00Z"

        response = requests.get(url)
        data = response.json()['data']
        return [TwitterModel(**item).dict() for item in data]
