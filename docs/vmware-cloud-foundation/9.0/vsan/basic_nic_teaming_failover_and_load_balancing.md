---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/nic-teaming-failover-and-load-balancing.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Basic NIC Teaming, Failover, and Load Balancing
---

# Basic NIC Teaming, Failover, and Load Balancing

For IP storage based solutions such as vSAN, it is best practice to implement network redundancy.

You can use NIC teaming to achieve network redundancy. You can configure two or more network adapters (NICs) as a team for high availability and load balancing. Basic NIC teaming is available with vSphere networking, and these techniques can affect vSAN design and architecture.

Several NIC teaming options are available. Avoid NIC teaming policies that require physical switch configurations, or that require an understanding of networking concepts such as Link Aggregation. Best results are achieved with a basic, simple, and reliable setup.

If you are not sure about NIC teaming options, use an Active/Standby configuration with explicit failover.