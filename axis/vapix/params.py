from dataclasses import dataclass, field, asdict
from packaging.version import Version
from .types import OverlayPositionType, OverlayColorType, ParamType, ServersSourceType, StaticAddressConfigurationParamsType, IPAddressConfigurationModeType, RequestParamType, MethodType, LinkLocalModeType

def _remove_none_values(data: dict) -> dict:
    """Utility function to recursively remove keys with None values."""
    if not isinstance(data, dict):
        return data
    return {
        key: _remove_none_values(value)
        for key, value in data.items()
        if value is not None
    }

@dataclass
class OverlayPositionCustomValue:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y
    
    @property
    def value(self):
        return [self.x, self.y]

@dataclass
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
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
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
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
class NTPClientConfiguration:
    enable: bool | None = None
    nts_enable: bool | None = None
    servers_source: ServersSourceType | None = None
    static_servers_list: list[str] | None = None
    static_ntske_servers_list: list[str] | None = None
    def get_all_params(self):
        all_params = {
            ParamType.ENABLE.value: self.enable,
            ParamType.NTS_ENABLE.value: self.nts_enable,
            ParamType.SERVERS_SOURCE.value: self.servers_source.value,
            ParamType.STATIC_SERVERS.value: self.static_servers_list,
            ParamType.STATIC_NTSKE_SERVERS.value: self.static_ntske_servers_list
        }
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
class HostnameConfiguration:
    use_dhcp_hostname: bool | None = None
    static_hostname: str | None = None
    
    def get_all_params(self):
        all_params = {
            ParamType.USE_DHCP_HOSTNAME.value: self.use_dhcp_hostname,
            ParamType.STATIC_HOSTNAME.value: self.static_hostname
        }
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
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
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass  
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
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
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
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
class AnalyticsMetadataVideoChannel:
    channel: int | None = None
    enabled: bool | None = None

    def get_all_params(self):
        all_params = {
            ParamType.CHANNEL.value: self.channel,
            ParamType.ENABLED.value: self.enabled
        }
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
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
        all_params = _remove_none_values(all_params)
        return all_params

class ApiVersion(Version):
    def __init__(self, major: int, minor: int):
        super().__init__(f"{major}.{minor}")

class FirmwareVersion(Version):
    def __init__(self, major: int, minor: int, patch: int):
        super().__init__(f"{major}.{minor}.{patch}")

@dataclass
class LoiteringGuardCamera:
    active: bool | None = None
    rotation: str | None = None
    overlay_resolution: str | None = None

    def get_all_params(self):
        all_params = {
            ParamType.ACTIVE.value: self.active,
            ParamType.ROTATION.value: self.rotation,
            ParamType.OVERLAY_RESOLUTION.value: self.overlay_resolution
        }
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
class ProfileFilter:
    filter_type: str | None = None
    data: list | None = None
    active: bool | None = None

    def get_all_params(self):
        all_params = {
            ParamType.TYPE.value: self.filter_type,
            ParamType.DATA.value: self.data,
            ParamType.ACTIVE.value: self.active
        }
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
class LoiteringGuardTrigger:
    trigger_type: str | None = None
    data: list | None = None
    active: bool | None = None

    def get_all_params(self):
        all_params = {
            ParamType.TYPE.value: self.trigger_type,
            ParamType.DATA.value: self.data,
            ParamType.ACTIVE.value: self.active
        }
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
class LoiteringGuardPerspective:
    trigger_type: str | None = None
    data: list | None = None
    height: int | None = None

    def get_all_params(self):
        all_params = {
            ParamType.TYPE.value: self.trigger_type,
            ParamType.DATA.value: self.data,
            ParamType.HEIGHT.value: self.height
        }
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
class LoiteringGuardProfile:
    name: str | None = None
    uid: int | None = None
    camera: int | None = None
    alarm_overlay_enabled: bool | None = None
    filters: list[ProfileFilter] | None = None
    triggers: list[LoiteringGuardTrigger] | None = None
    presets: list | None = None
    perspectives: list[LoiteringGuardPerspective] | None = None

    def get_all_params(self):
        filters = [filter.get_all_params() for filter in (self.filters or [])]
        triggers = [trigger.get_all_params() for trigger in (self.triggers or [])]
        perspectives = [perspective.get_all_params() for perspective in (self.perspectives or [])]
        all_params = {
            ParamType.NAME.value: self.name,
            ParamType.UID.value: self.uid,
            ParamType.CAMERA.value: self.camera,
            ParamType.ALARM_OVERLAY_ENABLED.value: self.alarm_overlay_enabled,
            ParamType.FILTERS.value: filters,
            ParamType.TRIGGERS.value: triggers,
            ParamType.PRESETS.value: self.presets,
            ParamType.PERSPECTIVES.value: perspectives
        }
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
class LoiteringGuardConfiguration:
    cameras: list[LoiteringGuardCamera] | None = None
    profiles: list[LoiteringGuardProfile] | None = None

    def get_all_params(self):
        cameras = [camera.get_all_params() for camera in (self.cameras or [])]
        profiles = [profile.get_all_params() for profile in (self.profiles or [])]
        all_params = {
            ParamType.CAMERAS.value: cameras,
            ParamType.PROFILES.value: profiles
        }
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
class ObjectAnalyticsDevice:
    id: int | None = None
    device_type: str | None = None
    rotation: str | None = None
    is_active: bool | None = None

    def get_all_params(self):
        all_params = {
            ParamType.ID.value: self.id,
            ParamType.TYPE.value: self.device_type,
            ParamType.ROTATION.value: self.rotation,
            ParamType.ACTIVE.value: self.is_active
        }
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
class ObjectAnalyticsMetadataOverlay:
    id: int | None = None
    draw_on_all_resolutions: bool | None = None
    resolutions: list[int] | None = None # "resolutions": ["<width>x<height>", "<width>x<height>", ...]

    def get_all_params(self):
        all_params = {
            ParamType.ID.value: self.id,
            ParamType.DRAW_ON_ALL_RESOLUTIONS.value: self.draw_on_all_resolutions,
            ParamType.RESOLUTIONS.value: self.resolutions
        }
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
class PerspectiveBar:
    height: int | None = None
    points: list | None = None # "points": [[<x>, <y>], [<x>, <y>], ...]

    def get_all_params(self):
        all_params = {
            ParamType.HEIGHT.value: self.height,
            ParamType.POINTS.value: self.points
        }
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
class ObjectAnalyticsPerspective:
    id: int | None = None
    bars: list[PerspectiveBar] | None = None

