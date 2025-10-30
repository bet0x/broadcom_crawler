---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vrealize-automation-8-x/configuring-vcf-automation-for-vm-apps-organization.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Configuring the Management Pack for VCF Automation for VM Apps Organization
---

# Configuring the Management Pack for VCF Automation for VM Apps Organization

If you have a VMware Cloud Foundation license, you can deploy VCF Automation for VM Apps Organization from the VCF Operations repository. This adapter works with a greenfield deployment of VMware Cloud Foundation 9.0 when you have already installed and configured the VMware Aria Automation 8.x Management Pack.

You must know the following details from from the steps you following in the VM Apps Organization Portal:

- Organization ID
- Credential name and the Refresh Token

For more information, see the topic, [Create a Service Account and Get a Refresh Token in VCF Automation for VM Apps](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/organization-management/vcfa-overview/getting-started-with-organizations-for-vm-apps-in-vcf-automation/administering-users-and-groups/learn-more-about-user-roles/create-a-service-account-and-get-a-refresh-token-in-vcf-automation-for-vm-apps.html).

If VMware Aria Automation 8.x Management Pack was already configured in Aria Operations, and you have upgraded to VMware Cloud Foundation 9.0, the management pack functions without requiring changes. This is provided that the VMware Aria Automation 8.x APIs remain compatible with VCF Automation 9.0 issued tokens and Cloud Services Platform APIs.

If you are deploying a new VMware Cloud Foundation 9.0 instance, and you previously had VMware Aria Automation 8.x Management Pack configured, then you must activate theVCF Automation for VM Apps Organization adapter.

1. From the left menu, click AdministrationIntegrations.
2. On the Repository tab, find the VCF Automation for VM Apps Organization tile.
3. Click the Activate button. Click Yes in the confirmation dialog box.
4. Fill the FQDN of the VCF Automation server. Enter the organization ID from the VM Apps Organization Portal in the VCF Automation Org ID field.
5. Set Auto Discovery to true.
6. Click the + button next in the Credential field. Select Tenant Scoped Service Account from the drop down, and enter the Credential Name and the Refresh Token.
7. From the Collectors/Groups drop-down menu, select the collector group.
8. Click Advanced Settings. From the User Count drop-down menu, select the number of user resources to be imported from VCF Automation. The User Count options are 20, 100, 200, 300, 400, and All Users.
9. Click OK.
10. Click the Add button to add the adapter instance to VCF Operations.