import unittest
import requests
import pyapod
import ssl
import urllib3
import datetime
import sys

class PyApodResponseTest(unittest.TestCase):
    def setUp(self):
        try:
            self.resp = pyapod.Apod()
        except Exception as networkerror:
            print("setUp method failed to execute :", networkerror)
            sys.exit(1)cd ..
    
    def test_date(self):
        self.assertTrue(type(self.resp.date) is str)
        self.assertTrue(type(self.resp.api_key) is str)

if __name__ == '__main__':
    unittest.main()