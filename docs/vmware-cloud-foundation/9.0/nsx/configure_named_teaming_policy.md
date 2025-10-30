---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/configuring-profiles/configure-named-teaming-policy.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure Named Teaming Policy
---

# Configure Named Teaming Policy

On a host running NSX with an N-VDS, you can use the named teaming policies to override the default teaming policy that was configured for some specific VLAN backed segments. This capability is used to steer VLAN traffic to specific uplinks.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/5c879e6c-885f-429b-af41-03bc06a04fd3.original.png)

In the figure, VMs (VM1, VM2) connected to overlay networks follow default teaming policy and use uplinks u1 and u2. However, an additional teaming policy named teaming policy VLAN-traffic is configured to steer vlan traffic (for VMs 'VM3, VM4' connected to VLAN segment) to uplinks u3 and u4 to separate overlay and VLAN traffic.

1. Configure an uplink profile, which will be consumed by transport node members of a VLAN Transport zone and define following:
   1. Set a default teaming policy with active uplinks (standby uplinks not supported for NSX Edge Transport nodes).
   2. Set a named teaming policy <p1> with mode 'failover order' and active uplink1.
   3. Set a named teaming policy <p2> with mode 'failover order' and active uplink2 and so on.

      For overlay segments, the default teaming is used by default. For VLAN segments, when a named teaming policy is defined, NSX ensures that the named teaming policy overrides the default teaming policy.
   4. Set the Transport VLAN and MTU.
   5. Click Save.

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/f5ee1499-dcb8-411c-877d-9fb06ae82172.original.png)
2. Configue VLAN Transport zone with teaming policy names specified in the uplink profile.

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/83f19cfd-79d0-4a47-931a-4f372f232746.original.png)
3. Create VLAN segment1 on VLANX and associate with teaming policy name <p1>.

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/bfe69e3a-fdbc-49b9-adb8-c2a0bc190d63.original.png)
4. Create a VLAN segment2 on VLANY and associate it with teaming policy name <p2>.
5. Configure a transport node to use uplink profile configured with the named teaming policy.

   Use a named teaming policy to pin traffic that egreeses from a specific uplink and ingresses into a ToR switch .

   A named teaming policy is only applicable to VLAN segments/logical switches. A named uplink profile only supports the Failover teaming policy. If a VLAN segment does not specify which teaming policy to use, the default teaming policy in the uplink profile will be used.

   If you use (Failover) Active/Standby for a VLAN-based segment, the traffic will be always forwarded through the active uplink. Traffic will not failover to the standby uplink. If you want to configure failover, define it in the distributed port group. This is valid only for Edge VM.

   NSX teaming policies apply to traffic entering and existing N-VDS but not the traffic exiting the hypervisor configured with PNICs on VDS. Hosts configured with PNICs on VDS, will follow the teaming policy defined in their respective VDS DVPGs in vCenter.

   An example of a VDS portgroup teaming that is defined in vCenter for NSX Edge VM.

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8bfa91d2-eb98-417c-837b-263a7b19b474.original.png)