---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-1-gateways/state-synchronization-of-tier-1-gateways.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > State Synchronization of Tier-1 Gateways
---

# State Synchronization of Tier-1 Gateways

Connection information of the traffic running on a given tier-1 SR (Service Router) is synchronized to its peer tier-1 SR in active-standby or stateful active-active HA modes.

The synchronization between the Active SR and Standby SR is triggered whenever there is a change in the local state of TCP SYN packet, after a certain interval, or if a local state is created or deleted. During synchronization, Edge uses proprietary protocol to replicate CCP packets between Active and Standby SRs.

State synchronization is not supported for TLS Inspection and IDPS.

Note the following about state synchronization:

- State synchronization is supported for Gateway Firewall, Identity Firewall, NAT, IPSec VPN, DHCP, FQDN analysis, and URL filtering.
- If new sessions were going through a tier-1 SR just before a failover, it might happen that those sessions were not synchronized on the associated tier-1 SR and potentially affect the traffic for those sessions.
- In active-standby mode, state synchronization is supported for Gateway Firewall, Identity Firewall, NAT, IPSec VPN, DHCP, FQDN analysis, and URL filtering.
- In active-active mode, state synchronization is supported for Gateway Firewall, Identity Firewall, NAT, FQDN analysis, and URL filtering. FQDN analysis is only supported with a single sub-cluster. IPSec VPN is not supported.
- If new sessions were going through a tier-1 SR just before a failover, it might happen that those sessions were not synchronized on the associated tier-1 SR and potentially affect the traffic for those sessions.