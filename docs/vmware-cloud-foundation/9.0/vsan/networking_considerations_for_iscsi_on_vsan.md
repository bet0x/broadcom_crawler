---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/networking-considerations-for-iscsi-on-vsan.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Networking Considerations for iSCSI on vSAN
---

# Networking Considerations for iSCSI on vSAN

vSAN iSCSI target service allows hosts and physical workloads
that reside outside the vSAN cluster to access the vSAN datastore. This feature enables an iSCSI initiator on a remote host to
transport block-level data to an iSCSI target on a storage device within the vSAN cluster.

The iSCSI targets on vSAN are managed using Storage Policy Based Management (SPBM) similar to
other vSAN objects. For the iSCSI LUNs, this space savings the
space through deduplication and compression, and provides security through encryption.
For enhanced security, vSAN iSCSI target service uses Challenge
Handshake Authentication Protocol (CHAP) and Mutual CHAP authentication.

vSAN identifies each
iSCSI target by a unique iSCSI qualified Name (IQN). The iSCSI target is presented to a
remote iSCSI initiator using the IQN, so that the initiator can access the LUN of the
target. vSAN iSCSI target service allows creating iSCSI
initiator groups. The iSCSI initiator group restricts access to only those initiators
that are members of the group.