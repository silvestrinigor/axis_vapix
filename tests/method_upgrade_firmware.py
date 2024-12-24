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
file_obj = open("/home/igor/sigs/axis_vapix/M3115-LVE_10_12_262.bin", "rb")
response = axis.vapix.axis_methods.upgrade_firmware_system_settings(axis_request, "M3115-LVE_10_12_262.bin", file_obj, types.FirmwareUpgradeType.NORMAL)
print(response.text)
