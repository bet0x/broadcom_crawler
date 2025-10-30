---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-virtual-private-clouds-in-vcenter/managing-your-virtual-private-cloud-subnets-in-vcenter/view-the-summaery-of-vpc-subnet-in-vcenter.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > View the Summary of VPC Subnet in vCenter
---

# View the Summary of VPC Subnet in vCenter

Learn how to view the summary of VPC subnet in vCenter.

1. From your browser, log in to the vSphere Client.
2. Navigate to the VPC Subnet.
3. Click Summary.
4. To view the statistics, click View More.
5. Cumulative statistics for all traffic through the ports on the subnet are displayed.
6. Click VPC Gateway Interface to view more details on data, total packets received and transmitted, and dropped packets received and transmitted.

   You can view the details of the VPC Subnet.

   | **Option** | **Description** |
   | --- | --- |
   | Access Mode | One of the following options is present:  - Private VPC - Private Transit Gateway - Public |
   | Gateway Connectivity | It displays if this subnet is connected to the other subnets in the VPC.  One of the options is present:  - Yes - No |
   | IP CIDR | Based on whether you create a private or a public subnet, IPs are allocated from the private or public CIDRs you defined in the connectivity profile of the VPC. |
   | Gateway Address | The default gateway address. |
   | VMs | Shows the total number virtual machines attached to this subnet across all data centers and vCenters. |
   | DHCP Type | One of the following options is present:  - **None**: DHCP will not be enabled in the subnet and all IP addresses will be set statically. - **DHCP Server**: The DHCP server specified in the service profile will automatically assign IP addresses - **DHCP Relay**: The DHCP relay specified in the service profile will forward DHCP messages from VMs connected to the subnet to an external DHCP. |