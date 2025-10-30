---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/networking-considerations-for-iscsi-on-vsan/characteristics-of-vsan-iscsi-network.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Characteristics of vSAN iSCSI Network
---

# Characteristics of vSAN iSCSI Network

Following are the characteristics of a vSAN iSCSI network:

- iSCSI Routing - iSCSI initiators can make routed connections to vSAN iSCSI targets over an L3 network.
- IPv4 and IPv6 - vSAN iSCSI network supports both IPv4 and IPv6.
- IP Security - IPSec on the vSAN iSCSI network provides increased security.

  ESX hosts support IPsec using IPv6 only.
- Jumbo Frames - Jumbo Frames are supported on the vSAN iSCSI network.
- NIC Teaming - All NIC teaming configurations are supported on the vSAN iSCSI network.
- Multiple Connections per Session (MCS) - vSAN iSCSI implementation does not support MCS.