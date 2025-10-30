---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Installing an NSX Manager Cluster
---

# Installing an NSX Manager Cluster

As an administrator, your first task will be to install NSX in setting up your NSX environment.

NSX Manager is the application that you use to administer your NSX environment. You can use the NSX Manager UI, API or CLI to manage workloads and NSX Edge nodes. In a production environment, for fault tolerance, deploy a cluster of three NSX Manager nodes, each running on a separate ESX host.

NSX Manager can be deployed on an ESX host and this section covers the use of vSphere Client to deploy the NSX Manager virtual appliances OVA/OVF on an ESX host.

As an admin, your first task is to install NSX Manager as part of setting up your NSX environment.

Make sure that you have the supported vSphere version. See [vSphere support](http://partnerweb.vmware.com/comp_guide2/sim/interop_matrix.php#interop&175=&2=&1=).