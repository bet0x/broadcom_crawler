---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/configure-edge-dpdk-interfaces.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure NSX Edge DPDK Interfaces
---

# Configure NSX Edge DPDK Interfaces

Configure an NSX Edge VM with a node switch to carry both overlay and external traffic.

In this topology, NSX Edge VM is configured with a node switch to carry overlay and external traffic.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/0c7ef839-6c4c-4a82-9109-83d1387a197b.original.png)

In this topology, the uplink profile attached is configured to use Multi-TEP to provide load balancing for overlay traffic by selecting default teaming to be Load Balancing Source teaming policy with active 'uplink1' and 'uplink2' on transport VLAN 200.

(optional) The uplink profile attached is also configured to use named teaming policy, where 'vlan300-policy' is mapped to uplink1 and 'vlan400-policy' is mapped to uplink2.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/b85bbc63-54ff-4fa4-95a4-d358a8052898.original.png)

To create the topology, follow these steps.

1. Uplink Profile creation with named-teaming policy for VLAN networks and default teaming for overlay networks. If named-teaming does not exist in uplink profile then default teaming is used for all networks.

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/a44b4d0c-12f8-4c2e-bfe2-39824359c0b3.original.png)
2. VLAN Transport Zone is created or modified to use named teaming policy VLAN300-Policy and VLAN400-Policy (if using named-teaming policy).

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8529e448-9197-48a8-8c40-5a3f2483cbe2.original.png)
3. In the NSX Edge configuration, “Uplink1” (fp-eth0) is vNIC2 on Edge VM and is mapped to use VLAN 300 Trunk PG and “Uplink2”(fp-eth1) is vNIC3 on Edge VM and is mapped to use VLAN 400 Trunk portgroup.

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/bc79dd38-d2a7-425b-a476-c54d76ccf465.original.png)
4. NSX Edge VM interfaces can connect to VDS Portgroups in vCenter or NSX VLAN Segments.

   If Edge interfaces will be connecting to NSX VLAN Segments, ESX Hosts (hosting the Edge VMs) should be configured as Host Transport Nodes and member of VLAN transport zone.

   An example of connecting VM interfaces to NSX VLAN segments.

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/aca6db53-5e18-477f-bf90-e6eedae3a3ce.original.png)

   An example of an NSX Edge VM with interfaces on vCenter VDS Edge Trunk Portgroups

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/4f584072-352c-4726-b292-e1de8a0350cc.original.png)

   1. If VM interfaces connect to NSX VLAN segments, named-teaming is enabled on the segments. The diagram shows that External VLAN segment 300 is configured to use a named teaming policy “Vlan300-Policy” that sends traffic from this VLAN on “Uplink1” (vNIC2 of Edge VM). "External VLAN segment 400" is configured to use a named teaming policy “Vlan400-Policy” that sends traffic from this VLAN on “Uplink2” (vNIC3 of Edge VM).

      ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/1e201e9b-deaa-4c76-bde0-e438b64adb80.original.png)
   2. If VM interfaces connect to VDS Portgroups in vCenter, then “Trunk1 PG” is configured to use active uplink as “VDS-Uplink1” and standby uplink as “VDS-Uplink2”. “Trunk2 PG” is configured to use active uplink as “VDS-Uplink2” and standby uplink as “VDS-Uplink1”. This configuration ensures that the traffic sent on “External VLAN Segment 300”uses vNIC2 of Edge VM to exit the Edge VM and then “VDS-Uplink1” and is sent to the left TOR switch. Similarly, traffic sent on VLAN 400 uses “VDS-Uplink2” and is sent to the TOR switch on the right.

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7c5fc6dc-29df-45c3-a896-69a403aae256.original.png)

   - ESX TEP and Edge TEP share the same VLAN: Use this configuration only if NSX Edge Trunk 1 portgroup and NSX Edge Trunk 2 portgroup are created from NSX as VLAN segments. Because any traffic between the Edge TEP to its own hypervisor’s TEP does not need to exit the hypervisor.
   - ESX TEP and Edge TEP use different VLANs: Use this configuration if NSX EdgeTrunk1 portgroup and NSX EdgeTrunk2 portgroup are created as VDS portgroups from vCenter. Any traffic between the NSX Edge TEP and its hypervisor TEP must exit the ESX. The top of rack switch must then route it back toward the ESX.