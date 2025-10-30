---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/move-a-contract-or-a-serial-number-between-site-ids.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Move a Contract or a Serial Number Between Site IDs
---

# Move a Contract or a Serial Number Between Site IDs

Registration of VCF Operation is linked to a VCF Business Services console tenant and a Broadcom SiteID*.* The license allocations are linked to their contracts via serial numbers. If a contract or serial number is moved from one Broadcom SiteID to another, this impacts existing VCF Operations that are linked to the first SiteID with licenses from that SiteID.

Verify that you have a product or user administrator privileges for the new SiteID.

You cannot move serial numbers, you must contact support and request the move. In some cases, when you expand or renew a contract, and if a new SiteID is added in the ordering process, serial numbers might be moved.

If you need to move your serial number from one SiteID to another, you must first submit a usage report from VCF Operations and download a new license file. You need to add licenses again in the new site. You must do this for all VCF Operations instances with a license from that serial number.

If one of your licenses appears as Inactive but your subscription is not expired, your serial number might have been moved.

When a serial number is moved, you might observe the following:

1. Existing licenses linked to that serial number become Inactive.
2. Existing assignments appear as over assigned.
3. License updates fail.
4. After 180 days, your license expires, your hosts are disconnected from vCenter, and you cannot start workload operations.

After the serial number is moved, you must register your VCF Operations instance to the new SiteID and re-license your environment. Failure to do so may result in service impact to your environment.

1. Find the licenses and the VCF Operations instances related to the serial number.
   1. Log in to the VCF Business Services console.
   2. Navigate to License ManagementLicenses.
   3. Use the search box to search for the serial number.

   All of the filtered licenses contain the searched serial number. The search results will have a column for **VCF Operations Name.** These are the instances that will need to be re-linked to the new siteID.
2. Generate a license usage file from each VCF Operations instance related to the serial number, and update its licenses.
   1. Log in to the VCF Operations instance.
   2. Navigate to License ManagementRegistration.
   1. Update licenses.
   - If the VCF Operations instance is in connected mode, verify that your license usage file was submitted within the last 24 hours by looking at the **Last Usage Report Generated** date, and click Update Licenses. For more information, see [Update Licenses in Connected Mode.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/update-licenses/updatelicenses.html)
   - If the VCF Operations instance is in connected mode, generate a license usage file. For more information, see [Report License Usage and Update Licenses in Disconnected Mode.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/update-licenses/update-licenses-in-disconnected-mode.html)
3. After you move your serial number, for each VCF Operations instance, create your licenses again by splitting the default license. For more information, see [Managing Licenses in the VCF Business Services console](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/manage-licenses-in-the-vcf-business-services-console.html).

   As a best practice, allocate the same capacity to the licenses as the capacity from the prior SiteID. Consider also using a distinct license name from the prior site.
4. Deactivate the VCF Operations instance in VCF Business Services console. For more information, see [Deactivate a Instance.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/unregister-vcf-ops.html)

   You must select the check box I no longer have access to the VCF Operations instance.
5. Restart registration for each VCF Operations instance linked to the serial number.
   1. Log in to the VCF Operations instance.
   2. Navigate to License ManagementRegistration.
   3. Click **ActionsRestart Registration.**

      This action does not impact the existing licenses in your environment.
6. Register each VCF Operations instance linked to the serial number with the new SiteID. For more information, see [Registering VCF Operations with the VCF Business Services console](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/register-vcf-operations.html).

   During registration, select the new Site ID, and the license you created in step 3.
7. Relicense your environment by assigning the licenses to the vCenter instances. For more information, see [Assign a Primary License to a Instance.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/assign-a-licenses-to-a-vcenter-instance.html)

   Both your old and new licenses are displayed in VCF Operations. After your next license update, if the old licenses are no longer assigned to vCenter instances, they do not appear in VCF Operations.

Update your licenses. For more information, see [Updating Licenses.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/update-licenses.html)