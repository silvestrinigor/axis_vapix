from enum import Enum
from abc import ABC, abstractmethod
class DevicePropertyType(Enum):
    ARCHITECTURE = "Architecture"
    BRAND = "Brand"
    BUILD_DATE = "BuildDate"
    HARDWARE_ID = "hardwareId"
    PROD_FULL_NAME = "ProdFullName"
    PROD_NBR = "ProdNbr"
    PROD_SHORT_NAME = "ProdShortName"
    PROD_TYPE = "ProdType"
    PROD_VARIANT = "ProdVariant"
    SERIAL_NUMBER = "SerialNumber"
    SOC = "Soc"
    SOC_SERIAL_NUMBER = "SocSerialNumber"
    VERSION = "Version"
    WEB_URL = "WebURL"
class RequestParamType(Enum):
    API_VERSION = "apiVersion"
    PARAMS = "params"
    CHANNEL = "channel"
    CAPTURE_MODE_ID = "captureModeId"
    CONTEXT = "context"
    METHOD = "method"
    FACTORY_DEFAULT_MODE = "factoryDefaultMode"
class MethodType(Enum):
    GET_PROPERTIES = "getProperties"
    GET_ALL_PROPERTIES = "getAllProperties"
    GET_ALL_UNRESTRICTED_PROPERTIES = "getAllUnrestrictedProperties"
    GET_SUPPORTED_VERSIONS = "getSupportedVersions"
    GET_API_LIST = "getApiList"
    ADD_IMAGE = "addImage"
    ADD_TEXT = "addText"
    LIST = "list"
    REMOVE = "remove"
    SET_IMAGE = "setImage"
    SET_TEXT = "setText"
    GET_OVERLAY_CAPABILITIES = "getOverlayCapabilities"
    GET_CAPTURE_MODES = "getCaptureModes"
    SET_CAPTURE_MODE = "setCaptureMode"
    GET_SERVICE_INFO = "getServiceInfo"
    GET_STATUS = "getStatus"
    START = "start"
    STOP = "stop"
    GET_DATE_TIME_INFO = "getDateTimeInfo"
    GET_ALL = "getAll"
    SET_DATE_TIME = "setDateTime"
    SET_TIME_ZONE = "setTimeZone"
    SET_POSIX_TIME_ZONE = "setPosixTimeZone"
    RESET_TIME_ZONE = "resetTimeZone"
    GET_NTP_INFO = "getNTPInfo"
    SET_NTP_CLIENT_CONFIGURATION = "setNTPClientConfiguration"
    GET_NETWORK_INFO = "getNetworkInfo"
    SET_HOSTNAME_CONFIGURATION = "setHostnameConfiguration"
    SET_IPV4_ADDRESS_CONFIGURATION = "setIPv4AddressConfiguration"
    SET_RESOLVER_CONFIGURATION = "setResolverConfiguration"
    STATUS = "status"
    ROLLBACK = "rollback"
    REBOOT = "reboot"
