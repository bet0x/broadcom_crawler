---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords/updating-sddc-manager-passwords/update-expired-sddc-manager-root-password.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Update an Expired SDDC Manager Root Password
---

# Update an Expired SDDC Manager Root Password

If the SDDC Manager root (root) user password expires, you must update the password using the vSphere Client.

1. In a web browser, log in to the management domain vCenter using the vSphere Client (https://<vcenter\_fqdn>/ui).
2. In the inventory, browse to and select the SDDC Manager virtual machine.
3. On the Summary tab, click Launch Remote Console.
4. Click within the console window and press Enter on the Login menu item.
5. Type root as the user name and enter the current password for the root user.
6. Type passwd root.
7. When prompted for a new password, enter a different password than the previous one and click Enter.