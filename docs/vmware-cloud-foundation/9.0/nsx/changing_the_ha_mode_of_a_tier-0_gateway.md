---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/changing-the-ha-mode-of-a-tier-0-gateway.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Changing the HA Mode of a Tier-0 Gateway
---

# Changing the HA Mode of a Tier-0 Gateway

You can change the high availability (HA) mode of a tier-0 gateway in certain circumstances.

Changing the HA mode is allowed only if there is no more than one service router running on the gateway, that is, uplinks on only one Edge transport node. However, you can have more than one uplink on the same Edge transport node.

After you set the HA mode from active-active to active-standby, you can set the failover mode. The default is non-preemptive.

HA mode change is not allowed if the following services or features are configured.

- DNS Forwarder
- IPSec VPN
- L2 VPN
- HA VIP
- Stateful Firewall
- SNAT, DNAT, NO\_SNAT, or NO\_DNAT
- Reflexive NAT applied on an interface
- Service Insertion
- VRF
- Service Interface