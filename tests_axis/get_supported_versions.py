import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import axis.vapix.types
from tests_axis import HOST, PORT, PASSWORD, USERNAME
import axis.vapix
import axis.vapix.defaults
import axis.vapix.methods
import axis
import requests
device = axis.vapix.defaults.AxisDevice(HOST, PORT, USERNAME, PASSWORD)
request = axis.vapix.methods.get_supported_versions(device, axis.vapix.types.ApiPathType.AXIS_CGI_API_DISCOVERY)
rp = request.prepare()
response = requests.session().send(rp)

print(response.text)