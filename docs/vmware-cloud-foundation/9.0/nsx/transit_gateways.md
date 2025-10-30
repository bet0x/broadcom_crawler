---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/transit-gateways.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Transit Gateways
---

# Transit Gateways

When a new tenant (NSX Project) is created, a default Transit Gateway is automatically created for the Project. Note that a Project can have only one Transit Gateway.

Transit Gateway

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ccc7b678-c7a0-40c7-ab88-fed6dfa214f8.cq5dam.web.1280.1280.jpeg)

A Transit Gateway (TGW) provides both inter-VPC communication and connection to the outside network through External Connections. This model keeps an inter-VPC communication inside a tenant.

With a Transit Gateway, there is no need for sharing a Tier-0 directly with a NSX Project. Instead, an External Connection is shared to the project, to which the TGW is connected.

A tenant admin can connect a TGW to one or more external External Connections - a single connection if the connection type is centralized (CTGW) or multiple connections if the connection type is distributed (DTGW). For more information about connection types, see [External Connections](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/external-connections.html).