---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/managing-vsphere-lifecycle-manager-images-for-vmware-cloud-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Managing vSphere Lifecycle Manager Images for VMware Cloud Foundation
---

# Managing vSphere Lifecycle Manager Images for VMware Cloud Foundation

VMware Cloud Foundation uses vSphere Lifecycle Manager images to apply software and firmware updates to the ESX hosts in an SDDC cluster.

You create vSphere Lifecycle Manager images in the vSphere Client and then import them into a VCF Instance using VCF Operations. You can use imported images when you:

- Upgrade the management domain or a workload domain.
- Create a workload domain.
- Add an SDDC cluster to the management domain or a workload domain.

You can create a composite image for a cluster that has hosts from different vendors or from the same vendor but different generations, family, or model. A composite image contains one default image and one or more alternative images. All images in a composite image contain the same base image and solutions, but may include different vendor or firmware and driver add-ons. When you create alternate images, you also specify the rules that are used to filter the hosts to which the alternative image is assigned.

For more information about vSphere Lifecycle Manager images, see [Managing Host and Cluster Lifecycle](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/managing-host-and-cluster-lifecycle.html) in the vSphere documentation.

If you are using an offline depot or no depot, you must use the VCF Download Tool to ensure that the latest ESX component data is available for creating vSphere Lifecycle Manager images in the vSphere Client.

- [Download ESX Component Data to an Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/managing-vsphere-lifecycle-manager-images-for-vmware-cloud-foundation/download-esx-component-data-to-an-offline-depot.html)
- [Download ESX Component Data Without an Online or Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/managing-vsphere-lifecycle-manager-images-for-vmware-cloud-foundation/download-esx-component-data-without-an-online-or-offline-depot.html)
- [Synchronize ESX Component Data for a VCF Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/managing-vsphere-lifecycle-manager-images-for-vmware-cloud-foundation/synchronize-esx-component-data-for-a-vcf-instance.html)