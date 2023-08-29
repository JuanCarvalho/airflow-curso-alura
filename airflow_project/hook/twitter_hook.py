import requests  # type: ignore
from airflow.providers.http.hooks.http import HttpHook


# WARNING: Este hook não funcionou, porque a api fake do twitter não tem um metodo de autenticação
# fica apenas como exemplo


class TwitterHook(HttpHook):
    def __init__(self, conn_id=None) -> None:
        self.conn_id = conn_id or 'twitter_connection'
        super().__init__(method='GET', http_conn_id=self.conn_id)

    def create_url(self):
        url = "https://labdados.com/2/tweets/search/recent?query=cama&tweet.fields=author_id," \
              "conversation_id,created_at,id,in_reply_to_user_id,public_metrics,lang,text&expansions=author_id&" \
              "user.fields=id,name,username,created_at&start_time=2023-06-08T00:00:00.00Z&end_time=2023-06-07T16:53:45.00Z"
        return url

    def connect_to_endpoint(self, url, session):
        request = requests.Request("GET", url)
        prep = session.prepare_request(request)
        self.log.info(f"URL: {url}")
        return self.run_and_check(session, prep, {})

    def run(self):
        session = self.get_conn({})
        url = self.create_url()
        return self.connect_to_endpoint(url, session)
