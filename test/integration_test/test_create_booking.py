'''
Author : Purtika
Objective :  Create and Verify by POST Request
TC#1 - Verify the Status Code, Headers
TC#2 - Verify the Body -> Booking ID
TC#3 - Verify the JSON Schema is Valid

Assertion
Expected Result == Actual Result

'''

# Payload
# Base URL
# Verify

from src.constants.apiconstants import base_url, url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.payload_manger import payload_create_booking
from src.helpers.utils import common_headers
from src.helpers.common_verifications import *
import pytest
class TestIntegration(object):

    @pytest.fixture(scope="module")
    def setup(self):
        print("Before")
    def test_create_booking_tc1(self):
        headers = {"Content-Type": "application/json",}
        response = post_request( url_create_booking(),auth= None, headers=common_headers(), payload= payload_create_booking(), in_json= False)
        print(response.json())
        verify_http_code(response, 200)
        #booking_id = response.json()["booking_id"]
       # verify_key_for_not_null_greater_than_zero(response.json()["booking_id"])
     #def test_create_booking_tc2(self):
     #   assert True == False

    #def test_create_booking_tc3(self):
     #   assert True == True

    @pytest.fixture(scope="module")
    def tear_down(self):
        print("End")