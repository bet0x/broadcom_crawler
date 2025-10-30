---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/find-the-ssh-fingerprint-of-a-server.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Find the SSH Fingerprint of a Remote Server
---

# Find the SSH Fingerprint of a Remote Server

Some tasks that involve communication
with a remote server require that you provide the SSH fingerprint for the remote server. The
SSH fingerprint is derived from a host key on the remote server.

To
connect using SSH, the NSX Manager and the remote server must have a host key type in common.
Support includes key size 256-bit, 384-bit, and 521-bit. Ensure whatever key size is
used at time of backup is used at time of restore. The default
location of this key is /etc/ssh/ssh\_host\_ecdsa\_key.pub.

Having the fingerprint for a remote server helps you
confirm you are connecting to the correct server, protecting you from
man-in-the-middle attacks. You can ask the administrator of the remote server to
provide the SSH fingerprint of the server. Or you can connect to the remote server
to find the fingerprint. Connecting to the server over console is more secure than
over the network.

1. Log in to the remote
   server as root.

   Logging in using a
   console is more secure than over the network.
2. Verify the required hashed ECDSA
   host key is present on the backup server by running #ssh-keyscan -t
   ecdsa <backup server
   IP/FQDN>.

   ```
   #ssh-keyscan -t ecdsa ftpserver.corp.local
      #ftpserver.corp.local:22 SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.5
      ftpserver.corp.local ecdsa-sha2-nistp256
   ```

   If the command output does not return an ECDSA host key, you must configure
   the key on the backup server. Contact the OS vendor if you need guidance for
   that configuration.
3. Locate the ECDSA key. The default
   location of the key is
   /etc/ssh/ssh\_host\_ecdsa\_key.pub.

   ```
   $ ls -al /etc/ssh/*pub
   -rw-r--r-- 1 root root  93 Apr  8 18:10 ssh_host_ecdsa_key.pub
   -rw-r--r-- 1 root root 393 Apr  8 18:10 ssh_host_rsa_key.pub
   ```
4. Get the fingerprint of
   the key.

   ```
   ssh-keygen -lf /etc/ssh/ssh_host_ecdsa_key.pub | awk '{print $2}'
   ```