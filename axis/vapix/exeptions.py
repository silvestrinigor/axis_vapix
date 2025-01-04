class AxisVapixException(Exception): 
    """Base exception for Axis Vapix errors."""
    def __init__(self, message: str = "An Axis Vapix error occurred"):
        super().__init__(message)

class AxisVapixVersionNotSupportedException(AxisVapixException): 
    def __init__(self):
        super().__init__("The specified version is not supported")

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

code_exeptions: dict[int, type[AxisVapixException]] = {
    2000: AxisVapixInvalidRequestException,
    4002: AxisVapixAuthorizationFailedException,
    2001: AxisVapixRequestBodyTooLargeException,
    1000: AxisVapixInternalErrorException,
    4000: AxisVapixMethodDoesNotExistException,
    4001: AxisVapixVersionNotSupportedException,
    4003: AxisVapixMissingParameterException,
    4004: AxisVapixInvalidParameterException,
    3000: AxisVapixInvalidJsonDataException,
}
