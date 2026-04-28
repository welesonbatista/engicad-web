from typing import Optional

class HttpRequest:
    def __init__(
        self,
        headers: Optional[dict] = None,
        body: Optional[dict] = None,
        path_params: Optional[dict] = None,
    ):
        self.headers = headers
        self.body = body
        self.path_params = path_params