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
keyargs = {defaults.RequestUrlParamType.GROUP.value:'Properties.EmbeddedDevelopment.Version'}
response = axis.vapix.methods.param_handle(axis_request, defaults.ActionType.LIST, **keyargs)
print(response.text.rstrip('\n'))
