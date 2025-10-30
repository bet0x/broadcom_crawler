---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/migrating-from-standard-to-distributed-vswitch.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Migrating from Standard to Distributed vSwitch
---

# Migrating from Standard to Distributed vSwitch

You can migrate from a vSphere Standard Switch to a vSphere Distributed Switch, and use Network I/O Control. This enables you to prioritize the QoS (Quality of Service) on vSAN traffic.

It is best to have access to the ESX hosts, although you might not need it. If something goes wrong, you can access the console of the ESX hosts.

Make a note of the original vSwitch setup. In particular, note the load-balancing and NIC teaming settings on the source. Make sure the destination configuration matches the source.

## Create a Distributed Switch

Create the distributed vSwitch and give it a name.

1. In the vSphere Client Host and Clusters view, right-click a data center and select menu New Distributed Switch.
2. Enter a name.
3. Select the version of the vSphere Distributed Switch.
4. Add the settings. Determine how many uplinks you are currently using for networking. This example has six: management, vMotion, VMs, and three for vSAN (a LAG configuration). Enter 6 for the number of uplinks. Your environment might be different, but you can edit it later.

   You can create a default port group at this point, but additional port groups are needed.
5. Finish the configuration of the distributed vSwitch.

The next step is to configure and create the additional port groups.

## Create Port Groups

A single default port group was created for the management network. Edit this port group to make sure it has all the characteristics of the management port group on the standard vSwitch, such as VLAN and NIC teaming, and failover settings.

Configure the management port group.

1. In the vSphere Client Networking view, select the distributed port group, and click Edit.
2. For some port groups, you must change the VLAN. Since VLAN 51 is the management VLAN, tag the distributed port group accordingly.
3. Click OK.

Create distributed port groups for vMotion, virtual machine networking, and vSAN networking.

1. Right-click the vSphere Distributed Switch and select menu Distributed Port Group > New Distributed Port Group.
2. For this example, create a port group for the vMotion network.

Create all the distributed port groups on the distributed vSwitch. Then migrate the uplinks, VMkernel networking, and virtual machine networking to the distributed vSwitch and associated distributed port groups.

Migrate the uplinks and networks in step-by-step fashion to proceed smoothly and with caution.

## Migrate Management Network

Migrate the management network (vmk0) and its associated uplink (vmnic0) from the standard vSwitch to the distributed vSwitch (vDS).

1. Add hosts to the vDS.
   1. Right-click the vDS and select menu Add and Manage Hosts.
   2. Add hosts to the vDS. Click the green Add icon (+), and add all hosts from the cluster.
2. Configure the physical adapters and VMkernel adapters.
   1. Click Manage physical adapters to migrate the physical adapters and VMkernel adapters, vmnic0 and vmk0 to the vDS.
   2. Select an appropriate uplink on the vDS for physical adapter vmnic0. For this example, use Uplink1. The physical adapter is selected and an uplink is chosen.
3. Migrate the management network on vmk0 from the standard vSwitch to the distributed vSwitch. Perform these steps on each host.
   1. Select vmk0, and click Assign port group.
   2. Assign the distributed port group created for the management network earlier.
4. Finish the configuration.
   1. Review the changes to ensure that you are adding four hosts, four uplinks (vmnic0 from each host), and four VMkernel adapters (vmk0 from each host).
   2. Click Finish.

When you examine the networking configuration of each host, review the switch settings, with one uplink (vmnic0) and the vmk0 management port on each host.

Repeat this process for the other networks.

## Migrate vMotion

To migrate the vMotion network, use the same steps used for the management network.

Before you begin, ensure that the distributed port group for the vMotion network has the same attributes as the port group on the standard vSwitch. Then migrate the uplink used for vMotion (vmnic1), with the VMkernel adapter (vmk1).

## Migrate vSAN Network

If you have a single uplink for the vSAN network, then use the same process as before. However, if you are using more than one uplink, there are additional steps.

If the vSAN network is using Link Aggregation (LACP), or it is on a different VLAN to the other VMkernel networks, place some of the uplinks into an unused state for certain VMkernel adapters.

For example, VMkernel adapter vmk2 is used for vSAN. However, uplinks vmnic3, 4 and 5 are used for vSAN and they are in a LACP configuration. Therefore, for vmk2, all other vmnics (0, 1 and 2) must be placed in an unused state. Similarly, for the management adapter (vmk0) and vMotion adapter (vmk0), place the vSAN uplinks/vmnics in an unused state.

Modify the settings of the distributed port group and change the path policy and failover settings. On the Manage physical network adapter page, perform the steps for multiple adapters.

Assign the vSAN VMkernel adapter (vmk2) to the distributed port group for vSAN.

If you are only now migrating the uplinks for the vSAN network, you might not be able to change the distributed port group settings until after the migration. During this time, vSAN might have communication issues. After the migration, move to the distributed port group settings and make any policy changes and mark any uplinks to be unused. vSAN networking then returns to normal when this task is finished. Use the vSAN health service to verify that everything is functional.

## Migrate VM Network

The final task needed to migrate the network from a standard vSwitch to a distributed vSwitch is to migrate the VM network.

Manage host networking.

1. Right-click the vDS and choose menu Add and Manage Hosts.
2. Select all the hosts in the cluster, to migrate virtual machine networking for all hosts to the distributed vSwitch.

   Do not move any uplinks. However, if the VM networking on your hosts used a different uplink, then migrate the uplink from the standard vSwitch.
3. Select the VMs to migrate from a virtual machine network on the standard vSwitch to the virtual machine distributed port group on the distributed vSwitch. Click Assign port group, and select the distributed port group.
4. Review the changes and click Finish. In this example, you are moving to VMs. Any templates using the original standard vSwitch virtual machine network must be converted to VMs, and edited. The new distributed port group for VMs must be selected as the network. This step cannot be achieved through the migration wizard.

Since the standard vSwitch no longer has any uplinks or port groups, it can be safely removed.

This completes the migration from a vSphere Standard Switch to a vSphere Distributed Switch.