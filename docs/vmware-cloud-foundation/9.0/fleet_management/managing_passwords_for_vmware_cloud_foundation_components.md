---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Managing Passwords for VMware Cloud Foundation Components
---

# Managing Passwords for VMware Cloud Foundation Components

Manage passwords for VMware Cloud Foundation according to industry standards and the requirements of your organization. You can use the VCF Operations console to update and remediate the passwords for VMware Cloud Foundation components.

For additional information on account and password management, see [Account Management Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-information-security-and-access-design-for-esxi/service-account-design-for-vmware-cloud-foundation.html).

VMware Cloud Foundation offers the following password management actions:

| Action | Description | VCF Component UI |
| --- | --- | --- |
| Update | You use the Update action to provide a new password for an account and change that password on the server side (where the account resides) and on the client side (where the account is used). | VCF Operations |
| Remediate | You use the Remediate action to provide the new password on the client side (where the account is used) after the password is changed on the server side (where the account resides). | VCF Operations |
| Rotate | You use the Rotate action to change the password with an auto-generated password on both server (where the account resides) and client (where the account is used) sides. | SDDC Manager |

When you deploy VMware Cloud Foundation or VMware Cloud Foundation components you can choose to specify or auto-generate the initial passwords for each component. After deployment, you can use the VCF Operations console to update and remediate the passwords for the VCF Management components (which can manage multiple VCF instances) and for the components in a VCF Instance or a VCF domain.

| VCF Management Components | VCF Instance / Domain Components |
| --- | --- |
| - Fleet Management - VCF Automation - VCF Identity Broker - VCF Operations - VCF Operations for logs - VCF Operations for networks | - ESX - NSX Manager - vCenter - SDDC Manager (backup password only) |

Use the VCF Operations console to:

- View password alerts and information about the components whose passwords are managed by VMware Cloud Foundation.
- Update passwords.
- Remediate passwords.

By using the VCF Operations UI, you can updates and remediates the following VCF Components' local accounts:

| VCF Instance / Domain Components | Local Account |
| --- | --- |
| ESX | root |
| vCenter | root |
| SDDC Manager | backup |
| NSX | root |
| admin |
| audit |

| VCF Management Components | Local Account |
| --- | --- |
| VCF Operations | root |
| admin |
| VCF Operations fleet management | root |
| admin@local |
| VCF Operations for networks | consoleuser |
| support |
| admin@local |
| VCF Operations for networks collector | consoleuser |
| support |
| VCF Operations for logs | root |
| admin |
| VCF Automation | admin |
| VCF Identity Broker | vmware-system-user |

You can also use the [SDDC Manager API](https://developer.broadcom.com/xapis/sddc-manager-api/latest/credentials/) to look up and manage credentials.

Password expiration information and connection status in VCF Operations are updated once a day. To get real-time information, use the SDDC Manager API.