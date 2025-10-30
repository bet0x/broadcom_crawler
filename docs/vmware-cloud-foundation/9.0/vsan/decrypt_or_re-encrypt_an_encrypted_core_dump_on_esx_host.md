---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/vsan-encryption-and-core-dumps/decrypt-or-re-encrypt-an-encrypted-core-dump-on-esxi-host.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Decrypt or Re-Encrypt an Encrypted Core Dump on ESX Host
---

# Decrypt or Re-Encrypt an Encrypted Core Dump on ESX Host

You can decrypt or re-encrypt an encrypted core dump on your ESX host by using the crypto-util CLI.

The ESX host key that was used to encrypt the core dump must be available on the ESX host that generated the core dump.

You can decrypt and examine the core dumps in the vm-support package yourself. Core dumps might contain sensitive information. Follow your organization's security and privacy policy to protect sensitive information, such as host keys.

For details about re-encrypting a core dump and other features of crypto-util, see the command-line help.

crypto-util is for advanced users.

1. Log directly in to the ESX host on which the core dump occurred. 

   If the ESX host is in lockdown mode, or if SSH access is not enabled, you might have to enable access first.
2. Determine whether the core dump is encrypted.

   | Option | Description |
   | --- | --- |
   | Monitor core dump | ``` crypto-util envelope describe vmmcores.ve ``` |
   | zdump file | ``` crypto-util envelope describe --offset 4096 zdumpFile ``` |
3. Decrypt the core dump, depending on its type.

   | Option | Description |
   | --- | --- |
   | Monitor core dump | ``` crypto-util envelope extract vmmcores.ve vmmcores ``` |
   | zdump file | ``` crypto-util envelope extract --offset 4096 zdumpEncryptedzdumpUnencrypted ``` |