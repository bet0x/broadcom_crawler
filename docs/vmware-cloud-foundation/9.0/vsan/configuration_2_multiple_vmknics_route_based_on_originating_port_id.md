---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/advanced-nic-teaming/nic-teaming-configuration-examples/configuration-2-multiple-vmknics-route-based-on-originating-port-id.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Configuration 2: Multiple vmknics, Route Based on Originating Port ID
---

# Configuration 2: Multiple vmknics, Route Based on Originating Port ID

You can use two non-routable VLANs that are logically and physically separated, to produce an air-gap topology.

This example provides configuration steps for a vSphere distributed switch, but you also can use vSphere standard switches. It uses two 10 GbE physical NICs and logically separates them on the vSphere networking layer.

Create two distributed port groups for each vSAN VMkernel vmknic. Each port group has a separate VLAN tag. For vSAN VMkernel configuration, two IP addresses on both VLANs are required for vSAN traffic.

Practical implementations typically use four physical uplinks for full redundancy.

For each port group, the teaming and failover policy use the default settings.

- Load balancing set to Route based on originating port ID
- Network failure detection set to Link Status Only
- Notify Switches set to the default value of Yes
- Failback set to the default value of Yes
- The uplink configuration has one uplink in the Active position and one uplink in the Unused position.

One network is completely isolated from the other network.

## vSAN Port Group 1

This example uses a distributed port group called vSAN-DPortGroup-1. VLAN 3266 is tagged for this port group with the following Teaming and Failover policy:

- Traffic on the port group tagged with VLAN 3266
- Load balancing set to Route based on originating port ID
- Network failure detection set to Link Status Only
- Notify Switches set to default value of Yes
- Failback set to default value of Yes
- The uplink configuration has Uplink 1 in the Active position and Uplink 2 in the Unused position.

## vSAN Port Group 2

To complement vSAN port group 1, configure a second distributed port group called vSAN-portgroup-2, with the following differences:

- Traffic on the port group tagged with VLAN 3265
- The uplink configuration has Uplink 2 in the Active position and Uplink 1 in the Unusedposition.

## vSAN VMkernel Port Configuration

Create two vSAN VMkernel interfaces and on both port groups. In this example, the port groups are named vmk1 and vmk2.

- vmk1 is associated with VLAN 3266 (172.40.0.xx), and as a result port group vSAN-DPortGroup-1.
- vmk2 is associated with VLAN 3265 (192.60.0.xx), and as a result port group vSAN-DPortGroup-2.

## Load Balancing

vSAN has no load balancing mechanism to differentiate between multiple vmknics, so the vSAN I/O path chosen is not deterministic across physical NICs. The vSphere performance charts show that one physical NIC is often more utilized than the other. A simple I/O test performed in our labs, using 120 VMs with a 70:30 read/write ratio with a 64K block size on a four-host all flash vSAN cluster, revealed an unbalanced load across NICs.

vSphere performance graphs show an unbalanced load across NICs.

## Network Uplink Redundancy Lost

Consider a network failure introduced in this configuration. vmnic1 is not enabled on a given vSAN host. As a result, port vmk2 is impacted. A failing NIC triggers both network connectivity alarms and redundancy alarms.

For vSAN, this failover process triggers approximately 10 seconds after CMMDS (Cluster Monitoring, Membership, and Directory Services) detects a failure. During failover and recovery, vSAN stops any active connections on the failed network, and attempts to re-establish connections on the remaining functional network.

Since two separate vSAN VMkernel ports communicate on isolated VLANs, vSAN health check failures might be triggered. This is expected as vmk2 can no longer communicate to its peers on VLAN 3265.

The performance charts show that the affected workload has restarted on vmnic0, since vmnic1 has a failure. This test illustrates an important distinction between vSphere NIC teaming and this topology. vSAN attempts to re-establish or restart connections on the remaining network.

However, in some failure scenarios, recovering the impacted connections might require up to 90 seconds to complete, due to ESX TCP connection timeout. Subsequent connection attempts might fail, but connection attempts time out at 5 seconds, and the attempts rotate through all possible IP addresses. This behavior might affect virtual machine guest I/O. As a result, application and virtual machine I/O might have to be retried.

For example, on Windows Server 2012 VMs, Event IDs 153 (device reset) and 129 (retry events) might be logged during the failover and recovery process. In the example, event ID 129 was logging for approximately 90 seconds until the I/O was recovered.

You might have to modify disk timeout settings of some guest OSes to ensure that they are not severely impacted. Disk timeout values might vary, depending on the presence of VMware Tools, and the specific guest OS type and version.

## Recovery and Failback

When the network is repaired, workloads are not automatically rebalanced unless another failure to force workload occurs, due to another failure. As soon as the impacted network is recovered, it becomes available for new TCP connections.