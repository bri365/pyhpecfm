#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains functions for working with aruba switches managed by the
desired HPE Composable Fabric Manager instance.
"""


def get_firmware(cfmclient, ):
    """
    Function takes input cfmclient type object to authenticate against CFM API and queries
    versions API to return the version number of the system represented by the CFCMclient object
    Current supported params are

    :param cfmclient: object of type CFMClient
    :return: list of dicts
    """
    path = 'v1/aruba/action'
    data = {'action': 'get_firmware', 'params': {'switch': '192.168.249.81'}}
    return cfmclient.post(path, data=data).json().get('result')


def register_device(cfmclient, ip, mac, tags):
    """
    Function takes input cfmclient type object to authenticate against CFM API and queries
    versions API to return the version number of the system represented by the CFCMclient object
    Current supported params are

    :param cfmclient: object of type CFMClient
    :return: list of dicts
    """
    path = 'v1/aruba/action'
    params = {'ip_address': ip, 'mac_address': mac, 'tags': tags}
    data = {'action': 'register_device', 'params': params}
    return cfmclient.post(path, data=data).json().get('result')
