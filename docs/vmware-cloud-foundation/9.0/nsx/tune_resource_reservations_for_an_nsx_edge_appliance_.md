---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/managing-resource-reservations-for-an-edge-vm-appliance/tune-resource-reservations-for-an-nsx-edge-appliance.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Tune Resource Reservations for an NSX Edge Appliance 
---

# Tune Resource Reservations for an NSX Edge Appliance

You can tune resource reservations on an NSX Edge VM appliance. By default, 100% resources are allocated to an NSX Edge VM. Flexibility to change resource reservations avoids the need to add additional capacity to the vCenter and the need to reduce current reservations on other non-Edge VMs.

- Verify that the cluster has sufficient capacity to avoid failures.

1. With admin privileges, log in
   to NSX Manager.
2. Select SystemFabricNodesEdge Transport Nodes.
3. Select the NSX Edge transport node.
4. Click ActionsChange Edge VM Resource Reservations.
5. In the Change Edge VM Resource Reservations window, you can customize the existing resource allocation applied to the Edge transport node.

   Action | Description || CPU Reservation Priority | Low - 2000 shares Normal - 4000 shares  High - 8000 shares  Extra High - 10000 shares |
   | Memory Reservation (%) | Reservation percentage is relative to the pre-defined value in the form factor. 100 indicates 100% of memory is reserved for the NSX Edge VM. If you enter 50, it indicates that 50% of memory is assigned to the Edge transport node. |
   | CPU Reservation (MHz) | Enter CPU reservation in MHz.  The maximum amount of MHz is equal to the number of vCPUs multiplied by the normal CPU operation rate of the physical CPU core.  If the MHz value entered exceeds the maximum CPU capacity of the physical CPU cores, the NSX Edge VM might fail to start even though the allocation was accepted. |
6. Click Save.

   If changes made to the resource reservations do not take effect, you might need to reboot the NSX Edge VM from vCenter.

   The NSX Edge VM appliance autostarts on ESX host reboot provided the NSX Edge cluster has vSphere HA turned off. For more details on vSphere HA, see the vSphere documentation.