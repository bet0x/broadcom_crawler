---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/managing-vsphere-lifecycle-manager-images-for-vmware-cloud-foundation/synchronize-esx-component-data-for-a-vcf-instance.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Synchronize ESX Component Data for a VCF Instance
---

# Synchronize ESX Component Data for a VCF Instance

vSphere Lifecycle Manager synchronizes to its download sources, including SDDC Manager, regularly and automatically, but you can also trigger synchronization at any time from VCF Operations.

To ensure that the most recent ESX component data is available for creating vSphere Lifecycle Manager images, you can update the contents of the vSphere Lifecycle Manager depot by synchronizing it with the SDDC Manager in a VCF Instance.

1. In VCF Operations, click Fleet ManagementLifecycle.
2. Click VCF Instances and click on the name of a VCF Instance.
3. Click Binary Management.
4. In the ESX Components section, click Synchronize Now.