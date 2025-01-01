import sys
import os
import requests
import requests.auth

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import axis.vapix
from tests_axis import HOST, PORT, PASSWORD, USERNAME
import axis
import axis.vapix.apis
import axis.vapix.types

import axis.vapix.defaults
import axis.vapix.devices
request = axis.vapix.apis.RequestParameterManagement(HOST, PORT).get_request(axis.vapix.types.ActionType.LIST)
request.auth = requests.auth.HTTPDigestAuth(USERNAME, PASSWORD)


axis.vapix.devices.Device(HOST, PORT, USERNAME, PASSWORD).get_device_properties()