from .defaults import ApiPathType
from .defaults import DevicePropertyType
from .defaults import MethodType
from .request import AxisRequest
from .request import JsonRequestConfig
from .defaults import ParamType
from .defaults import OverlayPositionType
from .defaults import OverlayColorType
from .defaults import TimeZoneType
from .defaults import TextOverlay, ImageOverlay, NTPClientConfiguration, HostnameConfiguration, IPv4AddressConfiguration, NetworkResolverConfiguration
from datetime import datetime
from .utils import serialize_datetime

def get_supported_versions(axis_request: AxisRequest, api: ApiPathType):
    request_config = JsonRequestConfig(method= MethodType.GET_SUPPORTED_VERSIONS, context= axis_request.request_context)
    return axis_request.request_post(api, request_config)
    
def get_properties(axis_request: AxisRequest, properties: list[DevicePropertyType]):
    params = {ParamType.PROPERTY_LIST.value: [prop.value for prop in properties]}
    request_config = JsonRequestConfig(method= MethodType.GET_PROPERTIES, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_BASIC_DEVICE_INFO, request_config)
    
def get_all_properties(axis_request: AxisRequest):
    request_config = JsonRequestConfig(method= MethodType.GET_ALL_PROPERTIES, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_BASIC_DEVICE_INFO, request_config)
    
def get_all_unrestricted_properties(axis_request: AxisRequest):
    request_config = JsonRequestConfig(method= MethodType.GET_ALL_UNRESTRICTED_PROPERTIES, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_BASIC_DEVICE_INFO, request_config)

def get_api_list(axis_request: AxisRequest):
    request_config = JsonRequestConfig(method= MethodType.GET_API_LIST, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_API_DISCOVERY, request_config)

