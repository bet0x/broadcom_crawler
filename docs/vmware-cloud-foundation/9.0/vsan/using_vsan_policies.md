---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-vsan-policies.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Using vSAN Policies
---

# Using vSAN Policies

When you use vSAN, you can define virtual machine storage requirements, such as performance and availability, in a policy.

In most cases, vSAN ensures that each virtual machine deployed to vSAN datastores is assigned at least one storage policy. After they are assigned, the storage policy requirements are pushed to the vSAN layer when a virtual machine is created. The virtual device is distributed across the vSAN datastore to meet the performance and availability requirements.

vSAN uses VASA storage provider to supply information about underlying storage to the vCenter. This information helps you to make appropriate decisions about virtual machine placement, and to monitor your storage environment.