---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/configure-an-edge-uplink-port-in-esxi.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure an NSX Edge Uplink Port in ESX
---

# Configure an NSX Edge Uplink Port in ESX

There are three options to configure uplink port changes on the ESX host that hosts the NSX autonomous Edge.

Consider performing this task if:

- Your east/west traffic between servers is timing out or works intermittently before timing out.
- The host kernel entry for migrated VMs are overwritten with the NSX Edge VM TEP address, instead of pointing to the correct TEP address of the ESX host hosting the VM.
- You are migrating from NSX-V to NSX
- Promiscuous mode is set to Accept on the virtual switch portgroup and the virtual machine guest OS places its vNIC in promiscuous mode.
- When running a packet capture within the VM, multicast and broadcast packets are received multiple times.
- The vSwitch is configured with NIC teaming and the load balancing policy is route based on originating port ID, route based on source MAC hash, use explicit failover order, or route based on physical NIC load.
- Multicast applications and protocols (such as CARP) running in virtual machines in promiscuous mode experience problems due to duplicated receive packets.

## Option 1: From the ESX host, configure the NSX Edges to use sink port mode and enable promiscuous mode on the trunk vNic using the CLI

This option configures the NSX Edge from the ESX host using the CLI.

1. SSH to the ESX host that hosts the autonomous NSX Edge.
2. To enable promiscuous mode when using a virtual switch to configure trunk interface and prevent the issues above, run the command:

   ```
   esxcli system settings advanced set -o
           /Net/ReversePathFwdCheckPromisc -i 1
   ```
3. To check that the setting is enabled, run the following command:

   ```
   esxcli system settings advanced list -o
           /Net/ReversePathFwdCheckPromisc
   ```

   ```
   Path: /Net/ReversePathFwdCheckPromisc
      Type: integer
      Int Value: 1
      Default Int Value: 0
      Min Value: 0
      Max Value: 1
      String Val ue:
      Default String Value:
      Valid Characters:
      Description: Block duplicate packet in a teamed environment when 
      the virtual switch is set to Promiscuous mode.
   ```

   This setting will discard packets coming from uplinks that are not associated with the particular client when promiscuous mode is enabled and will prevent duplicate packets from being received by the guest operating system. This will affect all promiscuous mode virtual machine and vmkernel interfaces on the ESX host.
4. In order for the setting to take effect, in the PortGroup security policy, set Promiscuous Mode from Accept to Reject and back to Accept to activate the configured change.

## Option 2: From the NSX Edge UI, change advanced settings for the NSX Edge host

This option configures the NSX Edge using the UI.

1. Log in to the ESX host UI.
2. Go to the ESX host advanced settings and change the Net.ReversePathFwdCheckPromisc value.
   1. Select ManageAdvanced Settings.
   2. Enter ReversePathFwdCheckPromisc in the search field in the upper right hand window corner.
   3. Select the key value in the table and click ActionsEdit option and enter 1 in the new window.

## Option 3: From the VMware vCenter server UI, change advanced settings for the ESX host

This option configures the ESX host using the vCenter UI.

1. Log in to the vCenter UI.
2. Go to the ESX host advanced settings and change the Net.ReversePathFwdCheckPromisc value.
   1. Select the ESX host from the management cluster, then ConfigureAdvanced System Settings.
   2. Select Net.ReversePathFwdCheckPromisc and click Edit and update the value to 1.

For example, the following image shows the vCenter interface with the Net.ReversePathFwdCheckPromisc value set to 1.![vCenter Advanced System Settings Net.ReversePathFwdCheckPromisc value set to 1](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/3e7c4f84-26eb-4b45-95e3-c806ad4936f4.original.png)