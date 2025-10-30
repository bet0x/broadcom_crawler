---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/nic-teaming-failover-and-load-balancing/basic-nic-teaming/configure-load-balancing-for-nic-teams.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Configure Load Balancing for NIC Teams
---

# Configure Load Balancing for NIC Teams

Several load-balancing techniques are available for NIC teaming, and each technique has its pros and cons.

## Route Based on Originating Virtual Port

In Active/Active or Active/Passive configurations, use Route based on originating virtual port for basic NIC teaming. When this policy is in effect, only one physical NIC is used per VMkernel port.

Pros

- This is the simplest NIC teaming method that requires minimal physical switch configuration.
- This method requires only a single port for vSAN traffic, which simplifies troubleshooting.

Cons

- A single VMkernel interface is limited to a single physical NIC's bandwidth. As typical vSAN environments use one VMkernel adapter, only one physical NIC in the team is used.

## Route Based on Physical NIC Load

Route Based on Physical NIC Load is based on Route Based on Originating Virtual Port, where the virtual switch monitors the actual load of the uplinks and takes steps to reduce load on overloaded uplinks. This load-balancing method is available only with a vSphere Distributed Switch, not on vSphere Standard Switches.

The distributed switch calculates uplinks for each VMkernel port by using the port ID and the number of uplinks in the NIC team. The distributed switch checks the uplinks every 30 seconds, and if the load exceeds 75 percent, the port ID of the VMkernel port with the highest I/O is moved to a different uplink.

Pros

- No physical switch configuration is required.
- Although vSAN has one VMkernel port, the same uplinks can be shared by other VMkernel ports or network services. vSAN can benefit by using different uplinks from other contending services, such as vMotion or management.

Cons

- As vSAN typically only has one VMkernel port configured, its effectiveness is limited.
- The ESX VMkernel reevaluates the traffic load after each time interval, which can result in processing overhead.

## Settings: Network Failure Detection

Use the default setting: Link status only. Do not use Beacon probing for link failure detection. Beacon probing requires at least three physical NICs to avoid split-brain scenarios. There can be a network traffic failover if the ESX host detects a link down event on an ESX host network interface. For more details, see Broadcom kbnowledge ase article [1005577](https://knowledge.broadcom.com/external/article?legacyId=1005577).

## Settings: Notify Switches

Use the default setting: Yes. Physical switches have MAC address forwarding tables to associate each MAC address with a physical switch port. When a frame comes in, the switch determines the destination MAC address in the table and decides the correct physical port.

If a NIC failover occurs, the ESX host must notify the network switches that something has changed, or the physical switch might continue to use the old information and send the frames to the wrong port.

When you set Notify Switches to Yes, if one physical NIC fails and traffic is rerouted to a different physical NIC in the team, the virtual switch sends notifications over the network to update the lookup tables on physical switches.

This setting does not catch VLAN misconfigurations, or uplink losses that occur further upstream in the network. The vSAN network partitions health check can detect these issues.

## Settings: Failback

This option determines how a physical adapter is returned to active duty after recovering from a failure. A failover event triggers the network traffic to move from one NIC to another. When a link up state is detected on the originating NIC, traffic automatically reverts to the original network adapter when Failback is set to Yes. When Failback is set to No, a manual failback is required.

Setting Failback to No can be useful in some situations. For example, after a physical switch port recovers from a failure, the port might be active but can take several seconds to begin forwarding traffic. Automatic Failback has been known to cause problems in certain environments that use the Spanning Tree Protocol. For more information about Spanning Tree Protocol (STP), see Broadcom knowledge base article [1003804](https://knowledge.broadcom.com/external/article?legacyId=1003804).

## Setting Failover Order

Failover order determines which links are active during normal operations, and which links are active in the event of a failover. Different supported configurations are possible for the vSAN network.

Active/Standby uplinks: If a failure occurs on an Active/Standby setup, the NIC driver notifies vSphere of a link down event on Uplink 1. The standby Uplink 2 becomes active, and traffic resumes on Uplink 2.

Active/Active uplinks: If you set the failover order to Active/Active, the virtual port used by vSAN traffic cannot use both physical ports at the same time.

If your NIC teaming configuration for both Uplink 1 and Uplink 2 is active, there is no need for the standby uplink to become active.

When using an Active/Active configuration, ensure that Failback is set to No. For more information, see Broadcom knowledge base article [2072928](https://knowledge.broadcom.com/external/article?legacyId=2072928).