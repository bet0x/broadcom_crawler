---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/vsan-encryption-and-core-dumps/collect-a-vm-support-package-for-a-host-in-an-encrypted-vsan-datastore.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Collect a vm-support Package for an ESX Host in an Encrypted vSAN Datastore
---

# Collect a vm-support Package for an ESX Host in an Encrypted vSAN Datastore

If data-at-rest encryption is enabled on a vSAN cluster, any core dumps in the vm-support package are encrypted.

Inform your support representative that data-at-rest encryption is enabled for the vSAN datastore. Your support representative might ask you to decrypt core dumps to extract relevant information.

Core dumps can contain sensitive information. Follow your organization's security and privacy policy to protect sensitive information such as host keys.

You can collect the package, and you can specify a password if you expect to decrypt the core dump later. The vm-support package includes log files, core dump files, and more.

1. Log in to vCenter using the vSphere Client.
2. Click Hosts and Clusters, and right-click the ESX host.
3. Select Export System Logs.
4. In the dialog box, select Password for encrypted core dumps, and specify and confirm a password.
5. Leave the defaults for other options or make changes if requested by Broadcom Technical Support, and click Finish.
6. Specify a location for the file.
7. If your support representative asked you to decrypt the core dump in the vm-support package, log in to any ESX host and follow these steps. 
   1. Log in to the ESX and connect to the directory where the vm-support package is located. 

      The filename follows the pattern esx.date\_and\_time.tgz.
   2. Make sure that the directory has enough space for the package, the uncompressed package, and the recompressed package, or move the package.
   3. Extract the package to the local directory. 

      ```
      vm-support -x *.tgz .
      ```

      The resulting file hierarchy might contain core dump files for the ESX host, usually in /var/core, and might contain multiple core dump files for virtual machines.
   4. Decrypt each encrypted core dump file separately. 

      ```
      crypto-util envelope extract --offset 4096 --keyfile vm-support-incident-key-file 
      --password encryptedZdumpdecryptedZdump
      ```

      vm-support-incident-key-file is the incident key file that you find at the top level in the directory.

      encryptedZdump is the name of the encrypted core dump file.

      decryptedZdump is the name for the file that the command generates. Make the name similar to the encryptedZdump name.
   5. Provide the password that you specified when you created the vm-support package.
   6. Remove the encrypted core dumps, and compress the package again. 

      ```
      vm-support --reconstruct
      ```
8. Remove any files that contain confidential information.