def add_dynamic_overlay_image(axis_request: AxisRequest, image_overlay: ImageOverlay):
    params = image_overlay.get_all_params()
    request_config = JsonRequestConfig(method= MethodType.ADD_IMAGE, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def add_dynamic_overlay_text(axis_request: AxisRequest, text_overlay: TextOverlay):
    params = text_overlay.get_all_params()
    request_config = JsonRequestConfig(method= MethodType.ADD_TEXT, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def list_overlays(axis_request: AxisRequest):
    params = {}
    request_config = JsonRequestConfig(method= MethodType.LIST, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def set_dynamic_overlay_text(axis_request: AxisRequest, text_overlay: TextOverlay):
    params = text_overlay.get_all_params()
    request_config = JsonRequestConfig(method= MethodType.SET_TEXT, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def set_dynamic_overlay_image(axis_request: AxisRequest, image_overlay: ImageOverlay):
    params = image_overlay.get_all_params()
    request_config = JsonRequestConfig(method= MethodType.SET_IMAGE, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def remove_dynamic_overlay(axis_request: AxisRequest, identity: int):
    params = {ParamType.IDENTITY.value: identity}
    request_config = JsonRequestConfig(method= MethodType.REMOVE, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def get_dynamic_overlay_capabilities(axis_request: AxisRequest):
    request_config = JsonRequestConfig(method= MethodType.GET_OVERLAY_CAPABILITIES, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def get_capture_modes(axis_request: AxisRequest):
    request_config = JsonRequestConfig(method= MethodType.GET_CAPTURE_MODES, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_CAPTURE_MODE, request_config)

def set_capture_mode(axis_request: AxisRequest, channel: int, capture_mode_id: int):
    request_config = JsonRequestConfig(method= MethodType.SET_CAPTURE_MODE, version= axis_request.api_version, context= axis_request.request_context, channel= channel, capture_mode_id= capture_mode_id)
    return axis_request.request_post(ApiPathType.AXIS_CGI_CAPTURE_MODE, request_config)

def get_clear_view_service_info(axis_request: AxisRequest):
    params = {}
    request_config = JsonRequestConfig(method= MethodType.GET_SERVICE_INFO, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_CLEAR_VIEW, request_config)

def start_cleaning_view(axis_request: AxisRequest, id: int, duration: int = None):
    params = {ParamType.ID.value: id}
    if duration != None:
        params[ParamType.DURATION.value] = duration
    request_config = JsonRequestConfig(method= MethodType.START, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_CLEAR_VIEW, request_config)

def stop_cleaning_view(axis_request: AxisRequest, id: int):
    params = {ParamType.ID.value: id}
    request_config = JsonRequestConfig(method= MethodType.STOP, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_CLEAR_VIEW, request_config)

def get_cleaning_view_status(axis_request: AxisRequest, id: int):
    params = {ParamType.ID.value: id}
    request_config = JsonRequestConfig(method= MethodType.GET_STATUS, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_CLEAR_VIEW, request_config)

def get_date_time_info(axis_request: AxisRequest):
    request_config = JsonRequestConfig(method= MethodType.GET_DATE_TIME_INFO, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_TIME, request_config)

def get_all_date_time_api_info(axis_request: AxisRequest):
    request_config = JsonRequestConfig(method= MethodType.GET_ALL, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_TIME, request_config)

def set_date_time(axis_request: AxisRequest, date_time: datetime):
    params = {ParamType.DATE_TIME.value: serialize_datetime(date_time)}
    request_config = JsonRequestConfig(method= MethodType.SET_DATE_TIME, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_TIME, request_config)

def set_time_zone(axis_request: AxisRequest, time_zone: TimeZoneType):
    params = {ParamType.TIME_ZONE.value: time_zone.value}
    request_config = JsonRequestConfig(method= MethodType.SET_TIME_ZONE, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_TIME, request_config)

def set_posix_time_zone(axis_request: AxisRequest, posix_time_zone: str, enable_dst: bool):
    params = {ParamType.POSIX_TIME_ZONE.value: posix_time_zone, ParamType.ENABLE_DST.value: enable_dst}
    request_config = JsonRequestConfig(method= MethodType.SET_POSIX_TIME_ZONE, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_TIME, request_config)

def reset_time_zone(axis_request: AxisRequest):
    request_config = JsonRequestConfig(method= MethodType.RESET_TIME_ZONE, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_TIME, request_config)

def get_ntp_info(axis_request: AxisRequest):
    request_config = JsonRequestConfig(method= MethodType.GET_NTP_INFO, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_NTP, request_config)

def set_ntp_client_configuration(axis_request: AxisRequest, configuration: NTPClientConfiguration):
    params = configuration.get_all_params()
    request_config = JsonRequestConfig(method= MethodType.SET_NTP_CLIENT_CONFIGURATION, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_NTP, request_config)

def get_network_info(axis_request: AxisRequest):
    request_config = JsonRequestConfig(method= MethodType.GET_NETWORK_INFO, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_NETWORK_SETTINGS, request_config)

def set_network_hostname(axis_request: AxisRequest, configuration: HostnameConfiguration):
    params = configuration.get_all_params()
    request_config = JsonRequestConfig(method= MethodType.SET_HOSTNAME_CONFIGURATION, version= axis_request.api_version, context= axis_request.request_context, params=params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_NETWORK_SETTINGS, request_config)

def set_network_ipv4_address(axis_request: AxisRequest, configuration: IPv4AddressConfiguration):
    params = configuration.get_all_params()
    request_config = JsonRequestConfig(method= MethodType.SET_IPV4_ADDRESS_CONFIGURATION, version= axis_request.api_version, context= axis_request.request_context, params=params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_NETWORK_SETTINGS, request_config)

def set_network_resolver(axis_request: AxisRequest, configuration: NetworkResolverConfiguration):
    params = configuration.get_all_params()
    request_config = JsonRequestConfig(method= MethodType.SET_RESOLVER_CONFIGURATION, version= axis_request.api_version, context= axis_request.request_context, params=params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_NETWORK_SETTINGS, request_config)
