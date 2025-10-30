---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/adding-and-removing-an-esxi-host-transport-node-to-and-from-vcenter-servers.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Adding and Removing an ESX Host Transport Node to and from vCenters
---

# Adding and Removing an ESX Host Transport Node to and from vCenters

You can move an ESX host transport node from one vCenter (VC) to another, and also from one NSX Manager cluster to another.

## Scenario 1: VC1 connected to NSX Manager cluster 1, and VC2 connected to NSX Manager cluster 2

Assuming ESX1, an ESX host transport node, is in VC1, you can move it to VC2 by performing the following steps:

1. Uninstall NSX from ESX1.
2. Move ESX1 to VC2.
3. Apply a transport node profile to ESX1.

## Scenario 2: Both VC1 and VC2 connected to NSX Manager cluster

Assuming ESX1, an ESX host transport node, is in VC1, you can move it to VC2 by performing the following steps:

1. Uninstall NSX from ESX1.
2. Move ESX1 to VC2.
3. Apply a transport node profile to ESX1.

## Scenario 3: VC1 connected to NSX Manager cluster 1

Assuming ESX1, an ESX host transport node, is in VC1, you can move it to NSX Manager cluster 2 as a standalone host by performing the following steps:

1. Uninstall NSX from ESX1.
2. Add ESX1 to NSX Manager cluster 2.

The user interface displays a warning, if at any point, your host transport node goes out of sync with the Management Plane. To initiate the resync operation, select ActionsSync Transport Node for your host transport node.