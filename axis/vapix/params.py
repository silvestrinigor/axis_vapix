from packaging.version import Version
from .types import OverlayPositionType, OverlayColorType, ParamType, ServersSourceType, StaticAddressConfigurationParamsType, IPAddressConfigurationModeType, RequestParamType, MethodType, LinkLocalModeType

class OverlayPositionCustomValue:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y
    
    @property
    def value(self):
        return [self.x, self.y]

class TextOverlay:
    camera:int | None= None
    font_size:int | None = None
    identity: int | None = None
    indicator: str | None = None
    position: OverlayPositionType | OverlayPositionCustomValue = OverlayPositionType.NONE
    text: str | None = None
    text_bg_color: OverlayColorType = OverlayColorType.NONE
    text_color: OverlayColorType = OverlayColorType.NONE
    text_length: int | None = None
    text_ol_color: OverlayColorType = OverlayColorType.NONE
    visible: bool | None = None

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
    camera:int | None = None
    identity: int | None = None
    overlay_path: str | None = None
    position: OverlayPositionType | OverlayPositionCustomValue = OverlayPositionType.NONE
    visible: bool | None = None

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
    enable: bool | None = None
    servers_source: ServersSourceType | None = None
    static_servers_list: list[str] | None = None
    
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
    use_dhcp_hostname: bool | None = None
    static_hostname: str | None = None
    
    def get_all_params(self):
        all_params = {
            ParamType.USE_DHCP_HOSTNAME.value: self.use_dhcp_hostname,
            ParamType.STATIC_HOSTNAME.value: self.static_hostname
        }
        # Remove any keys with None values
        all_params = {key: value for key, value in all_params.items() if value is not None}
        return all_params
    
class StaticAddressConfigurations:
    address: str | None = None
    prefix_length: int | None = None
    broadcast: str | None = None
    
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
    device_name: str | None = "eth0"
    enable: bool | None = None
    configuration_mode: IPAddressConfigurationModeType = IPAddressConfigurationModeType.NONE
    link_local_mode: LinkLocalModeType | None = None
    static_address_configurations: list[StaticAddressConfigurations] = None
    use_static_dhcp_fallback: bool | None = None
    use_dhcp_static_routes: bool | None = None
    def get_all_params(self):
        all_params = {
            ParamType.DEVICE_NAME.value: self.device_name,
            ParamType.ENABLE.value: self.enable,
            ParamType.CONFIGURATION_MODE.value: self.configuration_mode.value,
            ParamType.LINK_LOCAL_MODE.value: self.link_local_mode.value,
            ParamType.STATIC_ADDRESS_CONFIGURATION.value: self.static_address_configurations,
            ParamType.USE_STATIC_DHCP_FALLBACK.value: self.use_static_dhcp_fallback,
            ParamType.USE_DHCP_STATIC_ROUTES.value: self.use_dhcp_static_routes
        }
        # Remove any keys with None values
        all_params = {key: value for key, value in all_params.items() if value is not None}
        return all_params
    
class NetworkResolverConfiguration:
    use_dhcp_resolver_info: bool | None = None
    static_name_servers: list[str] | None = None
    static_search_domains: list[str] | None = None
    static_domain_name: str | None = None
    
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
    
class AnalyticsMetadataVideoChannel:
    channel: int | None = None
    enabled: bool | None = None

    def get_all_params(self):
        all_params = {
            ParamType.CHANNEL.value: self.channel,
            ParamType.ENABLED.value: self.enabled
        }
        # Remove any keys with None values
        all_params = {key: value for key, value in all_params.items() if value is not None}
        return all_params
    
class AnalyticsMetadataProducer:
    name: str | None = None
    video_channels: list[AnalyticsMetadataVideoChannel] | None = None

    def get_all_params(self):
        video_channels = []
        for video_channel in self.video_channels:
            video_channels.append(video_channel.get_all_params())
            
        all_params = {
            ParamType.NAME.value: self.name,
            ParamType.VIDEO_CHANNELS.value: video_channels
        }
        # Remove any keys with None values
        all_params = {key: value for key, value in all_params.items() if value is not None}
        return all_params

class ApiVersion(Version):
    def __init__(self, major: int, minor: int):
        super().__init__(f"{major}.{minor}")

class FirmwareVersion(Version):
    def __init__(self, major: int, minor: int, patch: int):
        super().__init__(f"{major}.{minor}.{patch}")

