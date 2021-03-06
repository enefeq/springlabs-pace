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


class AttestationGroupInput(object):
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
        'lien_status_data': 'LienStatusData',
        'subject': 'Subject'
    }

    attribute_map = {
        'lien_status_data': 'lienStatusData',
        'subject': 'subject'
    }

    def __init__(self, lien_status_data=None, subject=None, local_vars_configuration=None):  # noqa: E501
        """AttestationGroupInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._lien_status_data = None
        self._subject = None
        self.discriminator = None

        self.lien_status_data = lien_status_data
        self.subject = subject

    @property
    def lien_status_data(self):
        """Gets the lien_status_data of this AttestationGroupInput.  # noqa: E501


        :return: The lien_status_data of this AttestationGroupInput.  # noqa: E501
        :rtype: LienStatusData
        """
        return self._lien_status_data

    @lien_status_data.setter
    def lien_status_data(self, lien_status_data):
        """Sets the lien_status_data of this AttestationGroupInput.


        :param lien_status_data: The lien_status_data of this AttestationGroupInput.  # noqa: E501
        :type: LienStatusData
        """
        if self.local_vars_configuration.client_side_validation and lien_status_data is None:  # noqa: E501
            raise ValueError("Invalid value for `lien_status_data`, must not be `None`")  # noqa: E501

        self._lien_status_data = lien_status_data

    @property
    def subject(self):
        """Gets the subject of this AttestationGroupInput.  # noqa: E501


        :return: The subject of this AttestationGroupInput.  # noqa: E501
        :rtype: Subject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this AttestationGroupInput.


        :param subject: The subject of this AttestationGroupInput.  # noqa: E501
        :type: Subject
        """
        if self.local_vars_configuration.client_side_validation and subject is None:  # noqa: E501
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

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
        if not isinstance(other, AttestationGroupInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttestationGroupInput):
            return True

        return self.to_dict() != other.to_dict()
