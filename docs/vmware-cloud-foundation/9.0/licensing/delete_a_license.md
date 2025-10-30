---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/manage-licenses-in-the-vcf-business-services-console/delete-a-license.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Delete a License
---

# Delete a License

You can delete a split license from the VCF Business Services console console if you no longer need it. You cannot delete a split license if some of its capacity is assigned to a vCenter instance.

- Verify that the license is not assigned to a vCenter instance.
- Verify that the license is not added to a VCF Operations instance.

1. In the VCF Business Services console, navigate to License ManagementLicenses.
2. Next to the split license, click the vertical ellipsis, and click Delete.
3. In the dialog box which appears, click Delete.

The license is deleted and its capacity is merged with the default license capacity.