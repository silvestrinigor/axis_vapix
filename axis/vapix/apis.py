from requests import Request, Response
from packaging.version import Version
from datetime import datetime
import json
import io

from .types import DevicePropertyType, ParamType, RequestParamType, MethodType, ApiPathType, TimeZoneType, ActionType
from .utils import serialize_datetime

class RequestAxisVapix:
    def __init__(self, host: str, port: int, api_version: str | None = None, context: str | None = None):
        self._api_verion = api_version
        self._context = context
        self._host = host
        self._port = port
        self._api_path_type: ApiPathType = ApiPathType.NONE
    
    def _get_basic_request_body(self):
        request_body = {}
        if self._api_verion != None: request_body[RequestParamType.API_VERSION.value] = self._api_verion
        if self._context != None: request_body[RequestParamType.CONTEXT.value] = self._context 
        return request_body

    def _get_supported_versions(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_SUPPORTED_VERSIONS.value
        # Check if api_path_type is None and raise an exception
        if self._api_path_type.value == None: 
            raise ValueError("API path type is not set")
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

class RequestAnalyticsMetadataProducerConfiguration(RequestAxisVapix):
    """
    API Discovery: id=analytics-metadata-config
    """
    def __init__(self, host: str, port: int, api_version: str, context=None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_ANALYTICS_METADATA_CONFIG

    def list_producers(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def set_enable_producers(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_supported_metadata(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_supported_versions(self):
        return super()._get_supported_versions()

class RequestApiDiscoveryService(RequestAxisVapix):
    """
    Firmware: 8.50 and later
    Property: Properties.ApiDiscovery.ApiDiscovery="yes"
    """
    def __init__(self, host: str, port: int, api_version: str, context=None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_API_DISCOVERY

    def get_api_list(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_API_LIST.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()

class RequestAplicationApi(RequestAxisVapix): # TODO: Implement this class
    """
    Property: Properties.EmbeddedDevelopment.Version exists.
    list.cgi requries:
    Property: Properties.EmbeddedDevelopment.Version=1.20 and later.
    """
    def __init__(self, host: str, port: int, api_version: str = None, context = None):
        super().__init__(host, port, api_version, context)

    def upload(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def control_application(self) : # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def configure_application(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def list(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

class RequestBasicDeviceInformation(RequestAxisVapix):
    """
    Firmware: 8.40 and later
    API Discovery: id=basic-device-info
    Property: BasicDeviceInfo.BasicDeviceInfo="yes"
    """
    def __init__(self, host: str, port: int, api_version: str, context=None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_BASIC_DEVICE_INFO
    
    def get_properties(self, properties: list[DevicePropertyType]):
        params = {ParamType.PROPERTY_LIST.value: [prop.value for prop in properties]}
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_PROPERTIES.value
        request_body[RequestParamType.PARAMS.value] = params
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_all_properties(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_ALL_PROPERTIES.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_all_unrestricted_properties(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_ALL_UNRESTRICTED_PROPERTIES.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()

class RequestCaptureMode(RequestAxisVapix): # TODO: Implement this class
    """
    Firmware: 8.50 and later
    """
    def __init__(self, host: str, port: int, api_version=None, context=None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")

    def get_capture_modes(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def set_capture_mode(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

class RequestCertificateManagementApi(RequestAxisVapix): # TODO: Implement this class
    def __init__(self, host: str, port: int, api_version=None, context=None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")

class RequestClearView(RequestAxisVapix): # TODO: Implement this class
    """
    Property: Properties.API.HTTP.Version=3
    Property: Properties.ClearView.ClearView=yes
    Firmware: 7.10 and later
    """
    def __init__(self, host: str, port: int, api_version=None, context=None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")

    def get_service_info(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_status(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def start(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def stop(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_supported_versions(self):
        return super()._get_supported_versions()

class RequestCustomHttpHeaderApi(RequestAxisVapix): # TODO: Implement this class
    """
    API Discovery: id=customhttpheader
    Firmware: 9.80 and later
    """
    def __init__(self, host: str, port: int, api_version=None, context=None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")
    
    def list(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def set(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def remove(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_supported_versions(self):
        return super()._get_supported_versions()

class RequestDayNightApi(RequestAxisVapix): # TODO: Implement this class
    """
    API Discovery: id=daynight
    """
    def __init__(self, host: str, port: int, api_version: str = None, context = None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")

class RequestDecoderApi(RequestAxisVapix): # TODO: Implement this class
    """
    Property: Properties.API.Decoder.Decoder=yes
    Product category: Network Video Decoder
    """
    def __init__(self, host: str, port: int, api_version: str = None, context = None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")

    def get_capabilities(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_view_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def set_view_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_supported_versions(self):
        return super()._get_supported_versions()

class RequestNetworkSettingsApi(RequestAxisVapix): # TODO: Implement this class
    """
    API Discovery: id=network-settings
    Property: Properties.API.HTTP.Version=3
    Firmware: 8.50 and later
    """
    def __init__(self, host: str, port: int, api_version: str, context=None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")

class RequestNetworkSettings(RequestAxisVapix): # TODO: Implement this class
    """
    Property: Properties.API.HTTP.Version=3
    Firmware: 5.00 and later.
    """
    def __init__(self, host: str, port: int, api_version: str, context=None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")

    def add_a_new_vlam(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_network_info(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def remove_vlam(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

class RequestDynamicOverlayApi(RequestAxisVapix): # TODO: Implement this class
    """
    Property: Properties.API.HTTP.Version=3
    Property: Properties.DynamicOverlay.DynamicOverlay=yes
    Property: Properties.DynamicOverlay.Version=1.00
    Firmware: 7.10 and later
    """
    def __init__(self, host: str, port: int, api_version=None, context=None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")

    def add_image(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def add_text(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def list(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def remove(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def set_image(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def set_text(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_overlay_capabilities(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

class RequestOverlayModifiers(RequestAxisVapix): # TODO: Implement this class
    """
    Property: Properties.OverlayModifiers.OverlayModifiers="yes"
    Firmware: 5.1 and later
    """
    def __init__(self, host: str, port: int, api_version=None, context=None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")

    def get_overlay_modifiers(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

class RequestFindMyDevice(RequestAxisVapix): # TODO: Implement this class
    """
    API Discovery: id=findmydevice
    """
    def __init__(self, host: str, port: int, api_version=None, context=None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")
    
    def find(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def stop(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def get_supported_versions(self):
        return super()._get_supported_versions()

class RequestFirmwareManagementApi(RequestAxisVapix):
    """
    Property: Properties.FirmwareManagemenrequest_body_class = AxisRequestBodyt.Version=1.3
    API Discovery: id=fwmgr
    Firmware: 7.40 and later
    """
    def __init__(self, host: str, port: int, api_version: str, context = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_FIRMWARE_MANAGEMENT
    
    def status(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def upgrade(self, file_obj: io.BufferedReader, auto_rool_back = None, factory_default_mode = None, auto_commit = None):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.UPGRADE.value
        request_body[RequestParamType.PARAMS.value] = {}
        if auto_rool_back != None: request_body[RequestParamType.PARAMS.value][ParamType.AUTO_ROLLBACK.value] = auto_rool_back
        if factory_default_mode != None: request_body[RequestParamType.PARAMS.value][ParamType.FACTORY_DEFAULT_MODE.value] = factory_default_mode
        if auto_commit != None: request_body[RequestParamType.PARAMS.value][ParamType.AUTO_COMMIT.value] = auto_commit
        files = {'file': ('firmware_file.bin', file_obj, 'application/octet-stream')}
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body, files=files)

    def commit(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def roolback(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def purge(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def factory_default(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def stop_auto(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def reboot(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_supported_versions(self):
        return super()._get_supported_versions()

class RequestTextOverlay(RequestAxisVapix): # TODO: Implement this class
    """
    To use this functionality set Image.I#.Text.TextEnabled to yes and set Image.I#.Text.String to contain the modifier #D.
    Access control: operator
    Method: GET
    """
    def __init__(self, host: str, port: int, api_version=None, context=None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")

class RequestTimeApi(RequestAxisVapix):
    """
    API Discovery: id=time-service
    Firmware: 9.30 and later
    """
    def __init__(self, host: str, port: int, api_version: str = None, context = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_TIME
    
    def get_date_time_info(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_DATE_TIME_INFO.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)
    
    def get_all(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_ALL.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)
    
    def set_date_time(self, date_time: datetime):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SET_DATE_TIME.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.DATE_TIME.value: serialize_datetime(date_time)}
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)
    
    def set_time_zone(self, timezone: TimeZoneType):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SET_TIME_ZONE.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.TIME_ZONE.value: timezone.value}
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)
    
    def set_posix_time_zone(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def reset_time_zone(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def get_suported_versions(self):
        return super()._get_supported_versions()

class RequestVideoStreaming(RequestAxisVapix): # TODO: Implement this class
    """
    Property: Properties.API.HTTP.Version=3
    Firmware: 5.00 and later.
    """
    def __init__(self, host: str, port: int, api_version: str = None, context = None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")
    
class RequestObjectAnalyticsApi(RequestAxisVapix): # TODO: Implement this class
    """
    Use /axis-cgi/applications/list.cgi to check if the application is installed on your Axis device.
    """
    def __init__(self, host: str, port: int, api_version: str = None, context = None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")

    def get_configuration_capabilities(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def get_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def set_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def send_alarm(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def get_accumulated_count(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def reset_accumulated_counts(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def reset_passthrough(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def get_occupancy(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_supported_versions(self):
        return super()._get_supported_versions()
    
class RequestLoiteringGuard(RequestAxisVapix): # TODO: Implement this class
    """
    Software: EmbeddedDevelopment version 2.13 or higher is required for the ACAP to work.
    Property: Properties.EmbeddedDevelopment.Version=2.13
    In order to check if the ACAP is installed, use /axis-cgi/applications/list.cgi, which shows the status of all installed ACAPs. It also lists the url to the configuration page and the license state of the ACAP.
    """
    def __init__(self, host: str, port: int, api_version: str = None, context = None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")
    
    def get_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def set_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def send_alarm_event(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def get_configuration_capabilities(self):
        raise NotImplementedError("This function is not implemented yet.")

    def get_supported_versions(self):
        return super()._get_supported_versions()

class ResponseAxisCgi: # TODO: Implement this class
    def __init__(self, response: Response):
        self._response = response

    def is_json_response_with_error(self):
        # Check if the response has a JSON Content-Type
        if self._response.headers.get("Content-Type") != "application/json":
            raise ValueError("Response is not in JSON format")
        # Check for successful HTTP status code
        if self._response.status_code != 200:
            raise ValueError(f"Unexpected response status code: {self._response.status_code}")
        # Safely attempt to parse JSON
        try:
            json_data = self._response.json()
        except ValueError:
            raise ValueError("Response body is not valid JSON")
        # Check if the error key exists and is properly structured
        error = json_data.get("error")
        return isinstance(error, dict)