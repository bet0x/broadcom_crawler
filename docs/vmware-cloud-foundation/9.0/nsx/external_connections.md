---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/external-connections.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > External Connections
---

# External Connections

External Connection defines how the Transit Gateway (TGW) will connect to networks outside of NSX and which services will be available on it. Those connections are created from Default (/infra) and define the connection to the outside environment.

There are two types of External Connections and they both serve different requirements. You can select one based on the features you require for your network.

- Centralized Connection: It connects the TGW through a Tier-0 Gateway provisioned from NSX. The Tier-0 gateway is deployed on NSX Edge nodes and provides interconnection to the physical fabric.

  Centralized connections allow stateful services and dynamic routing with the physical fabric (BGP) at Tier-0 level. It also allows NAT configuration at TGW level. It requires setting up Edge nodes and managing their lifecycle. Create Centralized connection if you have an environment that requires full-scale NSX networking services, such as DHCP, NAT, and Layer 3 services.

- Distributed Connection: It connects the Transit Gateway directly to VLANs provisioned in the fabric. This happens directly on the ESX hosts, which implies that VLANs need to be available on the ESX.

  Distributed connection allows a lightweight connectivity to the data-center fabric without the need to deploy Edge nodes or configure dynamic routing. In addition to on-demand networking and distributed routing, other services available when using Distributed connections are External IPs (1:1 NAT) and distributed DHCP server.

Transit Gateway with Centralized connection and Transit Gateway with Distributed connection

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/2ae37346-4673-4f55-aedd-fcb662b409d8.cq5dam.web.1280.1280.jpeg)

A Transit Gateway can have only one Centralized connection or it can have multiple Distributed connections. So a given Transit Gateway would be in either one Centralized connection or in multiple Distributed connections.

Transit Gateway with a single Centralized connection and Transit Gateway with a Distributed connection

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/77984d1b-e319-4653-a6a0-d723fc5e951e.cq5dam.web.1280.1280.jpeg)

In both cases, an External connection relies on the fact that whatever objects a Transit Gateway connects with must be previously configured. For a Centralized connection, it requires a Tier-0 deployed with Edge nodes and external routing properly configured. In case of dynamic routing, such as BGP, make sure the "Transit Gateway Static" option is enabled in the route redistribution settings.

For a Distributed connection, it implies that the VLANs used for outside connections are available on ESX hosts on the same uplinks (physical NICs) as NSX overlay vmkernal adapter.