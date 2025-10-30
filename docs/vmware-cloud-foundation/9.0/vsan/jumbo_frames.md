---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/ip-network-transport-configuration/jumbo-frames.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Jumbo Frames
---

# Jumbo Frames

vSAN fully supports jumbo frames on the vSAN network.

Jumbo frames are Ethernet frames with more than 1500 bytes of payload. Jumbo frames typically carry up to 9000 bytes of payload, but variations exist.

Using jumbo frames can reduce CPU utilization and improve throughput.

Enable jumbo frames support for vSAN storage cluster deployments to improve performance.

You must decide whether these gains outweigh the overhead of implementing jumbo frames throughout the network. In data centers where jumbo frames are already enabled in the network infrastructure, you can use them for vSAN. The operational cost of configuring jumbo frames throughout the network might outweigh the limited CPU and performance benefits.