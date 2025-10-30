---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects/add-an-nsx-project/example-organizing-nsx-portgroups-in-vmware-vcenter-folders.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Example: Organizing NSX Port Groups in vCenter Folders
---

# Example: Organizing NSX Port Groups in vCenter Folders

While configuring a project, you can turn on the Organize NSX Portgroups in vCenter folders option to organize NSX port groups corresponding to project segments and NSX VPC subnets inside folders on vCenter.

Example:

Assume that your NSX deployment is configured as follows:

- Hosts are attached to a single vSphere Distributed Switch (VDS)
- Segments D1 and D2 are created in the default space
- Segments P1 and P2 are created in Project A
- VPC X is created in Project A
- Subnets S1 and S2 are created in VPC X

In the following figure, the diagram on the left shows the flat organization of the NSX port groups in vCenter when the option is turned off. The diagram on the right shows the hierarchical organization of NSX port groups inside the project and VPC folders when the option is turned on.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/e16fdb4c-3d52-4742-bd4e-b43b3b0df63d.original.png)

The left diagram shows that the NSX port groups for the segments in the default space, segments in the project, and subnets in the NSX VPC are organized in a flat hierarchy under the VDS object.

The right diagram shows that a hierarchical folder structure is created in vCenter, as follows:

- A root folder named NSX Managed Folders is created under the Datacenter object.
- Project-A folder is created inside the root folder.
- A P1 and a P2 segment folder, corresponding to each project segment, is created in the Project-A folder
- NSX port groups P1 and P2 corresponding to the segments in the project are organized inside the Project-A segment folder.
- VPC-X folder is placed inside the Project-A folder.
- NSX port groups S1 and S2 corresponding to the subnets in the VPC are organized inside the VPC-X folder.
- An S1 and an S2 subnet folder, corresponding to each VPC subnet, is created in the VPC-X folder.
- NSX port groups S1 and S2 corresponding to the subnets in the VPC are organized inside the VPC-X subnet folders.

- The segment and subnet folders are created only for the purpose of grouping the NSX port groups mapped to the same segment or subnet in a multi-VDS deployment. A multi-VDS example is presented below.
- The VDS object continues to remain inside the Datacenter object in VMware vCenter.
- NSX port groups D1 and D2 corresponding to the segments in the default space are not organized in folders. These port groups continue to be placed under the VDS object.

Now let us assume that the hosts are connected to multiple VDSs. Below, the figure on the left presents a scenario where the port groups are not organized in folders. A port group for each segment and subnet is present on both VDSs.

The figure on the right presents a scenario where the port-groups are organized in the hierarchical folder structure managed by NSX. In this case, we can see that each segment and subnet folder contains two port groups, mapped to the corresponding NSX segment or VPC subnet, which are created in each of the two VDSs

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8e300684-79e3-44f2-b1d4-ba149d843434.original.png)

For more documentation about organizing NSX port groups in vCenter folders, see the Procedure and What to do next sections in [Add an NSX Project](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects/add-an-nsx-project.html).