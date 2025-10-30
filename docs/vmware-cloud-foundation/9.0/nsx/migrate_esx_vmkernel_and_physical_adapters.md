---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/managing-transport-nodes/migrate-esx-vmkernel-and-physical-adapters.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Migrate ESX VMkernel and Physical Adapters
---

# Migrate ESX VMkernel and Physical Adapters

After preparing a host as a transport node, you can make changes to the current migration configuration of VMkernel adapters and physical adapters.

- Ensure that the host has at least one free physical adapter.
- Ensure that VMkernel adapters and port groups exist on the host.

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Go to SystemFabricHosts and select the Cluster tab.
3. Expand a cluster and select a host.
4. Click Actions > Migrate ESX VMkernel and Physical Adapters.
5. In the Migrate ESX VMkernel and Physical Adapters, enter the following details.

   | Field | Description |
   | --- | --- |
   | Direction | Make a selection: - Migrate to Logical Switches: To migrate VMkernel adapters from a VSS or VDS switch to an N-VDS switch in NSX. - Migrate to Port Groups: To migrate VMkernel adapters from an N-VDS switch to a VSS or VDS switch. |
   | Select Switch | Select the switch from which you want to migrate the VMkernel adapters and physical adapters. You can select from the available switches. |
   | Select VMkernel Adapters to Migrate | Click Add to enter the VMkernel adapter name and select destination as a logical switch or port group depending on where you want to migrate to. |
   | Edit Physical Adapters in N-VDS | Click Add to enter the physical adapter name and map it to an uplink on the host switch. |
6. Click Save to begin migration of VMkernel adapters and physical adapters.

The updated VMkernel adapters and physical adapters are migrated to the N-VDS switch or revert migrated to the VSS or VDS switch in the ESX host.