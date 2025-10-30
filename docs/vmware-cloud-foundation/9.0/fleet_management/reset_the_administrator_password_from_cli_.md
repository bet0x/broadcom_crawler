---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords/passwords-and-certificates-container/reset-the-admin-password-vapp.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Reset the Administrator Password from CLI 
---

# Reset the VCF Operations Administrator Password from CLI

You must reset the password if the admin account password is lost.

This procedure requires root account credentials.

- In VCF Operations vApp deployments, when you log in to the console of the virtual application for the first time, you are forced to set a root password.
- The VCF Operations console root password can be different than the admin account password that you set when configuring the VCF Operations primary node.

When the VCF Operations password for the built-in admin account is lost, follow these steps to reset it on vApp clusters.

1. Log in to the master node command-line console as root.
2. Enter the following command, and follow the prompts. 

   $VMWARE\_PYTHON\_BIN $VCOPS\_BASE/../vmware-vcopssuite/utilities/sliceConfiguration/bin/vcopsSetAdminPassword.py --reset