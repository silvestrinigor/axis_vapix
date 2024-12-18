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
class ApiType(Enum):
    AXIS_CGI_NETWORK_SETTINGS = "network-settings"
    AXIS_CGI_TIME = "time-service"
    AXIS_CGI_BASIC_DEVICE_INFO = "basic-device-info"
    AXIS_CGI_DYNAMIC_OVERLAY = "dynamicoverlay"
    AXIS_CGI_NTP = "ntp"
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
class TextOverlay:
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
class ImageOverlay:
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
class NTPClientConfiguration:
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
    


