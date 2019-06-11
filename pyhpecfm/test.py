import os

import aruba
from client import CFMClient
import system

cfm_ip = os.environ['CFM_IP']
cfm_username = os.environ['CFM_USERNAME']
cfm_password = os.environ['CFM_PASSWORD']

cfm = CFMClient(cfm_ip, cfm_username, cfm_password)

# unauthenticated calls, connect without login and token
cfm.connect(login=False)

# print(system.get_version(cfm))
# print(aruba.get_firmware(client))
print('\nRegistering camera with authorized applications\n')
result = aruba.register_device(cfm, '172.16.50.32', 'ec:71:db:5a:15:e2', ['faces'])
print(result.get('output').get('result'))

# delete unauthenticated session
cfm.disconnect()

# authenticated calls
# print(system.get_audit_logs(client))
