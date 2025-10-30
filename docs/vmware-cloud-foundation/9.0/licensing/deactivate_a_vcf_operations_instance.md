---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/unregister-vcf-ops.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Deactivate a VCF Operations Instance
---

# Deactivate a VCF Operations Instance

When you deactivate a VCF Operations instance from the VCF Business Services console, you can no longer add any licenses to that instance, and you cannot perform and license management operations.

- Verify that there are no licensed vCenter or VCF Instances managed by this VCF Operations instance.
- Remove all licenses from the VCF Operations instance. For more information, see [Remove a License from a vCenter Instance.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/remove-a-licenses-from-a-vcenter-instance.html)
- Report license usage for the VCF Operations instance. For more information, see [Report License Usage and Update Licenses in Disconnected Mode](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/update-licenses/update-licenses-in-disconnected-mode.html).

Once you deactivate a VCF Operations instance, if you want to reactivate it, the same licenses added to it prior the deactivation might not be available.

1. In the VCF Business Services console, navigate to License ManagementVCF Operations Registrations.
2. Click the vertical ellipsis next to VCF Operations instance you want to deactivate.
3. Click Deactivate.

   A dialog box appears.
4. In the Deactivate a VCF Operations Instance dialog box, click Deactivate.

The VCF Operations instance is deactivated. You can view it in the list of VCF Operations Registrations with a status Deactivated.