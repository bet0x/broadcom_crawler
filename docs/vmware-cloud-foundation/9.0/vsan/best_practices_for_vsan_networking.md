---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/designing-the-virtual-san-network/best-practices-for-virtual-san-networking.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Best Practices for vSAN Networking
---

# Best Practices for vSAN Networking

Consider networking best practices for vSAN to improve performance and throughput.

- vSAN OSA: For hybrid configurations, dedicate at least 1 GbE physical network adapter. Place vSAN traffic on a dedicated or shared 10 GbE physical adapter for best networking performance. For all-flash configurations, use a dedicated or shared 10 GbE physical network adapter.
- vSAN ESA: Use a dedicated or shared 25 GbE physical network adapter or higher
- Provision one additional physical NIC as a failover NIC.
- If you use a shared network adapter, place the vSAN traffic on a distributed switch and configure Network I/O Control to guarantee bandwidth to vSAN.