from requests import Request, Response
from .types import RequestParamType, MethodType, ApiPathType

class RequestAxisVapix:
    """
    A class to interact with the Axis VAPIX API.
    Axis API documentation: https://developer.axis.com/vapix/
    """
    def __init__(self, host: str, port: int, api_version: str | None = None, context: str | None = None):
        self._api_verion = api_version
        self._context = context
        self._host = host
        self._port = port
        self._api_path_type: ApiPathType = ApiPathType.NONE
    
    def _get_basic_request_body(self):
        """
        Constructs a basic request body dictionary with API version and context if they are set.

        Returns:
            dict: A dictionary containing the API version and context if they are not None.
        """
        request_body = {}
        if self._api_verion != None: request_body[RequestParamType.API_VERSION.value] = self._api_verion
        if self._context != None: request_body[RequestParamType.CONTEXT.value] = self._context 
        return request_body

    def _get_supported_versions(self):
        """
        Constructs a request to get the supported versions of the API.

        Returns:
            Request: A POST request object to get the supported versions.
        
        Raises:
            ValueError: If the API path type is not set.
        """
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_SUPPORTED_VERSIONS.value
        # Check if api_path_type is None and raise an exception
        if self._api_path_type.value == None: 
            raise ValueError("API path type is not set")
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)
    
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

class RequestNetworkSettings(RequestAxisVapix): # TODO: Implement this class
    """
    Property: Properties.API.HTTP.Version=3
    Firmware: 5.00 and later.
    """
    def __init__(self, host: str, port: int, api_version: str, context=None):
        super().__init__(host, port, api_version, context)
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

class RequestVideoStreaming(RequestAxisVapix): # TODO: Implement this class
    """
    Property: Properties.API.HTTP.Version=3
    Firmware: 5.00 and later.
    """
    def __init__(self, host: str, port: int, api_version: str = None, context = None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")
        
class ResponseAxisCgi:
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
    
    def is_textplain_response_with_error(self):
        # Check for successful HTTP status code
        if self._response.status_code != 200:
            raise ValueError(f"Unexpected response status code: {self._response.status_code}")
        # Safely attempt to parse text
        try:
            text_data = self._response.text
        except ValueError:
            raise ValueError("Response body is not valid text")
        # Check if the error key exists and is properly structured
        return "Error".lower() in text_data.lower()


 