class ConnectorError(Exception):
    def __init__(self,  error_json, *args: object) -> None:
        super().__init__(*args)
        self.error_json = error_json
        self.status_code = 400
