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
axis_request = axis.vapix.request.AxisDefaultRequestMaker(host= HOST, port= PORT, username= USERNAME, password= PASSWORD)
keyargs = {types.RequestUrlParamType.GROUP.value:'Properties.EmbeddedDevelopment.Version'}
response = axis.vapix.axis_methods.param_handle(axis_request, types.ActionType.LIST, **keyargs)
print(response.text.rstrip('\n'))
