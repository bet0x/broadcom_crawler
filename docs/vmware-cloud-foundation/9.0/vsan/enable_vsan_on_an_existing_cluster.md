---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/enabling-virtual-san/enable-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Enable vSAN on an Existing Cluster
---

# Enable vSAN on an Existing Cluster

You can enable vSAN on an existing cluster, and configure features and services.

- Verify that your environment meets all requirements. See [Requirements for Enabling vSAN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/requirements-for-creating-a-virtual-san-cluster.html).
- Ensure that the vSAN network on the existing vSAN cluster has a VMkernel NIC, configured with a static or DHCP IP address and the VMkernel port tagged with the vSAN traffic.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, select Services.
   1. Select a configuration type (vSAN HCI, Two node vSAN cluster, vSAN Stretched cluster, Compute Cluster, or vSAN Storage Cluster).
   2. Select I need local vSAN Datastore if you plan to add disk groups or storage pools to the cluster ESX hosts.
   3. Click Configure to open the Configure vSAN wizard.

      If the vSAN HCL configuration is compatible with the vSAN ESA cluster, vSAN ESA gets auto enabled.
4. Configure the vSAN services to use, and click Next.

   - Configure data management features, including deduplication and compression, data-at-rest encryption, data-in-transit encryption.
   - Select Remote Direct Memory Access (RDMA) if your network supports it. For more information, see [vSphere RDMA.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/ip-network-transport-configuration/vsphere-rdma.html)
   - Create and assign a default datastore policy for vSAN ESA. This auto-policy management allows best capacity utilization after the cluster configuration is complete.
5. Claim disks for the vSAN cluster, and click Next.

   - For vSAN ESA, if the disks are compatible, the auto-claim get enabled. vSAN can claim all the eligible disks and add additional hosts.
   - For vSAN OSA, each ESX host that contribute storage requires at least one flash device for cache, and one or more devices for capacity. For vSAN ESA, each ESX host that contributes storage requires one or more flash devices.
6. Create fault domains to groupESX hosts that can fail together.
7. Review the configuration, and click Finish.