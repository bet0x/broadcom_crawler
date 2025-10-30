---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/key-load-balancer-concepts.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Key Load Balancer Concepts
---

# Key Load Balancer Concepts

Load balancer
includes virtual servers, server pools, and health checks monitors.

A load balancer is connected to a Tier-1 logical
router. The load balancer hosts single or multiple virtual servers. A virtual server is
an abstract of an application service, represented by a unique combination of IP, port,
and protocol. The virtual server is associated to single to multiple server pools. A
server pool consists of a group of servers. The server pools include individual server
pool members.

To test whether each server is correctly running
the application, you can add health check monitors that check the health status of a
server.

![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/29a89cf1-8303-460d-91fb-f1442d5ee395.original.png)