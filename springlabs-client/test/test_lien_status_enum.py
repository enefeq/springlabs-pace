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
from springlabs.models.lien_status_enum import LienStatusEnum  # noqa: E501
from springlabs.rest import ApiException

class TestLienStatusEnum(unittest.TestCase):
    """LienStatusEnum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LienStatusEnum
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = springlabs.models.lien_status_enum.LienStatusEnum()  # noqa: E501
        if include_optional :
            return LienStatusEnum(
            )
        else :
            return LienStatusEnum(
        )

    def testLienStatusEnum(self):
        """Test LienStatusEnum"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
