---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-in-transit-encryption.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN Data-In-Transit Encryption
---

# vSAN Data-In-Transit Encryption

vSAN can encrypt data-in-transit, as it moves across hosts in your vSAN cluster.

vSAN can encrypt data-in-transit across hosts in the cluster. When you enable data-in-transit encryption, vSAN encrypts all data and metadata traffic between hosts.

vSAN data-in-transit encryption has the following characteristics:

- vSAN uses AES-256 bit encryption on data-in-transit.
- vSAN data-in-transit encryption is not related to data-at-rest-encryption. You can enable or disable each one separately.
- Forward secrecy is enforced for vSAN data-in-transit encryption.
- Traffic between data hosts and witness hosts is encrypted.
- File service data traffic between the VDFS proxy and VDFS server is encrypted.
- vSAN file services inter-host connections are encrypted.

vSAN uses symmetric keys that are generated dynamically and shared between hosts. Hosts dynamically generate an encryption key when they establish a connection, and they use the key to encrypt all traffic between the hosts. You do not need a key management server to perform data-in-transit encryption.

Each host is authenticated when it joins the cluster, ensuring connections only to trusted hosts are allowed. When a host is removed from the cluster, its authentication certificate is removed.

vSAN data-in-transit encryption is a cluster-wide setting. When enabled, all data and metadata traffic is encrypted as it transits across hosts.