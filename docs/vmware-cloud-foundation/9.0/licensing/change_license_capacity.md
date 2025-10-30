---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/manage-licenses-in-the-vcf-business-services-console/edit-license-capacity.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Change License Capacity
---

# Change License Capacity

You can change the license capacity of split licenses as many times as you need. You can allocate more capacity or remove some of the capacity of the split licenses at any time. Any change in the capacity allocated to split licenses, affects the default license.

The capacity that you add to split licenses is extracted from the capacity of the default license. The capacity you remove from the split licenses is added back to the default license. You cannot add more capacity to a split license than the capacity available in the default license. If you need more capacity than what is available in the default license, you must free up capacity from the other split licenses which belong to the same product type, or you must purchase more capacity.

You cannot reduce the capacity of a license below the quantity of the license that is currently used. If you try to reduce the capacity of an assigned license, the operation fails. For example, if you have a license with capacity of 250 cores, and it is assigned to a vCenter instance, which has 4 ESX hosts added to it, each using 50 cores license capacity, you cannot reduce the capacity of the license to less than 200 cores.

If at a certain point the used capacity is higher than the capacity allocated to the assigned licenses, you must allocate more capacity to the licenses. Before you add more capacity, you cannot assign the over used licenses to new vCenter instances. If a vCenter is licensed by a license that is over used, you can only add new ESX hosts that are in evaluation mode.

1. In the VCF Business Services console, navigate to License ManagementLicenses.
2. Click the vertical ellipsis next to the split license, and select Change Capacity.
3. In the New Capacitycolumn, enter the new amount of allocated capacity.

   For example, if your license has 150 cores of allocated capacity, and you want to add 50 cores, you add 200 in the New Capacity column.

   You cannot assign a higher amount of capacity than what is available in the default license.
4. Click Save and Next.
5. On the Summary page, review your changes, and click Finish.

The new capacity of the license appears in the list of licenses.