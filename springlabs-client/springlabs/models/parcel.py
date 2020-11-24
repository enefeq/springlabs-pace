# coding: utf-8

"""
    Spring PACE Product Client Software Server

    This section describes the API calls and their usage to interact with the Spring Network.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@springlabs.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from springlabs.configuration import Configuration


class Parcel(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'apn': 'str',
        'fips_county_code': 'str'
    }

    attribute_map = {
        'apn': 'apn',
        'fips_county_code': 'fipsCountyCode'
    }

    def __init__(self, apn=None, fips_county_code=None, local_vars_configuration=None):  # noqa: E501
        """Parcel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._apn = None
        self._fips_county_code = None
        self.discriminator = None

        self.apn = apn
        self.fips_county_code = fips_county_code

    @property
    def apn(self):
        """Gets the apn of this Parcel.  # noqa: E501


        :return: The apn of this Parcel.  # noqa: E501
        :rtype: str
        """
        return self._apn

    @apn.setter
    def apn(self, apn):
        """Sets the apn of this Parcel.


        :param apn: The apn of this Parcel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and apn is None:  # noqa: E501
            raise ValueError("Invalid value for `apn`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                apn is not None and len(apn) > 255):
            raise ValueError("Invalid value for `apn`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                apn is not None and len(apn) < 0):
            raise ValueError("Invalid value for `apn`, length must be greater than or equal to `0`")  # noqa: E501

        self._apn = apn

    @property
    def fips_county_code(self):
        """Gets the fips_county_code of this Parcel.  # noqa: E501


        :return: The fips_county_code of this Parcel.  # noqa: E501
        :rtype: str
        """
        return self._fips_county_code

    @fips_county_code.setter
    def fips_county_code(self, fips_county_code):
        """Sets the fips_county_code of this Parcel.


        :param fips_county_code: The fips_county_code of this Parcel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and fips_county_code is None:  # noqa: E501
            raise ValueError("Invalid value for `fips_county_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                fips_county_code is not None and len(fips_county_code) > 255):
            raise ValueError("Invalid value for `fips_county_code`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                fips_county_code is not None and len(fips_county_code) < 0):
            raise ValueError("Invalid value for `fips_county_code`, length must be greater than or equal to `0`")  # noqa: E501

        self._fips_county_code = fips_county_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Parcel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Parcel):
            return True

        return self.to_dict() != other.to_dict()