---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-network-topologies/standard-deployments.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Standard Deployments
---

# Standard Deployments

vSAN supports several single-site deployment types.

## Layer-2, Single Site, Single Rack

This network topology is responsible for forwarding packets through intermediate Layer 2 devices such as hosts, bridges, or switches.

Layer 2 implementations are simplified even further and introduces unicast support. IGMP Snooping is not required.

![Single site, single rack diagram](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/9b8abbc5-f86d-4297-b134-2c1dec3c79d7.original.png)

## Layer 2, Single Site, Multiple Racks

This network topology works with the Layer 2 implementation where there are multiple racks, and multiple top-of-rack switches, or TORs, connected to a core switch.

![Layer 2, single site, multiple racks diagram](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/59d14cc7-8820-4c1c-9c0e-c991784ef55a.original.png)

## Layer 3, Single Site, Multiple Racks

This network topology works for vSAN deployments where Layer 3 is used to route vSAN traffic.

This simple Layer 3 network topology uses multiple racks in the same data center, each with its own TOR switch. Route the vSAN network between the different racks over L3, to allow all the hosts in the vSAN cluster to communicate. Place the vSAN VMkernel ports on different subnets or VLANs, and use a separate subnet or VLAN for each rack.

This network topology routes packets through intermediate Layer 3 capable devices, such as routers and Layer 3 capable switches. Whenever hosts are deployed across different Layer 3 network segments, the result is a routed network topology.

![Layer 3, single site, multiple racks diagram](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ab0aad68-fe0e-440b-bff5-747b271acf98.original.png)