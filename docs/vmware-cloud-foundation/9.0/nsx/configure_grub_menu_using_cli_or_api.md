---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-on-esxi-using-the-command-line-ovf-tool/configure-an-appliance-to-display-the-grub-menu-at-boot-time/configure-grub-menu-using-cli-or-api.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure GRUB Menu Using CLI or API
---

# Configure GRUB Menu Using CLI or API

You must configure an NSX appliance to display the GRUB menu at boot time if you want to reset the root password of the appliance.

You can use CLI or API commands to set the GRUB timeout value and password. You can follow these commands post deployment of NSX.

If the configuration is not performed after deploying the appliance and you forget the root password, resetting it is not possible.

1. Using CLI to set GRUB menu:
   1. Log in to the NSX command line interface.
   2. Run set grub menu timeout <value>.

      Where <value> is time in seconds. The default timeout value is 4.
   3. Run set grub user root password <newpassword>.

      OR
   4. Run set grub user root password

      Enter password:<newpassword>

      Confirm password:<newpassword>
2. Using API to set GRUB menu:
   1. Use the GET API to retrieve GRUB menu values.

      ```
      GET https://<nsx-mgr>/api/v1/node/grub

      Example Response:
      {
        "timeout": 4,
        "users": [
          {
            "username": "root"
          }
        ]
      }
      ```
   2. Set the GRUB timeout value.

      ```
      PUT https://<nsx-mgr>/api/v1/node/grub { "timeout": 4 }
      Example Response:
      {
        "timeout": 4
      }
      ```
   3. Set the GRUB menu password.

      ```
      PUT https://<nsx-mgr>/api/v1/node/grub/root { "password": "Str0ng_Pwd!Wins$" }
      Example Response:
      {
        "username": "root"
      }
      ```
3. Get GRUB timeout value.

   get grub menu timeout

   GRUB Menu Timeout = 4