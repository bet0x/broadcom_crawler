---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/assign-a-licenses-to-a-vcenter-instance.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Assign a Primary License to a vCenter Instance
---

# Assign a Primary License to a vCenter Instance

You assign a primary license to a vCenter instance. Your other assets that are connected to that vCenter instance, including ESX hosts, are then licensed automatically.

- Verify that you have the Manage Licenses permission assigned.
- Verify that the VCF Operations instance is registered with the VCF Business Services console.
- Verify that licenses are added to this VCF Operations instance.
- Verify that the vCenter instance to which you want to assign a license is integrated with the VCF Operations instance registered for license management. If the vCenter instance is part of a VCF domain, verify that the VCF Instance is integrated with the VCF Operations instance. For more information about adding vCenter instances and VCF instances to VCF Operations, see [Configuring a vCenter Account in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations.html), or [Configuring a VCF Cloud Account in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vmware-cloud-foundation/configuring-vmware-cloud-foundation.html).

After you integrate a vCenter instance or a VCF Instance with VCF Operations for license management, it takes up to 4 collection cycles before the vCenter instance appears in the Licenses tab of VCF Operations.

The vCenter instance can be standalone or part of a VCF Instance. You cannot assign a license to a vCenter instance if it requires more license capacity than the available capacity of the license you want to assign. If you try to assign the license to a vCenter instance which requires more capacity than the capacity available in the license, the assignment fails. If you try to add a host to a licensed vCenter instance, and the cores of the host are more than the available capacity left in the license assigned to the vCenter instance, the host is added in evaluation mode. If the host has exceeded the 90 day evaluation period, you cannot add it to the vCenter instance unless you increase the available capacity of the license.

If the host is in evaluation mode, it is added to the vCenter instance even if the license capacity is not sufficient. During the evaluation period of the host, you must add more capacity to the license to license the host. If the host is not licensed when the evaluation period expires, it is disconnected from the vCenter instance. The virtual machines running on the disconnected host remain intact. When there is enough available capacity in the license assigned to the vCenter instance, all disconnected hosts reconnect to the vCenter system.

For example, you add a license with 1000 cores allocated capacity to the VCF Operations instance. You then add 4 vCenter instances to be managed by this VCF Operations instance. The aggregate license consumption of the 4 vCenter instances requires 1500 cores. This means you cannot assign the license to all of them, as the aggregate consumption across all of the vCenter instances cannot exceed 1000 cores.

For more information about calculating the license capacity you need for your environment, see Broadcom knowledge base article [95927](https://knowledge.broadcom.com/external/article?legacyId=95927).

When a license expires, your hosts are disconnected from the vCenter instance, which can be a standalone instance or part of a VCF Instance, and you cannot start any workload operations. After you assign a valid license to the vCenter instance, the hosts are automatically reconnected to the vCenter instance unless you added them to another vCenter instance in the meantime.

1. In the VCF Operations instance, navigate to License ManagementLicenses.
2. Select the Version 9+ tab.
3. From the vCenter Systems table, select one or more vCenter instances to which you want to assign a license.

   The table contains only vCenter instances of version 9+ managed by the current VCF Operations instance. If a vCenter instance is added the VCF Operations instance for monitoring only, it does not appear in this table.
4. Click Assign Primary License.

   A list with the licenses added to VCF Operations appears. The licenses which you cannot assign appear at the bottom of the list, and the column Assignable shows No.
5. Select a license to assign, and click Assign.

In the Primary License Name column of the vCenter Systems table, you can view the licenses that you assigned to the vCenter instance. If the assignment failed for a vCenter instance, and you want to view the details of the task, click View Details in the banner above the table and hover over the information icon in the Status column.