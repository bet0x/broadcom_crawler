---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Lifecycle Management of VCF Management Components
---

# Lifecycle Management of VCF Management Components

Use the VMware Cloud Foundation Operations fleet management appliance to manage, upgrade, patch, and install the following management components in VCF 9.0.

- VCF Operations
- VCF Operations for networks
- VCF Operations for logs
- VCF Automation
- VCF Identity Broker

When you update your VCF environment to a maintenance release version (x.y.z), you first update your management components that operate on the fleet level before you update the core components in your instances. For the management components, start with the VCF Operations fleet management appliance, followed by the VCF Operations instance and then proceed with the remaining components in your preferred order. For the core components, start with SDDC Manager, followed by NSX, vCenter, ESX hosts, and vSAN. See [Lifecycle Management of VCF Core Components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components.html).

Before you can upgrade, patch, or deploy the VCF management components, you must download the binaries to the VCF Operations fleet management appliance. The method that you use to download the binaries depends on how you access the internet in your environment.

- Online depot: The VCF Operations fleet management appliance connects directly to the online depot and requires a download token.
- Offline depot that is a self-managed web server: The VCF Operations fleet management appliance connect to the internet through a web server and requires a download token.
- Offline depot that is a local server: The VCF Operations fleet management appliance cannot connect to the internet but can connect to a computer with internet access. This depot is ideal for dark site environments.

After downloading binaries, you can proceed with your deployment, upgrade, or patch.

- For deployment, see: [Completing the Deployment of Your Platform](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform.html).
- For upgrading, see: [Import an Existing VMware Aria Automation Instance Into VCF Operations and Upgrade to VCF Automation 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/phase-3-import-and-upgrade-aria-automation-8-to-vcf-automation-9.html) or [Import an Existing VMware Aria Operations for Networks Instance Into VCF Operations and Upgrade to VCF Operations for Networks](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/phase-4-upgrade-additional-management-components-in-vcf-9.html), or [Upgrade an Individual VCF Management Component](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/upgrade-or-update-the-vcf-management-components-in-a-vcf-fleet/upgrade-a-vcf-management-component.html).
- For patching, see [Patch an Individual VCF Management Component](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/upgrade-or-update-the-vcf-management-components-in-a-vcf-fleet/update-a-vcf-management-component.html).