---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/key-load-balancer-concepts/supported-load-balancer-features.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Supported Load Balancer Features
---

# Supported Load Balancer Features

You can use an NSX load balancer with the management appliance and with VCF Automation All Apps. A load balancer supports the following features.

- Layer 4 (TCP and UDP) - The NSX load balancer can make traffic distribution decisions based on information at the transport layer of the network. Decisions are based on IP addresses and TCP/UDP socket information (source/destination IP and port) only. It does not inspect or make load balancer descisions based on Layer 7 (application layer) data, such as HTTP or HTTPs requests. This means no content-based routing URL-based redirection, or advanced apllication-aware features.
- Server pools - Static and dynamic with NSGroup
- Persistence - Source-IP
- Health check monitors - Active monitor which includes TCP, UDP, and ICMP, and passive monitor
- SNAT - Transparent, Automap, and IP List
- The Load Balancing runbook lists the topology for the given load balancer instance.

Note: SSL -Terminate-mode and proxy-mode is not supported in NSX limited export release.

![A diagram of load balancer features.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/2673ce53-a014-4f7a-9e8e-b9d959dc1f4c.original.png)