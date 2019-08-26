# coding: utf-8

"""
    Alertmanager API

    API of the Prometheus Alertmanager (https://github.com/prometheus/alertmanager)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Matcher(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'value': 'str',
        'is_regex': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'is_regex': 'isRegex'
    }

    def __init__(self, name=None, value=None, is_regex=None):  # noqa: E501
        """Matcher - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._value = None
        self._is_regex = None
        self.discriminator = None

        self.name = name
        self.value = value
        self.is_regex = is_regex

    @property
    def name(self):
        """Gets the name of this Matcher.  # noqa: E501


        :return: The name of this Matcher.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Matcher.


        :param name: The name of this Matcher.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this Matcher.  # noqa: E501


        :return: The value of this Matcher.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Matcher.


        :param value: The value of this Matcher.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def is_regex(self):
        """Gets the is_regex of this Matcher.  # noqa: E501


        :return: The is_regex of this Matcher.  # noqa: E501
        :rtype: bool
        """
        return self._is_regex

    @is_regex.setter
    def is_regex(self, is_regex):
        """Sets the is_regex of this Matcher.


        :param is_regex: The is_regex of this Matcher.  # noqa: E501
        :type: bool
        """
        if is_regex is None:
            raise ValueError("Invalid value for `is_regex`, must not be `None`")  # noqa: E501

        self._is_regex = is_regex

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Matcher, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Matcher):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
