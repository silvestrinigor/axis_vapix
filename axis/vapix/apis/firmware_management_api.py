"""
https://developer.axis.com/vapix/network-video/firmware-management-api
"""

from requests import Request
import json
from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, FactoryDefaultModeType, AutoCommitType, AutoRollbackType, MethodType, RequestParamType, ParamType
from ..params import ApiVersion

class RequestFirmwareManagementApi(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_FIRMWARE_MANAGEMENT
    
    def status(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.STATUS.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json=request_body)

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

        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", files=((None, json_data),(None, firmware)))
        
    def commit(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.COMMIT.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json=request_body)

    def roolback(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.ROLLBACK.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json=request_body)

    def purge(self): 
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.PURGE.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json=request_body)

    def factory_default(self, factory_default: FactoryDefaultModeType = FactoryDefaultModeType.NONE):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.FACTORY_DEFAULT.value
        params = {}
        if factory_default != FactoryDefaultModeType.NONE:
            params[ParamType.FACTORY_DEFAULT_MODE.value] = factory_default.value
        if params != {}:
            request_body[RequestParamType.PARAMS.value] = params
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json=request_body)

    def stop_auto(self):  
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.STOP_AUTO.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json=request_body)

    def reboot(self):  
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.REBOOT.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json=request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()
