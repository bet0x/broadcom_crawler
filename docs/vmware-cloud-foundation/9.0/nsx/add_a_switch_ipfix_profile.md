---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/add-a-switch-ipfix-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Switch IPFIX Profile
---

# Add a Switch IPFIX Profile

You can configure IPFIX profiles for switches, also known as segments.

Flow-based network monitoring enable network administrators to gain insight into traffic traversing a network.

With vSphere Distributed Services Engine, some of the network operations can be offloaded from the server CPU to a Data Processing Unit (DPU also known as SmartNIC). vSphere 8.0 supports NVIDIA BlueField and AMD Pensando DPU devices only.

For more information about VMware vSphere Distributed Services Engine, see Introducing VMware vSphere® Distributed Services EngineTM and Networking Acceleration by Using DPUs in the VMware vSphere® product documentation.

If you want to configure IPFIX on DPU backed VDS, you must create vmknic on 'ops' TCP/IP stack. Else, the flow information is not exported to collector.

Starting with VCF9.0, switch IPFIX only supports UDP packets fragmentation and does not support fragmented packets of other supported protocols. So IPFIX will export the correct packets/bytes information for the UDP fragment packets, but for other protocol fragment packets IPFIX will skip these packets and export nothing.

1. With admin privileges, log in
   to NSX Manager.
2. Select Plan &
   TroubleshootIPFIX.
3. Click the Switch IPFIX Profiles tab.
4. Click Add Switch IPFIX Profile.
5. Enter the following details:

   | Setting | Description |
   | --- | --- |
   | Name and Description | Enter a name and optionally a description. If you want to create a global profile, name the profile global. A global profile cannot be edited or deleted from the UI, but you can do so using NSX APIs. When a GLOBAL profile is specified, UI does not allow binding of any Segment/Segment Port/Group to this profile. A global Switch IPFIX excludes all VMs on the service subnet of a VPC. |
   | Active Timeout (seconds) | The length of time after which a flow times out, even if more packets associated with the flow are received. Default is 300. |
   | Packet Sampling Probability (%) | An estimate of the percentage of packets that will be sampled. Increasing this setting can have a performance impact on the hypervisors and collectors. If all hypervisors are sending more IPFIX packets to the collector, the collector might not be able to collect all packets. Setting the probability at the default value of 0.1% decreases the performance impact. |
   | Collector Configuration | Select a collector from the drop-down menu. |
   | Applied To | Select a category: Segment, Segment Port, Groups, or Selected Count. The IPFIX profile applies to the selected object. |
   | Priority | This parameter resolves conflicts when multiple profiles apply. The IPFIX exporter uses the profile with the highest priority only. A lower value means a higher priority. |
   | Max Flows | The maximum flows cached on a bridge. Default is 16384. |
   | Observation Domain ID | The observation domain ID identifies which observation domain the network flows originate from. Enter 0 to indicate no specific observation domain. |
   | Tags | Enter a tag to make searching easier. |
6. Click Save and then Yes to continue configuring the profile.
7. Click Applied To to apply the profile to an NSGroup. You can select one or more NSGroups.

   IPFIX Profile supports NSGroups with member types: Other NSGroups, Segment, and Segment Port. To learn more about NSGroups, see [Add a Group](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/add-a-group.html).
8. Click Save.