# -*- coding: utf-8 -*-
"""
Discover demo Aruba switches.
"""

import client
import fabric
import os

cfm_ip = '192.168.249.167'
cfm_username = 'admin'
cfm_password = 'plexxi'

aruba_username = 'admin'
aruba_password = 'goplexxi'

cfm = client.CFMClient(cfm_ip, cfm_username, cfm_password)

fabrics = fabric.get_fabrics(cfm)

fabric_uuid = None
for f in fabrics:
    if f['name'] == 'Aruba':
        fabric_uuid = f['uuid']

if not fabric_uuid:
    aruba_fabric = {
        'host': '192.168.249.81',
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
for ip in ['192.168.249.82', '192.168.249.83', '192.168.249.84']:
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
