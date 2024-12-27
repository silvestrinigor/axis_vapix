import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import axis.vapix.devices

import axis.vapix.defaults
import axis.vapix.handlers
import axis.vapix.methods
import axis.vapix.types
import axis.vapix.request
from tests import HOST, PORT, PASSWORD, USERNAME
import axis
from axis.vapix import types
import axis.vapix.utils
axis_request = axis.vapix.defaults.AxisDevice(host= HOST, port= PORT, username= USERNAME, password= PASSWORD)
keyargs = {types.RequestUrlParamType.GROUP.value:'root.Properties.System.SerialNumber'}
request = axis.vapix.methods.param_handle(axis_request, types.ActionType.LIST, **keyargs)
response = axis.vapix.request.RequestMaker().send_request(request)

print(response.text.rstrip('\n'))

device = axis.vapix.devices.DeviceManager(host= HOST, port= PORT, username= USERNAME, password= PASSWORD)
print(device.serial_number)