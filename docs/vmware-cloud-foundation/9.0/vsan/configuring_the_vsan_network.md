---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/preparing-a-new-or-existing-cluster-for-virtual-san/configuring-virtual-san-networking.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Configuring the vSAN Network
---

# Configuring the vSAN Network

Before you enable vSAN on a cluster of ESX hosts, you must provide the necessary network infrastructure to carry vSAN communication.

vSAN provides a distributed storage solution, which implies exchanging data across the ESX hosts that participate in the cluster. Preparing the network for installing vSAN includes certain configuration aspects.

For information about network design guidelines, see [Designing the vSAN Network](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/designing-the-virtual-san-network.html#GUID-cbf63199-0e87-4e95-96da-6dc0f41afc69-en).

## Placing Hosts in the Same Subnet

Hosts must be connected in the same subnet for best networking performance. vSAN can also connect hosts in the same Layer 3 network if necessary.

## Dedicating Network Bandwidth on a Physical Adapter

Allocate at least 1 GbE bandwidth for vSAN. You might use one of the following configuration options:

- vSAN OSA: Dedicate 1 GbE physical adapters for a hybrid host configuration, or use dedicated or shared 10 GbE physical adapters if possible. Use dedicated or shared 10 GbE physical adapters for all-flash configurations.
- vSAN ESA: Support the use of dedicated or shared 10 GbE physical adapters. Use dedicated or shared 25 GbE physical adapters or higher is recommended.
- Direct vSAN traffic on a physical adapter that handles other system traffic and use vSphere Network I/O Control on a distributed switch to configure shares for vSAN.

## Configuring a Port Group on a Virtual Switch

Configure a port group on a virtual switch for vSAN.

- Assign the physical adapter for vSAN to the port group as an active uplink.

  When you need a NIC team for network availability, select a teaming algorithm based on the connection of the physical adapters to the switch.
- If designed, assign vSAN traffic to a VLAN by enabling tagging in the virtual switch.

## Examining the Firewall on a Host for vSAN

vSAN sends messages on certain ports on each host in the cluster. Verify that the host firewalls allow traffic on these ports.

When you enable vSAN on a cluster, all required ports are added to ESX firewall rules and configured automatically. There is no need for an administrator to open any firewall ports or enable any firewall services manually.

You can view open ports for incoming and outgoing connections. Select the ESX host, and click Configure > Security Profile.