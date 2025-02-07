"""
https://developer.axis.com/vapix/
"""
from .connection import AxisServer, AxisCredencial, ApiVersion, FirmwareVersion
from .requests import AxisSession, AuthType

__all__ = [
    "AxisServer",
    "AxisCredencial",
    "AxisSession",
    "ApiVersion",
    "FirmwareVersion",
    "AuthType"
]