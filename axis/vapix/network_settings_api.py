from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from requests import Request
from enum import Enum
from typing import Optional, List, Dict
from .requests import VapixRequestBuilderWithVersion
from .api import VapixApiABC

class LinkLocalModeType(Enum):
    OFF = "off"
    ON = "on"
    FALLBACK = "fallback"

class IPAddressConfigurationModeType(Enum):
    DHCP = "DHCP"
    STATIC = "static"    
    
@dataclass
class HostnameConfiguration:
    useDhcpHostname: Optional[bool] = None
    staticHostname: Optional[str] = None

@dataclass
class StaticAddressConfigurations:
    address: Optional[str] = None
    prefixLength: Optional[int] = None
    broadcast: Optional[str] = None

@dataclass  
class IPv4AddressConfiguration:
    deviceName: Optional[str] = None
    enable: Optional[bool] = None
    configurationMode: Optional[str] = None
    linkLocalMode: Optional[str] = None
    staticAddressConfigurations: Optional[List[StaticAddressConfigurations]] = None
    useStaticDhcpFallback: Optional[bool] = None
    useDhcpStaticRoutes: Optional[bool] = None

@dataclass
class IPv6AddressConfiguration:
    deviceName: Optional[str] = None
    enable: Optional[bool] = None
    configurationMode: Optional[str] = None
    linkLocalMode: Optional[str] = None
    staticAddressConfigurations: Optional[List[StaticAddressConfigurations]] = None
    useStaticDhcpFallback: Optional[bool] = None
    useDhcpStaticRoutes: Optional[bool] = None

@dataclass
class WLANStationAuthenticationParams:
    identity: Optional[str] = None
    password: Optional[str] = None
    eapolVersion: Optional[str] = None
    peapVersion: Optional[str] = None
    label: Optional[int] = None

@dataclass
class WLANStationAuthentication:
    mode: Optional[str] = None
    params: Optional[WLANStationAuthenticationParams | Dict] = None

@dataclass
class WLANStationConfiguration:
    deviceName: Optional[str] = None
    ssid: Optional[str] = None
    authentication: Optional[WLANStationAuthentication | Dict] = None

class NetworkSettingsApiABC(VapixApiABC, ABC):
    API_PATH = "axis-cgi/network_settings.cgi"
    API_DISCOVERY_ID = "network-settings"
    FIRMWARE_LOWER_SUPPORTED_VERSION = "8.50"

    @abstractmethod
    def addVlan(self, masterDeviceName: str, VlanId: int):
        pass
    
    @abstractmethod
    def getNetworkInfo(self):
        pass
    
    @abstractmethod
    def removeVlan(self, VlanName: str):
        pass
        
    @abstractmethod
    def setHostnameConfiguration(self, useDhcpHostname: Optional[bool], staticHostname: Optional[str]):
        pass
    
    @abstractmethod
    def setIPv4AddressConfiguration(self, configuration: Dict | IPv4AddressConfiguration):
        pass
    
    @abstractmethod
    def setIPv6AddressConfiguration(self):
        pass
    
    @abstractmethod
    def setGlobalProxyConfiguration(self, httpProxy: str, httpsProxy: str):
        pass
    
    @abstractmethod
    def setResolverConfiguration(self, useDhcpResolverInfo: Optional[bool], staticNameServers: Optional[List[str]], staticSearchDomains: Optional[List[str]], staticDomainName: Optional[str]):
        pass
    
    @abstractmethod
    def setWired8021XConfiguration(self, deviceName: Optional[str], enabled: Optional[bool], mode: Optional[str], identity: Optional[str], eapolVersion: Optional[str]):
        pass
    
    @abstractmethod
    def scanWLANNetworks(self, deviceName: Optional[str], refresh: Optional[bool]):
        pass
    
    @abstractmethod
    def setWLANStationConfiguration(self, configuration: WLANStationConfiguration | Dict):
        pass
    
    @abstractmethod
    def testWLANStationSettings(self):
        pass
    
    @abstractmethod
    def wlanSwitchAPToStation(self):
        pass
    
