---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/add-a-vpc-connectivity-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a VPC Connectivity Profile
---

# Add a VPC Connectivity Profile

A connectivity profile defines common northbound connectivity configuration for VPCs. When a project is created, a default connectivity profile is also created for it.

1. From your browser, log in to the NSX Manager.
2. Click the Project drop-down menu, and select the project for which you want to add a connectivity profile. By default, the Default project is selected.
3. Go to VPCs Profiles  VPC Connectivity Profile.
4. Click Add VPC Connectivity Profile.
5. Enter the following fields.

   | Field Name | Description |
   | --- | --- |
   | Name | Enter a name for the VPC connectivity profile. |
   | Transit Gateway | By default, the system created transit gateway is already selected. |
   | External IP Blocks | Enter external IP blocks that can be used to create public subnets and also the External IP binding for 1:1 NAT in the VPC. The entered IP blocks allow outside connectivity to VPC workloads either on public subnets or through external IPs. |
   | Private-Transit Gateway IP Blocks | Enter private IP blocks to create private subnets in the VPC. The entered IP blocks are available for inter-VPC communication. Networks created from the Private - Transit Gateway IP blocks are not advertised. |
   | VPC | Shows the number of VPCs associated with this profile. |
   | Status | Shows if the connectivity profile is successfully created. |
   | VPC Service Gateway Configurations | |
   | Edge Cluster | Select an edge cluster for this profile. |
   | N-S Services | Turn on the toggle to enable service gateway for the connected subnets and to support centralized services such as N-S firewall, NAT, or gateway QoS profile in the VPC. |
   | Default Outbound NAT | Turn on the toggle to ensure workloads on private subnets have outbound access outside of VPC. One SNAT rule per VPC will be auto-plumbed with IP used for translation taken from an External IP block for this VPC.  Note that this toggle is available only if the **N-S Services** toggle is turned on. |
   | N-S Ingress QoS Profile | Select an appropriate ingress profile. For more information, see [Segment Profiles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles.html). |
   | N-S Egress QoS Profile | Select an appropriate egress profile. For more information, see [Segment Profiles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles.html). |
   | Description | Enter a description for the connectivity profile. |
   | Tags | Enter tags and scope for this connectivity profile. |
6. Click Save.