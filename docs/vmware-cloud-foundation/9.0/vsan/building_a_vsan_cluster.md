---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/what-is-vsan/building-a-virtual-san-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Building a vSAN Cluster
---

# Building a vSAN Cluster

You can choose the storage architecture and deployment option when creating a vSAN cluster.

Chose the vSAN storage architecture that best suits your resources and your needs.

## vSAN Express Storage Architecture

vSAN ESA is designed for high-performance NVMe based TLC flash devices and high performance networks. Each ESX host that contributes storage contains a single storage pool of one or more flash devices. Each flash device provides caching and capacity to the cluster.

![
          vSAN ESA diagram](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/cb540352-e086-4dbc-b8d1-9d7d45d422fa.original.png)

## vSAN Original Storage Architecture

vSAN OSA is designed for a wide range of storage devices, including flash solid state drives (SSD) and magnetic disk drives (HDD). Each ESX host that contributes storage contains one or more disk groups. Each disk group contains one flash cache device and one or more capacity devices.

![
          vSAN OSA diagram](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/427b4bbf-6702-4a4f-a464-b4f3cdb95f98.cq5dam.web.1280.1280.jpeg)

Depending on your requirement, you can deploy vSAN in the following ways.

## vSAN ReadyNode

The vSAN ReadyNode is a preconfigured solution of the vSAN software provided by Broadcom partners, such as Cisco, Dell, HPE, Fujitsu, IBM, and Supermicro. This solution includes validated server configuration in a tested, certified hardware form factor for vSAN deployment that is recommended by the server OEM and VMware. For information about the vSAN ReadyNode solution for a specific partner, visit the Broadcom Partner Portal at <https://partnerportal.broadcom.com/web/partner-portal>.

For more information on vSAN ReadyNode, see the Broadcom knowledge base article [326476](https://knowledge.broadcom.com/external/article/326476/what-you-can-and-cannot-change-in-a-vsan.html).

## User-Defined vSAN Cluster

You can build a vSAN cluster by selecting individual software and hardware components, such as drivers, firmware, and storage I/O controllers that are listed in the Broadcom Compatibility Guide at [https://compatibilityguide.broadcom.com/](http://www.vmware.com/resources/compatibility/search.php). You can choose any servers, storage I/O controllers, capacity and flash cache devices, memory, any number of cores you must have per CPU, that are certified and listed on the Broadcom Compatibility Guide. Review the compatibility information on the Broadcom Compatibility Guide before choosing software and hardware components, drivers, firmware, and storage I/O controllers that vSAN supports. When designing a vSAN cluster, use only devices, firmware, and drivers that are listed on the Broadcom Compatibility Guide. Using software and hardware versions that are not listed in the Broadcom Compatibility Guide might cause cluster failure or unexpected data loss. For information about designing a vSAN cluster, see [Designing and Sizing a vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster.html). For vSAN ESA requirements, see [vSAN ESA ReadyNode Hardware Guidance](https://partnerweb.vmware.com/comp_guide2/vsanesa_profile.php).