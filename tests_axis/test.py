import sys
import os
import requests
import requests.auth
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import axis.vapix
from tests_axis import HOST, PORT, PASSWORD, USERNAME
import axis
import axis.vapix.apis
import axis.vapix.types
request = axis.vapix.apis.RequestParameterManagement(HOST, PORT).get_request(axis.vapix.types.ActionType.LIST)
request.auth = requests.auth.HTTPDigestAuth(USERNAME, PASSWORD)

requestp = request.prepare()
response = requests.Session().send(requestp)
with open('personal/test.xml', 'w') as f:
    f.write(response.text)