class ApiPathType(Enum):
    AXIS_CGI_API_DISCOVERY = "axis-cgi/apidiscovery.cgi"
    AXIS_CGI_AUDIO_DEVICE_CONTROL = "axis-cgi/audiodevicecontrol.cgi"
    AXIS_CGI_AUDIO_TRANSMIT = "axis-cgi/audio/transmit.cgi"
    AXIS_CGI_AUDIO_RECEIVE = "axis-cgi/audio/receive.cgi"
    AXIS_CGI_BASIC_DEVICE_INFO = "axis-cgi/basicdeviceinfo.cgi"
    AXIS_CGI_CAPTURE_MODE = "axis-cgi/capturemode.cgi"
    AXIS_CGI_CLEAR_VIEW = "axis-cgi/clearviewcontrol.cgi"
    AXIS_CGI_DYNAMIC_OVERLAY = "axis-cgi/dynamicoverlay/dynamicoverlay.cgi"
    AXIS_CGI_FIND_MY_DEVICE = "axis-cgi/findmydevice.cgi"
    AXIS_CGI_FIRMWARE_MANAGEMENT = "axis-cgi/firmwaremanagement.cgi"
    AXIS_CGI_LEGACY_PARAMETER_HANDLING = "axis-cgi/param.cgi?action="
    AXIS_CGI_ADMIN_LEGACY_PARAMETER_HANDLING = "axis-cgi/admin/param.cgi?action="
    AXIS_CGI_NETWORK_SETTINGS = "axis-cgi/network_settings.cgi"
    AXIS_CGI_TIME = "axis-cgi/time.cgi"
    AXIS_CGI_NTP = "axis-cgi/ntp.cgi"
    AXIS_CGI_APPLICATIONS_UPLOAD = "axis-cgi/applications/upload.cgi"
    AXIS_CGI_APPLICATIONS_CONTROL = "axis-cgi/applications/control.cgi?"
    AXIS_CGI_APPLICATIONS_CONFIG = "axis-cgi/applications/config.cgi?"
    AXIS_CGI_APPLICATIONS_LICENSE = "axis-cgi/applications/license.cgi?"
    AXIS_CGI_APPLICATIONS_LIST = "axis-cgi/applications/list.cgi"
    LOCAL_OBJECT_ANALYTICS = "local/objectanalytics/control.cgi"
    LOCAL_LOITERING_GUARD = "local/loiteringguard/control.cgi"
    AXIS_CGI_SYSTEM_SETTINGS_PWDGRP = "axis-cgi/pwdgrp.cgi?"
    AXIS_CGI_SYSTEM_SETTINGS_FACTORYDEFAULT = "axis-cgi/factorydefault.cgi"
    AXIS_CGI_SYSTEM_SETTINGS_HARDFACTORYDEFAULT = "axis-cgi/hardfactorydefault.cgi"
    AXIS_CGI_SYSTEM_SETTINGS_FIRMWARE_UPGRADE = "axis-cgi/firmwareupgrade.cgi?"
    AXIS_CGI_SYSTEM_SETTINGS_RESTART = "axis-cgi/restart.cgi"
    AXIS_CGI_PARAM = "axis-cgi/param.cgi?"
class ApiType(Enum):
    AXIS_CGI_NETWORK_SETTINGS = "network-settings"
    AXIS_CGI_TIME = "time-service"
    AXIS_CGI_BASIC_DEVICE_INFO = "basic-device-info"
    AXIS_CGI_DYNAMIC_OVERLAY = "dynamicoverlay"
    AXIS_CGI_NTP = "ntp"
    AXIS_CGI_FIRMWARE_MANAGEMENT = "fwmgr"
    AXIS_CGI_SYSTEM_SETTINGS_PWDGRP = "user-management"
    AXIS_CGI_PARAM = "param-cgi"
class FirmwareUpgradeType(Enum):
    NORMAL = "normal"
    FACTORY_DEFAULT = "factorydefault"
    NONE = None
class RequestUrlParamType(Enum):
    TYPE = "type="
    ACTION = "action="
    USERGROUP = "usergroup="
    GROUP = "group"
class ActionType(Enum):
    ADD = "add"
    REMOVE = "remove"
    UPDATE = "update"
    LIST = "list"
    LIST_DEFINITIONS =  "listdefinitions"
class ParamType(Enum):
    POSIX_TIME_ZONE = "posixTimeZone"
    ENABLE_DST = "enableDst"
    PROPERTY_LIST = "propertyList"
    CAMERA = "camera"
    TEXT = "text"
    TEXT_BG_COLOR = "textBGColor"
    POSITION = "position"
    TEXT_COLOR = "textColor"
    TEXT_OL_COLOR = "textOLColor"
    IDENTITY = "identity"
    OVERLAY_PATH = "overlayPath"
    FONT_SIZE = "fontSize"
    TEXT_BACK_GROUND_COLOR = "textBGColor"
    ID = "id"
    DURATION = "duration"
    DATE_TIME = "dateTime"
    TIME_ZONE = "timeZone"
    INDICATOR = "indicator"
    INDICATOR_BG = "indicatorBG"
    INDICATOR_COLOR = "indicatorColor"
    INDICATOR_OL = "indicatorOL"
    INDICATOR_SIZE = "indicatorSize"
    PT_POSITION = "ptPosition"
    REFERENCE = "reference"
    SCALABLE = "scalable"
    SCROLL_SPEED = "scrollSpeed"
    SIZE = "size"
    TEXT_LENGTH = "textLength"
    VISIBLE = "visible"
    ENABLE = "enable"
    SERVERS_SOURCE = "serversSource"
    STATIC_SERVERS = "staticServers"
    USE_DHCP_HOSTNAME = "useDhcpHostname"
    STATIC_HOSTNAME = "staticHostname"
    STATIC_ADDRESS_CONFIGURATION = "staticAddressConfigurations"
    DEVICE_NAME = "deviceName"
    CONFIGURATION_MODE = "configurationMode"
    STATIC_DEFAULT_ROUTER = "staticDefaultRouter"
    USE_DHCP_RESOLVER_INFO = "useDhcpResolverInfo"
    STATIC_NAME_SERVERS = "staticNameServers"
    STATIC_SEARCH_DOMAINS = "staticSearchDomains"
    STATIC_DOMAIN_NAME = "staticDomainName"
    AUTO_ROLLBACK = "autoRollback"
    AUTO_COMMIT = "autoCommit"
    FACTORY_DEFAULT_MODE = "factoryDefaultMode"
