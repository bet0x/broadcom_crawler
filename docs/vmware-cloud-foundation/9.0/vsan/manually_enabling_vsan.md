---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/enabling-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Manually Enabling vSAN
---

# Manually Enabling vSAN

To create a vSAN cluster, you create a vSphere host cluster and enable vSAN on the cluster.

A vSAN cluster can include hosts with capacity and hosts without capacity. Follow these guidelines when you create a vSAN cluster.

- A vSAN cluster must include a minimum of three ESX hosts. For a vSAN cluster to tolerate host and device failures, at least three hosts that join the vSAN cluster must contribute capacity to the cluster. For best results, consider adding four or more hosts contributing capacity to the cluster.
- Only ESX hosts can join the vSAN cluster.
- Before you move a host from a vSAN cluster to another cluster, make sure that the destination cluster is vSAN enabled.
- To be able to access the vSAN datastore, an ESX host must be a member of the vSAN cluster.

After you enable vSAN, the vSAN storage provider is automatically registered with vCenter and the vSAN datastore is created. For information about storage providers, see the [vSphere Storage](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-storage.html) guide.