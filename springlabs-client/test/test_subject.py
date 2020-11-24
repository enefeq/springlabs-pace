# coding: utf-8

"""
    Spring PACE Product Client Software Server

    This section describes the API calls and their usage to interact with the Spring Network.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@springlabs.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import springlabs
from springlabs.models.subject import Subject  # noqa: E501
from springlabs.rest import ApiException

class TestSubject(unittest.TestCase):
    """Subject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Subject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = springlabs.models.subject.Subject()  # noqa: E501
        if include_optional :
            return Subject(
                address = springlabs.models.address.Address(
                    address_city = '0', 
                    address_line1 = '0', 
                    address_line2 = '0', 
                    address_state = '0', 
                    address_zip = '0', ), 
                parcel = springlabs.models.parcel.Parcel(
                    apn = '0', 
                    fips_county_code = '0', )
            )
        else :
            return Subject(
        )

    def testSubject(self):
        """Test Subject"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
