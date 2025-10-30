---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/state-synchronization-of-tier-0-gateways.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > State Synchronization of Tier-0 Gateways
---

# State Synchronization of Tier-0 Gateways

Connection information of the traffic running on a given tier-0 SR (Service Router) is synchronized to its peer tier-0 SR in active-standby or stateful active-active HA modes.

The synchronization between the Active SR and Standby SR is triggered whenever there is a change in the local state of TCP SYN packet, after a certain interval, or if a local state is created or deleted. During synchronization, Edge uses proprietary protocol to replicate CCP packets between Active and Standby SRs.

Note the following points about state synchronization:

- State synchronization is supported for Gateway Firewall, Identity Firewall, NAT, IPSec VPN, and DHCP.
- If new sessions were going through a tier-0 SR just before a failover, it might happen that those sessions were not synchronized on the associated tier-0 SR and potentially affect the traffic for those sessions.
- In active-standby mode, state synchronization is supported for Gateway Firewall, Identity Firewall, NAT, IPSec VPN, and DHCP.
- In active-active mode, state synchronization is supported for Gateway Firewall, Identity Firewall, and NAT. IPSec VPN is not supported.
- If new sessions were going through a tier-0 SR just before a failover, it might happen that those sessions were not synchronized on the associated tier-0 SR and potentially affect the traffic for those sessions.