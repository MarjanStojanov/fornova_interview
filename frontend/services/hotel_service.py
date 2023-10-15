from connectors.backend_connector import BackendConnector


class HotelService:
    """layer that handles business logic and data fetching from db/externals"""

    def search(self, keyword, page=1, limit=10) -> dict:
        return BackendConnector().search(keyword=keyword, page=page, limit=limit)

    def browse(self, page=1, limit=10) -> dict:
        return BackendConnector().browse(page=page, limit=limit)
