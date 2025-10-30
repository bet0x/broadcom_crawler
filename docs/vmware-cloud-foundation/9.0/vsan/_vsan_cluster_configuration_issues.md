---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/vsan-cluster-configuration-issues.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN Cluster Configuration Issues
---

# vSAN Cluster Configuration Issues

After you change the vSAN configuration, vCenter performs validation checks for vSAN configuration.

Error messages indicate that vCenter has detected a problem with vSAN configuration.

Validation checks are also performed as a part of a host synchronization process.

If vCenter detects any configuration problems, it displays error messages. Use the following methods to fix vSAN configuration problems.

vSAN Configuration Errors and Solutions



| vSAN Configuration Error | Solution |
| --- | --- |
| Host with the vSAN service enabled is not in the vCenter cluster | Add the host to the vSAN cluster. 1. Right-click the host, and select Move To. 2. Select the vSAN cluster and click OK. |
| Host is in a vSAN enabled cluster but does not have vSAN service enabled | Verify whether vSAN network is properly configured and enabled on the host. See [Configure a vSAN Cluster for Using the vSphere Client](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/enabling-virtual-san/configure-a-cluster-for-vsan-using-the-vsphere-client.html). |
| vSAN network is not configured | Configure vSAN network. See [Configuring the vSAN Network](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/preparing-a-new-or-existing-cluster-for-virtual-san/configuring-virtual-san-networking.html). |
| Host cannot communicate with all other nodes in the vSAN enabled cluster | Might be caused by network isolation. |
| Found another host participating in the vSAN service which is not a member of this host's vCenter cluster. | Make sure that the vSAN cluster configuration is correct and all ESX hosts are in the same vCenter inventory. |