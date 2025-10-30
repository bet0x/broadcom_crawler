---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/edge-bridging-extending-overlay-segments-to-vlan/configure-an-edge-vm-for-bridging.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure an Edge VM for Bridging
---

# Configure an Edge VM for Bridging

If you plan to run a bridge on an NSX Edge VM, use this section to understand the specific configuration to perform in the vSphere infrastructure.

As an example, our scenario includes two virtual machines, VM1 and VM2, on transport node ESX 1 attached to an overlay segment S. The VMs can communicate at layer 2 with the physical host on the right side of the diagram thanks to a bridge instantiated on the edge VM running on ESX host 2. The TEP (tunnel end point) on ESX 1 encapsulates the traffic from VM1/VM2 and forwards it to the TEP of the edge VM. Then the bridge unencapsulates the traffic and sends it tagged with VLAN ID 10 on its VLAN uplink. Then the traffic gets switched to the physical host. 

Edge VM Bridging

![Shows Edge VM connectivty using layer 2 bridging](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/aa575625-82fd-4015-8510-8270a9e2089d.original.png)

As you can see on the diagram, the VLAN uplink of the bridge is linked to port p, which is attached to distributed portgroup dvpg1. This port p is injecting into dvpg1 traffic with the source mac addresses mac1 and mac2 of virtual machined VM1 and VM2. Port p must also accept traffic with destination mac addresses mac1 and mac2, so that the physical host can reach VM1 and VM2. When a bridge is running on the edge VM, the port of this edge VM behaves in a non-standard way as far as the vSphere switching infrastructure is concerned. That means that dvpg1 will need some additional configuration to accommodate the edge VM. The following section lists the different options based on your environment.

## Option 1: Edge VM is on a VSS portgroup

This option is for when the Edge VM is connected to a VSS (vSphere Standard Switch). You must enable promiscuous mode and forged transmit.

- Set promiscuous mode on the portgroup.
- Allow forged transmit on the portgroup.
- Run the following command to enable reverse filter on the ESX host where the Edge VM is running:

  ```
  esxcli system settings advanced set -o /Net/ReversePathFwdCheckPromisc -i 1
  ```

  Then disable and enable promiscuous mode on the portgroup with the following steps:
  - Edit the portgroup's settings.
  - Disable promiscuous mode and save the settings.
  - Edit the portgroup's settings again.
  - Enable promiscuous mode and save the settings.
- Do not have other port groups in promiscuous mode on the same host sharing the same set of VLANs.
- Avoid running other VMs attached to the portgroup in promiscuous mode on the same host, as the traffic gets replicated to all those VMs and affect performance.

## Option 2a: Edge VM is on a VDS 6.6.0 (or later) portgroup

This option is for when the Edge VM is connected to a VDS (vSphere Distributed Switch). You must be running ESX 6.7 or later, and VDS 6.6.0 or later.

- Enable MAC learning with the option “allow unicast flooding” on the distributed portgroup.

  Starting with vSphere 8.0, you can enable the Mac Learning UI option in the distributed portgroup configuration. For previous releases, you need to use the VIM API DVSMacLearningPolicy and setting allowUnicastFlooding to true.

If the MAC learning feature is available for your release and VDS version, it is highly recommended over setting forged transmit and promiscuous mode.

The only exception is when all of the following conditions are met:

- You bridge a segment to VLAN 0.
- You use a distributed router on this segment.
- The edge VM is on the same VDS prepared for NSX.

In this case, do not use the MAC learning option. Instead, use Option 2b as a special case, if you cannot use the edge VM on regular vSphere VDS.

## Option 2b: Edge VM is on a VDS 6.5.0 (or earlier) portgroup

This option is for when the Edge VM is connected to a VDS (vSphere Distributed Switch). You enable promiscuous mode and forged transmit.

- Set promiscuous mode on the distributed portgroup.
- Allow forged transmit on the distributed portgroup.
- Run the following command to enable reverse filter on the ESX host where the Edge VM is running:

  ```
  esxcli system settings advanced set -o /Net/ReversePathFwdCheckPromisc -i 1
  ```

  Then disable and enable promiscuous mode on the distributed portgroup with the following steps:
  - Edit the distributed portgroup's settings.
  - Disable promiscuous mode and save the settings.
  - Edit the distributed portgroup's settings again.
  - Enable promiscuous mode and save the settings.
- Do not have other distributed port groups in promiscuous mode on the same host sharing the same set of VLANs.
- Avoid running other VMs attached to the distributed portgroup in promiscuous mode on the same host, as the traffic gets replicated to all those VMs and affects performance.

## Option 3: Edge VM is connected to an NSX segment

If the Edge is deployed on a host with NSX installed, it can connect to a VLAN segment and use MAC Learning, which is the preferred configuration option.

- Create a new MAC Discovery segment profile by navigating to NetworkingSegmentsProfiles.
  - Click Add Segment ProfileMAC Discovery.
  - Enable MAC Learning. This will also enable Unknown Unicast Flooding. Keep the flooding option enabled for bridging to work in all scenarios.
  - Click Save.
- Edit the segment used by the Edge by navigating to NetworkingSegments.
  - Click the menu icon (3 dots) and select Edit.
  - Expand the Segment Profiles section, then set the MAC Discovery profile to the one created above.

If you bridge a segment to VLAN 0 and you use a distributed router on this segment, the gateway might not route VLAN 0 traffic when using MAC learning. In this scenario, avoid option 3. Avoid option 2a if the edge VM is attached to the distributed portgroup of a VDS prepared for NSX for vSphere.