# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class NETWORK(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, network=None):  # noqa: E501
        """NETWORK - a model defined in Swagger

        :param network: The network of this NETWORK.  # noqa: E501
        :type network: str
        """
        self.swagger_types = {
            'network': str
        }

        self.attribute_map = {
            'network': 'Network'
        }

        self._network = network

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NETWORK of this NETWORK.  # noqa: E501
        :rtype: NETWORK
        """
        return util.deserialize_model(dikt, cls)

    @property
    def network(self):
        """Gets the network of this NETWORK.


        :return: The network of this NETWORK.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this NETWORK.


        :param network: The network of this NETWORK.
        :type network: str
        """
        if network is None:
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network