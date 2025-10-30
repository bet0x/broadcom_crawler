---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/virtual-san-configuration-on-an-esxi-host-might-fail.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN Configuration on an ESX Host Might Fail
---

# vSAN Configuration on an ESX Host Might Fail

In certain circumstances, the task of configuring vSAN on a particular host might fail.

An ESX host that joins a vSAN cluster fails to have vSAN configured.

If a host does not meet hardware requirements or experiences other problems, vSAN might fail to configure the host. For example, insufficient memory on the host might prevent vSAN from being configured.

1. Place the host that causes the failure in Maintenance Mode.
2. Move the host out of the vSAN cluster.
3. Resolve the problem that prevents the host to have vSAN configured.
4. Move the host back into the vSAN cluster.
5. Exit Maintenance Mode.