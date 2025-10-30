---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/create-a-vpc.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure a VPC
---

# Configure a VPC

Prerequisites

- You must have a role of a Project Admin or an Enterprise Admin.
- You must have a VPC Connectivity Profile and VPC Service Profile configured.
- If you want to configure stateful rules, ensure you have the VMware Firewall with Advanced Threat Prevention license.

1. From your browser, log in to the NSX Manager.
2. Click the Project drop-down menu, and select the project where you want to add an NSX VPC. By default, the Default project is selected.
3. Go to VPCs Virtual Private Cloud.
4. Click Add VPC.
5. On the Basic Info page, enter the following information.

   | Field Name | Description |
   | --- | --- |
   | Name | Enter a name for the VPC. |
   | VPC Connectivity | This field is shown only for a custom project when a Tier-0 gateway is shared with the project (to support the connectivity model prior to VCF 9.0).  You can choose from the following connectivity options:  - Transit Gateway via selected Connectivity Profile (Recommended): You can select the default connectivity profile and continue the VPC configuration based on the simplified VPC model. For more information about the VPC Connectivity Profile, see [Add a VPC Connectivity Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/add-a-vpc-connectivity-profile.html). - Tier-0 Gateway: You can select a tier-0 gateway for connectivity and continue the VPC configuration based on the old connectivity method. For more information about configuring VPC based on the old model, see [Add an NSX VPC](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-virtual-private-clouds/add-an-nsx-vpc.html). |
   | Connectivity Profile | Select a connectivity profile for this VPC. For more information about the VPC Connectivity Profile, see [Add a VPC Connectivity Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/add-a-vpc-connectivity-profile.html).  The connectivity profile is used to connect VPCs through a transit gateway and does not require you to share a Tier-0 gateway with the project.  Note that if your connectivity profile has some missing configurations, you can configure them from the links in the warning displayed on the topology graphic |
   | Service Profile | Select a service profile for this VPC. For more information about the VPC Service Profile, see [Add a VPC Service Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/add-a-vpc-service-profile.html). |
   | Private- VPC IP CIDRs | Enter a block of IP CIDRs that can be assigned to private subnets of this VPC. These CIDRs are local to VPCs and can overlap between the VPCs. |
   | Short Log Identifier | Enter a short log Identifier that should be used to identify the VPC context in log. |
   | Description | Enter a description for the VPC. |
   | Tags | Enter a tag and scope for the VPC. |
   | Advanced Settings | |
   | Enable for Avi Load Balancer | Turn on this toggle to enable the discovery of this VPC in the AVI load balancer. This feature provides multi-cloud load balancing, web application firewall, application analytics and container ingress services from the data center to the cloud. For the toggle to be available, the VPC must have one private IP CIDR |
6. Click Save and Go Next .
7. On the VPC created confirmation window, click Yes, Continue.
8. On the Additional Configurations page, enter the following information.

   | Field Name | Description |
   | --- | --- |
   | Users | Click Set and set role assignments to user or user groups. Note that you can add roles to users, only if your role is permitted to assign roles of other users. |
   | Connectivity | |
   | Subnets | Click Set and add subnets for the VPC. For more information, see [Add a Subnet for the VPC](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/add-a-subnet-for-the-vpc.html). |
   | Static Routes | Click Set to set the static routes. |
   | Network Services | |
   | External IPs | Click Set to set external IPs for the VMs attached to subnets.  You will need to select the VM, the NIC, and whether to auto-assign the IPs.  If you want to provide a IP from an IP block, use the NSX API. |
   | NAT | Note that NAT is not available for a DTGW. |
   | Security - Note that Groups and N-S Firewall are available only if you have the VMware Firewall with Advanced Threat Prevention license. | |
   | E-W Firewall Rules | Click Set to add E-W firewall rules. For more information, see the vDefend documentation. |
   | Groups | Click Set to add groups on which security rules are to be applied. For more information, see the vDefend documentation. |
   | N-S Firewall Rules | Click Set to add N-S firewall rules. For more information, see the vDefend documentation. |
9. Click Finish.