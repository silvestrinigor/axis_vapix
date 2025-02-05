class AxisVapixException(Exception): 
    """Base exception for Axis Vapix errors."""
    def __init__(self, message: str = "An Axis Vapix error occurred"):
        super().__init__(message)

class AxisVapixHTTPException(AxisVapixException):
    """Base exception for Axis Vapix HTTP errors."""
    def __init__(self, status_code: int, message: str):
        super().__init__(f"Request failed with status code {status_code} and message: {message}")

class AxisVapixVersionNotSupportedException(AxisVapixException): 
    def __init__(self):
        super().__init__("The specified version is not supported")

class AxisVapixClientError(AxisVapixHTTPException): ...

class AxisVapixServerError(AxisVapixHTTPException): ...

class AxisVapixInternalErrorException(AxisVapixException): 
    def __init__(self):
        super().__init__("Internal error")

class AxisVapixInvalidRequestException(AxisVapixException): 
    def __init__(self):
        super().__init__("Invalid request")

class AxisVapixRequestBodyTooLargeException(AxisVapixException): 
    def __init__(self):
        super().__init__("Request body too large")

class AxisVapixInvalidJsonDataException(AxisVapixException): 
    def __init__(self):
        super().__init__("Invalid JSON data")

class AxisVapixMethodDoesNotExistException(AxisVapixException): 
    def __init__(self):
        super().__init__("Method does not exist")

class AxisVapixAuthorizationFailedException(AxisVapixException): 
    def __init__(self):
        super().__init__("Authorization failed")

class AxisVapixMissingParameterException(AxisVapixException): 
    def __init__(self):
        super().__init__("Missing parameter(s)")

class AxisVapixInvalidParameterException(AxisVapixException): 
    def __init__(self):
        super().__init__("Invalid parameter(s)")

class AxisVapixMessageCouldNotBeParsedException(AxisVapixException):
    def __init__(self):
        super().__init__("Message could not be parsed or contains unknown parameters or values")

class AxisVapixUnknownMethodException(AxisVapixException):
    def __init__(self):
        super().__init__("Unknown method in request")

class AxisVapixApiVersionNotCompatibleException(AxisVapixException):
    def __init__(self):
        super().__init__("API version not compatible")

class AxisVapixSystemBusyException(AxisVapixException):
    def __init__(self):
        super().__init__("System is busy with another firmware management request")

class AxisVapixUnexpectedInternalErrorException(AxisVapixException):
    def __init__(self):
        super().__init__("Unexpected internal error")

code_exceptions: dict[int, type[AxisVapixException]] = {
    2000: AxisVapixInvalidRequestException,
    4002: AxisVapixAuthorizationFailedException,
    2001: AxisVapixRequestBodyTooLargeException,
    1000: AxisVapixInternalErrorException,
    4000: AxisVapixMethodDoesNotExistException,
    4001: AxisVapixVersionNotSupportedException,
    4003: AxisVapixMissingParameterException,
    4004: AxisVapixInvalidParameterException,
    3000: AxisVapixInvalidJsonDataException,
    400: AxisVapixMessageCouldNotBeParsedException,
    405: AxisVapixUnknownMethodException,
    417: AxisVapixApiVersionNotCompatibleException,
    423: AxisVapixSystemBusyException,
    500: AxisVapixUnexpectedInternalErrorException,
}