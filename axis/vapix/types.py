from enum import Enum

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
    FACTORY_DEFAULT = "factoryDefault"
    UPGRADE = "upgrade"
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
    GET_CONFIGURATION_CAPABILITIES = "getConfigurationCapabilities"
    GET_CONFIGURATION = "getConfiguration"
    SEND_ALARM = "sendAlarm"
    SEND_ALARM_EVENT = "sendAlarmEvent"
    GET_ACCUMULATED_COUNTS = "getAccumulatedCounts"
    RESET_ACCUMULATED_COUNTS = "resetAccumulatedCounts"
    RESET_PASSTHROUGH = "resetPassthrough"
    GET_OCCUPANCY = "getOccupancy"
    LIST_PRODUCERS = "listProducers"
    SET_ENABLED_PRODUCERS = "setEnabledProducers"
    GET_SUPPORTED_METADATA = "getSupportedMetadata"

class ApiPathType(Enum):
    AXIS_CGI_ANALYTICS_METADATA_CONFIG = "axis-cgi/analyticsmetadataconfig.cgi"
    AXIS_CGI_API_DISCOVERY = "axis-cgi/apidiscovery.cgi"
    AXIS_CGI_AUDIO_DEVICE_CONTROL = "axis-cgi/audiodevicecontrol.cgi"
    AXIS_CGI_AUDIO_TRANSMIT = "axis-cgi/audio/transmit.cgi"
    AXIS_CGI_AUDIO_RECEIVE = "axis-cgi/audio/receive.cgi"
    AXIS_CGI_BASIC_DEVICE_INFO = "axis-cgi/basicdeviceinfo.cgi"
    AXIS_CGI_CAPTURE_MODE = "axis-cgi/capturemode.cgi"
    AXIS_CGI_CLEAR_VIEW = "axis-cgi/clearviewcontrol.cgi"
    AXIS_CGI_DYNAMIC_OVERLAY_API = "axis-cgi/dynamicoverlay/dynamicoverlay.cgi" # Dynamic overlay API
    AXIS_CGI_DYNAMIC_OVERLAY = "axis-cgi/dynamicoverlay.cgi?" # Dynamic text overlay
    AXIS_CGI_FIND_MY_DEVICE = "axis-cgi/findmydevice.cgi"
    AXIS_CGI_FIRMWARE_MANAGEMENT = "axis-cgi/firmwaremanagement.cgi"
    AXIS_CGI_LEGACY_PARAMETER_HANDLING = "axis-cgi/param.cgi?action="
    AXIS_CGI_ADMIN_LEGACY_PARAMETER_HANDLING = "axis-cgi/admin/param.cgi?action="
    AXIS_CGI_NETWORK_SETTINGS_API = "axis-cgi/network_settings.cgi"
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
    NONE = None

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
    LIST_DEFINITIONS = "listdefinitions"
    START = "start"
    STOP = "stop"
    RESTART = "restart"
    NONE = None

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
    SCENARIO = "scenario"
    PRODUCERS = "producers"
    NAME = "name"
    ENABLED = "enabled"
    CHANNEL = "channel"
    VIDEO_CHANNELS = "videochannels"
    PROFILE = "profile"
    
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

class AutoCommitType(Enum):
    NEVER = "never"
    BOOT = "boot"
    STARTED = "started"
    DEFAULT = "default"
    NONE = None

class IPAddressConfigurationModeType(Enum):
    DHCP = "DHCP"
    STATIC = "static"
    NONE = None

class ContentType(Enum):
    APPLICATION_JSON = "application/json"
    APPLICATION_OCTETSTREAM = "application/octet-stream"
    MUILTPART_FORMDATA = "multipart/form-data"
