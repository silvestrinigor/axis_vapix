import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import axis.vapix.methods
import axis.vapix.defaults
import axis.vapix.request
from tests import HOST, PORT, PASSWORD, USERNAME
import axis

axis_request = axis.vapix.request.AxisRequestMaker(host= HOST, port= PORT, username= USERNAME, password= PASSWORD)
#response = axis.vapix.methods.get_all_properties(axis_request)
#response = axis.vapix.methods.get_properties(axis_request, [axis.defaults.DeviceProperty.ARCHTECTURE])
#response = axis.vapix.methods.get_supported_versions(axis_request, axis.defaults.AxisApi.AXIS_CGI_BASIC_DEVICE_INFO)
#response = axis.vapix.methods.get_all_unrestricted_properties(axis_request)
response = axis.vapix.methods.get_api_list(axis_request)
#response = axis.vapix.methods.add_dynamic_overlay_text(axis_request, 1, "teste", axis.defaults.OverlayPosition.BOTTOM_RIGHT, text_color= axis.defaults.OverlayTextColor.RED)
#response = axis.vapix.methods.add_dynamic_overlay_image(axis_request, 1, "axis(128x44).ovl")
#response = axis.vapix.methods.list_overlays(axis_request)
#response = axis.vapix.methods.set_dynamic_overlay_text(axis_request, 1, back_ground_color= axis.defaults.OverlayColor.RED)
#response = axis.vapix.methods.set_dynamic_overlay_image(axis_request, 1, camera= 2)
#response = axis.vapix.methods.get_dynamic_overlay_capabilities(axis_request)
#response = axis.vapix.methods.get_capture_modes(axis_request)
#response = axis.vapix.methods.set_capture_mode(axis_request)
#response = axis.vapix.methods.get_clear_view_service_info(axis_request)

print(response.text)
