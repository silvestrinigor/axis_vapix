"""
https://developer.axis.com/vapix/network-video/firmware-management-api
"""
import json
from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, FactoryDefaultModeType, AutoCommitType, AutoRollbackType, MethodType, RequestParamType, ParamType
from ..params import ApiVersion, FirmwareVersion
from .. import request

FIRMWARE_MANAGEMENT_API_LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(7, 40, 0)
FIRMWARE_MANAGEMENT_API_DISCOVERY_API_ID = "fwmgr"

class RequestFirmwareManagementApi(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_FIRMWARE_MANAGEMENT
    
    def status(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.STATUS.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json=request_body)

    def upgrade(self, file_path: str, factory_default: FactoryDefaultModeType = FactoryDefaultModeType.NONE, auto_commit: AutoCommitType = AutoCommitType.NONE, auto_rollback: AutoRollbackType = AutoRollbackType.NONE):
        # Create the JSON data with the dynamic API version
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.UPGRADE.value
        params = {}
        if factory_default != FactoryDefaultModeType.NONE:
            params[ParamType.FACTORY_DEFAULT_MODE.value] = factory_default.value
        if auto_commit != AutoCommitType.NONE:
            params[ParamType.AUTO_COMMIT.value] = auto_commit.value
        if auto_rollback != AutoRollbackType.NONE:
            params[ParamType.AUTO_ROLLBACK.value] = auto_rollback.value
        if params != {}:
            request_body[RequestParamType.PARAMS.value] = params

        json_data = json.dumps(request_body).encode('utf-8')  # Encode JSON to bytes

        with open(file_path, 'rb') as firmware_file: # Using with open in Python is a best practice for handling files because it ensures that the file is properly closed
            firmware = firmware_file.read() 

        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", files=((None, json_data),(None, firmware)))
        
    def commit(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.COMMIT.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json=request_body)

    def roolback(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.ROLLBACK.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json=request_body)

    def purge(self): 
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.PURGE.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json=request_body)

    def factory_default(self, factory_default: FactoryDefaultModeType = FactoryDefaultModeType.NONE):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.FACTORY_DEFAULT.value
        params = {}
        if factory_default != FactoryDefaultModeType.NONE:
            params[ParamType.FACTORY_DEFAULT_MODE.value] = factory_default.value
        if params != {}:
            request_body[RequestParamType.PARAMS.value] = params
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json=request_body)

    def stop_auto(self):  
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.STOP_AUTO.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json=request_body)

    def reboot(self):  
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.REBOOT.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json=request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()

class FirmwareManagementApi(RequestFirmwareManagementApi):
    def __init__(self, host, port, api_version, context = None):
        super().__init__(host, port, api_version, context)
        
    def status(self, session: request.AxisVapixSession, auth):
        request = super().status()
        request.auth = auth
        self._send_request(request, session)
        
    def upgrade(self, session: request.AxisVapixSession, auth, file_path: str, factory_default = FactoryDefaultModeType.NONE, auto_commit = AutoCommitType.NONE, auto_rollback = AutoRollbackType.NONE):
        request = super().upgrade(file_path, factory_default, auto_commit, auto_rollback)
        request.auth = auth
        self._send_request(request, session)
        
    def commit(self, session: request.AxisVapixSession, auth):
        request = super().commit()
        request.auth = auth
        self._send_request(request, session)
        
    def roolback(self, session: request.AxisVapixSession, auth):
        request = super().roolback()
        request.auth = auth
        self._send_request(request, session)
        
    def purge(self, session: request.AxisVapixSession, auth):
        request = super().purge()
        request.auth = auth
        self._send_request(request, session)
        
    def factory_default(self, session: request.AxisVapixSession, auth, factory_default: FactoryDefaultModeType = FactoryDefaultModeType.NONE):
        request = super().factory_default(factory_default)
        request.auth = auth
        self._send_request(request, session)
        
    def stop_auto(self, session: request.AxisVapixSession, auth):
        request = super().stop_auto()
        request.auth = auth
        self._send_request(request, session)
        
    def reboot(self, session: request.AxisVapixSession, auth):
        request = super().reboot()
        request.auth = auth
        self._send_request(request, session)
        
    def get_supported_versions(self, session: request.AxisVapixSession, auth):
        request = super().get_supported_versions()
        request.auth = auth
        self._send_request(request, session)

    async def async_status(self, session: request.AxisVapixAsyncSession, auth):
        request = super().status()
        request.auth = auth
        await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)

    async def async_upgrade(self, session: request.AxisVapixAsyncSession, auth, file_path: str, factory_default = FactoryDefaultModeType.NONE, auto_commit = AutoCommitType.NONE, auto_rollback = AutoRollbackType.NONE):
        request = super().upgrade(file_path, factory_default, auto_commit, auto_rollback)
        request.auth = auth
        await session.post(request.url, data=request.data, files=request.files, headers=request.headers, auth=request.auth)

    async def async_commit(self, session: request.AxisVapixAsyncSession, auth):
        request = super().commit()
        request.auth = auth
        await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)

    async def async_roolback(self, session: request.AxisVapixAsyncSession, auth):
        request = super().roolback()
        request.auth = auth
        await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)

    async def async_purge(self, session: request.AxisVapixAsyncSession, auth):
        request = super().purge()
        request.auth = auth
        await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)

    async def async_factory_default(self, session: request.AxisVapixAsyncSession, auth, factory_default: FactoryDefaultModeType = FactoryDefaultModeType.NONE):
        request = super().factory_default(factory_default)
        request.auth = auth
        await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)

    async def async_stop_auto(self, session: request.AxisVapixAsyncSession, auth):
        request = super().stop_auto()
        request.auth = auth
        await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
    
    async def async_reboot(self, session: request.AxisVapixAsyncSession, auth):
        request = super().reboot()
        request.auth = auth
        await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
    
    async def async_get_supported_versions(self, session: request.AxisVapixAsyncSession, auth):
        request = super().get_supported_versions()
        request.auth = auth
        await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
    