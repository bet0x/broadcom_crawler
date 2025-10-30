---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/add-an-edge-bridge-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add and attach NSX Edge Bridge Profile to a Segment
---

# Add and attach NSX Edge Bridge Profile to a Segment

The NSX Edge bridge profile specifies the primary NSX Edge node that will be the preferred node for the active bridge and backup node that will be preferred for the backup bridge.

- Verify that the NSX Edge cluster is available with minimum of two edge nodes (BareMetal or VM form factor).
- For the VM form factor NSX Edge, verify NSX Edge uplink VDS Trunk port group in vCenter has the following configuration:
  - Forged transmit
  - MAC learning (recommended) or promiscous mode/sink port configured
  - Active/Standby teaming policy.

Consider dedicating an NSX Edge uplink (vNIC) to bridged traffic so that other kinds of traffic to and from the NSX Edge do not suffer from the performance impact related to promiscuous mode.

- Verify NSX Edge TNs member of NSX Edge Cluster are attached to overlay as well as VLAN Transport Zone.

NSX Edge Bridge connects NSX overlay logical segment with a traditional VLAN at layer 2. The edge bridge leverages DPDK for high performance forwarding. The traffic bridged in or out of the NSX domain is subject to an edge bridge firewall instance. The NSX Edge bridge functionality is mainly for migration scenarios (physical to virtual or virtual to virtual) or for integration of physical, non-virtualized appliances to the virtualized environment.

Starting with NSX 2.5, the same segment can be attached to several bridges on different Edge Clusters and VLANs.

At the time of the creation of the Bridge Profile, no Bridge is instantiated yet. The Bridge Profile is just a template for the creation of one or several Bridge pairs. Once a Bridge Profile is created, you can attach a segment to it. By doing so, an active Bridge instance is created on the primary Edge, while a standby Bridge is provisioned on the backup Edge. NSX creates a Bridge Endpoint object, which represents this pair of Bridges. The attachment of the segment to the Bridge Endpoint is represented by a dedicated logical port.

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Select NetworkingSegmentsProfilesEdge Bridge ProfilesAdd Edge Bridge Profile.
3. Enter the NSX Edge cluster profile details. 

   Option | Description || Name and Description | Enter a NSX Edge bridge cluster profile name. You can optionally enter the profile details such as, the primary and backup node details. |
   | Edge Cluster | Select the NSX Edge cluster that you can to use. |
   | Primary Node | Designate the preferred NSX Edge node from the cluster. |
   | Backup Node | Designate the back up NSX Edge node if the primary node fails. |
   | Failover Mode | Select either Preemptive or Non-Preemptive mode.  The default HA mode is preemptive, which can slowdown traffic when the preferred NSX Edge node goes back online. The non-preemptive mode does not cause any traffic slowdown.  In the preemptive mode, the Bridge on the primary Edge will always become the active bridge forwarding traffic between overlay and VLAN as soon as it is available. In the non-preemptive mode, the Bridge on the primary Edge will remain standby if it becomes available when the Bridge on the backup Edge is already active. |
4. After you create a Bridge Profile, associate it to a segment.
5. Select NetworkingSegnmentsNSXAdd Segment.
6. Enter the required details, connect to overlay transport zone and click Save.
7. Edit the segment to which you want to add the Bridge Profile.
8. In the Additional Settings section, in the Edge Bridges field, select Set.
9. Click Add Edge Bridge.
10. Select the Edge Bridge Profile.
11. Select the Transport Zone where the bridged traffic is sent to the N-VDS selected by the transport zone.
12. Select the VLAN ID for the VLAN traffic as well as the physical port you select on the NSX Edge for sending or receiving this VLAN traffic.
13. (Optional) Select the teaming policy to decide how N-VDS balances traffic across its uplinks.
14. Click Add.
15. Click Save.

The newly created NSX Edge Bridge Profile is associated to a segment to balance VLAN traffic.

- Verify the configuration and state of L2 bridges on the NSX Edge.
  1. SSH to the NSX Edge as an admin.
  2. Run get bridge.
  3. Verify that the Device State is Up.