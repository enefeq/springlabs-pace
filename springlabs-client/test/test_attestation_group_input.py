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
from springlabs.models.attestation_group_input import AttestationGroupInput  # noqa: E501
from springlabs.rest import ApiException

class TestAttestationGroupInput(unittest.TestCase):
    """AttestationGroupInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AttestationGroupInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = springlabs.models.attestation_group_input.AttestationGroupInput()  # noqa: E501
        if include_optional :
            return AttestationGroupInput(
                lien_status_data = springlabs.models.lien_status_data.LienStatusData(
                    canceled = springlabs.models.status_canceled.StatusCanceled(
                        canceled = True, 
                        timestamp = '2019-01-01T01:01:01+00:00', ), 
                    funded = springlabs.models.status_data.StatusData(
                        amount = '0', 
                        timestamp = '2019-01-01T01:01:01+00:00', ), 
                    notice_to_proceed = springlabs.models.status_data.StatusData(
                        amount = '0', 
                        timestamp = '2019-01-01T01:01:01+00:00', ), 
                    signed_assessment_contract = springlabs.models.status_data.StatusData(
                        amount = '0', 
                        timestamp = '2019-01-01T01:01:01+00:00', ), ), 
                subject = springlabs.models.subject.Subject(
                    address = springlabs.models.address.Address(
                        address_city = '0', 
                        address_line1 = '0', 
                        address_line2 = '0', 
                        address_state = '0', 
                        address_zip = '0', ), 
                    parcel = springlabs.models.parcel.Parcel(
                        apn = '0', 
                        fips_county_code = '0', ), )
            )
        else :
            return AttestationGroupInput(
                lien_status_data = springlabs.models.lien_status_data.LienStatusData(
                    canceled = springlabs.models.status_canceled.StatusCanceled(
                        canceled = True, 
                        timestamp = '2019-01-01T01:01:01+00:00', ), 
                    funded = springlabs.models.status_data.StatusData(
                        amount = '0', 
                        timestamp = '2019-01-01T01:01:01+00:00', ), 
                    notice_to_proceed = springlabs.models.status_data.StatusData(
                        amount = '0', 
                        timestamp = '2019-01-01T01:01:01+00:00', ), 
                    signed_assessment_contract = springlabs.models.status_data.StatusData(
                        amount = '0', 
                        timestamp = '2019-01-01T01:01:01+00:00', ), ),
                subject = springlabs.models.subject.Subject(
                    address = springlabs.models.address.Address(
                        address_city = '0', 
                        address_line1 = '0', 
                        address_line2 = '0', 
                        address_state = '0', 
                        address_zip = '0', ), 
                    parcel = springlabs.models.parcel.Parcel(
                        apn = '0', 
                        fips_county_code = '0', ), ),
        )

    def testAttestationGroupInput(self):
        """Test AttestationGroupInput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
