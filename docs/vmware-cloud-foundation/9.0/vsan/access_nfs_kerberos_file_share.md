---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service/access-vsan-file-shares/access-nfs-kerberos-file-share.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Access NFS Kerberos File Share
---

# Access NFS Kerberos File Share

A Linux client accessing an NFS Kerberos share should have a valid Kerberos ticket.

Sample NFSv4 commands for verifying the NFS Kerberos file share from a host client:

An NFS Kerberos share can be mounted using the following mount command:

```
[root@localhost ~]# mount -t nfs4 -o minorversion=1,sec=krb5/krb5i/krb5p <primary ip address>:/vsanfs/TestShare-0 /mnt/TestShare-0
[root@localhost ~]# cd /mnt/TestShare-0/
[root@localhost TestShare-0]# mkdir bar
[root@localhost TestShare-0]# touch foo
[root@localhost TestShare-0]# ls -l
total 0
drwxr-xr-x. 1 root root 0 Feb 19 18:35 bar
-rw-r--r--. 1 root root 0 Feb 19 18:35 foo
```

Changing Ownership of a NFS Kerberos share

You must log in using the AD domain user name for changing the ownership of a share. The AD domain user name provided in the file service configuration acts as a sudo user for the Kerberos file share.

```
[root@localhost ~]# mount -t nfs4 -o minorversion=1,sec=sys <primary ip address>:/vsanfs/TestShare-0 /mnt/TestShare-0
[fsadmin@localhost ~]# chown user1 /mnt/TestShare-0
[user1@localhost ~]# ls -l /mnt/TestShare-0
total 0
drwxr-xr-x. 1 user1 domain  users 0 Feb 19 18:35 bar
-rw-r--r--. 1 user1 domain users 0 Feb 19 18:35 foo
```