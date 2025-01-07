from requests import Request, Response
import re
from .exeptions import AxisVapixException, AxisVapixHTTPException, AxisVapixClientError, AxisVapixServerError, code_exceptions

class AxisVapixResponseHandler:
    def __init__(self, response: Response, request: Request):
        self._response = response
        self._request = request

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
