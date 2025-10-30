---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/configuring-ntp-on-appliances-and-transport-nodes.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configuring NTP on Appliances and Transport Nodes
---

# Configuring NTP on Appliances and Transport Nodes

Some features require that NTP be configured on all the components in the NSX environment.

It is highly recommended that you configure NTP for all components, regardless of the features you plan to use.

Change NTP time configuration in small increments. Do not change the time in a one large jump. If you change the time in a large increment, you must restart the appliance for correct functionality.

To configure NTP on an appliance, see [Configuring Appliances](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/configuring-appliances.html#GUID-950812da-4212-4437-91d3-4dfaeef1686e-en).

To configure NTP for all Manager and Edge nodes, see [Configure a Node Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/configure-a-node-profile.html#GUID-039fa17d-48f8-4fa6-9949-30ad93be4e9c-en).

To configure NTP for an ESX host, see the topic Synchronize ESX Clocks with a Network Time Server, in VSphere Security.

By default, different NTP services run in different Linux distributions. In all releases, run the timedatectl to view the synchronization status. Only one NTP service can be running at a time.

The following Linux distributions are supported with their default NTP services:

| Linux Server | NTP Client |
| --- | --- |
| RHEL/CentOS 7.6 | chronyd.service |
| RHEL/CentOS 7.7 | chronyd.service |
| RHEL/CentOS 8.0 | chronyd.service |
| RHEL/CentOS 8.2 | chronyd.service |
| Ubuntu 18.04 | systemd-timesyncd |
| Ubuntu 20.04 | systemd-timesyncd |
| SLES12 SP4 | systemd-timedated |