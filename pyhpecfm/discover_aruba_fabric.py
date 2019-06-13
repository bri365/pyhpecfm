# -*- coding: utf-8 -*-
"""
Discover demo Aruba switches.
"""

import client
import fabric
import os

cfm_ip = os.environ['CFM_IP']
cfm_username = os.environ['CFM_USERNAME']
cfm_password = os.environ['CFM_PASSWORD']

aruba_username = os.environ['ARUBA_USERNAME']
aruba_password = os.environ['ARUBA_PASSWORD']

cfm = client.CFMClient(cfm_ip, cfm_username, cfm_password)

fabrics = fabric.get_fabrics(cfm)

fabric_uuid = None
for f in fabrics:
    if f['name'] == 'Aruba':
        fabric_uuid = f['uuid']

if not fabric_uuid:
    aruba_fabric = {
        'host': '10.10.8.31',
        'name': 'Aruba',
        'description': 'Aruba demo fabric',
        'username': aruba_username,
        'password': aruba_password
    }
    result = fabric.create_fabric(cfm, aruba_fabric, fabric_type='aruba')
    fabric_uuid = result['uuid']

print('Fabric UUID {}'.format(fabric_uuid))

switches = fabric.get_switches(cfm)
switch_ips = [sw['ip_address'] for sw in switches]
for ip in ['10.10.8.32', '10.10.8.33', '10.10.8.34']:
    if ip not in switch_ips:
        aruba_switch = {
            'host': ip,
            'name': 'Aruba',
            'description': 'Aruba discovered switch',
            'fabric_uuid': fabric_uuid,
            'username': aruba_username,
            'password': aruba_password
        }
        result = fabric.create_switch(cfm, aruba_switch, fabric_type='aruba')
        print('  Switch {} created'.format(ip))
