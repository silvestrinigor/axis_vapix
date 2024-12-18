import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import axis.vapix.handlers
import axis.vapix.methods
import axis.vapix.defaults
import axis.vapix.request
from tests import HOST, PORT, PASSWORD, USERNAME
import axis
from axis.vapix import defaults
import axis.vapix.utils
axis_request = axis.vapix.request.AxisDefaultRequestMaker(host= HOST, port= PORT, username= USERNAME, password= PASSWORD)
response = axis.vapix.methods.get_network_info(axis_request)
is_response_with_error = axis.vapix.handlers.is_response_with_error(response=response)
if is_response_with_error:
    print("response contain a error")
print(response.json())
