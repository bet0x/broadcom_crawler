---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/configure-the-reference-host-as-a-transport-node-in-nsx.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure the Reference Host as a Transport Node in NSX
---

# Configure the Reference Host as a Transport Node in NSX

After the reference host is associated with the custom image profile and configured with a VSS or DVS switch, deploy the reference host as a NSX transport node with NSX enabled DVS switch.

1. From a browser, log in to NSX at https://<NSXManager\_IPaddress>.
2. To locate the reference host, navigate to SystemFabricHostsClusters.
3. You also need to create a VLAN transport zone to define span of a virtual network. The span is defined by attaching VDS switches to the transport zone. Based on this attachment, VDS can access segments defined within the transport zone. See [Create Transport Zones](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/create-transport-zones.html).
4. Create a VLAN segment on the transport zone. The created segment is displayed as a logical switch.

   1. Navigate to Networking -> Segments.
   2. Select the transport zone to attach the segment.
   3. Enter VLAN ID.
   4. Click Save.

   ![In the Segments tab, create a VLAN segment for a transport zone.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/f82406e4-15e4-4feb-bf07-417302b896f9.original.png)
5. Create an uplink profile for the reference host that defines how an VDS switch connects to the physical network. See the topic Create an Uplink Profile .
6. Configure the reference host as a transport node. See [Prepare ESX Cluster Hosts as Transport Nodes by Using TNP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/preparing-esxi-hosts-as-transport-nodes/prepare-esxi-cluster-hosts-as-transport-nodes.html).

   1. On the Clusters tab, select the reference host.
   2. (On a VDS switch) Click Configure NSX and select the previously created transport zone, VDS, uplink profile.
7. Click Finish to begin installation of NSX on the reference host.

   (On a VDS switch) After installation, configuration status of the reference host is displayed as Success. In the vCenter, the VDS switch is displayed as NSX switch.

   The reference host is listed under Other Hosts.

Extract and Verify the Host Profile. See [Extract and Verify the Host Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/extract-and-verify-the-host-profile.html#GUID-a5db2fbf-9959-4bee-943b-492461adedbf).