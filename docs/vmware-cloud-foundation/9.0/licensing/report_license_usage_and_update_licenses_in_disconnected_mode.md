---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/update-licenses/update-licenses-in-disconnected-mode.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Report License Usage and Update Licenses in Disconnected Mode
---

# Report License Usage and Update Licenses in Disconnected Mode

When a VCF Operations instance is in disconnected mode, you must manually exchange the usage file and the license file between the VCF Operations instance and the VCF Business Services console.

- Verify that your VCF Operations instance is registered in the VCF Business Services console.

You must update your licenses and submit a license usage file at least once every 6 months (180 days). If license usage data is not submitted within the required reporting time-frame, and you do not update your licenses, your licenses are treated as expired, your hosts are disconnected from the vCenter instance, and you cannot start any workload operations.

You can generate a new license file without submitting a usage file as long as it is within your usage reporting due date. As a best practice, always submit a usage file before you download a new license file.

1. In the VCF Operations instance, navigate to License ManagementRegistration.
2. Click Generate Usage File, and save the usage file.
3. In the VCF Business Services console, navigate to License ManagementVCF Operations Registrations.
4. Next to the VCF Operations instance for which you want to update licenses, click the vertical ellipsis, and click Upload Usage File.
5. In the Upload Usage File wizard, upload the usage file, and click Save and Next.

   A license file is generated.
6. Click Download and save the license file.
7. Click Finish.
8. In the VCF Operations instance, navigate to License ManagementRegistration.
9. Click Import License File.

   The Import License File dialog box appears.
10. Click Browse, upload the license file, and click Import.
11. When the license file is imported, click Complete.