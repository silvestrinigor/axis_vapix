from requests import Response
from aiohttp import ClientResponse
import re
from .exeptions import AxisVapixException, AxisVapixHTTPException, AxisVapixClientError, AxisVapixServerError, code_exceptions

class AxisVapixResponseHandler:
    def __init__(self, response: Response):
        self._response = response

    def handle_errors(self):
        status_code = self._response.status_code
        # Handle non-200 status codes
        if status_code != 200:
            if 400 <= status_code < 500:
                raise AxisVapixClientError(
                    status_code,
                    f"Client error for request {self._request.method} {self._request.url}: {self._response.text}"
                )
            elif 500 <= status_code < 600:
                raise AxisVapixServerError(
                    status_code,
                    f"Server error for request {self._request.method} {self._request.url}: {self._response.text}"
                )
            else:
                raise AxisVapixHTTPException(
                    status_code,
                    f"Unexpected error for request {self._request.method} {self._request.url}: {self._response.text}"
                )        
        content_type = self._response.headers.get("Content-Type", "")
        if "text/html" in content_type:
            self._handle_html_error()

        if "application/json" in content_type:
            self._handle_json_error()

        if not ("application/json" in content_type or "text/html" in content_type):
            raise AxisVapixException(f"Unsupported Content-Type: {content_type}")

    def is_response_success(self):
        try:
            self.handle_errors()
            return True
        except AxisVapixException:
            return False

    def _handle_html_error(self):
        match = re.search(r"Error:\s*(.+)", self._response.text)
        if match:
            error_message = match.group(1).strip()
            raise AxisVapixException(f"HTML Error: {error_message}")
        else:
            raise AxisVapixException("An unknown HTML error occurred.")
        
    def _handle_json_error(self):
        try:
            # Attempt to parse the JSON response
            self._response_json = self._response.json()

            # Check if the response contains an 'error' field
            error = self._response_json.get("error", None)

            # If 'error' is not found or is None, there's no error in the response
            if error is None:
                return  # No error in response, simply return

            # If there's an 'error', extract the code and message
            error_code = error.get("code", "Unknown")
            error_message = error.get("message", "No error message provided.")

            # Handle the error based on the error_code
            if error_code in code_exceptions:
                raise code_exceptions[error_code]()  # Raise the appropriate exception
            else:
                raise AxisVapixException(f"Unknown error code {error_code}: {error_message}")

        except ValueError:
            # Catch JSON parsing errors
            raise AxisVapixException("Invalid JSON response received.")

class AxisVapixAsyncResponseHandler:
    def __init__(self, response: ClientResponse):
        self._response = response

    # Make handle_errors async to properly await _handle_json_error and _handle_html_error
    async def handle_errors(self):
        status_code = self._response.status
        request = self._response  # Use request from the response object

        # Handle non-200 status codes
        if status_code != 200:
            error_message = f"Client error for request {request.method} {request.url}: {self._response.text}"
            if 400 <= status_code < 500:
                raise AxisVapixClientError(status_code, error_message)
            elif 500 <= status_code < 600:
                raise AxisVapixServerError(status_code, error_message)
            else:
                raise AxisVapixHTTPException(status_code, error_message)

        # Check content_type and handle accordingly
        content_type = self._response.content_type

        # Handle string content_type (the usual case)
        if isinstance(content_type, str):
            if "text/html" in content_type:
                # Async handling of HTML errors
                await self._handle_html_error()
            elif "application/json" in content_type:
                # Async handling of JSON errors
                await self._handle_json_error()

        # Handle dictionary content_type (if it contains MIME information as keys/values)
        elif isinstance(content_type, dict):
            if 'main' in content_type:
                if 'text/html' in content_type['main']:
                    # Handle HTML errors if found in dictionary
                    await self._handle_html_error()

                elif 'application/json' in content_type['main']:
                    # Handle JSON errors if found in dictionary
                    await self._handle_json_error()
        else:
            # If content_type is neither string nor dictionary, raise error
            raise AxisVapixException(f"Unsupported Content-Type structure: {content_type}")

    async def is_response_success(self):
        try:
            # Now awaiting handle_errors() because it's an async function
            await self.handle_errors()
            return True
        
        except AxisVapixException:
            return False

    async def _handle_html_error(self):
        response_text = await self._response.text()
        match = re.search(r"Error:\s*(.+)", response_text)
        if match:
            error_message = match.group(1).strip()
            raise AxisVapixException(f"HTML Error: {error_message}")
        else:
            raise AxisVapixException("An unknown HTML error occurred.")

    async def _handle_json_error(self):
        try:
            # Attempt to parse the JSON response
            response_json = await self._response.json()

            # Check if the response contains an 'error' field
            error = response_json.get("error", None)

            # If 'error' is not found or is None, there's no error in the response
            if error is None:
                return  # No error in response, simply return

            # If there's an 'error', extract the code and message
            error_code = error.get("code", "Unknown")
            error_message = error.get("message", "No error message provided.")

            # Handle the error based on the error_code
            if error_code in code_exceptions:
                raise code_exceptions[error_code]()  # Raise the appropriate exception
            else:
                raise AxisVapixException(f"Unknown error code {error_code}: {error_message}")

        except ValueError:
            # Catch JSON parsing errors
            raise AxisVapixException("Invalid JSON response received.")