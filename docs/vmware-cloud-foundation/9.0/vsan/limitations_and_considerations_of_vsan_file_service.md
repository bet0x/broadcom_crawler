---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service/limitations-and-considerations-of-vsan-file-service.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Limitations and Considerations of vSAN File Service
---

# Limitations and Considerations of vSAN File Service

Consider the following when configuring vSAN file service:

- vSAN supports two-node configurations and stretched clusters.
- vSAN supports 64 file servers in a 64 host setup.
- vSAN OSA cluster supports 100 file shares.
- vSAN supports file service on ESA.
- vSAN ESA cluster supports 500 file shares. Out of those 500 file shares, maximum 100 file shares can be SMB. For example, if you create 100 SMB file shares then the cluster can only support additional 400 NFS file shares.
- vSAN file service can connect only to a single network or port group.
- vSAN file services does not support the following:
  - Read-Only Domain Controllers (RODC) for joining domains because the RODC cannot create computer accounts. As a security best practice, a dedicated org unit should be pre-created in the Active Directory and the user name mentioned here should be controlling this organization.
  - Disjoint namespace. When the primary DNS suffix of a server within an Active Directory domain does not match the DNS name of the domain itself, it is referred to as disjoint namespace.
  - Multiple domains and Single Active Directory Forest environments.
- When a host enters maintenance mode, the file server moves to another FSVM. The FSVM on the host that entered maintenance mode is powered off. After the host exits maintenance mode, the FSVM is powered on.