@dataclass
class ObjectAnalyticsTrigger:
    trigger_type: str | None = None
    vertices: list | None = None # "vertices": [[<x>, <y>], [<x>, <y>], ...]
    alarm_direction: str | None = None # "alarmDirection": "leftToRight", "rightToLeft"
    counting_direction: str | None = None # "countingDirection": "leftToRight", "rightToLeft"

    def get_all_params(self):
        all_params = {
            ParamType.TYPE.value: self.trigger_type,
            ParamType.VERTICES.value: self.vertices,
            ParamType.ALARM_DIRECTION.value: self.alarm_direction,
            ParamType.COUNTING_DIRECTION.value: self.counting_direction
        }
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
class ScenarioFilter:
    filter_type: str | None = None
    width: int | None = None
    height: int | None = None
    time: int | None = None
    distance: int | None = None
    min_speed: float | None = None
    max_speed: float | None = None
    vertices: list | None = None # "vertices": [[<x>, <y>], [<x>, <y>], ...]

    def get_all_params(self):
        all_params = {
            ParamType.TYPE.value: self.filter_type,
            ParamType.WIDTH.value: self.width,
            ParamType.HEIGHT.value: self.height,
            ParamType.TIME.value: self.time,
            ParamType.DISTANCE.value: self.distance,
            ParamType.MIN_SPEED.value: self.min_speed,
            ParamType.MAX_SPEED.value: self.max_speed,
            ParamType.VERTICES.value: self.vertices
        }
        all_params = _remove_none_values(all_params)
        return all_params



@dataclass
class ObjectAnalyticsObjectClassificator:
    classificator_type: str | None = None
    sub_types: list | None = None 

    def get_all_params(self):
        all_params = {
            ParamType.TYPE.value: self.classificator_type,
            ParamType.SUB_TYPES.value: self.sub_types
        }
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
class ObjectAnalyticsScenario:
    id: int | None = None
    name: str | None = None
    scenario_type: str | None = None
    metadata_overlay: int | None = None
    alarm_rate: str | None = None
    devices: list[int] | None = None
    triggers: list[ObjectAnalyticsTrigger] | None = None
    filters: list[ScenarioFilter] | None = None
    object_classificators: list[ObjectAnalyticsObjectClassificator] | None = None
    perspectives: list[int] | None = None # "perspectives": [id]
    presets: list[int] | None = None # "presets": [id]

    def get_all_params(self):
        triggers = [trigger.get_all_params() for trigger in (self.triggers or [])]
        filters = [filter.get_all_params() for filter in (self.filters or [])]
        object_classificators = [object_classificator.get_all_params() for object_classificator in (self.object_classificators or [])]
        all_params = {
            ParamType.ID.value: self.id,
            ParamType.NAME.value: self.name,
            ParamType.TYPE.value: self.scenario_type,
            ParamType.METADATA_OVERLAY.value: self.metadata_overlay,
            ParamType.ALARM_RATE.value: self.alarm_rate,
            ParamType.DEVICES.value: self.devices,
            ParamType.TRIGGERS.value: triggers,
            ParamType.FILTERS.value: filters,
            ParamType.CLASSIFICATORS.value: object_classificators,
            ParamType.PERSPECTIVES.value: self.perspectives,
            ParamType.PRESETS.value: self.presets
        }
        all_params = _remove_none_values(all_params)
        return all_params

@dataclass
class ObjectAnalyticsConfiguration:
    devices: list[ObjectAnalyticsDevice] | None = None
    metadata_overlay: list[ObjectAnalyticsMetadataOverlay] | None = None
    perspectives: list[ObjectAnalyticsPerspective] | None = None
    scenarios: list[ObjectAnalyticsScenario] | None = None

    def get_all_params(self):
        devices = [device.get_all_params() for device in (self.devices or [])]
        metadata_overlay = [overlay.get_all_params() for overlay in (self.metadata_overlay or [])]
        perspectives = [perspective.get_all_params() for perspective in (self.perspectives or [])]
        scenarios = [scenario.get_all_params() for scenario in (self.scenarios or [])]
        all_params = {
            ParamType.DEVICES.value: devices,
            ParamType.METADATA_OVERLAY.value: metadata_overlay,
            ParamType.PERSPECTIVES.value: perspectives,
            ParamType.SCENARIOS.value: scenarios
        }
        all_params = _remove_none_values(all_params)
        return all_params