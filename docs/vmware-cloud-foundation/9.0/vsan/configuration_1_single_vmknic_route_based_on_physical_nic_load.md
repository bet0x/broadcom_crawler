---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/advanced-nic-teaming/nic-teaming-configuration-examples/configuration-1-single-vmknic-route-based-on-physical-nic-load.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Configuration 1: Single vmknic, Route Based on Physical NIC Load
---

# Configuration 1: Single vmknic, Route Based on Physical NIC Load

You can configure basic Active/Active NIC Teaming with the Route based on Physical NIC Load policy for vSAN hosts. Use a vSphere Distributed Switch (vDS).

For this example, the vDS must have two uplinks configured for each host. A distributed port group is designated for vSAN traffic and isolated to a specific VLAN. Jumbo frames are already enabled on the vDS with an MTU value of 9000.

Configure teaming and failover for the distributed port group for vSAN traffic as follows:

- Load balancing policy set to Route Based on Physical Nic Load.
- Network failure detection set to Link status only.
- Notify Switches set to Yes.
- Failback set to No. You can set Failback to yes, but not for this example.
- Ensure both uplinks are in the Active uplinks position.

## Network Uplink Redundancy Lost

When the link down state is detected, the workload switches from one uplink to another. There is no noticeable impact to the vSAN cluster and VM workload.

## Recovery and Failback

When you set Failback to No, traffic is not promoted back to the original vmnic. If Failback is set to Yes, traffic is promoted back to the original vmnic on recovery.

## Load Balancing

Since this is a single VMkernel NIC, there is no performance benefit to using Route based on physical load.

Only one physical NIC is in use at any time. The other physical NIC is idle.