import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import axis.vapix.methods
import axis.vapix.defaults
import axis.vapix.request
from tests import HOST, PORT, PASSWORD, USERNAME
import axis

axis_request = axis.vapix.request.AxisDefaultRequestMaker(host= HOST, port= PORT, username= USERNAME, password= PASSWORD)
#response = axis.vapix.methods.get_all_properties(axis_request)
#response = axis.vapix.methods.get_properties(axis_request, [axis.defaults.DeviceProperty.ARCHTECTURE])
response = axis.vapix.methods.get_supported_versions(axis_request, axis.vapix.defaults.ApiPathType.AXIS_CGI_TIME)
#response = axis.vapix.methods.get_all_unrestricted_properties(axis_request)
#response = axis.vapix.methods.get_api_list(axis_request)
#response = axis.vapix.methods.add_dynamic_overlay_text(axis_request, 1, "teste", axis.defaults.OverlayPosition.BOTTOM_RIGHT, text_color= axis.defaults.OverlayTextColor.RED)
#response = axis.vapix.methods.add_dynamic_overlay_image(axis_request, 1, "/etc/overlays/axis(128x44).ovl")
#response = axis.vapix.methods.list_overlays(axis_request)
#text_overlay = axis.vapix.defaults.TextOverlay()
#text_overlay.text = "teste"
#text_overlay.identity = 4
#response = axis.vapix.methods.set_dynamic_overlay_text(axis_request, text_overlay)
#response = axis.vapix.methods.set_dynamic_overlay_image(axis_request, 1, camera= 2)
#response = axis.vapix.methods.get_dynamic_overlay_capabilities(axis_request)
#response = axis.vapix.methods.get_capture_modes(axis_request)
#response = axis.vapix.methods.set_capture_mode(axis_request)
#response = axis.vapix.methods.get_clear_view_service_info(axis_request)
#response = axis.vapix.methods.get_ntp_info(axis_request)
ntp_configuraton = axis.vapix.defaults.NTPClientConfiguration()
ntp_configuraton.enable = True
ntp_configuraton.servers_source = axis.vapix.defaults.ServersSourceType.STATIC
#response = axis.vapix.methods.set_ntp_client_configuration(axis_request, ntp_configuraton)
print(response.text)
