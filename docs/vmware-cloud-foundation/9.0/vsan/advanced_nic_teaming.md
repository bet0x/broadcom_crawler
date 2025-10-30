---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/advanced-nic-teaming.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Advanced NIC Teaming
---

# Advanced NIC Teaming

You can use advanced NIC teaming methods with multiple VMkernel adapters having two dedicated subnets to configure the vSAN network. If you use Link Aggregation Protocol (LAG/LACP), the vSAN network can be configured with a single VMkernel adapter.

You can use advanced NIC teaming to implement an air gap, so a failure that occurs on one network path does not impact the other network path. If any part of one network path fails, the other network path can carry the traffic. Configure multiple VMkernel NICs for vSAN on different subnets, such as another VLAN or separate physical network fabric.

vSphere and vSAN do not support multiple VMkernel adapters (vmknics) on the same subnet. For more details, see Broadcom knowledge base article [2010877](https://knowledge.broadcom.com/external/article?legacyId=2010877).

![Advanced NIC teaming](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/006089e5-bb55-4da8-85ff-53747fa6318e.original.png)