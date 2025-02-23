"""
https://developer.axis.com/vapix/
"""
from .connection import AxisServerInfo, ApiVersion, FirmwareVersion
from .requests import AxisSession, AuthType

from .apis.analytics_metadata_configuration import AnalyticsMetadataProducerConfiguration
from .apis.api_discovery_service import ApiDiscoveryService
from .apis.basic_device_information import BasicDeviceInformation
from .apis.firmware_management_api import FirmwareManagementApi
from .apis.loitering_guard import LoiteringGuard
from .apis.network_settings_api import NetworkSettingsApi
from .apis.ntp_api import NtpApi
from .apis.object_analytics_api import ObjectAnalyticsApi
from .apis.overlay_api import DynamicOverlayApi
from .apis.time_api import TimeApi
from .apis.capture_mode import CaptureMode

__all__ = [
    "AxisServerInfo",
    "AxisCredencial",
    "AxisSession",
    "ApiVersion",
    "FirmwareVersion",
    "AuthType",

    'AnalyticsMetadataProducerConfiguration',
    'ApiDiscoveryService',
    'BasicDeviceInformation',
    'FirmwareManagementApi',
    'LoiteringGuard',
    'NetworkSettingsApi',
    'NtpApi',
    'ObjectAnalyticsApi',
    'DynamicOverlayApi',
    'TimeApi',
    'CaptureMode'
]

