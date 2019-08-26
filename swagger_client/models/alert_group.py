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

from swagger_client.models.gettable_alert import GettableAlert  # noqa: F401,E501
from swagger_client.models.label_set import LabelSet  # noqa: F401,E501
from swagger_client.models.receiver import Receiver  # noqa: F401,E501


class AlertGroup(object):
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
        'labels': 'LabelSet',
        'receiver': 'Receiver',
        'alerts': 'list[GettableAlert]'
    }

    attribute_map = {
        'labels': 'labels',
        'receiver': 'receiver',
        'alerts': 'alerts'
    }

    def __init__(self, labels=None, receiver=None, alerts=None):  # noqa: E501
        """AlertGroup - a model defined in Swagger"""  # noqa: E501

        self._labels = None
        self._receiver = None
        self._alerts = None
        self.discriminator = None

        self.labels = labels
        self.receiver = receiver
        self.alerts = alerts

    @property
    def labels(self):
        """Gets the labels of this AlertGroup.  # noqa: E501


        :return: The labels of this AlertGroup.  # noqa: E501
        :rtype: LabelSet
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this AlertGroup.


        :param labels: The labels of this AlertGroup.  # noqa: E501
        :type: LabelSet
        """
        if labels is None:
            raise ValueError("Invalid value for `labels`, must not be `None`")  # noqa: E501

        self._labels = labels

    @property
    def receiver(self):
        """Gets the receiver of this AlertGroup.  # noqa: E501


        :return: The receiver of this AlertGroup.  # noqa: E501
        :rtype: Receiver
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        """Sets the receiver of this AlertGroup.


        :param receiver: The receiver of this AlertGroup.  # noqa: E501
        :type: Receiver
        """
        if receiver is None:
            raise ValueError("Invalid value for `receiver`, must not be `None`")  # noqa: E501

        self._receiver = receiver

    @property
    def alerts(self):
        """Gets the alerts of this AlertGroup.  # noqa: E501


        :return: The alerts of this AlertGroup.  # noqa: E501
        :rtype: list[GettableAlert]
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this AlertGroup.


        :param alerts: The alerts of this AlertGroup.  # noqa: E501
        :type: list[GettableAlert]
        """
        if alerts is None:
            raise ValueError("Invalid value for `alerts`, must not be `None`")  # noqa: E501

        self._alerts = alerts

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
        if issubclass(AlertGroup, dict):
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
        if not isinstance(other, AlertGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
