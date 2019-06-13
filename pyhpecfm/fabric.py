#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains functions related to working with the fabric characteristics of the
desired HPE Composabale Fabric Manager instance
"""


####################
# Fabric functions #
####################

def get_fabrics(cfmclient, fabric_uuid=None):
    """
    Get :List of Fabrics currently defined in Composable Fabric .

    :param cfmclient:
    :param fabric_uuid: switch_uuid: UUID of switch from which to fetch port data
    :return: list of Dictionary objects where each dictionary represents a port on a
    Composable Fabric Module
    :rtype: list
    """
    path = 'fabrics'
    if fabric_uuid:
        path = 'fabrics/{}'.format(fabric_uuid)
    return cfmclient.get(path).json().get('result')


def get_fabric_ip_networks(cfmclient, fabric_uuid=None):
    """
    Get :List of Fabrics currently defined in Composable Fabric .

    :param cfmclient:
    :param fabric_uuid: switch_uuid: UUID of switch from which to fetch port data
    :return: list of Dictionary objects where each dictionary represents a port on a
    Composable Fabric Module
    :rtype: list
    """
    path = 'fabric_ip_networks'
    if fabric_uuid:
        path = 'fabric_ip_networks/{}'.format(fabric_uuid)
    return cfmclient.get(path).json().get('result')


def create_fabric(cfmclient, data, fabric_type=None):
    """
    Create :A Composable Fabric.
    """
    path = 'fabrics'
    params = {'type': fabric_type} if fabric_type else None
    return cfmclient.post(path, params, data).json().get('result')


#####################
# Fitting functions #
#####################

def perform_fit(cfmclient, fabric_uuid, name, description):
    """
    Function causes Composable Fabric Manager to perform a full fit across managed fabrics
    :param cfmclient:
    :return:
    """
    data = {
        'fabric_uuid': '{}'.format(fabric_uuid),
        'name': '{}'.format(name),
        'description': '{}'.format(description)
            }
    path = 'fits'
    return cfmclient.post(path, data=data)


######################
# Switches functions #
######################

def get_switches(cfmclient, params=None):
    """
    Function takes input cfmclient type object to authenticate against CFM API and queries
    all currently configured switches from the system and returns a list of dictionaries
    where each item in the list represents a single switch.
    Current supported params are

    :param cfmclient: object of type CFMClient
    :param params: dict of query parameters used to filter request from API
    :return: list of dicts

    >>> client= CFMClient('10.101.0.210', 'admin', 'plexxi')
    >>> get_switches(client, params={'ports': True})
    >>> get_switches(client, params={'ports': True, 'software': True})
    >>> get_switches(client, params={'ports': True, 'software': True, 'fabric': True})
    """
    path = 'switches'
    return cfmclient.get(path, params).json().get('result')


def create_switch(cfmclient, data, fabric_type=None):
    """
    Create :A Composable Fabric switch.
    """
    path = 'switches'
    params = {'type': fabric_type} if fabric_type else None
    return cfmclient.post(path, params, data).json().get('result')


##################
# Port functions #
##################

def get_ports(cfmclient, switch_uuid=None):
    """
    Get Composable Fabric switch ports.
    :param cfmclient: object of type CFMClient
    :param switch_uuid: switch_uuid: UUID of switch from which to fetch port data
    :return: list of Dictionary objects where each dictionary represents a port on a
    Composable Fabric Module
    :rtype: list
    """
    path='ports'
    if switch_uuid:
        path = 'ports?switches={}&type=access'.format(switch_uuid)
        return cfmclient.get(path).json().get('result')
    else:
        return cfmclient.get(path).json().get('result')


def update_ports(cfmclient, port_uuids, field, value):
    """
    Function to update various attributes of composable fabric module ports
    :param cfmclient:
    :param port_uuids: list of str where each string represents a single unique port in a
    composable fabric
    :param field: str specific field which is desired to be modified (case-sensitive)
    :param value: str specific field which sets the new desired value for the field
    :return: dict which contains count, result, and time of the update
    :rtype: dict
    """
    if port_uuids:
        data = [{
            'uuids': port_uuids,
            'patch': [
                {
                    'path': '/{}'.format(field),
                    'value': value,
                    'op': 'replace'
                }
            ]
        }]
        cfmclient.patch('ports', data)

##################
# VLAN functions #
##################

def get_vlan_groups(cfmclient, params=None):
    """
    Get Composable Fabric vlan groups.
    :param cfmclient: object of type CFMClient
    :return: list of Dictionary objects where each dictionary represents a vlan group on a
    Composable Fabric.
    :rtype: list
    """
    path='vlan_groups'
    return cfmclient.get(path, params).json().get('result')

#TODO POST VLAN_GROUP FUNCTION

#TODO PUT VLAN GROUP FUNCTION

#TODO DELETE VLAN GROUP FUNCTION


def get_vlan_properties(cfmclient, fabric_uuid):
    """
    Get Composable Fabric vlan properties for a specific fabric.
    :param cfmclient: object of type CFMClient
    :param fabric_uuid: object of type string which represents a valid fabric UUID on the specific
    CFM instance.
    :return: list of Dictionary objects where each dictionary represents a vlan group on a
    Composable Fabric.
    :rtype: list
    """
    path='vlan_properties/{}'.format(fabric_uuid)
    return cfmclient.get(path).json().get('result')

####################
# VPC functions #
####################

def get_vpcs(cfmclient, uuid=None):
    """
    Get :List of VPCs currently defined in Composable Fabric.

    :param cfmclient: Connected CFM API client
    :param uuid: specific VPC UUID to retrieve
    :return: list of VPC dictionary objects
    :rtype: list
    """
    path = 'vpcs'
    if uuid:
        path += '/{}'.format(uuid)
    return cfmclient.get(path).json().get('result')

def get_bgp(cfmclient, uuid):
    """
    Get VPC BGP configuration.

    :param cfmclient: Connected CFM API client
    :param uuid: VPC UUID from which to retrieve BGP info
    :return: BGP dictionary object
    :rtype: list
    """
    path = 'vpcs/{}/bgp'.format(uuid)
    return cfmclient.get(path).json().get('result')

def get_bgp_leaf_spine(cfmclient, uuid):
    """
    Get VPC BGP leaf and spine configuration.

    :param cfmclient: Connected CFM API client
    :param uuid: VPC UUID from which to retrieve BGP info
    :return: BGP dictionary object
    :rtype: list
    """
    path = 'vpcs/{}/bgp/leaf_spine'.format(uuid)
    return cfmclient.get(path).json().get('result')
