---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/advanced-nic-teaming/link-aggregation-group-overview/static-and-dynamic-link-aggregation.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Static and Dynamic Link Aggregation
---

# Static and Dynamic Link Aggregation

You can use LACP to combine and aggregate multiple network connections.

When LACP is in active or dynamic mode, a physical switch sends LACP messages to network devices, such as ESX hosts, to negotiate the creation of a Link Aggregation Group (LAG).

To configure Link Aggregation on hosts using vSphere Standard Switches (and pre-5.5 vSphere Distributed Switches), configure a static channel-group on the physical switch. See your vendor documentation for more details.

![Link aggregation](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/9508f5d0-af3f-473d-b932-619bb7c920de.original.png)

## Pros and Cons of Dynamic Link Aggregation

Consider the tradeoffs to using Dynamic Link Aggregation.

Pros

Improves performance and bandwidth. One vSAN host or VMkernel port can communicate with many other vSAN hosts using many different load-balancing options.

Provides network adapter redundancy. If a NIC fails and the link-state fails, the remaining NICs in the team continue to pass traffic.

Improves traffic balancing. Balancing of traffic after failures is automatic and fast.

Cons

Less flexible. Physical switch configuration requires that physical switch ports be configured in a port-channel configuration.

More complex. Use of multiple switches to produce full physical redundancy configuration is complex. Vendor-specific implementations add to the complexity.