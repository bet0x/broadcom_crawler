---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/reactivate-a-vcf-operations-instance.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Reactivate a VCF Operations Instance
---

# Reactivate a VCF Operations Instance

You can reactivate a deactivated VCF Operations instance.

If you want to restore the same license configuration that was in use before the VCF Operations instance deactivation, add the same licenses to the instance that were added before the deactivation. If those licenses are not available, add new licenses to the instance.

1. In the VCF Business Services console, navigate to License ManagementVCF Operations Registrations.
2. Click the VCF Operations instance that you want to reactivate.

   The details and licenses page for the instance appears.
3. Click Reactivate.

   A dialog box appears.
4. In the Reactivate VCF Operations dialog box, click Reactivate.
5. Add licenses to the VCF Operations instance. For information on how to add licenses, see [Add a License to VCF Operations.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/add-a-license-to-vcf-operations.html)
6. Update your registration with the VCF Business Services console.

   |  |  |
   | --- | --- |
   | Connected Registration | 1. In the VCF Business Services console, click the vertical ellipsis next to the VCF Operations instance. 2. Click Generate Activation code. 3. In the Generate Activation Code dialog box, copy the activation code, and click Finish. 4. In the VCF Operations instance, navigate to License ManagementRegistration. 5. Click ActionsEnter Activation Code. 6. In the Enter Activation Code dialog box, paste the activation code, and click Activate. |
   | Disconnected Registration | 1. In the VCF Operations instance, navigate to License ManagementRegistration, and click Generate Usage File. 2. In the VCF Business Services console, navigate to License ManagementVCF Operations Registration, and click Upload Usage File. 3. In the Upload Usage File wizard, click Browse and upload the usage file that you generated in the VCF Operations instance. 4. Click Save and Next. A license file is generated. 5. Download the license file, and click Finish. 6. In the VCF Operations instance, navigate to License ManagementRegistration, and click Import License File. 7. In the Import License File dialog box, click Browse and import the license file. 8. Click Complete. |

Your VCF Operations instance is reactivated and you can use it for license management. If you used the licenses that were previously added, you do not need to assign the license to the already licensed vCenter instances managed by this VCF Operations instance prior to its deactivation.