---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/preparing-esxi-hosts-as-transport-nodes/prepare-esxi-individual-hosts-as-transport-nodes/static-ip-list-assigned-to-vteps-during-transport-node-configuration.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Static IP List Assigned to VTEPs During Transport Node Configuration
---

# Static IP List Assigned to VTEPs During Transport Node Configuration

Static IP addresses are assigned to VTEPs during transport node configuration in the order they are entered in the static IP address list. Know the limitations and workaround when working with static IP list.

## How NSX assigns static IP addresses during transport node configuration

- During Transport Node creation, NSX will honor the static IP list order when assigning these IP addresses to VTEPs. For example, a Static IPv4 List ordered as 10.10.10.1, 10.10.10.2, 10.10.10.3, 10.10.10.4, will be assigned to VTEPs vmk1, vmk2, vmk3, vmk4 in the same order, 10.10.10.1 will be assigned to vmk1, 10.10.10.2 will be assigned to vmk2 and so on.
- During a Transport Node update, NSX will not honor static IP address order if the same list was already in use. Re-shuffling of the list elements will not lead to update in IP Addresses of existing VTEPs.
- During NSX or Transport Node upgrade, NSX will not honor static IP list order and existing VTEPs will remain as is.

## Scenario: Assign IP addresses to VTEPs in a specific order when a transport node is already created

If you want Transport Nodes to have VTEPs being assigned IP addresses in a specific order, when the Transport Node is already created, you can do any one of the following:

- Delete and Configure NSX again with the desired order of IP addresses in Static IPv4 List.
- Reconfigure Transport Node to change Uplink Profile assigned to Transport Node:

  1. Reconfigure the Transport Node to use an Uplink Profile with Teaming Policy as 'Failover Order', with the Static IPv4 List containing a new single IP address. Alternatively, use any Uplink Profile with Teaming Policy Load Balance Source, if it contains only one Active Uplink.
  2. Reconfigure Transport Node again to use the desired Uplink Profile with desired order of IP-addresses in Static IPv4 List. Use a new or a different Ip address that will not be used in the static IP list. This is to avoid re-use of IP-addresses and VTEPs from the intended Static IPv4 List.
- Reconfigure Transport Node to change IP Assignment Type to other options (DHCP, IP Pool v4 Pool), keeping all other parameters same. Then, reconfigure Transport Node again to use the desired Uplink Profile with desired order of IP-addresses in Static IPv4 List.