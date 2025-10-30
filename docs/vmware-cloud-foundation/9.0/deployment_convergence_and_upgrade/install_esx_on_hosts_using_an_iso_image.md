---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation/install-esx-on-hosts-using-the-iso.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Install ESX on Hosts Using an ISO Image
---

# Install ESX on Hosts Using an ISO Image

Install ESX on all hosts you plan to use in your VMware Cloud Foundation or VMware vSphere Foundation platform.

Download the ESX ISO from the Broadcom Support Portal. For the supported ESX versions, see the VMware Cloud Foundation Release Notes. If the required version of ESX does not have an ISO available on the Broadcom Support Portal, you can create one. See [Creating a Custom ESX ISO Image Using VMware PowerCLI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation/create-a-custom-esx-iso-image-using-vmware-powercli.html) or [Creating a Custom ESX ISO Image Using vSphere Lifecycle Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation/create-a-custom-esx-iso-image-using-vsphere-lifecycle-manager.html).

1. Mount the ESX ISO on the host and restart the machine.
2. Set the BIOS or UEFI to boot from the mounted ISO.
3. On the welcome screen, press Enter to continue.
4. Accept the End User License Agreement by pressing Enter.
5. On the Select a Disk to Install or Upgrade screen, select the drive on which to install ESX on and press Enter.
6. Select the keyboard type for the host. 

   You can change the keyboard type after installation in the direct console.
7. Enter the root password for the host.
8. In the Confirm Install screen, press F11 to confirm the start of the installation.
9. On the Installation Complete screen, press Enter to reboot the host.
10. Set the first boot device to be the drive on which you installed ESX.
11. Repeat this procedure for all remaining hosts.

[Configure the Network on VMware Cloud Foundation or vSphere Foundation Hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation/configure-the-network-on-vmware-cloud-foundation-hosts.html).