import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import axis.vapix.devices
import axis.vapix.methods
import axis.vapix.defaults
import axis.vapix.request
from tests import HOST, PORT, PASSWORD, USERNAME
import axis

device = axis.vapix.devices.Device(host= HOST, port= PORT, username= USERNAME, password= PASSWORD)
print(device.type)