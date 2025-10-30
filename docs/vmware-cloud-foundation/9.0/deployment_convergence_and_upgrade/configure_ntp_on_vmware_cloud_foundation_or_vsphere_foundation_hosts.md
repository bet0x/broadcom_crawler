---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation/configure-ntp-on-vmware-cloud-foundation-hosts.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Configure NTP on VMware Cloud Foundation or vSphere Foundation Hosts
---

# Configure NTP on VMware Cloud Foundation or vSphere Foundation Hosts

Complete the initial configuration of all ESX hosts by configuring the NTP service to avoid time synchronization issues.

Repeat this procedure for all ESX hosts you are adding. If you completed the Planning and Preparation Workbook, refer to it for the required values.

1. In a web browser, log in to the ESX host using the VMware Host Client.
2. Configure and start the NTP service.
   1. In the navigation pane, click Manage, and click the System tab.
   2. Click Time & date and click Edit NTP Settings.
   3. On the Edit NTP Settings page, select the Use Network Time Protocol (enable NTP client) radio button, and change the NTP service startup policy to Start and stop with host.
   4. In the NTP servers text box, enter the NTP Server FQDN or IP Address, and click Save.
   5. Click the Services tab, select ntpd, and click Start.
3. Repeat this procedure for all remaining hosts.

[Regenerate the Self-Signed Certificate on ESX Hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation/regenerate-the-self-signed-certificate-on-esx-hosts.html).