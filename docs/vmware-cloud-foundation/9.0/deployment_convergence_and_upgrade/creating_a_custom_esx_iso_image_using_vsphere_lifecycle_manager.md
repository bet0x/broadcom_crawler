---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation/create-a-custom-esx-iso-image-using-vsphere-lifecycle-manager.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Creating a Custom ESX ISO Image Using vSphere Lifecycle Manager
---

# Creating a Custom ESX ISO Image Using vSphere Lifecycle Manager

If you have access to a vSphere environment, you can use vSphere Lifecycle Manager to create and export a custom ISO.

Import the ESX patch and vendor add-on (if applicable) zip files to the vSphere Lifecycle Manager depot. See [Import Updates to the vSphere Lifecycle Manager Depot](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/managing-host-and-cluster-lifecycle-8-0/working-with-vsphere-lifecycle-manager-depots/updating-the-vlcm-depot.html).

1. Log in to vCenter using the vSphere Client.
2. Create a new temporary cluster, selecting the Manage all hosts in the cluster with a single image check box.
3. Select the ESX version and vendor add-on (optional) and click OK.
4. Export the vSphere Lifecycle Manager image as an ISO. 

   See [Export an Image](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/managing-host-and-cluster-lifecycle-7-0/using-images-to-install-and-update-esxi-hosts-and-clusters/working-with-images/using-existing-images/export-an-image.html).
5. Delete the temporary cluster.