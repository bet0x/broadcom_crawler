---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords/rotate-passwords-for-vcf-components.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Rotate Passwords for VMware Cloud Foundation Components
---

# Rotate Passwords for VMware Cloud Foundation Components

Use SDDC Manager to rotate passwords for managed components or schedule automatic rotation on a recurring basis. During rotation, SDDC Manager generates a randomized password based on the component password policy and re-establishes respective component integrations.

Plan a maintenance window to avoid service interruptions if you are rotating passwords for multiple accounts.

ESX accounts can be rotated, but scheduled rotation is not supported.

SDDC Manager UI offers preset intervals for scheduled password rotation. Use the API to schedule password rotation for custom intervals.

1. Log in to SDDC Manager at https://sddc\_manager\_fqdn with a user assigned the Administrator role.
2. In the left pane, navigate to SecurityPassword management.
3. On the Password management page, select the account which password you want to change and click the Rotate password button.
4. In the Rotate password dialog box, click Rotate.