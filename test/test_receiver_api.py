# coding: utf-8

"""
    Alertmanager API

    API of the Prometheus Alertmanager (https://github.com/prometheus/alertmanager)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.receiver_api import ReceiverApi  # noqa: E501
from swagger_client.rest import ApiException


class TestReceiverApi(unittest.TestCase):
    """ReceiverApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.receiver_api.ReceiverApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_receivers(self):
        """Test case for get_receivers

        """
        pass


if __name__ == '__main__':
    unittest.main()
