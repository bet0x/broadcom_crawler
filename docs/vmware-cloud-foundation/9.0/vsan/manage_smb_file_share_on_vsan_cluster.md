---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service/manage-smb-file-share-on-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Manage SMB File Share on vSAN Cluster
---

# Manage SMB File Share on vSAN Cluster

vSAN file service supports the shared folders snap-in for the Microsoft Management Console (MMC) for managing the SMB shares on the vSAN cluster.

You can perform the following tasks on vSAN file system SMB shares using the MMC tool:

- Manage Access Control List (ACL).
- Close open files.
- View active sessions.
- View open files.
- Close client connections.

1. Copy the MMC Command using the following procedure:

   1. In the vSphere Client, navigate to the cluster.

      Click the Configure tab.

      Under vSAN, click File Service Shares.

      List of all the vSAN file shares appears.
   2. Select the SMB file share that you want to manage from the Windows client using the MMC tool.
   3. Click COPY MMC COMMAND.

      The MMC command gets copied to your clipboard. For example: fsmgmt.msc /computer:\\vsan-file-service-dns-name.
2. Log into the Windows client as a file service admin user. The file service admin user is configured when you create the file service domain. A file service admin user has all the privileges on the file server.
3. In the search box on the taskbar, type Run, and then select Run.
4. In the Run box, run the MMC command that you have copied to access and manage the SMB share using the MMC tool.