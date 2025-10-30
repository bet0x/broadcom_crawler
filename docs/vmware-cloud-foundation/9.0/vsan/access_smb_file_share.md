---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service/access-vsan-file-shares/access-smb-file-share.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Access SMB File Share
---

# Access SMB File Share

You can access an SMB file share from a Windows client.

Ensure that the Windows client is joined to the Active Directory domain that is configured with vSAN file service.

1. Copy the SMB file share path using the following procedure:

   1. In the vSphere Client, navigate to the cluster.
   2. Click the Configure tab.
   3. Under vSAN, click File Service Shares.

      List of all the vSAN file shares appears.
   4. Select the SMB file share that you want to access from the Windows client.
   5. Click COPY PATH > SMB.

      The SMB file share path gets copied to your clipboard.
2. Log into the Windows client as a normal Active Directory domain user.
3. Access the SMB file share using path that you have copied. For example: \\vsan-file-server-dns-name\namespace\share-name.