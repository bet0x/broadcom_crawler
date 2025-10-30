---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/license-management-for-cloud-services-providers-and-hyperscalers/create-licenses-(for-vcsps).html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Create Licenses as a Provider
---

# Create Licenses as a Provider

After you purchase a contract serial number and a product, you must create licenses against a contract serial number combination.

Verify that you are in the correct tenant.

Depending on the type of your contract, you can exceed the commit capacity for the created licenses.

- For TFC commit contracts, when you create new licenses, the capacity you enter for the licenses can exceed the commit capacity. The license entitlement is 125 percent of the commit capacity.
- For non-TFC commit contracts, the license entitlement is 100 percent of the commit capacity. You cannot exceed the commit capacity.

The capacity of the licenses must be between 1 and 100 000 cores.

1. Log in to the VCF Business Services console.
2. Navigate to License ManagementLicenses.
3. Click Manage Licenses.
4. From the All Serial Numbers and Products, select the serial number and the product you want to create the new license against.

   You can see all of the licenses previously created for the selected serial number and product with high-level details for commit contract capacity, the maximum capacity, total number of licenses created, and the total allocated capacity. You can also see the expiration date and consumed capacity of each license individually.
5. Click Create.
6. Enter a name and capacity for the license and click Next.

   For TFC contracts, the sum of the capacity of the created licenses can exceed the commit capacity by 125 percent. For non-TFC contracts the sum of the capacity of the created licenses cannot exceed the commit capacity.
7. View the summary and click Finish.