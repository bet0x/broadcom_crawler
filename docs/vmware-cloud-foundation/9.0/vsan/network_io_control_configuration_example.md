---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/network-i-o-control/nioc-configuration-example.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Network I/O Control Configuration Example
---

# Network I/O Control Configuration Example

You can configure Network I/O Control for a vSAN cluster.

Consider a vSAN cluster with a single 10 GbE physical adapter. This NIC handles traffic for vSAN, vSphere vMotion, and VMs. To change the shares value for a traffic type, select that traffic type from the System Traffic view (VDS > Configure > Resource Allocation > System Traffic), and click Edit. The shares value for vSAN traffic has been changed from the default of Normal/50 to High/100.

Edit the other traffic types to match the share values shown in the table.

Sample NIOC Settings



|  |  |  |
| --- | --- | --- |
| Traffic Type | Shares | Value |
| vSAN | High | 100 |
| vSphere vMotion | Low | 25 |
| Virtual machine | Normal | 50 |
| iSCSI/NFS | Low | 25 |

For example. if a 10GbE adapter is saturated, Network I/O Control allocates 5 GbEs to vSAN on the physical adapter, 3.5 GbEs to virtual machine traffic, and 1.5 GbEs to vMotion. Use these values as a starting point to configure NIOC configuration on your vSAN network. Ensure that vSAN has the highest priority of any protocol.

For more details about the various parameters for bandwidth allocation, see the [vSphere Networking](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-networking.html) guide.

With each of the vSphere editions for vSAN, VMware provides a vSphere Distributed Switch as part of the edition. Network I/O Control can be configured with any vSAN edition.