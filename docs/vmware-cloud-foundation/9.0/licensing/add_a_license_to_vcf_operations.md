---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/add-a-license-to-vcf-operations.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Add a License to VCF Operations
---

# Add a License to VCF Operations

To license your environment, you must first add licenses to the VCF Operations instance that you registered with the VCF Business Services console.

- Verify that you have a valid subscription for VCF or vSphere Foundation.
- Verify that your VCF Operations instance is registered with the VCF Business Services console.

After you add licenses to your VCF Operations instance, you can assign those licenses to the vCenter instances.

You can add any capacity to your VCF Operations, up to what you have purchased. A license cannot be added to more than one VCF Operations instance at a time.

1. In the VCF Business Services console, navigate to License ManagementLicenses.
2. Click Add to VCF Operations.

   The Add Licenses to a VCF Operations Instance wizard appears.
3. Select the licenses that you want to add, and click Next.
4. Select the VCF Operations instance to which you want to add the licenses, and click Next.
5. View the summary, and click Save and Next.
6. If your registration is in disconnected mode, download the license file, and click Finish.
7. To complete the process and have your licenses ready to assign to vCenter instances, update your licenses in the VCF Operations instance.

   |  |  |
   | --- | --- |
   | Registration in connected mode | Navigate to License ManagementRegistration, and click Update Licenses. |
   | Registration in disconnected mode | 1. Navigate to License ManagementRegistration. 2. Click Import License File. 3. In the Import License File pop-up window, click Browse. 4. Upload the license file, and click Complete. |

The licenses are added to the VCF Operations instance. To view the license list in VCF Operations, navigate to License ManagementLicenses, and select the Version 9+ tab.