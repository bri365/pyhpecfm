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
cfm.connect()

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
vpc = vpcs[0].get('uuid')

bgp = fabric.get_bgp(cfm, vpc)
print(bgp)

# not yet fully implemented
# leaf_spine = fabric.get_bgp_leaf_spine(cfm, vpc)

leaf_spine_config = {
  'subnet': {
    'prefix_length': 24,
    'address': '172.10.10.0'
  },
  'enable': true,
  'name': 'My BGP configuration',
  'holddown_timer': 90,
  'keepalive_timer': 30,
  'asn_ranges': '65100-65120',
  'spine_switches': [
    '1c35f445-0e2c-4d0a-b8fd-dae75924567e'
  ],
  'description': 'CFM created BGP configuration'
}

