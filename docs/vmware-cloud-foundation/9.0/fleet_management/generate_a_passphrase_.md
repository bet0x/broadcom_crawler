---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords/passwords-and-certificates-container/generate-a-passphrase.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Generate a Passphrase 
---

# Generate a VCF Operations Passphrase

When users need to add a node to the VCF Operations cluster, you can generate a temporary passphrase instead of giving them the primary administrator login credentials, which might be a security issue.

Create and configure the primary node.

A temporary passphrase is good for one use only.

1. In a Web browser, navigate to the VCF Operations administration interface at https://master-node-name-or-ip-address/admin.
2. Log in with the admin user name and password for the master node.
3. In the list of cluster nodes, select the master node.
4. From the toolbar above the list, click the option to generate a passphrase.
5. Enter a number of hours before the passphrase expires.
6. Click Generate. 

   A random alphanumeric string appears, which you can send to a user who needs to add a node.

Have the user supply the passphrase when adding a node.