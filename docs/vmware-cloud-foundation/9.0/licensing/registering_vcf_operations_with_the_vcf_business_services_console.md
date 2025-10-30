---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/register-vcf-operations.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Registering VCF Operations with the VCF Business Services console
---

# Registering VCF Operations with the VCF Business Services console

Starting with version 9.0, you access and manage the licenses for your environment by using VCF Operations and the VCF Business Services console. You must register the VCF Operations instance with the VCF Business Services console.

You must install a VCF Operations instance version 9.0 in order to access and manage your licenses. If you want to access and manage your 9.0 licenses, and you already have an earlier version of VCF Operations installed, you must upgrade the instance to version 9.0.

If you want to use a VCF Operations instance only for monitoring your assets, and not for license management, you do not need to register it with the VCF Business Services console. If used for monitoring purposes only, the VCF Operations instance is automatically licensed with the license assigned to the vCenter instances of version 9 added to it if those vCenter instances are licensed from another VCF Operations instance.

After you deploy or upgrade your VCF Operations instance to version 9.0, it works in evaluation mode for up to 90 days. During that period you must register VCF Operations in the VCF Business Services console and license your environment.

You can use specific VCF Operations capabilities based on the primary license that is assigned to each vCenter.

| Product | VCF Operations Capabilities |
| --- | --- |
| VCF | License Management, Monitoring, Fleet Management |
| vSphere Foundation | License management, Monitoring |

One VCF Operations instance can manage a mix of version 9.0 licenses.

You can choose whether to register your VCF Operations instance in connected or disconnected mode.

- In disconnected mode, to register VCF Operations, you must manually transfer files between the VCF Operations instance and the VCF Business Services console. After the registration, you must manually transfer files to report license usage, and to update licenses.
- In connected mode, VCF Operations registration does not require manual transfer of files, the registration is performed by using an activation code. After the registration, usage reporting is automated, and the update of licenses is simplified.

To use VCF Operations for licensing, verify that the Virtual Management Infrastructure (VIM) adapter is running.

By default the FQDN of VCF Operations is prepopulated as a display name when you start the registration process in the VCF Business Services console. The FQDN is only saved if you do not enter another display name. If you change the FQDN with another display name, the connectivity between VCF Operations and the VCF Business Services console is not impacted. You can change the display name at any time after the registration.

If you do not want to include the FQDN in the registration details, you can use the following API:

```
PUT {VCF_Ops_URI}/suite-api/api/deployment/config/globalsettings/GENERATE_DEFAULT_LICENSE_MANAGER_ASSET_NAME/false
```

**How to view the detailed contents of your registration file**

If your VCF Operations instance is in connected mode, the registration details are sent automatically by using a combination of query string parameters and API parameters. If your VCF Operations instance is in disconnected mode, you must manually download the registration information as a JSON Web Signed (JWS) file. The information provided to Broadcom for registration is equivalent between connected and disconnected mode, but sent in different formats.

You can view the registration file contents only in disconnected mode.

1. From the VCF Operations instance, navigate to License ManagementRegistration, and click Download Registration File.
2. Use a text editor to open the file, and copy the content.
3. Paste the content of the registration file into a JWT decoding tool.

After the content is decoded, you can view the collected registration information.

Registration File Content



| Property | Description |
| --- | --- |
| model\_version | File format version: 1.0.0. |
| asset\_name | The FQDN of the VCF Operations instance. It is pre-populated as display name for the instance in the VCF Business Services console. This is ONLY saved by Broadcom if you choose to keep the display name the same as the FQDN. |
| created\_on | Date and time when the registration file was created. |
| asset\_type | AC |
| xr2 | A unique opaque fingerprint of the VCF Operations instance. It is used in conjunction with the asset\_id to link subsequent usage data to the registered VCF Operations instance. No identifiable details about your environment can be derived from the fingerprint. |
| asset\_id | The unique ID of the VCF Operations instance you register with this file. |
| request\_id | Unique ID of the registration file. |