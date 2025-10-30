---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/requirements-for-creating-a-virtual-san-cluster/cluster-requirements.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Cluster Requirements for vSAN
---

# Cluster Requirements for vSAN

Verify that a host cluster meets the requirements for enabling vSAN.

- All capacity devices, drivers, and firmware versions in your vSAN configuration must be certified and listed in the vSAN section of the Broadcom Compatibility Guide at: <https://compatibilityguide.broadcom.com/>.
- A standard vSAN cluster must contain a minimum of three ESX hosts that contribute capacity to the cluster. A two host vSAN cluster consists of two data hosts and an external witness host. For information about the considerations for a three-host cluster, see [Design Considerations for a vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/design-considerations-for-a-virtual-san-cluster.html#GUID-fa720212-3a46-4886-8e21-bbd278cfb596-en).
- An ESX host that resides in a vSAN cluster must not participate in other clusters.