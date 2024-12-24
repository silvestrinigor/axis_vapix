import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import axis.vapix.handlers
import axis.vapix.axis_methods
import axis.vapix.types
import axis.vapix.request
from tests import HOST, PORT, PASSWORD, USERNAME
import axis
from axis.vapix import types
import axis.vapix.utils
axis_request = axis.vapix.request.AxisDefaultAsyncRequestMaker(host= HOST, port= PORT, username= USERNAME, password= PASSWORD)
x = axis.vapix.axis_methods.get_network_info(axis_request)
response = axis_request.send_async_requests([x])
print(response[0].text)
