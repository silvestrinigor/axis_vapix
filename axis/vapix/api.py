from packaging import version
from .requests import VapixRequest, VapixResponse, AxisSession


class ApiVersion(version.Version):
    def __init__(self, major: int, minor: int):
        super().__init__(f"{major}.{minor}")


class FirmwareVersion(version.Version):
    def __init__(self, major: int, minor: int, patch: int):
        super().__init__(f"{major}.{minor}.{patch}")


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