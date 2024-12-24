import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import axis.vapix.utils
import axis.vapix.devices
import axis.vapix.axis_methods
import axis.vapix.types
import axis.vapix.request
import time
from datetime import datetime
import pytz
from tests import HOST, PORT, PASSWORD, USERNAME
import axis
current_time_naive = datetime.now()
# Use pytz to localize the naive datetime to a specific timezone
timezone = pytz.timezone(axis.vapix.types.TimeZoneType.AMERICA_SAO_PAULO.value)
current_time_aware = timezone.localize(current_time_naive)
print(axis.vapix.utils.serialize_datetime(current_time_aware))
device = axis.vapix.devices.Device(host= HOST, port= PORT, username= USERNAME, password= PASSWORD)
device.date_time = current_time_aware
device.time_zone = axis.vapix.types.TimeZoneType.AMERICA_SAO_PAULO