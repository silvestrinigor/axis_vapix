"""
https://developer.axis.com/vapix/
"""
from .connection import AxisServerInfo, ApiVersion, FirmwareVersion
from .requests import AxisSession, AuthType

__all__ = [
    "AxisServer",
    "AxisCredencial",
    "AxisSession",
    "ApiVersion",
    "FirmwareVersion",
    "AuthType"
]