class StaticAddressConfigurationParamsType(Enum):
    ADRESS = "address"
    PREFIX_LENGTH = "prefixLength"
    BROADCAST = "broadcast"
class OverlayPositionType(Enum):
    BOTTOM_RIGHT = "bottomRight"
    TOP_RIGHT = "topRight"
    BOTTOM = "bottom"
    TOP = "top"
    BOTTOM_LEFT = "bottomLeft"
    TOP_LEFT = "topleft"
    NONE = None
class OverlayPositionCustomValue:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y
    
    @property
    def value(self):
        return [self.x, self.y]
class OverlayColorType(Enum):
    WHITE = "white"
    BLACK = "black"
    GREY = "grey"
    MOSAIC = "mosaic" # Hardware dependent
    CAMELEON = "cameleon" # Hardware dependent
    RED = "red"
    TRANSPARENT = "transparent"
    SEMI_TRANSPARENT = "semiTransparent"
    NONE = None
class TimeZoneType(Enum):
    EUROPE_STOCKHOLM = "Europe/Stockholm"
    EUROPE_LONDON = "Europe/London"
    EUROPE_PARIS = "Europe/Paris"
    AMERICA_NEW_YORK = "America/New_York"
    AMERICA_LOS_ANGELES = "America/Los_Angeles"
    ASIA_TOKYO = "Asia/Tokyo"
    ASIA_SINGAPORE = "Asia/Singapore"
    AUSTRALIA_SYDNEY = "Australia/Sydney"
    AFRICA_JOHANNESBURG = "Africa/Johannesburg"
    AMERICA_SAO_PAULO = "America/Sao_Paulo"
    AMERICA_MANAUS = "America/Manaus"
    AMERICA_ACRE = "America/Acre"
class ResponseType(Enum):
    DATA = "data"
    API_VERSION = "apiVersion"
    METHOD = "method"
    ERROR = "error"
class ResponseDataType(Enum):
    API_LIST = "apiList"
    PROPERTY_LIST = "propertyList"
    DATE_TIME = "dateTime"
    LOCAL_DATE_TIME = "localDateTime"
    TIME_ZONE = "timeZone"
    POSIX_TIME_ZONE = "posixTimeZone"
    DST_ENABLE = "dstEnabled"
    IMAGE_FILES = "imageFiles"
    IMAGE_OVERLAYS = "imageOverlays"
    TEXT_OVERLAYS = "textOverlays"
class ResponseDataApiType(Enum):
    ID = "id"
    VERSION = "version"
    NAME = "name"
    DOCK_LINK = "dockLink"
    STATUS = "status"
class ServersSourceType(Enum):
    DHCP = "DHCP"
    STATIC = "static"
    NONE = None
class FactoryDefaultModeType(Enum):
    SOFT = "soft"
    HARD = "hard"
    NONE = None
class IPAddressConfigurationModeType(Enum):
    DHCP = "DHCP"
    STATIC = "static"
    NONE = None
class ParamConfig(ABC):
    @abstractmethod
    def get_all_params(self):
        pass
class TextOverlay(ParamConfig):
    camera:int = None
    font_size:int = None
    identity: int = None
    indicator: str = None
    position: OverlayPositionType | OverlayPositionCustomValue = OverlayPositionType.NONE
    text: str = None
    text_bg_color: OverlayColorType = OverlayColorType.NONE
    text_color: OverlayColorType = OverlayColorType.NONE
    text_length: int = None
    text_ol_color: OverlayColorType = OverlayColorType.NONE
    visible: bool = None

    def get_all_params(self):
        all_params = {
            ParamType.CAMERA.value: self.camera,
            ParamType.FONT_SIZE.value: self.font_size,
            ParamType.IDENTITY.value: self.identity,
            ParamType.INDICATOR.value: self.indicator,
            ParamType.POSITION.value: self.position.value,
            ParamType.TEXT.value: self.text,
            ParamType.TEXT_BG_COLOR.value: self.text_bg_color.value,
            ParamType.TEXT_COLOR.value: self.text_color.value,
            ParamType.TEXT_LENGTH.value: self.text_length,
            ParamType.TEXT_OL_COLOR.value: self.text_ol_color.value,
            ParamType.VISIBLE.value: self.visible
        }
        # Remove any keys with None values
        all_params = {key: value for key, value in all_params.items() if value is not None}
        return all_params
