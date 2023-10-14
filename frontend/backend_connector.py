from requests import session
from errors import ConnectorError
from config import Config


class BackendConnector:
    """layer that is in charge of making any third party API calls"""
    def __init__(self) -> None:
        self.session = session()

        config = Config()
        self.host = config.BACKEND_HOST
        self.api_key = config.BACKEND_API_KEY

    def headers(self):
        return {
            "Content-Type": "application/json",
            "X-API-KEY": self.api_key,
        }

    def browse(self, page=1, limit=10):
        response = self.session.get(
            url=f"{self.host}/hotels/browse",
            params={
                "page": page,
                "limit": limit,
            },
            headers=self.headers(),
        )
        if response.status_code != 200:
            raise ConnectorError(response.json())

        return response.json()

    def search(self, keyword, page, limit):
        response = self.session.post(
            url=f"{self.host}/hotels/search",
            json={
                "keyword": keyword,
                "page": page,
                "limit": limit,
            },
            headers=self.headers(),
        )

        if response.status_code != 200:
            raise ConnectorError(response.json())

        return response.json()
