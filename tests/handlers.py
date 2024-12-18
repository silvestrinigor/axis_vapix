import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import axis.vapix.devices
import axis.vapix.methods
import axis.vapix.defaults
import axis.vapix.request
import axis.vapix.handlers
from tests import HOST, PORT, PASSWORD, USERNAME
import axis

axis_request = axis.vapix.request.AxisRequestMaker(host= HOST, port= PORT, username= USERNAME, password= PASSWORD)
#response = axis.vapix.methods.get_all_properties(axis_request)
#response = axis.vapix.methods.get_properties(axis_request, [axis.defaults.DeviceProperty.ARCHTECTURE])
#response = axis.vapix.methods.get_supported_versions(axis_request, axis.defaults.AxisApi.AXIS_CGI_BASIC_DEVICE_INFO)
#response = axis.vapix.methods.get_all_unrestricted_properties(axis_request)
#response = axis.vapix.methods.get_api_list(axis_request)
#response = axis.vapix.methods.add_dynamic_overlay_text(axis_request, 1, "teste", axis.defaults.OverlayPosition.BOTTOM_RIGHT, text_color= axis.defaults.OverlayTextColor.RED)
#response = axis.vapix.methods.add_dynamic_overlay_image(axis_request, 1, "axis(128x44).ovl")
response = axis.vapix.methods.list_overlays(axis_request)

content = axis.vapix.handlers.ListOverlaysResponseHandler(response).image_overlays
print(content)