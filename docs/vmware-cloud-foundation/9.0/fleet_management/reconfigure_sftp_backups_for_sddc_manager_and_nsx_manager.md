---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/reconfigure-sftp-backups-for-sddc-manager-and-nsx-manager.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Reconfigure SFTP Backups for SDDC Manager and NSX Manager
---

# Reconfigure SFTP Backups for SDDC Manager and NSX Manager

By default, SDDC Manager and NSX Manager backups are stored on the SDDC Manager appliance. Change the destination of the backups to an external SFTP server.

- The external SFTP server must support a 256-bit length ECDSA SSH public key.
- The external SFTP server must support a 2048-bit length RSA SSH public key
- You will need the SHA256 fingerprint of RSA key of the SFTP server.
- Host Key algorithms: At least one of rsa-sha2-512 or rsa-sha2-256 and one of ecdsa-sha2-nistp256, ecdsa-sha2-nistp384, or ecdsa-sha2-nistp521.
- Additional pre-requisites when FIPS Security Mode is enabled on SDDC Manager:

  | Algorithms and Ciphers | Required when FIPS Security Mode is Enabled |
  | --- | --- |
  | Kex Algorithms | At least one of: - diffie-hellman-group-exchange-sha256 - ecdh-sha2-nistp256 - ecdh-sha2-nistp384 - ecdh-sha2-nistp521 |
  | Message Authentication Key (MAC) Algorithms | hmac-sha2-256 |
  | Ciphers | At least one of: - TLS\_DHE\_DSS\_WITH\_AES\_128\_CBC\_SHA256 - TLS\_DHE\_DSS\_WITH\_AES\_256\_CBC\_SHA256 - TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA256 - TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384 - TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256 - TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA256 - TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA256 - TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384 - TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384 - TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256 - TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256 - TLS\_AES\_128\_GCM\_SHA256 - TLS\_AES\_256\_GCM\_SHA384 |

SHA1 algorithms are not supported.

1. Log in to the VCF Operations interface at https://<vcf\_operations\_fqdn> with a user assigned the Administrator role.
2. Navigate to AdministrationSDDC Manager.
3. Select the VCF Instance to configure backup.
4. In the right hand pane, click the Backup Settings tab and then click Site Settings.
5. On the Backup Settings page, enter the settings and click Save.

   | Setting | Value |
   | --- | --- |
   | Host FQDN or IP | The FQDN or IP Address of the SFTP server. |
   | Port | 22 |
   | Transfer Protocol | SFTP |
   | Username | A service account with privileges to the SFTP server.  For example: svc-vcf-bck. |
   | Password | The password for the username provided. |
   | Backup Directory | The directory on the SFTP server where backups are saved.  For example: /backups/. |
   | SSH Fingerprint | The SSH Fingerprint is automatically retrieved from the SFTP server, verify the SSH Fingerprint. |
   | Confirm Fingerprint | Selected |
   | Encryption Passphrase | The encryption passphrase used to encrypt the backup data.  The encryption passphrase should be stored safely as it is required during the restore process. |
6. In the Confirm your changes to backup settings dialog box, click Confirm.