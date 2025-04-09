class VapixException(Exception): 
    """Base exception for Axis Vapix errors."""
    def __init__(self, message: str = "An Axis Vapix error occurred"):
        super().__init__(message)

class AxisVapixHTTPException(VapixException):
    """Base exception for Axis Vapix HTTP errors."""
    def __init__(self, status_code: int, message: str):
        super().__init__(f"Request failed with status code {status_code} and message: {message}")

class VapixVersionNotSupportedException(VapixException): 
    def __init__(self):
        super().__init__("The specified version is not supported")

class AxisVapixClientError(AxisVapixHTTPException): ...

class AxisVapixServerError(AxisVapixHTTPException): ...

class VapixInternalErrorException(VapixException): 
    def __init__(self):
        super().__init__("Internal error")

class VapixInvalidRequestException(VapixException): 
    def __init__(self):
        super().__init__("Invalid request")

class VapixRequestBodyTooLargeException(VapixException): 
    def __init__(self):
        super().__init__("Request body too large")

class VapixInvalidJsonDataException(VapixException): 
    def __init__(self):
        super().__init__("Invalid JSON data")

class VapixMethodDoesNotExistException(VapixException): 
    def __init__(self):
        super().__init__("Method does not exist")

class VapixAuthorizationFailedException(VapixException): 
    def __init__(self):
        super().__init__("Authorization failed")

class VapixMissingParameterException(VapixException): 
    def __init__(self):
        super().__init__("Missing parameter(s)")

class VapixInvalidParameterException(VapixException): 
    def __init__(self):
        super().__init__("Invalid parameter(s)")

class VapixMessageCouldNotBeParsedException(VapixException):
    def __init__(self):
        super().__init__("Message could not be parsed or contains unknown parameters or values")

class VapixUnknownMethodException(VapixException):
    def __init__(self):
        super().__init__("Unknown method in request")

class VapixApiVersionNotCompatibleException(VapixException):
    def __init__(self):
        super().__init__("API version not compatible")

class VapixSystemBusyException(VapixException):
    def __init__(self):
        super().__init__("System is busy with another firmware management request")

class VapixUnexpectedInternalErrorException(VapixException):
    def __init__(self):
        super().__init__("Unexpected internal error")

code_exception: dict[int, type[VapixException]] = {
    2000: VapixInvalidRequestException,
    4002: VapixAuthorizationFailedException,
    2001: VapixRequestBodyTooLargeException,
    1000: VapixInternalErrorException,
    4000: VapixMethodDoesNotExistException,
    4001: VapixVersionNotSupportedException,
    4003: VapixMissingParameterException,
    4004: VapixInvalidParameterException,
    3000: VapixInvalidJsonDataException,
    400: VapixMessageCouldNotBeParsedException,
    405: VapixUnknownMethodException,
    417: VapixApiVersionNotCompatibleException,
    423: VapixSystemBusyException,
    500: VapixUnexpectedInternalErrorException,
}