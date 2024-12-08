from .defaults import ApiPathType
from .defaults import DevicePropertyType
from .defaults import MethodType
from .request import AxisRequest
from .request import JsonRequestConfig
from .defaults import ParamType
from .defaults import OverlayPositionType
from .defaults import OverlayColorType
from .defaults import TimeZoneType
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

def add_dynamic_overlay_image(axis_request: AxisRequest, camera: int, overlay_path: str):
    params = {ParamType.CAMERA.value: camera, ParamType.OVERLAY_PATH.value: overlay_path}
    request_config = JsonRequestConfig(method= MethodType.ADD_IMAGE, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def add_dynamic_overlay_text(axis_request: AxisRequest, camera: int, text: str, position: OverlayPositionType = None, font_size: int= None, text_color: OverlayColorType= None, back_ground_color: OverlayColorType = None, **kwargs):
    params = {ParamType.CAMERA.value: camera, ParamType.TEXT.value: text}
    if position != None:
        params[ParamType.POSITION.value] = position.value
    if font_size != None:
        params[ParamType.FONT_SIZE.value] = font_size
    if text_color != None:
        params[ParamType.TEXT_COLOR.value] = text_color.value
    if back_ground_color != None:
        params[ParamType.TEXT_BACK_GROUND_COLOR.value] = back_ground_color.value
    for key, value in kwargs.items():
        params[key] = value
    request_config = JsonRequestConfig(method= MethodType.ADD_TEXT, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def list_overlays(axis_request: AxisRequest):
    params = {}
    request_config = JsonRequestConfig(method= MethodType.LIST, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def set_dynamic_overlay_text(axis_request: AxisRequest, identity: int, text: str = None, position: OverlayPositionType = None, font_size: int= None, text_color: OverlayColorType= None, back_ground_color: OverlayColorType= None, **kwargs):
    params = {ParamType.IDENTITY.value: identity}
    if text != None:      
        params[ParamType.TEXT.value] = text
    if position != None:
        params[ParamType.POSITION.value] = position.value
    if font_size != None:
        params[ParamType.FONT_SIZE.value] = font_size
    if text_color != None:
        params[ParamType.TEXT_COLOR.value] = text_color.value
    if back_ground_color != None:
        params[ParamType.TEXT_BACK_GROUND_COLOR.value] = back_ground_color.value
    for key, value in kwargs.items():
        params[key] = value
    request_config = JsonRequestConfig(method= MethodType.SET_TEXT, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def set_dynamic_overlay_image(axis_request: AxisRequest, identity: int, camera: int= None, overlay_path: str= None, **kwargs):
    params = {ParamType.IDENTITY.value: identity}
    if overlay_path != None:
        params[ParamType.OVERLAY_PATH.value] = overlay_path
    if camera != None:
        params[ParamType.CAMERA.value] = camera
    for key, value in kwargs.items():
        params[key] = value
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

