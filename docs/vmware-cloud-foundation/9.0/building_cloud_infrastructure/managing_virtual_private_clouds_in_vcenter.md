---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-virtual-private-clouds-in-vcenter.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Managing Virtual Private Clouds in vCenter
---

# Managing Virtual Private Clouds in vCenter

Learn how to manage Virtual Private Clouds (VPC) in vCenter.

A virtual private cloud (VPC) is a configurable pool of shared network resources allocated within a cloud environment, providing a certain level of isolation between the different organizations using the resources. A subnet is a range of IP addresses in VPC and a workload is connected to a subnet.

In vSphere 8.0 Update 3, a hierarchical folder based approach was introduced to represent NSX projects and VPC in the vSphere Client that facilitates separate management by its various users. With this framework, NSX DVPGs were systematically organized in their respective folders. This streamlined the structural hierarchy between NSX and the vCenter inventory.

Prior to VCF 9.0, VPCs, subnets, and various VPC services were configured only from NSX. To connect the workloads, administrators had to navigate to vCenter. VCF 9.0 offers a simplified networking solution.

In VCF 9.0, VPCs and Subnets which are primarily NSX objects are integrated in vCenter. The administrator manages the VPC and subnet in vCenter. This implementation allows the VC admin to create, read, update and delete the NSX VPC from the vSphere Client. You can also navigate from and to NSX objects within the vCenter. For more information on VPCs in NSX, see [Virtual Private Cloud in NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx.html).