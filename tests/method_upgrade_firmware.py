import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
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
file_obj = open("/home/igor/sigs/axis_vapix/firmwares/M3115-LVE_10_12_262.bin", "rb")
"""request = axis.vapix.axis_methods.upgrade_firmware_system_settings(axis_request, "M3115-LVE_10_12_262.bin", file_obj, types.FirmwareUpgradeType.NORMAL)
print(request.get_kwargs())
response = axis.vapix.request.RequestMaker().send_request(request)
print(response.text)

request = request = axis.vapix.axis_methods.set_firmware_reboot(axis_request, axis.vapix.defaults.ApiVersion(1,1))
response = axis.vapix.request.RequestMaker().send_request(request)
print(response.text)"""
request= axis.vapix.methods.get_all_properties(axis_request, axis.vapix.defaults.ApiVersion(1,0), context="tese")
response = axis.vapix.request.RequestMaker().send_request(request)
print(response.text)

request = axis.vapix.methods.upgrade_firmware(axis_request, file_obj, axis.vapix.defaults.ApiVersion(1,0), context="tese")
print(request.get_kwargs())
response = axis.vapix.request.RequestMaker().send_request(request)
print(response.text)


'''
import requests
import json
from requests.auth import HTTPDigestAuth

# Define the URL
url = F'http://{HOST}:8000/axis-cgi/firmwaremanagement.cgi'

# Prepare the JSON payload
data = {
    "apiVersion": "1.0",
    "context": "abc",
    "method": "upgrade"
}

# Path to the firmware file
firmware_file_path = '/home/igor/sigs/axis_vapix/firmwares/M3115-LVE_10_12_262.bin'

# Open the firmware file in binary mode
with open(firmware_file_path, 'rb') as firmware_file:
    # Prepare the multipart/form-data payload
    files = {
        'file': ('firmware_file.bin', firmware_file, 'application/octet-stream')
    }
    
    # Prepare the data (JSON payload)
    json_payload = json.dumps(data)

    # Digest Authentication credentials
    username = USERNAME
    password = PASSWORD
    
    # Send the POST request with Digest Authentication
    response = requests.post(
        url,
        data={'data': json_payload},  # Include the JSON data in the form-data body
        files=files,                   # Include the firmware file in the form-data body
        auth=HTTPDigestAuth(username, password)  # Digest Authentication
    )

# Print the response
print(f'Status Code: {response.status_code}')
print(f'Response Text: {response.text}')
'''