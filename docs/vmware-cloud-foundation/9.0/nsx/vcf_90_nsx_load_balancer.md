---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > VCF 9.0 NSX Load Balancer
---

# VCF 9.0 NSX Load Balancer

The NSX logical load balancer offers high-availability service for applications and distributes the network traffic load among multiple servers.

![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/dde0334e-1d67-4a13-8f62-64778a0990b7.original.png)

The load balancer distributes incoming service requests evenly among multiple servers in such a way that the load distribution is transparent to users. Load balancing helps in achieving optimal resource utilization, maximizing throughput, minimizing response time, and avoiding overload.

You can map a virtual IP address to a set of pool servers for load balancing. The load balancer accepts TCP and UDP requests on the virtual IP address and decides which pool server to use.

Depending on your environment needs, you can scale the load balancer performance by increasing the existing virtual servers and pool members to handle heavy network traffic load.

Logical load balancer is supported only on the tier-1 gateway. One load balancer can be attached only to a tier-1 gateway.