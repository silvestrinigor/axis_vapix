"""
https://developer.axis.com/vapix/
"""
from .connection import AxisServer, AxisCredencial
from .requests import AxisSession, AuthType
from .api import ApiVersion, FirmwareVersion

__all__ = [
    "AxisServer",
    "AxisCredencial",
    "AxisSession",
    "ApiVersion",
    "FirmwareVersion",
    "AuthType"
]