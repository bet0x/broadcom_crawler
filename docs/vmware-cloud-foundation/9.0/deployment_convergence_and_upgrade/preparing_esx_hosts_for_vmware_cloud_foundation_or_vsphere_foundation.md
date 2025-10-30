---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Preparing ESX Hosts for VMware Cloud Foundation or vSphere Foundation
---

# Preparing ESX Hosts for VMware Cloud Foundation or vSphere Foundation

Before you can begin the process of deploying a new VMware Cloud Foundation or VMware vSphere Foundation platform, you must prepare the ESX hosts.

The number of required hosts depends on the type of storage and the deployment model that you plan to use. You can use the Planning and Preparation Workbook to determine the minimum number of ESX hosts required for your environment. See [Planning and Preparation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/planning-and-preparation.html).

Preparing the ESX hosts involves installing the correct version of ESX and performing some basic configuration tasks.

For the supported ESX version, see the VMware Cloud Foundation Release Notes.

If your environment requires a custom ISO file for ESX, you can create one using VMware PowerCLI or vSphere Lifecycle. See [Creating a Custom ESX ISO Image Using VMware PowerCLI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation/create-a-custom-esx-iso-image-using-vmware-powercli.html) and [Creating a Custom ESX ISO Image Using vSphere Lifecycle Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation/create-a-custom-esx-iso-image-using-vsphere-lifecycle-manager.html).

You might need to create a custom ISO image for ESX in the following situations:

- The ESX version specified in the VMware Cloud Foundation Release Notes does not have an associated ISO file on the Broadcom Support Portal. This can be the case for ESX patch releases.
- You need an async patch version of ESX.
- You need a vendor-specific (OEM) ISO file.

VMware Cloud Foundation does not support stateless ESX hosts.

With VMware Cloud Foundation 9.0.1 and later, you can use non-certified ESA disks during vSAN ESA cluster configuration for proof-of-concept purposes only. For more information, see kB [408300](http://knowledge.broadcom.com/external/article/408300).