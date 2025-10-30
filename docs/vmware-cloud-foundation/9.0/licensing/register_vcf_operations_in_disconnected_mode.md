---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/register-vcf-operations/register-vcf-operations-in-disconnected-mode.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Register VCF Operations in Disconnected Mode
---

# Register VCF Operations in Disconnected Mode

You must register the VCF Operations instance that you want to use for license management with the VCF Business Services console. If your environment is disconnected from the Internet, you can register your VCF Operations instance in disconnected mode.

- Verify that you have a VCF Operations instance version 9.0.
- Verify that you have a valid subscription for a VMware product.

After you register your VCF Operations instance in disconnected mode, you must manually submit usage reports in the VCF Business Services console. Then you must update your licenses by importing a license file in the VCF Operations instance.

1. Log in to VCF Operations, and select License ManagementRegistration.
2. In the disconnected mode pane, click Download Registration File, and save the registration file.
3. Use a computer with Internet connection and log in to the VCF Business Services console (vcf.broadcom.com) with your Broadcom Support Portal credentials.
4. Select the Site ID to which you want to register this VCF Operations instance.

   If you have only one site, it is selected by default.
5. Navigate to License ManagementVCF Operations Registrations, and click New Registration.

   The New Registration wizard appears.
6. Click Browse, and upload the registration file that you downloaded from VCF Operations.
7. Click Save and Next.

   If you upload a registration file that is already used to register another VCF Operations instance, the operation fails with an error.
8. Enter a unique display name for your VCF Operations instance, and click Save and Next.

   By default the FQDN of VCF Operations is prepopulated as a display name when you start the registration process in the VCF Business Services console. The FQDN is only saved if you do not enter another display name. If you change the FQDN with another display name, the connectivity between VCF Operations and the VCF Business Services console is not impacted. You can change the display name at any time after the registration.

   If you do not want to include the FQDN in the registration details, you can use the following API:

   ```
   PUT {VCF_Ops_URI}/suite-api/api/deployment/config/globalsettings/GENERATE_DEFAULT_LICENSE_MANAGER_ASSET_NAME/false
   ```
9. Select licenses to add to your VCF Operations instance, and click Save and Next.
10. View the summary of the registration, and click Save and Next.

    To complete the registration, you download a license file and upload it in VCF Operations.
11. Download the license file, and click Finish.
12. In the VCF Operations instance, navigate to License ManagementRegistration.
13. In the disconnected mode pane, click Import License File.
14. In the Import License File dialog box, click Browse, and select and import the license file.
15. If you failed to download and import the license file, you can generate a new, valid license file, and import it in VCF Operations without registering again:
    1. In the VCF Business Services console console, navigate to License ManagementVCF Operations Registrations.
    2. Next to the VCF Operations instance you want to register, click on the vertical ellipsis button.
    3. From the actions menu, select Generate License File.

       A dialog box appears.
    4. When the license file is generated, download the file, and click Finish.
    5. To import the file in the VCF Operations instance, follow steps 12-14.
16. Click Complete.

- Add licenses to your VCF Operations instance. For more information, see [Add a License to VCF Operations.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/add-a-license-to-vcf-operations.html)
- Update the licenses at least once every 6 months. For more information about updating licenses, see [Update Licenses.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/update-licenses/updatelicenses.html)