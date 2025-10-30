---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/manage-licenses-in-the-vcf-business-services-console/split-licenses.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Split Default Licenses
---

# Split Default Licenses

You can split default licenses into as many licenses as you need within the total available capacity of the default license. You can allocate a part of the default license capacity to the new licenses that you create as a result of the split.

The total combined capacity of the split licenses cannot be larger than the total capacity of the default license.

1. In the VCF Business Services console, navigate to License ManagementLicenses.
2. Click the Version 9+ tab.
3. Click Manage Licenses (Split/Merge).

   The Manage Licenses wizard appears.
4. From the drop-down menu, select a product for which you want to split the default license.
5. Click Next.

   The default license for this product appears.
6. Click Create.

   A new line for the split license appears in the table.
7. In the Name column, enter a name for the license.
8. In the New Capacitycolumn, enter the amount of capacity you want to allocate to the new license.

   You cannot allocate higher amount of capacity than what is available in the default license.
9. Click Next.
10. On the Summary page, review your changes, and click Finish.

Your newly created license appears in the list of licenses in the VCF Business Services console.

If your default license is added to a VCF Operations instance, you must update the license in that VCF Operations instance after the split.