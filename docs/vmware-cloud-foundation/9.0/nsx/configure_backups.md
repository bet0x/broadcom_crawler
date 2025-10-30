---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/configure-backup-location.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure Backups
---

# Configure Backups

Before backups can occur, you must configure a backup file server. After you configure a backup file server, you can start a backup at any time or schedule recurring backups. Administrators can choose to connect to the SFTP backup server using an SSH private key or a password-based authentication.

- Verify that the SFTP server is running the supported OS and the supported SFTP software. The following table displays the supported and tested software for backup, although other software versions might work.

  | Currently supported OS | Specifically tested version | SFTP software version |
  | --- | --- | --- |
  | CentOS | 8.4 | OpenSSH\_8.0p1 |
  |  | 7.9 or 7.7 | OpenSSH\_7.4p1 |
  | RHEL | 8.4 | OpenSSH\_8.0p1 |
  |  | 7.9 or 7.7 | OpenSSH\_7.4p1 |
  | Ubuntu | 20.04 | OpenSSH\_8.2p1 |
  |  | 18.04 | OpenSSH\_7.6p1 |
  | Windows | Windows Server 2019 Standard | OpenSSH\_for\_Windows\_8.1p1 |
- Verify that the SFTP server is ready for use and is running SSH and SFTP, using the following commands:

  - $ ssh backup\_user@sftp\_server
  - $ sftp backup\_user@sftp\_server
- Verify the required hashed ECDSA host key is present on the backup server. See [Find the SSH Fingerprint of a Remote Server](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/find-the-ssh-fingerprint-of-a-server.html#GUID-d1cf8ef2-a6fb-40b4-b67c-71f98a51cd61-en).
- Ensure that the directory path where you want to store your backups exists and that you have read/write permissions to that directory.You cannot use the root directory (/).
- If you are using the SSH private key option, ensure:

  - The SFTP backup server configuration includes an SSH public key linked to one of the users (in ~/.ssh/authorized\_keys in a Linux server).
  - To complete the NSX Manager configuration, you have the corresponding private key.
  - You verify that you are storing the private key in a place other than the configuration.
- If you have multiple NSX deployments, you must use a different directory for storing the backup of each deployment.
- If your NSX Manager or your Global Manager appliance has the DNS server access set to "publish\_fqdns": true, you must configure that setting on the new NSX Manager or new Global Manager appliance before restore. Follow instructions at "Configuring NSX Manager for Access by the DNS Server" in the NSX Installation Guide.

1. From a browser, log in with admin privileges to the NSX Manager or Global Manager at https://<manager-ip-address>.
2. Select SystemBackup &
   Restore.
3. Click Edit under the SFTP Server label to configure your SFTP server.
4. Enter the FQDN or IP address of the backup file server.

   The protocol text box is already filled in. SFTP is the only supported protocol.
5. Change the default port if necessary. The default TCP port is 22.
6. In the Directory Path text box, enter the absolute directory path where the backups will be stored.

   The directory must already exist and cannot be the root directory (/). Avoid using path drive letters or spaces in directory names; they are not supported.If the backup file server is a Windows machine, you must use the forward slash when you specify the destination directory. For example, if the backup directory on the Windows machine is c:\SFTP\_Root\backup, specify /SFTP\_Root/backup as the destination directory.

   The path to the backup directory can contain only the following characters: alphanumerics ( a-z , A-Z, 0-9 ), underscore ( \_ ) , plus and minus sign ( + - ), tilde and percent sign ( ~ % ), forward slash ( / ), and period (.).

   The backup process generates a name for the backup file that can be quite long. On a Windows server, the length of the full path name of the backup file can exceed the limit set by Windows and cause backups to fail. To avoid this issue, see [Knowledge Base article 312385: NSX backups are failing on Windows backup server](https://knowledge.broadcom.com/external/article?articleNumber=312385).
7. Choose which authentication method you want to use to log into the backup file server.
   1. To enter a user name and password that authenticates to the backup file server, select Password and enter the required information.
   2. To use an SSH private key to send NSX backups to the SFTP server, select SSH Private Key and enter the required information.

   If you edit the backup configuration, you do not need to re-enter the password or SSH Private Key.
8. You can leave the SSH Fingerprint blank and accept or reject the fingerprint provided by the server after you click Save in a later step. If necessary, you can retrieve the SSH fingerprint by using this API: POST /api/v1/cluster/backups?action=retrieve\_ssh\_fingerprint.

   For more details, see [Find the SSH Fingerprint of a Remote Server](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/find-the-ssh-fingerprint-of-a-server.html#GUID-d1cf8ef2-a6fb-40b4-b67c-71f98a51cd61-en).
9. Verify that the required ECDSA host key is present on the backup server by running #ssh-keyscan -t ecdsa <backup server IP/FQDN>.

   ```
   #ssh-keyscan -t ecdsa ftpserver.corp.local
    #ftpserver.corp.local:22 SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.5
    ftpserver.corp.local ecdsa-sha2-nistp256
   ```

   Starting in 4.1, NSX supports the ECDSA cipher, TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_SHA384, in support of EAL4 compliance. Support also includes RSA for SSH private key generation using key sizes 1024-bits, 2048-bits, and 4096-bits. 4096-bits is recommended.If the command output does not return a supported ECDSA key or if the key is empty, then the configured backup server does not have the supported cipher ECDSA and you must update the configuration and generate new keys on the backup server. Contact the OS vendor if you need guidance for that configuration.
10. Enter a passphrase.

    You will need this passphrase to restore a backup. If you forget the passphrase, you cannot restore any backups.
11. Click Save.

The Backup and Restore page refreshes with the newly configured SFTP server updated.

After you successfully configure a backup file server, you can click Start Backup to manually start a backup immediately. Or, to schedule recurring automatic backups see [Start or Schedule Backups](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/configure-backup-location/start-or-schedule-backups.html#GUID-113ac642-95e9-47d8-b8ae-3b0a0b7f45e2-en). To see a list of available backups if you cannot access an NSX Manager or Global Manager appliance, see [Listing Available Backups](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/configure-backup-location/list-the-available-backups.html#GUID-22a69cad-cc4c-40c1-85c9-0c443100d9b9-en) for details.