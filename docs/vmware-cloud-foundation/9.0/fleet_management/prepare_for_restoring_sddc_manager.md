---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/vcf-52-restore-sddc-manager/preparing-to-restore-sddc-manager.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Prepare for Restoring SDDC Manager
---

# Prepare for Restoring SDDC Manager

Before restoring SDDC Manager, you must download and decrypt the encrypted backup file from the SFTP server.

Verify that your host machine with access to the SDDC has OpenSSL installed.

The procedures have been written based on the host machine being a Linux-based operating system.

The backup file contains sensitive data about your SDDC Manager instance, including passwords in plain text. As a best practice, you must control access to the decrypted files and securely delete them after you complete the restore operation.

1. Identify the backup file for the restore and download it from the SFTP server to your host machine.
2. On your host machine, open a terminal and run the following command to extract the content of the backup file.

   ```
   OPENSSL_FIPS=1 openssl enc -d -aes-256-cbc -md sha256 -in filename-of-restore-file | tar -xz
   ```
3. When prompted, enter the encryption\_password.
4. In the extracted folder, locate and open the metadata.json file in a text editor.
5. Locate the sddc\_manager\_ova\_location value and copy the URL.
6. In a web browser, paste the URL and download the OVA file.
7. In the extracted folder, locate and view the contents of the security\_password\_vault.json file.
8. Locate the entityType BACKUP value and record the backup password.