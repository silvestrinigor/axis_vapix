import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import axis.vapix.devices
import axis.vapix.axis_methods
import axis.vapix.types
import axis.vapix.request
import time
from tests import HOST, PORT, PASSWORD, USERNAME
import axis

device = axis.vapix.devices.Device(host= HOST, port= PORT, username= USERNAME, password= PASSWORD)
print(device.date_time)
print(device.version)
print(device.serial_number)
print(device.time_zone)
print(device.is_time_dst_enable)

