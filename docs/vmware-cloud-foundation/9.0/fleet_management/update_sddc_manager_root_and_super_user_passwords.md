---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords/updating-sddc-manager-passwords/update-sddc-manager-root-and-super-user-passwords.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Update SDDC Manager Root and Super User Passwords
---

# Update SDDC Manager Root and Super User Passwords

For security reasons, you can change passwords for the SDDC Manager root (root) and super user (vcf) accounts. Changing these passwords periodically or when certain events occur, such as an administrator leaving your organization, reduces the likelihood of security vulnerabilities.

The SDDC Manager root password expires after 90 days. To update an expired root password, see [Update an Expired SDDC Manager Root Password](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords/updating-sddc-manager-passwords/update-expired-sddc-manager-root-password.html).

1. SSH in to the SDDC Manager appliance using the vcf user account.
2. Enter su to switch to the root user.
3. Enter one of the following commands:

   |  |  |
   | --- | --- |
   | passwd vcf | To change the super user password. |
   | passwd root | To change the root password. |
4. Enter and retype the new password. For example: 

   ```
   root@sddc-manager [ /home/vcf ]# passwd vcf
   New password:
   Retype new password:
   passwd: password updated successfully
   ```

The password is updated.