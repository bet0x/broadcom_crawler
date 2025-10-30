---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vcf-automation-management-pack/deployment-scenarios-for-vcfa.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Considerations for Deploying the Management Pack for VCF Automation for All Apps Organization
---

# Considerations for Deploying the Management Pack for VCF Automation for All Apps Organization

The integration and upgrade is based on whether the VMware Aria Automation 8.x management pack was previously installed and whether VMware Cloud Foundation 9.0 is installed as a clean deployment or an upgraded environment.

## Deploying the VCF Automation 9.0 Management Pack in VMware Cloud Foundation 9.0

- VMware Cloud Foundation 9.0 must be a clean deployment and you should not have VMware Aria Automation 8.x management pack configured.
- VCF Automation for All Apps Organization
   adapter does not support upgraded installations.

If you have a VMware Cloud Foundation license, the VCF Automation for All Apps Organization adapter is automatically created after VCF Automation is installed. You can deploy VCF Automation in the following two ways:

- Using Fleet Manager. For more informaton, see [Deploying VCF Automation as a Day-N Operation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/install-vcf-automation-as-a-day-n-operation.html).
- Using the VCF Installer. For more information, see [Deploy Components by Using VCF Installer to Complete the Converging to VCF Process](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-/use-existing-vsphere-infrastructure-to-create-a-new-vcf-fleet-or-a-new-vcf-instance-using-the-deployment-wizard.html).