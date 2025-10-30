---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/remove-a-license-from-vcf-operations.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Remove a License from VCF Operations
---

# Remove a License from VCF Operations

To remove a license from VCF Operations, the license must not be assigned to any vCenter instance in your environment.

- Verify that there are no licensed vCenter or VCF Instances managed by this VCF Operations instance.
- Remove all licenses from the VCF Operations instance. For more information, see [Remove a License from a vCenter Instance.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/remove-a-licenses-from-a-vcenter-instance.html)
- Report license usage for the VCF Operations instance. For more information, see [Report License Usage and Update Licenses in Disconnected Mode](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/update-licenses/update-licenses-in-disconnected-mode.html).

After you remove the license from VCF Operations, you can assign the license to another VCF Operations instance or you can delete it. To complete the license removal, you must update your licenses in VCF Operations.

1. In the VCF Business Services console, navigate to License ManagementLicenses.
2. Select the Version 9+ tab.
3. Next to the license you want to remove, click the vertical ellipsis, and click Remove License from VCF Operations.

   A dialog box appears.
4. Click Remove.
5. If your VCF Operations registration is in connected mode, update your licenses in the VCF Operations instance:
   1. In the dialog box, click Finish.
   2. In the VCF Operations instance, navigate to License ManagementRegistration.
   3. Click Update Licenses.
6. If your VCF Operations registration is in disconnected mode, manually upload the license file in VCF Operations:
   1. In the Download the License File dialog box, click Download, and save the license file.
   2. Click Finish.
   3. In the VCF Operations instance, navigate to License ManagementRegistration.
   4. Click Import License File.
   5. In the Import License File dialog box, click Browse, select and import the license file.
   6. Click Complete.

To see the change in the VCF Operations instance, update your licenses. For more information about updating licenses, see [Update Licenses.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/update-licenses/updatelicenses.html)