class NetworkSettingsApiRequest(NetworkSettingsApiABC, VapixRequestBuilderWithVersion):
    
    def addVlan(self, masterDeviceName, VlanId):
        params = {
            "masterDeviceName": masterDeviceName,
            "VlanId": VlanId
        }
        return self._create_request_with_params(self.addVlan.__name__, params)
    
    def getNetworkInfo(self):
        return self._create_no_params_request(self.getNetworkInfo.__name__)
    
    def removeVlan(self, VlanName):
        return self._create_request_with_params(self.removeVlan.__name__, {"VlanName": VlanName})
    
    def setHostnameConfiguration(self, useDhcpHostname, staticHostname):
        params = {}
        if useDhcpHostname is not None:
            params["useDhcpHostname"] = useDhcpHostname
        if staticHostname is not None:
            params["staticHostname"] = staticHostname
        return self._create_request_with_params(self.setHostnameConfiguration.__name__, params)
    
    def setWlanConfiguration(self, countryCode):
        return self._create_request_with_params(self.setWlanConfiguration.__name__, {"countryCode": countryCode})
    
    def setIPv4AddressConfiguration(self, configuration):
        if isinstance(configuration, IPv4AddressConfiguration):
            configuration = self._remove_none_values(asdict(configuration))
        return self._create_request_with_params(self.setIPv4AddressConfiguration.__name__, configuration)
    
    def setGlobalProxyConfiguration(self, httpProxy, httpsProxy):
        params = {
            "httpProxy": httpProxy,
            "httpsProxy": httpsProxy
        }
        return self._create_request_with_params(self.setGlobalProxyConfiguration.__name__, params)

    def setResolverConfiguration(self, useDhcpResolverInfo, staticNameServers, staticSearchDomains, staticDomainName):
        params = {
            "useDhcpResolverInfo": useDhcpResolverInfo,
            "staticNameServers": staticNameServers,
            "staticSearchDomains": staticSearchDomains,
            "staticDomainName": staticDomainName
        }
        params = self._remove_none_values(params)
        return self._create_request_with_params(self.setResolverConfiguration.__name__, params)
    
    def setWired8021XConfiguration(self, deviceName, enabled, mode, identity, eapolVersion):
        params = {
            "deviceName": deviceName,
            "enabled": enabled,
            "mode": mode,
            "identity": identity,
            "eapolVersion": eapolVersion,
        }
        params = self._remove_none_values(params)
        return self._create_request_with_params(self.setWired8021XConfiguration.__name__, params)
    
    def scanWLANNetworks(self, deviceName, refresh):
        params = {
            "deviceName": deviceName,
            "refresh": refresh,
        }
        params = self._remove_none_values(params)
        return self._create_request_with_params(self.scanWLANNetworks.__name__, params)

    def setWLANStationConfiguration(self, configuration):
        if isinstance(configuration, WLANStationConfiguration):
            configuration = self._remove_none_values(asdict(configuration))
        return self._create_request_with_params(self.setIPv4AddressConfiguration.__name__, configuration)

    def testWLANStationSettings(self, deviceName, timeout):
        params = {
            "deviceName": deviceName,
            "timeout": timeout,
        }
        params = self._remove_none_values(params)
        return self._create_request_with_params(self.testWLANStationSettings.__name__, params)
    
    def setIPv6AddressConfiguration(self, configuration):
        if isinstance(configuration, IPv6AddressConfiguration):
            configuration = self._remove_none_values(asdict(configuration))
        return self._create_request_with_params(self.setIPv6AddressConfiguration.__name__, configuration)

    def wlanSwitchAPToStation(self):
        return self._create_no_params_request(self.wlanSwitchAPToStation.__name__)