---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service/access-vsan-file-shares/access-an-nfs-file-share.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Access NFS File Share
---

# Access NFS File Share

You can access a file share from a host client, using an operating system that communicates with NFS file systems. For RHEL-based Linux distributions, NFS 4.1 support is available in RHEL 7.3 and CentOS 7.3-1611 running kernel 3.10.0-514 or later. For Debian based Linux distributions, NFS 4.1 support is available in Linux kernel version 4.0.0 or later. All NFS clients must have unique hostnames for NFSv4.1 to work. You can use the Linux mount command with the Primary IP to mount a vSAN file share to the client. For example: mount -t nfs4 -o minorversion=1,sec=sys <primary ip>:/vsanfs/<share name>. NFSv3 support is available for RHEL-based and Debian based Linux distributions. You can use the Linux mount command to mount a vSAN file share to the client. For example: mount -t nfs vers=3 <nfsv3\_access\_point> <localmount\_point>.

Sample v41 commands for verifying the NFS file share from a host client:

```
[root@localhost ~]# mount -t nfs4 -o minorversion=1,sec=sys <primary ip address>:/vsanfs/TestShare-0 /mnt/TestShare-0
[root@localhost ~]# cd /mnt/TestShare-0/
[root@localhost TestShare-0]# mkdir bar
[root@localhost TestShare-0]# touch foo
[root@localhost TestShare-0]# ls -l
total 0
drwxr-xr-x. 1 root root 0 Feb 19 18:35 bar
-rw-r--r--. 1 root root 0 Feb 19 18:35 foo
```