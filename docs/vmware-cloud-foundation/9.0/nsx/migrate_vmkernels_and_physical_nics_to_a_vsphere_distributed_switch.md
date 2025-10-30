---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/preparing-esxi-hosts-as-transport-nodes/migrate-vmkernels-and-physical-nics-to-a-vsphere-distributed-switch.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Migrate VMkernels and Physical NICs to a vSphere Distributed Switch
---

# Migrate VMkernels and Physical NICs to a vSphere Distributed Switch

Manually migrate VMkernel adapters from a vSphere Standard Switch or from an N-VDS switch to a vSphere Distributed Switch.

- ESX hosts are prepared as transport nodes using vSphere Distributed Switch.

Starting with NSX 3.0, transport nodes can be created using vSphere Distributed Switch.

After preparing the transport node with vSphere Distributed Switch host switch type (referred to as an NSX Switch in vCenter), manually migrate VMkernel adapters (vmks) and physical NICs (vmnics) to an NSX Switch on the ESX host.

In the procedure below, consider this switch configuration:

- vmk0, vmk1 are connected to vSwitch0, and vmnic0, vmnic1 are configured as uplink 1 and 2 respectively on the vSwitch0.
- NSX Switch does not have any vmnic or VMkernel adapter configured.

![Both vmk0 an vmk1 are connected to vSwitch and vmnic0 and vmnic1 are configured as uplink 1 and uplink 2 on vSwitch.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/56568429-91ea-4b9a-b1d3-a095d957f911.original.png)

![
            NSX switch does not have any vmnic or vmks configured on it.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8eeb0d6c-b4c7-41a8-aaf1-f676ea9df8b2.original.png)

At the end of the procedure, vmnic0, vmnic1 and vmk0, vmk1 are migrated to vSphere Distributed Switch (referred to as an NSX Switch in vCenter).

1. From a browser, log in with admin privileges to a vCenter at https://<vCenterServer-ip-address>.
2. Navigate to HostConfigureVirtual Switches.
3. View existing vmknics configured on vSwitch0.
4. Make a note of the vmknics to be migrated to the distributed virtual port group of the NSX Switch.
5. Navigate to HomeNetworking, to view all switches configured in the data center.
6. In the Switch page, click ActionsAdd and Manage Hosts.
7. Select Manage Host Networking.
8. Click Next.
9. In the Select Member Hosts window, select hosts.
10. Click Ok.
11. In the Manage physical adapters window, claim unassigned adapters, as there are available vmnics that can be attached to a switch.
    1. Select an unclaimed uplink and click Assign uplink.
    2. Map a vmnic to an uplink on the NSX Switch.
    3. Click Ok.
12. In the Manage VMkernel adapters window, assign port groups to NSX Switch.
    1. Select a vmk on vSwitch0 and click Assign port group.
    2. Select a NSX port group to assign a vmk to an NSX segment.
    3. Perform steps a and b for the remaining hosts that are managed by the switch.
13. Finish the Add and Manage Hosts wizard.
14. To verify vmk0 and pnics are migrated from vSwitch0 to NSX Switch on the ESX host, navigate toHostConfigureVirtual SwitchesVirtual Switches. View the updated switch configuration.
15. Alternatively, run the API command, https://<NSXManager-IP-address>/api/v1/logical-ports, to verify migration of VMkernel adapters is successful.

    All vmk0 ports are set to Unblocked VLAN state because management traffic and services are managed by vmk0 ports. These vmk0 ports in Unblocked VLAN state allows admins to connect to the vmk0 port if hosts lose connectivity.

Navigate to NSX Manager. In the SystemFabricHostsClusters tab, verify configuration status changed from Degraded to Success, as vmnics and vmks are migrated to the NSX Switch, the vSphere Distributed Switch.