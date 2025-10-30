---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/managing-proactive-hardware/associating-and-dissociating-hosts.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Associating and Dissociating ESX Hosts
---

# Associating and Dissociating ESX Hosts

After registering HSM with PHM, you need to associate appropriate ESX hosts available in the vCenter with the HSM.

This enables PHM on each host. HSM informs PHM on any change in the managed host list. PHM associates the managed ESX hosts available in a vSAN cluster. When a host is associated or dissociated with PHM, vCenter event gets generated. For detailed information about associating and dissociating ESX hosts, refer to the respective OEM-provided documentation.