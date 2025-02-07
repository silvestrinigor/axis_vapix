from .requests import AxisSession, VapixRequest, VapixResponse
from .connection import ApiVersion

class IVapixApiClass:
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        self.session = session
        self.api_version = api_version
        self._base_url = f"http://{session.server.host}:{session.server.port}/"

    def _send_request(self, request: VapixRequest):
        prepared_request = request.prepare()
        response = self.session.send(request=prepared_request)
        response: VapixResponse
        return response