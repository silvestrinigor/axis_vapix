from .types import OverlayPositionType, OverlayColorType, OverlayPositionCustomValue, ParamType, ServersSourceType, StaticAddressConfigurationParamsType, IPAddressConfigurationModeType, RequestParamType, MethodType
from packaging.version import Version

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
    
class HostnameConfiguration:
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
    
class StaticAddressConfigurations:
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
        
class IPv4AddressConfiguration:
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
    
class NetworkResolverConfiguration:
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
        
class AxisDevice:
    firmware_version: Version
    prod_type: str
    address: str
    
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        
    def get_base_url(self):
        return f"http://{self.host}:{self.port}/"
    
class AxisRequestBody:
    def __init__(self):
        self.request_body = {}
    
    def add__or_set_api_version(self, api_version: Version):
        self.add_or_set_request_param(RequestParamType.API_VERSION, api_version.__str__())
    
    def add_or_set_context(self, text:str):
        self.add_or_set_request_param(RequestParamType.CONTEXT, text)
    
    def add_or_set_method(self, method: MethodType):
        self.add_or_set_request_param(RequestParamType.METHOD, method.value)
    
    def add_or_set_method_params(self, param_type: ParamType, value):
        if RequestParamType.PARAMS.value not in self.request_body:
            self.request_body[RequestParamType.PARAMS.value] = {}
        if not isinstance(self.request_body[RequestParamType.PARAMS.value], dict):
            raise ValueError("PARAMS must be a dictionary.")
        self.request_body[RequestParamType.PARAMS.value][param_type.value] = value
        request_params = self.request_body[RequestParamType.PARAMS.value]
        request_params = {key: value for key, value in request_params.items() if value is not None}
        self.request_body[RequestParamType.PARAMS.value] = request_params
    
    def add_or_set_request_param(self, param_type: RequestParamType, value):
        self.request_body[param_type.value] = value
    
    def get_request_body(self):
        return {key: value for key, value in self.request_body.items() if value is not None}
    