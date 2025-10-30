---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords/passwords-and-certificates-container/change-the-administrator-password.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Reset the VCF Operations Administrator Password from the Administration UI
---

# Reset the VCF Operations Administrator Password from the Administration UI

Passwords are used by users to access the product interfaces or to console sessions on cluster nodes. You might need to reset the VCF Operations administrator password as part of securing or maintaining your deployment and if you forget the admin account password.

1. In a Web browser, navigate to the VCF Operations administration interface at https://<master-node-name> or <master-node-ip-address>/admin.
2. Log in with the admin user name and password for the master node.
3. In the left pane, click Administrator Settings.
4. In the Change Administrator Password section, enter the current password, and enter the new password twice to ensure its accuracy. 

   You cannot change the administrator user name.
5. Click Save.
6. Optionally, to recover a forgotten password, configure the Password Recovery Settings. 

   Password Recovery Settings



   | Password Recovery Settings Options | Description |
   | --- | --- |
   | Your E-mail | Email id to which you want to receive the recovery email. |
   | SMTP Server | DNS name or IP address of the SMTP server that is used to send the password recovery email. |
   | Port | Port used for the communication. By default, 25 is used for a non-secure port and 465 for a secure port. |
   | SSL (SMTPS) | Activate to protect the communication using the secure socket layer. |
   | STARTTLS Encryption | Activate to switch the insecure communication starting with the TLS handshake. |
   | Sender E-mail | The email id from which the password recovery email is sent. |
   | User name | User name for the STMP server account, as some servers require authentication. |
   | Password | Password for the SMTP server account. |
   | Test | To verify the mandatory fields and make an attempt to communicate with the given SMTP server. |
7. Click Save. Optionally, click Reset to enter the details again.