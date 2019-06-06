import aruba
from client import CFMClient
import system

cfm = CFMClient('localhost', 'admin', 'plexxi')

# unauthenticated calls, connect without login and token
cfm.connect(login=False)

print(system.get_version(cfm))
# print(aruba.get_firmware(client))
print(aruba.register_device(cfm, '172.16.50.101', '00:01:02:03:04:05', ['camera', 'faces']))

# delete unauthenticated session
cfm.disconnect()

# authenticated calls
# print(system.get_audit_logs(client))
