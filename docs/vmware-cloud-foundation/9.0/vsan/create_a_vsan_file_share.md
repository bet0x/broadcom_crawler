---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service/create-a-vsan-file-share.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Create a vSAN File Share
---

# Create a vSAN File Share

When the vSAN file service is enabled, you can create one or more file shares on the vSAN datastore.

- If you are creating an SMB file share or a NFSv4.1 file share with Kerberos security, then ensure that you have configured vSAN file service to an Active Directory domain.
- Ensure that you have set Host.Config.Storage privilege.

Considerations for Share Name and Usage

- Usernames with non-ascii characters can be used to access share data.
- Share names cannot exceed 80 characters and can contain English characters, numbers, and hyphen character. Every hyphen character must be preceded and followed by a number or alphabet. Consecutive hyphens are not allowed.
- For SMB type shares, file and directories can contain any Unicode compatible strings.
- For pure NFSv4 type shares, the file and directories can contain any UTF-8 compatible strings. See [Network File System (NFS) Version 4 Protocol](https://datatracker.ietf.org/doc/html/rfc7530).
- For pure NFSv3 and NFSv3+NFSv4 shares file and directories can contain only ASCII compatible strings.
- Migrating any share data from older NFSv3 to new vSAN file service shares with NFSv4 only requires conversion of all file and directories names to UTF-8 encoding. There are third part tools to achieve the same.

vSAN file service does not support using NFS file shares on ESX .

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click File Shares.

   vSAN ESA cluster supports 500 file shares. Out of those 500 file shares, maximum 100 file shares can be SMB. For example, if you create 100 SMB file shares then the cluster can only support additional 400 NFS file shares.

   Each file server on a vSAN ESA cluster can support a maximum of 50 file shares and requires at least 10 IPs to have the maximum of 500 shares. With the increase in the file servers or file shares per host, there might be an impact on the performance of vSAN file service. For best performance, the number of IP addresses must to be equal to the number of hosts in the vSAN cluster.
4. Click Add.

   The Create file share wizard opens.
5. In the General page, enter the following information and click Next.

   - Name: Enter a name for the file share.
   - Protocol: Select an appropriate protocol. vSAN file service supports SMB and NFS file system protocols.

     If you select the SMB protocol, you can also configure the SMB file share to accept only the encrypted data using the Protocol encryption or Access based enumeration option. The access based enumeration displays only the files and folders that you have permissions to access. The files or folders are hidden if you do not have the Read (or equivalent) permissions. You can enable both protocol encryption and access based enumeration in a vSAN cluster.

     If you select the NFS protocol, you can configure the file share to support either NFS 3, NFS 4, or both NFS 3 and NFS 4 versions. If you select NFS 4 version, you can set either AUTH\_SYS or Kerberos security.

     SMB protocol and Kerberos security for NFS protocol can be configured only if the vSAN file service is configured with Active Directory. For more information, see [Configure vSAN File Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service/configure-vsan-file-service.html#GUID-1a2185d1-43c9-47f9-a87d-67ec224e82d8-en).
   - With SMB protocol, you can hide the files and folders that the share client user does not have permission to access using the Access based enumeration option.
   - Storage Policy: Select an appropriate storage policy.
   - Affinity site: This option is available if you are creating a file share on a vSAN stretched cluster. This option helps you place the file share on a file server that belongs to the site of your choice. Use this option when you prefer low latency while accessing the file share. The default value is Either, which indicates that the file share is placed on a site with less traffic on either preferred or secondary site.
   - Storage space quotas: You can set the following values:
     - Share warning threshold: When the share reaches this threshold, a warning message is displayed.
     - Share hard quota: When the share reaches this threshold, new block allocation is denied.
   - Labels: A label is a key-value pair that helps you organize file shares. You can attach labels to each file share and then filter them based on their labels. A label key is a string with 1~250 characters. A label value is a string and the length of the label value should be less than 1k characters. vSAN file service supports up to 5 labels per share.
6. The Net access control page, provides options to define access to the file share. Net access control options are available only for NFS shares. Select one of the following options and click Next.

   - No access: Select this option to make the file share inaccessible from any IP address.
   - Allow access from any IP: Select this option to make the file share accessible from all IP addresses.
   - Customize net access: Select this option to define permissions for specific IP addresses. Using this option you can specify whether a particular IP address can access, make changes, or only read the file share. You can also enable Root squash for each IP address. Root squash protects the NFS server from unauthorized root-level client access. You can enter the IP addresses in the following formats:

     - A single IP address. For example, 123.23.23.123
     - CIDR (Classless Inter-Domain Routing) notation by using a slash followed by a number, indicating how many bits of the IP address are dedicated to the network portion.
     - A range by specifying a starting IP address and ending IP address separated by a hyphen ( - ). For example, 123.23.23.123-123.23.23.128
     - Asterisk ( \* ) to imply all the clients.
7. In the Review page, review the settings, and then click Finish.

   A new file share is created on the vSAN datastore.