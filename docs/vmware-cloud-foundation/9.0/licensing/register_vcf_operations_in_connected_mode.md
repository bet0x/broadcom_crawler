---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/register-vcf-operations/register-vcf-operation-in.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Register VCF Operations in Connected Mode
---

# Register VCF Operations in Connected Mode

You must register the VCF Operations instance that you want to use for license management with the VCF Business Services console. If your environment is connected to the Internet, you can register your VCF Operations instance in connected mode. Connected mode provides a faster and simplified registration process, and makes updating your licenses easier. Connected mode is recommended for anyone who has an Internet connection.

- Verify that you have a valid subscription for VCF or vSphere Foundation.
- Verify that your VCF Operations instance is connected to the Internet. If you need to configure an Internet proxy, see [Configuring Cloud Proxies in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-alerts-and-actions/outbound-settings/configuring-http-s-proxy.html).
- Verify that you have either a user administrator or a product administrator role in your support site to access the VCF Business Services console. Alternatively, a user administrator must give you tenant access.

1. Log in to VCF Operations, and select License ManagementRegistration.
2. In the connected mode pane, click Start Registration.

   The VCF Business Services console opens in a new tab.
3. Log in to the VCF Business Services console by using your Broadcom Support Portal credentials.

   The registration wizard appears.
4. Select the Site ID to which you want to register this VCF Operations instance and click Next.

   If you have only one site, it is selected by default.
5. Enter a unique display name for your VCF Operations instance, and click Save and Next.

   By default the FQDN of VCF Operations is prepopulated as a display name when you start the registration process in the VCF Business Services console. The FQDN is only saved if you do not enter another display name. If you change the FQDN with another display name, the connectivity between VCF Operations and the VCF Business Services console is not impacted. You can change the display name at any time after the registration.

   If you do not want to include the FQDN in the registration details, you can use the following API:

   ```
   PUT {VCF_Ops_URI}/suite-api/api/deployment/config/globalsettings/GENERATE_DEFAULT_LICENSE_MANAGER_ASSET_NAME/false
   ```
6. Select licenses to add to your VCF Operations instance, and click Save and Next.

   To license your environment, you must add a primary license to your VCF Operations instance. You can add licenses during the registration process, or at any time after that.
7. View the summary of the registration, and click Generate Activation Code.

   To complete the registration, you must copy the activation code and enter it in VCF Operations .
8. Click Copy, and click Finish.
9. In the VCF Operations instance, navigate to License ManagementRegistration.
10. In the connected mode pane, click Enter Activation Code.
11. Paste the activation code, and click Activate.
12. If you failed to copy and paste the activation code, you must generate a new, valid activation code, and paste it in VCF Operations:
    1. In the VCF Operations instance, navigate to License ManagementRegistration.
    2. In the connected mode pane, click Start Registration.

       The VCF Business Services console opens in a new tab.
    3. Log in to the VCF Business Services console by using your Broadcom Support Portal credentials.
    4. Select the Site ID to which you want to register this VCF Operations instance and click Next.

       A new activation code is presented.
    5. Copy the activation code and click Finish.
    6. To paste the code in the VCF Operations instance, follow steps 8-10.

- Add licenses to your VCF Operations instance. For more information, see [Add a License to VCF Operations.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/add-a-license-to-vcf-operations.html)
- Update the licenses at least once every 6 months. For more information about updating licenses, see [Update Licenses.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/update-licenses/updatelicenses.html)