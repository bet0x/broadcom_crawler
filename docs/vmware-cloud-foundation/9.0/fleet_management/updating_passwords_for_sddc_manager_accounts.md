---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords/updating-sddc-manager-passwords.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Updating Passwords for SDDC Manager Accounts
---

# Updating Passwords for SDDC Manager Accounts

The process for updating SDDC Manager passwords varies, depending on which account you are updating.

The following table lists the SDDC Manager user accounts and links to the procedures for how to update them.

| SDDC Manager Account | Update Procedure |
| --- | --- |
| backup | [Update Passwords for VMware Cloud Foundation Components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords/update-passwords.html) |
| vcf  root | [Update SDDC Manager Root and Super User Passwords](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords/updating-sddc-manager-passwords/update-sddc-manager-root-and-super-user-passwords.html) |
| admin@local | Use the PATCH /v1/users/local/admin API to update the local user password.  See [Update password for local account](https://developer.broadcom.com/xapis/vmware-cloud-foundation-api/latest/users/#_usecase_updatelocaluserpassword) for more information. |