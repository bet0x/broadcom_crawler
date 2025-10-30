---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking/vsan-network-characteristics/using-unicast-in-vsan-network/ipv6-support-on-unicast-network.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > IPv6 Support on Unicast Network
---

# IPv6 Support on Unicast Network

vSAN supports IPv6 with unicast communications.

With IPv6, the link-local address is automatically configured on any interface using the link-local prefix. By default, vSAN does not add the link local address of a node to other neighboring cluster nodes. As a result, vSAN does not support IPv6 link local addresses for unicast communications.