from dataclasses import dataclass
from packaging import version


@dataclass
class AxisServer:
    host: str
    port: int


@dataclass
class AxisCredencial:
    username: str
    password: str


class ApiVersion(version.Version):
    def __init__(self, major: int, minor: int):
        super().__init__(f"{major}.{minor}")


class FirmwareVersion(version.Version):
    def __init__(self, major: int, minor: int, patch: int):
        super().__init__(f"{major}.{minor}.{patch}")
