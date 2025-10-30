---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation/configure-the-virtual-machine-network-port-group-on-vmware-cloud-foundation-hosts.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Configure the Virtual Machine Network Port Group on VMware Cloud Foundation or vSphere Foundation Hosts
---

# Configure the Virtual Machine Network Port Group on VMware Cloud Foundation or vSphere Foundation Hosts

Configure the Virtual Machine Network port group for each ESX host by using the VMware Host Client.

You configure the VLAN ID of the VM Network port group on the vSphere Standard Switch. This configuration provides connectivity to the Management network to allow communication during the automated deployment.

Repeat this procedure for all hosts that you are adding to your VCF or VMware vSphere Foundation environment. If you completed the Planning and Preparation Workbook, refer to it for the required values.

1. In a web browser, log in to the ESX host using the VMware Host Client.
2. Click OK to join the Customer Experience Improvement Program.
3. Configure a VLAN for the VM Network port group. 
   1. In the navigation pane, click Networking.
   2. Click the Port groups tab, select the VM network port group, and click Edit Settings.
   3. On the Edit port group - VM network page, enter the VM Management Network VLAN ID, and click Save.
4. Repeat this procedure for all remaining hosts.

[Configure NTP on VMware Cloud Foundation or vSphere Foundation Hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation/configure-ntp-on-vmware-cloud-foundation-hosts.html).