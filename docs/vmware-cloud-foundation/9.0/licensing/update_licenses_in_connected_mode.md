---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/update-licenses/updatelicenses.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Update Licenses in Connected Mode
---

# Update Licenses in Connected Mode

After any change to your licenses in the VCF Business Services console, to reflect the changes in your environment, update your licenses in the VCF Operations instance. If your VCF Operations registration is in connected mode, the usage file is submitted automatically on a daily basis. You must still update your licenses in the VCF Operations instance at least once every 180 days to verify that the usage file has been submitted correctly and to keep your environment licensed.

- Verify that you added one or more licenses to the VCF Operations instance.
- Verify that a usage file is generated after the last license update.

You must update your licenses at least once every 6 months (180 days). If license usage data is not submitted within the required reporting time-frame, and you do not update your licenses, your licenses are treated as expired, your hosts are disconnected from the vCenter instance, and you cannot start any workload operations. You can also update your licenses at any time to either extend your usage reporting refresh period.

1. In the VCF Operations instance, navigate to License ManagementRegistration.
2. To verify that your license usage file was submitted within the last 24 hours, check the Last Usage Report Generated date**.**
3. Click Update Licenses.

Your VCF Operations instance is updated with the latest license information available from the VCF Business Services console.