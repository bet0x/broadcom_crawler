---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/stateful-services-on-tier-0-and-tier-1-gateways.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Stateful Services on Tier-0 and Tier-1 on NSX
---

# Stateful Services on Tier-0 and Tier-1 on NSX

To meet the demands of stateful services such as more bandwidth and throughput, you can configure Tier-0 and Tier-1 gateways in Active-Active (A-A) configuration. Stateful services are required for next generation firewall, Layer 7 rules, URL filtering or TLS decryption.

You can scale-out or scale-in the number of service routers by adding NSX Edge nodes to the cluster.

As you scale-in or scale-out NSX Edge nodes, you might see loss of traffic packets for existing flows.

The supported stateful gateway services are:

- Gateway Firewall L3-L4
- APP-ID (L7)
- User-ID
- URL Filtering
- TLS Inspection
- IDS/IPS
- Malware Detection and Sandboxing
- NAT
- DHCP Relay Server
- DHCP Server

The unsupported services are:

- FQDN Analysis
- L2VPN
- IPSecVPN
- Gateway Network Introspection
- Local DHCP Server
- Service Interface

In your existing topology, if Tier-1 gateway is in active-standby (A-S) mode, you cannot reconfigure it in A-A HA mode and it cannot share the same NSX Edge cluster with A-A stateful Tier-0 gateways. As a workaround, deploy that Tier-1 gateway in active-standby mode on a separate cluster. Then, deploy Tier-0 gateway on another NSX Edge cluster. If your environment requires a Tier-1 gateway, configure it in A-A HA mode. See [Supported Topologies](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/stateful-services-on-tier-0-and-tier-1-gateways/supported-topologies.html#GUID-19ecc224-5278-46ca-aa81-411ea59c2175-en).