---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-management-domain/shut-down.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Shut Down VCF Identity Broker
---

# Shut Down VCF Identity Broker

To gracefully power off the VCF Identity Broker, use the VCF Operations user interface.

After you stop VCF Identity Broker, you cannot use accounts from external identity providers. All subsecuential operations must be done by using local accounts.

1. Log in to VCF Operations at https://<vcf\_operations\_fqdn> as a user with the Administrator role.
2. Navigate to Fleet ManagementLifecycleVCF ManagementComponents.
3. In the Components tab, locate the component that you are starting or stopping and, in the Action column, click Manage.
4. On the component management page, click the ellipsis icon and select Power off.
5. Verify the information and click Submit.

   This operation takes several minutes to complete.