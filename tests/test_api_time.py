import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from axis.vapix.apis import time_api
from axis.vapix.utils import serialize_datetime, is_timezone_aware
import unittest
import datetime
from datetime import datetime
from requests import Request
import pytz


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

if __name__ == '__main__':
    unittest.main()

