---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/view-the-usage-and-capacity-of-categories-of-objects.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > View the Usage and Capacity of Categories of Objects
---

# View the Usage and Capacity of Categories of Objects

You can view the usage and capacity of different categories of objects. By default, an alarm is generated when the current inventory a category of objects reaches a certain level.

You can set thresholds for each object category. If a threshold is reached, an alarm will be generated. You can see alarms by navigating to HomeAlarms.

To see the usage and capacity of different categories of objects, click one of the following tabs:

- NetworkingNetwork OverviewCapacity
- SecuritySecurity OverviewCapacity
- InventoryInventory OverviewCapacity
- SystemSystem OverviewCapacity

You can also navigate to Plan & TroubleshootConsolidated Capacity to see all the object categories on one page.

## Capacity Information

On each capacity page, for each category of objects, the following information is displayed:

- Current Inventory - The number of objects that have been successfully created or configured. A color-coded bar is displayed to indicate the usage percentage. If usage is below the minimum capacity threshold, the color is green. If usage is at or above the minimum capacity threshold but below the maximum capacity threshold, the color is orange. If usage is at or above the maximum capacity threshold, the color is red.
- Maximum Capacity.
- Minimum Capacity Threshold - This is the usage level at which the usage bar mentioned above will show an orange color. You can change this value. The default is 70%.
- Maximum Capacity Threshold - This is the usage level at which the usage bar mentioned above will show a red color. You can change this value. The default is 100%.

If you change the minimum or maximum capacity threshold, you can click Revert to go back to the last saved value. You can click Reset Values to restore the default values for all the object categories.

## Object Categories

The networking capacity page shows the following object categories:

- Segments
- System-wide DHCP Ranges
- Tier-0 Gateways
- Tier-1 Gateways
- DHCP Server Instances
- System-wide NAT Rules
- Prefix Lists
- Tier-1 Gateways with NAT Enabled
- Segment Ports

The security capacity page shows the following object categories:

- Introspection Rules N-S Tier-1
- Service Chains
- Active Directory Groups (Identity Firewall)
- Saved Firewall Rules Configuration
- Introspection Policies E-W
- Introspection Policies N-S Tier-0
- System-wide Firewall Rules
- System-wide Endpoint Protection Enabled Virtual Machines
- Introspection Rules N-S Tier-0
- Introspection Rules E-W
- Distributed Firewall Sections
- Introspection Policies N-S Tier-1
- System-wide Firewall Sections
- Active Directory Domains (Identity Firewall)
- System-wide Endpoint Protection Enabled Hosts
- Distributed Firewall Rules
- Service Paths

The inventory capacity page shows the following object categories:

- Groups
- vSphere Clusters
- Services
- Hypervisor Hosts
- Groups based on IP Addresses

The system capacity page shows the following object categories:

- Compute Managers
- System-wide Edge Nodes
- Edge clusters