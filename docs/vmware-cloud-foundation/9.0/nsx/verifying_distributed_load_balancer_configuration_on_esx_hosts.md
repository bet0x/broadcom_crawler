---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/distributed-load-balancer/verifying-distributed-load-balancer-configuration-on-esxi-hosts.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Verifying Distributed Load Balancer Configuration on ESX Hosts
---

# Verifying Distributed Load Balancer Configuration on ESX Hosts

Verify whether the Distributed Load Balancer was configured completely on ESX hosts.

## 

After you securely connect to the ESX host, run /opt/vmware/nsx-nestdb/bin/nestdb-cli. From the nestdb-cli prompt, run the following commands.

| Command | Sample Response |
| --- | --- |
| To view the configured DLB service, run get LbServiceMsg. | {'id': {'left': 13946864992859343551, 'right': 10845263561610880178}, 'virtual\_server\_id': [{'left': 13384746951958284821, 'right': 11316502527836868364}], 'display\_name': 'mydlb', 'size': 'DLB', 'enabled': True, 'access\_log\_enabled': False, 'log\_level': 'LB\_LOG\_LEVEL\_INFO', 'applied\_to': {'type': 'CONTAINER', 'attachment\_id': {'left': 2826732686997341216, 'right': 10792930437485655035}}} |
| To view the virtual server configured for DLB, run get LbVirtualServerMsg. | {'port': '80', 'revision': 0, 'display\_name': 'mytcpvip', 'pool\_id': {'left': 4370937730160476541, 'right': 13181758910457427118}, 'enabled': True, 'access\_log\_enabled': False, 'id': {'left': 13384746951958284821, 'right': 11316502527836868364}, 'ip\_protocol': 'TCP', 'ip\_address': {'ipv4': 2071690107}, 'application\_profile\_id': {'left': 1527034089224553657, 'right': 10785436903467108397}} |
| To view configuration of the DLB pool members, run get LbPoolMsg. | {'tcp\_multiplexing\_number': 6, 'display\_name': 'mylbpool', 'tcp\_multiplexing\_enabled': False, 'member': [{'port': '80', 'weight': 1, 'display\_name': 'Member\_VM30', 'admin\_state': 'ENABLED', 'ip\_address': {'ipv4': 3232261280}, 'backup\_member': False}, {'port': '80', 'weight': 1, 'display\_name': 'Member\_VM31', 'admin\_state': 'ENABLED', 'ip\_address': {'ipv4': 3232261281}, 'backup\_member': False}, {'port': '80', 'weight': 1, 'display\_name': 'Member\_VM32', 'admin\_state': 'ENABLED', 'ip\_address': {'ipv4': 3232261282}, 'backup\_member': False}], 'id': {'left': 4370937730160476541, 'right': 13181758910457427118}, 'min\_active\_members': 1, 'algorithm': 'ROUND\_ROBIN'} |
| To view NSX controller configuration pushed to the ESX host, run get ContainerMsg. | {'container\_type': 'CONTAINER', 'id': {'left': 2826732686997341216, 'right': 10792930437485655035}, 'vif': ['cd2e482b-2998-480f-beba-65fbd7ab1e62', 'f8aa2a58-5662-4c6b-8090-d1bd19174205', '83a1f709-e675-4e42-b677-ff501fd0f4ec', 'b8366b39-4c81-41fc-b89e-de7716462b2f'], 'name': 'default.clientVMGroup', 'mac\_address': [{'mac': 52237218275}, {'mac': 52243694681}, {'mac': 52233233291}, {'mac': 52239463383}], 'ip\_address': [{'ipv4': 16844388}, {'ipv4': 16844644}, {'ipv4': 16844132}, {'ipv4': 3232261283}, {'ipv4': 16844298}, {'ipv4': 16844554}, {'ipv4': 16844042}]} |
| To view application profile configuration on the ESX host, run get LbApplicationProfileMsg. | {'display\_name': 'default-tcp-lb-app-profile', 'id': {'left': 1527034089224553657, 'right': 10785436903467108397}, 'application\_type': 'FAST\_TCP', 'fast\_tcp\_profile': {'close\_timeout': 8, 'flow\_mirroring\_enabled': False, 'idle\_timeout': 1800}} |