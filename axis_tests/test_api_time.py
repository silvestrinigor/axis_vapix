import sys
import os

import requests.auth
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from axis.vapix.apis import time_api
from axis.vapix.utils import serialize_datetime, is_timezone_aware
import unittest
import datetime
from datetime import datetime
from requests import Request
import requests
import pytz
from axis_tests import HOST, PORT, USERNAME, PASSWORD
from axis.vapix import request, handlers

class TestRequestTimeApi(unittest.TestCase):

    def test_set_date_time_with_timezone_aware(self):
        """
        set_date_time should raise ValueError if the datetime object is not timezone-aware
        """
        date_time = datetime.now()
        date_time_aware = date_time.replace(tzinfo=pytz.utc)
        
        time_request = time_api.RequestTimeApi("host", 80, time_api.ApiVersion(1, 0))
        
        with self.assertRaises(ValueError):
            time_request.set_date_time(date_time)

        self.assertIsInstance(time_request.set_date_time(date_time_aware), Request)

class TestSerializeDateTime(unittest.TestCase):

    def test_serialize_datetime(self):
        """
        serialize_datetime should return a string representation of the datetime object
        the date format should be: "YYYY-MM-DDTHH:MM:SSZ"
        """
        date_time = datetime.now().replace(tzinfo=pytz.utc)
        serialized_date_time = serialize_datetime(date_time)
        self.assertIsInstance(serialized_date_time, str)
        self.assertEqual(serialized_date_time[-1], "Z")
        self.assertRegex(serialized_date_time, r"\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")

    def test_is_timezone_aware(self):
        """
        is_timezone_aware should return True if the datetime object is timezone-aware
        """
        date_time = datetime.now().replace(tzinfo=pytz.utc)
        self.assertTrue(is_timezone_aware(date_time))

        date_time = datetime.now()
        self.assertFalse(is_timezone_aware(date_time))

class TestSendTimeApiResponseHander(unittest.TestCase):
    def setUp(self):
        api_request = time_api.RequestTimeApi(HOST, PORT, time_api.ApiVersion(1,0))
        request1 = api_request.get_all()
        request1.auth = requests.auth.HTTPDigestAuth(USERNAME, PASSWORD)
        request2 = api_request.get_date_time_info()
        request2.auth = requests.auth.HTTPDigestAuth(USERNAME, PASSWORD)
        request3 = api_request.get_suported_versions()
        request3.auth = requests.auth.HTTPDigestAuth(USERNAME, PASSWORD)

        with request.AxisVapixSession() as session:
            self.response1 = session.send(request1.prepare())
            self.response2 = session.send(request2.prepare())
            self.response3 = session.send(request3.prepare())

    def test_check_response(self):
        self.assertTrue(handlers.AxisVapixResponseHandler(self.response1, None).is_response_success())
        self.assertTrue(handlers.AxisVapixResponseHandler(self.response2, None).is_response_success())
        self.assertTrue(handlers.AxisVapixResponseHandler(self.response3, None).is_response_success())
        
            
if __name__ == '__main__':
    unittest.main()

