import sys
import os

import requests.auth
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from tests_axis import HOST, PORT, PASSWORD, USERNAME
import axis.vapix
import axis.vapix.defaults
import axis.vapix.methods
import axis
import requests
import axis.vapix.network_video
import axis.vapix.types

net_vid = axis.vapix.network_video.BasicDeviceInformationRequest(HOST, PORT, "1.2")

request = net_vid.get_properties([axis.vapix.types.DevicePropertyType.ARCHITECTURE])
request.auth = requests.auth.HTTPDigestAuth(USERNAME, PASSWORD)
rp = request.prepare()

response = requests.Session().send(rp)



print(response.text)


request = net_vid.get_all_properties()
request.auth = requests.auth.HTTPDigestAuth(USERNAME, PASSWORD)
rp = request.prepare()

response = requests.Session().send(rp)



print(response.text)