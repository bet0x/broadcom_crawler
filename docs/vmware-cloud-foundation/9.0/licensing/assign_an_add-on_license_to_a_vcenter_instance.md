---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/assign-an-addon-license-to-an-asset.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Assign an Add-on License to a vCenter Instance
---

# Assign an Add-on License to a vCenter Instance

Add-on licenses are available for VCF and vSphere Foundation products. You can assign add-on licenses only after you assign primary licenses to the vCenter instances.

- Verify that you have the Manage Licenses permission assigned.
- Verify that your VCF Operations instance is registered with the VCF Business Services console.
- Verify that add-on licenses are added to the VCF Operations instance.
- Verify that the vCenter instance to which you want to assign a license is integrated with the VCF Operations instance. If the vCenter instance is part of a VCF domain, verify that the VCF Instance is integrated with the VCF Operations instance. For more information about adding vCenter instances and VCF Instances to VCF Operations, see [Configuring a vCenter Account in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations.html), or [Configuring a VCF Cloud Account in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vmware-cloud-foundation/configuring-vmware-cloud-foundation.html).

You cannot assign a license to a vCenter instance if that instance requires more license capacity than the available license capacity of the license you want to assign. To be able to use an add-on license, you must first add a primary license to your VCF Operations instance, and assign it to the vCenter instances.

1. In the VCF Operations instance, navigate to License ManagementLicenses.
2. Select the Version 9+ tab.
3. From the vCenter Systems table, select one or more vCenter instances to which you want to assign a license.

   The table contains only vCenter instances of version 9+ managed by the current VCF Operations instance. If a vCenter instance is added to the VCF Operations instance for monitoring only, it does not appear in this table.
4. Click Assign Add-on License.

   A list with the licenses added to VCF Operations appears. You cannot assign licenses which do not have the required capacity to license the selected vCenter instances. These licenses appear at the bottom of the list, and the column Assignable shows No.
5. Select a license to assign, and click Assign.

In the Add-on License Name column of the vCenter Systems table, you can view the licenses that you assigned to the vCenter instance. If the assignment failed for a vCenter instance, and you want to view the details of the task, click View Details in the banner above the table and hover over the information icon in the Status column.