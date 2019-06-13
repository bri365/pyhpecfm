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

cfm = client.CFMClient(cfm_ip, cfm_username, cfm_password)

fabrics = fabric.get_fabrics(cfm)

fabric_uuid = None
for f in fabrics:
    if f['name'] == 'Aruba':
        fabric_uuid = f['uuid']

if not fabric_uuid:
    print('Aruba fabric not found')
    exit(1)

print('Aruba fabric UUID {}'.format(fabric_uuid))

vpcs = fabric.get_vpcs(cfm)
print(vpcs)
vpc = vpcs[0]

bgp = fabric.get_bgp(cfm, vpc)
print(bgp)

leaf_spine = fabric.get_bgp_leaf_spine(cfm, vpc)
print(leaf_spine)
