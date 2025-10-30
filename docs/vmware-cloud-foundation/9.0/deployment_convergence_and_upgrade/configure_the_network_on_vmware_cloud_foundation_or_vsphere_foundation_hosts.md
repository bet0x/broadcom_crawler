---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation/configure-the-network-on-vmware-cloud-foundation-hosts.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Configure the Network on VMware Cloud Foundation or vSphere Foundation Hosts
---

# Configure the Network on VMware Cloud Foundation or vSphere Foundation Hosts

Use the ESX Direct Console User Interface (DCUI) for host network configuration and administrative access.

Perform the following tasks to configure the host network settings:

- Configure the network adapter (vmk0) and VLAN ID for the Management Network.
- Configure the IP address, subnet mask, gateway, DNS server, and FQDN for the ESX host.

Repeat this procedure for all hosts that you are adding to your VCF or VMware vSphere Foundation platform. If you completed the Planning and Preparation Workbook, refer to it for the required values.

1. Open the DCUI of the ESX host.
   1. Open a console window to the host.
   2. Press F2 to enter the DCUI.
   3. Log in using the esx\_root\_user\_password.
2. Configure the network.
   1. Select Configure Management Network and press Enter.
   2. Select VLAN (Optional) and press Enter.
   3. Enter the VLAN ID for the ESX Management Network and press Enter.
   4. Select IPv4 Configuration and press Enter.
   5. Select Set static IPv4 address and network configuration and press the Space bar.
   6. Enter the IPv4 Address, Subnet Mask and Default Gateway and press Enter.
   7. Select DNS Configuration and press Enter.
   8. Select Use the following DNS Server address and hostname and press the Space bar.
   9. Enter the Primary DNS Server, Alternate DNS Server and Hostname (FQDN) and press Enter.
   10. Select Custom DNS Suffixes and press Enter.
   11. Ensure that there are no suffixes listed and press Enter.
3. Press Escape to exit and press Y to confirm the changes.
4. Repeat this procedure for all remaining hosts.

[Configure the Virtual Machine Network Port Group on VMware Cloud Foundation or vSphere Foundation Hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation/configure-the-virtual-machine-network-port-group-on-vmware-cloud-foundation-hosts.html).