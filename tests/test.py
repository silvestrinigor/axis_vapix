import sys
import os
import requests
import requests.auth
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import axis.vapix
import axis.vapix.apis.time_api
import axis.vapix.utils
from tests import HOST, PORT, PASSWORD, USERNAME


