from dataclasses import dataclass


@dataclass
class AxisServer:
    host: str
    port: int


@dataclass
class AxisCredencial:
    username: str
    password: str