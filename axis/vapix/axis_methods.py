import requests.auth
from .types import ApiPathType, RequestMethod, MethodType, DevicePropertyType, ParamType
from .request import RequestBuilder
from .defaults import AxisDevice, AxisRequestBody, ApiVersion
import requests

def get_supported_versions(device: AxisDevice, api: ApiPathType, context: str = ""):
    url = device.get_base_url() + api.value
    request_body_class = AxisRequestBody()
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.GET_SUPPORTED_VERSIONS)
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    request_build.set_auth(device.username,device.password, requests.auth.HTTPDigestAuth)
    return request_build

def get_properties(device: AxisDevice, properties: list[DevicePropertyType], api_version: ApiVersion,context: str = ""):
    params = {ParamType.PROPERTY_LIST.value: [prop.value for prop in properties]}
    url = device.get_base_url() + ApiPathType.AXIS_CGI_BASIC_DEVICE_INFO.value
    request_body_class = AxisRequestBody()
    request_body_class.add_or_set_context(context)
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_method_params(params)
    request_body_class.add_or_set_method(MethodType.GET_PROPERTIES)
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    request_build.set_auth(device.username,device.password, requests.auth.HTTPDigestAuth)
    return request_build
"""
def get_all_properties(axis_request: AxisRequest):
    request_config = axis_json_request_config(method= MethodType.GET_ALL_PROPERTIES, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_BASIC_DEVICE_INFO, request_config)
    
def get_all_unrestricted_properties(axis_request: AxisRequest):
    request_config = axis_json_request_config(method= MethodType.GET_ALL_UNRESTRICTED_PROPERTIES, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_BASIC_DEVICE_INFO, request_config)

def get_api_list(axis_request: AxisRequest):
    request_config = axis_json_request_config(method= MethodType.GET_API_LIST, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_API_DISCOVERY, request_config)

def add_dynamic_overlay_image(axis_request: AxisRequest, image_overlay: ImageOverlay):
    params = image_overlay.get_all_params()
    request_config = axis_json_request_config(method= MethodType.ADD_IMAGE, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def add_dynamic_overlay_text(axis_request: AxisRequest, text_overlay: TextOverlay):
    params = text_overlay.get_all_params()
    request_config = axis_json_request_config(method= MethodType.ADD_TEXT, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def list_overlays(axis_request: AxisRequest):
    params = {}
    request_config = axis_json_request_config(method= MethodType.LIST, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def set_dynamic_overlay_text(axis_request: AxisRequest, text_overlay: TextOverlay):
    params = text_overlay.get_all_params()
    request_config = axis_json_request_config(method= MethodType.SET_TEXT, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def set_dynamic_overlay_image(axis_request: AxisRequest, image_overlay: ImageOverlay):
    params = image_overlay.get_all_params()
    request_config = axis_json_request_config(method= MethodType.SET_IMAGE, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def remove_dynamic_overlay(axis_request: AxisRequest, identity: int):
    params = {ParamType.IDENTITY.value: identity}
    request_config = axis_json_request_config(method= MethodType.REMOVE, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def get_dynamic_overlay_capabilities(axis_request: AxisRequest):
    request_config = axis_json_request_config(method= MethodType.GET_OVERLAY_CAPABILITIES, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY, request_config)

def get_capture_modes(axis_request: AxisRequest):
    request_config = axis_json_request_config(method= MethodType.GET_CAPTURE_MODES, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_CAPTURE_MODE, request_config)

def set_capture_mode(axis_request: AxisRequest, channel: int, capture_mode_id: int):
    request_config = axis_json_request_config(method= MethodType.SET_CAPTURE_MODE, version= axis_request.api_version, context= axis_request.request_context, channel= channel, capture_mode_id= capture_mode_id)
    return axis_request.request_post(ApiPathType.AXIS_CGI_CAPTURE_MODE, request_config)

def get_clear_view_service_info(axis_request: AxisRequest):
    params = {}
    request_config = axis_json_request_config(method= MethodType.GET_SERVICE_INFO, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_CLEAR_VIEW, request_config)

def start_cleaning_view(axis_request: AxisRequest, id: int, duration: int = None):
    params = {ParamType.ID.value: id}
    if duration != None:
        params[ParamType.DURATION.value] = duration
    request_config = axis_json_request_config(method= MethodType.START, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_CLEAR_VIEW, request_config)

def stop_cleaning_view(axis_request: AxisRequest, id: int):
    params = {ParamType.ID.value: id}
    request_config = axis_json_request_config(method= MethodType.STOP, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_CLEAR_VIEW, request_config)

def get_cleaning_view_status(axis_request: AxisRequest, id: int):
    params = {ParamType.ID.value: id}
    request_config = axis_json_request_config(method= MethodType.GET_STATUS, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_CLEAR_VIEW, request_config)

def get_date_time_info(axis_request: AxisRequest):
    request_config = axis_json_request_config(method= MethodType.GET_DATE_TIME_INFO, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_TIME, request_config)

def get_all_date_time_api_info(axis_request: AxisRequest):
    request_config = axis_json_request_config(method= MethodType.GET_ALL, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_TIME, request_config)

def set_date_time(axis_request: AxisRequest, date_time: datetime):
    params = {ParamType.DATE_TIME.value: serialize_datetime(date_time)}
    request_config = axis_json_request_config(method= MethodType.SET_DATE_TIME, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_TIME, request_config)

def set_time_zone(axis_request: AxisRequest, time_zone: TimeZoneType):
    params = {ParamType.TIME_ZONE.value: time_zone.value}
    request_config = axis_json_request_config(method= MethodType.SET_TIME_ZONE, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_TIME, request_config)

def set_posix_time_zone(axis_request: AxisRequest, posix_time_zone: str, enable_dst: bool):
    params = {ParamType.POSIX_TIME_ZONE.value: posix_time_zone, ParamType.ENABLE_DST.value: enable_dst}
    request_config = axis_json_request_config(method= MethodType.SET_POSIX_TIME_ZONE, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_TIME, request_config)

def reset_time_zone(axis_request: AxisRequest):
    request_config = axis_json_request_config(method= MethodType.RESET_TIME_ZONE, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_TIME, request_config)

def get_ntp_info(axis_request: AxisRequest):
    request_config = axis_json_request_config(method= MethodType.GET_NTP_INFO, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_NTP, request_config)

def set_ntp_client_configuration(axis_request: AxisRequest, configuration: NTPClientConfiguration):
    params = configuration.get_all_params()
    request_config = axis_json_request_config(method= MethodType.SET_NTP_CLIENT_CONFIGURATION, version= axis_request.api_version, context= axis_request.request_context, params= params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_NTP, request_config)

def get_network_info(axis_request: AxisRequest):
    request_config = axis_json_request_config(method= MethodType.GET_NETWORK_INFO, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_NETWORK_SETTINGS, request_config)

def set_network_hostname(axis_request: AxisRequest, configuration: HostnameConfiguration):
    params = configuration.get_all_params()
    request_config = axis_json_request_config(method= MethodType.SET_HOSTNAME_CONFIGURATION, version= axis_request.api_version, context= axis_request.request_context, params=params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_NETWORK_SETTINGS, request_config)

def set_network_ipv4_address(axis_request: AxisRequest, configuration: IPv4AddressConfiguration):
    params = configuration.get_all_params()
    request_config = axis_json_request_config(method= MethodType.SET_IPV4_ADDRESS_CONFIGURATION, version= axis_request.api_version, context= axis_request.request_context, params=params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_NETWORK_SETTINGS, request_config)

def set_network_resolver(axis_request: AxisRequest, configuration: NetworkResolverConfiguration):
    params = configuration.get_all_params()
    request_config = axis_json_request_config(method= MethodType.SET_RESOLVER_CONFIGURATION, version= axis_request.api_version, context= axis_request.request_context, params=params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_NETWORK_SETTINGS, request_config)

def get_firmware_status(axis_request: AxisRequest):
    request_config = axis_json_request_config(method= MethodType.STATUS, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_FIRMWARE_MANAGEMENT, request_config)

def set_firmware_rollback(axis_request: AxisRequest):
    request_config = axis_json_request_config(method= MethodType.ROLLBACK, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_FIRMWARE_MANAGEMENT, request_config)

def set_firmware_factory_default(axis_request: AxisRequest, mode: FactoryDefaultModeType):
    request_config = axis_json_request_config(method= MethodType.ROLLBACK, version= axis_request.api_version, context= axis_request.request_context, factory_default_mode= mode)
    return axis_request.request_post(ApiPathType.AXIS_CGI_FIRMWARE_MANAGEMENT, request_config)

def set_firmware_reboot(axis_request: AxisRequest):
    request_config = axis_json_request_config(method= MethodType.REBOOT, version= axis_request.api_version, context= axis_request.request_context)
    return axis_request.request_post(ApiPathType.AXIS_CGI_FIRMWARE_MANAGEMENT, request_config)

def upgrade_firmware_system_settings(axis_request: AxisRequest, file_name: str, file_obj: io.BufferedReader,  type: FirmwareUpgradeType = FirmwareUpgradeType.NORMAL) -> requests.Response:
    url_params = RequestUrlParamType.TYPE.value + type.value
    files = {file_name: file_obj}
    return axis_request.request_post(ApiPathType.AXIS_CGI_SYSTEM_SETTINGS_FIRMWARE_UPGRADE, url_params=url_params, files=files)

def upgrade_firmware(axis_request: AxisRequest, file_name: str, file_obj: io.BufferedReader, auto_rool_back = None, factory_default_mode: FactoryDefaultModeType = FactoryDefaultModeType.NONE, auto_commit = None) -> requests.Response:
    params = {
        ParamType.FACTORY_DEFAULT_MODE.value: factory_default_mode.value,
        ParamType.AUTO_COMMIT.value: auto_commit,
        ParamType.AUTO_ROLLBACK.value: auto_rool_back
    }
    params = {key: value for key, value in params.items() if value is not None}
    files = {file_name: file_obj}
    request_config = axis_json_request_config(method= MethodType.ROLLBACK, version= axis_request.api_version, context= axis_request.request_context, files=files, params=params)
    return axis_request.request_post(ApiPathType.AXIS_CGI_FIRMWARE_MANAGEMENT, request_config)

def param_handle(axis_request: AxisRequest, action: ActionType, **keyargs) -> requests.Response:
    url_params = RequestUrlParamType.ACTION.value + action.value
    if keyargs:
        encoded_params = urllib.parse.urlencode(keyargs)
        url_params = f"{url_params}&{encoded_params}"
    if action == ActionType.LIST:
        return axis_request.request_get(ApiPathType.AXIS_CGI_PARAM, url_params=url_params)
    else:
        return axis_request.request_post(ApiPathType.AXIS_CGI_PARAM, url_params=url_params)
"""