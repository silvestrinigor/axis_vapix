import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from axis.vapix.params import ApiVersion, FirmwareVersion
import unittest

class TestApiVersion(unittest.TestCase):

    def test_string_api_version_from_class(self):
        """
        the ApiVersion class should return a string representation of the version
        example: ApiVersion(1, 0) should return "1.0"
        """
        api_version = ApiVersion(1, 0)
        self.assertEqual(str(api_version), "1.0")

class TestFirmwareVersion(unittest.TestCase):

    def test_string_firmware_version_from_class(self):
        """
        the FirmwareVersion class should return a string representation of the version
        example: FirmwareVersion(1, 0, 0) should return "1.0.0"
        """
        firmware_version = FirmwareVersion(1, 0, 0)
        self.assertEqual(str(firmware_version), "1.0.0")

if __name__ == '__main__':
    unittest.main()

