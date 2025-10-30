---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Downloading Binaries to VCF Installer
---

# Downloading Binaries to VCF Installer

Before you can deploy VMware vSphere Foundation or VMware Cloud Foundation, you must download the required binaries to the VCF Installer appliance.

If the VCF Installer appliance can connect to the internet (either directly or through a proxy server), you can connect it to an online depot and download the binaries using a download token generated from the Broadcom Support Portal.

If the VCF Installer appliance cannot connect to the internet, you can connect it to an offline depot or use the VMware Cloud Foundation Download Tool.

VMware Cloud Foundation required binaries:

- VMware Cloud Foundation Automation
- VMware NSX
- VMware Cloud Foundation Operations
- VMware Cloud Foundation Operations fleet management
- VMware Cloud Foundation Operations collector
- VMware vCenter
- SDDC Manager

VMware vSphere Foundation required binaries:

- VMware Cloud Foundation Operations
- VMware vCenter

You do not need to download all of the binaries if you are reusing existing components. Even if you skip deployment of VCF Operations and VCF Automation in order to deploy them later with custom networking, you should still download the binaries, since they are required for the custom networking deployment.