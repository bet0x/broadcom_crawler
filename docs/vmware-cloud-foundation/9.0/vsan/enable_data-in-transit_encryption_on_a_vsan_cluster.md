---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-in-transit-encryption/enable-data-in-transit-encryption-on-a-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Enable Data-In-Transit Encryption on a vSAN Cluster
---

# Enable Data-In-Transit Encryption on a vSAN Cluster

You can enable data-in-transit encryption by editing the configuration parameters of a vSAN cluster.

1. In the vSphere Client, navigate to an existing cluster.
2. Click the Configure tab.
3. Under vSAN, select Services.
4. Click the Data-In-Transit Encryption Edit  button.
5. Click to enable Data-In-Transit encryption, and select a rekey interval.
6. Click Apply.

Encryption of data-in-transit is enabled on the vSAN cluster. vSAN encrypts all data moving across hosts and file service inter-host connections in the cluster.