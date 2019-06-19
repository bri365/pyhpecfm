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
cfm.connect()

fabrics = fabric.get_fabrics(cfm)

fabric_uuid = None
for f in fabrics:
    if f['name'] == 'Aruba':
        fabric_uuid = f['uuid']

if not fabric_uuid:
    print('Aruba fabric not found')
    exit(1)

print('\nAruba fabric UUID {}'.format(fabric_uuid))

switches = fabric.get_switches(cfm, {'fabric_uuid': fabric_uuid})
spine_ip_addresses = ['192.168.249.83', '192.168.249.84']
spine_uuids = [sw['uuid'] for sw in switches if sw['ip_address'] in spine_ip_addresses]

vpcs = fabric.get_vpcs(cfm)
print('\nVPCs:\n{}'.format(vpcs))
vpc = vpcs[0].get('uuid')

bgp = fabric.get_bgp(cfm, vpc)
print('\nBGP:\n{}'.format(bgp))

# not yet fully implemented
# leaf_spine = fabric.get_bgp_leaf_spine(cfm, vpc)

leaf_spine_config = {
  'subnet': {
    'prefix_length': 24,
    'address': '192.168.1.0'
  },
  'enable': True,
  'name': 'ArubaCX demo',
  'holddown_timer': 90,
  'keepalive_timer': 30,
  'asn_ranges': '65030-65050',
  'spine_switch_uuids': spine_uuids,
  'description': 'CFM created BGP configuration'
}
print('\nleaf_spine_config:\n{}'.format(leaf_spine_config))

result = fabric.update_bgp_leaf_spine(cfm, vpc, leaf_spine_config)
print('\nbgp_leaf_spine result:\n{}'.format(result))
