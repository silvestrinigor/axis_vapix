from .types import DevicePropertyType, ParamType, RequestParamType, MethodType, ApiPathType
from requests import Request

class RequestNetworkVideo:
    def __init__(self, host: str, port: int, api_version = None, context = None):
        self.api_verion = api_version
        self.context = context
        self.host = host
        self.port = port
        self.api_path_type: ApiPathType = ApiPathType.NONE

    def _get_basic_request_body(self):
        request_body = {}
        if self.api_verion != None: request_body[RequestParamType.API_VERSION.value] = self.api_verion
        if self.context != None: request_body[RequestParamType.CONTEXT.value] = self.context 
        return request_body

    def _get_supported_versions(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_SUPPORTED_VERSIONS.value
        # Check if api_path_type is None and raise an exception
        if self.api_path_type.value == None: 
            raise ValueError("API path type is not set")
        return Request("POST", f"http://{self.host}:{self.port}/{self.api_path_type.value}", json= request_body)

class RequestAnalyticsMetadataProducerConfiguration(RequestNetworkVideo):
    # TODO: Implement this class
    """
    API Discovery: id=analytics-metadata-config
    """
    def __init__(self, host, port, api_version=None, context=None):
        super().__init__(host, port, api_version, context)
        self.api_path_type = ApiPathType.AXIS_CGI_ANALYTICS_METADATA_CONFIG

    def list_producers(self):
        # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def set_enable_producers(self):
        # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_supported_metadata(self):
        # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_supported_versions(self):
        return super()._get_supported_versions()

class RequestApiDiscoveryService(RequestNetworkVideo):
    """
    Firmware: 8.50 and later
    Property: Properties.ApiDiscovery.ApiDiscovery="yes"
    """
    def __init__(self, host, port, api_version=None, context=None):
        super().__init__(host, port, api_version, context)
        self.api_path_type = ApiPathType.AXIS_CGI_API_DISCOVERY

    def get_api_list(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_API_LIST.value
        return Request("POST", f"http://{self.host}:{self.port}/{self.api_path_type.value}", json= request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()

class RequestBasicDeviceInformation(RequestNetworkVideo):
    """
    Firmware: 8.40 and later
    API Discovery: id=basic-device-info
    Property: BasicDeviceInfo.BasicDeviceInfo="yes"
    """
    def __init__(self, host, port, api_version=None, context=None):
        super().__init__(host, port, api_version, context)
        self.api_path_type = ApiPathType.AXIS_CGI_BASIC_DEVICE_INFO
    
    def get_properties(self, properties: list[DevicePropertyType]):
        params = {ParamType.PROPERTY_LIST.value: [prop.value for prop in properties]}
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_PROPERTIES.value
        request_body[RequestParamType.PARAMS.value] = params
        return Request("POST", f"http://{self.host}:{self.port}/{self.api_path_type.value}", json= request_body)

    def get_all_properties(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_ALL_PROPERTIES.value
        return Request("POST", f"http://{self.host}:{self.port}/{self.api_path_type.value}", json= request_body)

    def get_all_unrestricted_properties(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_ALL_UNRESTRICTED_PROPERTIES.value
        return Request("POST", f"http://{self.host}:{self.port}/{self.api_path_type.value}", json= request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()

class RequestCaptureMode(RequestNetworkVideo):
    # TODO: Implement this class
    """
    Firmware: 8.50 and later
    """
    def __init__(self, host: str, port: int, api_version=None, context=None):
        super().__init__(host, port, api_version, context)

    def get_capture_modes(self):
        # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def set_capture_mode(self):
        # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

class RequestCertificateManagementApi(RequestNetworkSettings):
    # TODO: Implement this class
    raise NotImplementedError("This function is not implemented yet.")

class RequestClearView(RequestNetworkVideo):
    # TODO: Implement this class
    def __init__(self, host: str, port: int, api_version=None, context=None):
        super().__init__(host, port, api_version, context)


class RequestNetworkSettingsApi(RequestNetworkVideo):
    # TODO: Implement this class
    """
    API Discovery: id=network-settings
    Property: Properties.API.HTTP.Version=3
    Firmware: 8.50 and later
    """
    def __init__(self, host, port, api_version=None, context=None):
        super().__init__(host, port, api_version, context)
        
class RequestNetworkSettings(RequestNetworkVideo):
    # TODO: Implement this class
    """
    Property: Properties.API.HTTP.Version=3
    Firmware: 5.00 and later.
    """
    def __init__(self, host, port, api_version=None, context=None):
        super().__init__(host, port, api_version, context)
        
    def add_a_new_vlam(self):
        # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_network_info(self):
        # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def remove_vlam(self):
        # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

class RequestDynamicOverlayApi(RequestNetworkVideo):
    # TODO: Implement this class
    """
    Property: Properties.API.HTTP.Version=3
    Property: Properties.DynamicOverlay.DynamicOverlay=yes
    Property: Properties.DynamicOverlay.Version=1.00
    Firmware: 7.10 and later
    """
    def __init__(self, host: str, port: int, api_version=None, context=None):
        super().__init__(host, port, api_version, context)

    def add_image(self):
        # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def add_text(self):
        # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def list(self):
        # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def remove(self):
        # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def set_image(self):
        # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def set_text(self):
        # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_overlay_capabilities(self):
        # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

class RequestOverlayModifiers(RequestNetworkVideo):
    # TODO: Implement this class
    """
    Property: Properties.OverlayModifiers.OverlayModifiers="yes"
    Firmware: 5.1 and later
    """
    def __init__(self, host: str, port: int, api_version=None, context=None):
        super().__init__(host, port, api_version, context)

    def get_overlay_modifiers(self):
        # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

class RequestTextOverlay(RequestNetworkVideo):
    # TODO: Implement this class
    """
    To use this functionality set Image.I#.Text.TextEnabled to yes and set Image.I#.Text.String to contain the modifier #D.
    Access control: operator
    Method: GET
    """
    def __init__(self, host: str, port: int, api_version=None, context=None):
        super().__init__(host, port, api_version, context)
