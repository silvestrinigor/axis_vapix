import sys
import os
import requests
import requests.auth

import axis.vapix.firmware_management_api
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import axis.vapix
from tests_axis import HOST, PORT, PASSWORD, USERNAME
import axis
import axis.vapix.apis
import axis.vapix.types
print(HOST)
print(PORT)

firmware_file_path = "/home/igor/sigs/axis_vapix/firmwares/M3115-LVE_10_12_262.bin"
api = axis.vapix.apis.RequestFirmwareManagementApi(HOST, PORT, "1.4", "upgrade firmware")
request = api.upgrade(firmware_file_path)
request.auth = requests.auth.HTTPDigestAuth(USERNAME, PASSWORD)
requestp = request.prepare()
response = requests.Session().send(requestp)
print(response.text)
