# -*- coding: utf-8 -*-
"""
This module is used for testing.
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

aruba_fabric = {
    'host': '10.10.8.31',
    'name': 'Aruba',
    'description': 'Aruba demo fabric',
    'username': aruba_username,
    'password': aruba_password
}

result = fabric.create_fabric(cfm, aruba_fabric, fabric_type='aruba')
print(result)
print(result.json())
exit()
fabric_uuid = result.json()

for ip in ['10.10.8.32', '10.10.8.33', '10.10.8.34']:
    aruba_switch = {
        'host': ip,
        'name': 'Aruba',
        'description': 'Aruba discovered switch',
        'fabric_uuid': fabric_uuid,
        'username': aruba_username,
        'password': aruba_password
    }
    result = fabric.create_switch(cfm, aruba_switch, fabric_type='aruba')
    print(result)
    print(result.json())