class ImageOverlay(ParamConfig):
    camera:int = None
    identity: int = None
    overlay_path: str = None
    position: OverlayPositionType | OverlayPositionCustomValue = OverlayPositionType.NONE
    visible: bool = None

    def get_all_params(self):
        all_params = {
            ParamType.CAMERA.value: self.camera,
            ParamType.OVERLAY_PATH.value: self.overlay_path,
            ParamType.IDENTITY.value: self.identity,
            ParamType.POSITION.value: self.position.value,
            ParamType.VISIBLE.value: self.visible
        }
        # Remove any keys with None values
        all_params = {key: value for key, value in all_params.items() if value is not None}
        return all_params
class NTPClientConfiguration(ParamConfig):
    enable: bool = None
    servers_source: ServersSourceType = None
    static_servers_list: list[str] = None
    
    def get_all_params(self):
        all_params = {
            ParamType.ENABLE.value: self.enable,
            ParamType.SERVERS_SOURCE.value: self.servers_source.value,
            ParamType.STATIC_SERVERS.value: self.static_servers_list
        }
        # Remove any keys with None values
        all_params = {key: value for key, value in all_params.items() if value is not None}
        return all_params
class HostnameConfiguration(ParamConfig):
    use_dhcp_hostname: bool = None
    static_hostname: str = None
    
    def get_all_params(self):
        all_params = {
            ParamType.USE_DHCP_HOSTNAME.value: self.use_dhcp_hostname,
            ParamType.STATIC_HOSTNAME.value: self.static_hostname
        }
        # Remove any keys with None values
        all_params = {key: value for key, value in all_params.items() if value is not None}
        return all_params
class StaticAddressConfigurations(ParamConfig):
    address: str = None
    prefix_length: int = None
    broadcast: str = None
    
    def get_all_params(self):
        all_params = {
            StaticAddressConfigurationParamsType.ADRESS.value: self.address,
            StaticAddressConfigurationParamsType.PREFIX_LENGTH.value: self.prefix_length,
            StaticAddressConfigurationParamsType.BROADCAST.value: self.broadcast
        }
        # Remove any keys with None values
        all_params = {key: value for key, value in all_params.items() if value is not None}
        return all_params
    
    def __repr__(self):
        self.get_all_params()
class IPv4AddressConfiguration(ParamConfig):
    device_name: str = "eth0"
    configuration_mode: IPAddressConfigurationModeType = IPAddressConfigurationModeType.NONE
    static_address_configurations: list[StaticAddressConfigurations] = None
    
    def get_all_params(self):
        all_params = {
            ParamType.DEVICE_NAME.value: self.device_name,
            ParamType.CONFIGURATION_MODE.value: self.configuration_mode.value,
            ParamType.STATIC_ADDRESS_CONFIGURATION.value: self.static_address_configurations
        }
        # Remove any keys with None values
        all_params = {key: value for key, value in all_params.items() if value is not None}
        return all_params
class NetworkResolverConfiguration(ParamConfig):
    use_dhcp_resolver_info: bool = None
    static_name_servers: list[str] = None
    static_search_domains: list[str] = None
    static_domain_name: str = None
    
    def get_all_params(self):
        all_params = {
            ParamType.USE_DHCP_RESOLVER_INFO.value: self.use_dhcp_resolver_info,
            ParamType.STATIC_NAME_SERVERS.value: self.static_name_servers,
            ParamType.STATIC_SEARCH_DOMAINS.value: self.static_search_domains,
            ParamType.STATIC_DOMAIN_NAME.value: self.static_domain_name
        }
        # Remove any keys with None values
        all_params = {key: value for key, value in all_params.items() if value is not None}
        return all_params
class AxisVapixExeption(Exception): ...
class AxisVapixVersionNotSupportedExeption(AxisVapixExeption): ...