---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/upgrading-the-vsan-cluster/about-the-virtual-san-disk-format.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > About the vSAN Disk Format
---

# About the vSAN Disk Format

After you complete your ESX update, upgrade the vSAN on-disk format to access the complete feature set of vSAN.

Each vSAN release supports the on-disk format of prior releases. All hosts in the cluster must have the same on-disk format version. Because some features are tied to the on-disk format version, it's best to upgrade the vSAN on-disk format to the highest version supported by the ESX version. For more information, refer to the Broadcom knowledge base article [2148493](https://knowledge.broadcom.com/external/article/327034).

vSAN on-disk format version 3 and higher require only a metadata upgrade that takes a few minutes. No disk evacuation or reconfiguration is performed during the on-disk format upgrade.

Before you upgrade the vSAN on-disk format, run the Pre-Check Upgrade to ensure a smooth upgrade. The pre-check identifies potential issues that might prevent a successful upgrade, such as failed disks or unhealthy objects.

Once you upgrade the on-disk format, you cannot roll back software on the hosts or add certain older hosts to the cluster.