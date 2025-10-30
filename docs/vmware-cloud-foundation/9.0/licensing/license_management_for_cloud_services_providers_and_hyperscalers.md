---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/license-management-for-cloud-services-providers-and-hyperscalers.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > License Management for Cloud Services Providers and Hyperscalers
---

# License Management for Cloud Services Providers and Hyperscalers

Starting with version 9.0 of VMware Cloud Foundation (VCF) and VMware vSphere Foundation (vSphere Foundation), you license your environment by using a VCF Operations instance and the VMware Cloud Foundation Business Services console ([vcf.broadcom.com](http://vcf.broadcom.com)). License files replace the use of the 25-character license keys.

## Cloud services providers and hyperscalers requirements

To manage licenses as a provider (either cloud services provider or hyperscaler), you must meet the following requirements.

- Verify that you are enrolled in the Broadcom Advantage Partner Program.
- Verify that you have an account in Broadcom Support Portal.
- Verify that you have an active commit contract with Broadcom.
- Verify that you have installed VCF Operations 9.0 and vCenter 9.0. The vCenter should be associated with VCF Operations.

## What's new?

- License keys are no longer used. To license your environment, in the Broadcom Support Portal, you must sign a commit contract that is associated with a commit capacity. The capacity is displayed in the unit of measure for the specific product. For example, for VCF you specify the number of cores in the contract, and you also receive a default license for vSAN with a number of TiBs that equals the number of cores that you commit a contract for. For example, if you sign a commit contract for VCF for 500 cores, you also receive 500 TiBs of vSAN, which are added in a separate license.
- The signed commit contract can be TFC or non-TFC, depending on the termination of contract clauses.
- Once a commit contract is signed and available in the Broadcom Support Portal, you must create licenses against the contract serial number and the product in the contract.

- For TFC commit contracts, when you create new licenses, the capacity you allocate for the licenses can exceed the commit capacity. The entitlement for the maximum license capacity is 125 percent of the commit capacity. If the total allocated capacity in the created licenses reaches the maximum capacity, you can no longer create new licenses.
- For non-TFC commit contracts, the entitlement is 100 percent of the committed license capacity. The maximum capacity is the same as the commit capacity. You cannot exceed the commit capacity. If the total allocated capacity in the created licenses reaches the commit capacity, you can no longer create new licenses.
- If the license usage against the deployed licenses exceeds the commit capacity, you might get billed for over use.
- End customers can share licenses for portability with you if you both meet certain requirements. For more information, see [License Sharing](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/license-sharing/license-sharing(1).html).
- To license your environment, you must have an installed VCF Operations instance, register it in the VCF Business Services console, and add licenses with available capacity. You can register VCF Operations to the VCF Business Services console either in connected or in disconnected mode. Connected registration is recommended for cloud services providers and hyperscalers.

- You must update your licenses at least once every 6 months. For more information, see [Updating Licenses](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/update-licenses.html).
- You assign licenses only to the vCenter instances. The other product components added to the licensed vCenter instances are then automatically licensed. For more information about products and product components, see [Products and Product Components.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/licensing-overview/offerings-and-components.html)
- To collect the billable license usage, you must deploy a VCF usage meter instance. VCF usage meter collects the license configurations in the metered environments and communicates the data to the cloud. The data is converted to core usage per hour for each license and sent ot Broadcom for billing.
- You must register the VCF usage meter instance in the VCF Business Services console. The billed data is available in the VCF Business Services console for partners to download and review.

## License Management Between Tenants and Sites

You can manage licenses in all the tenants of the sites you belong to. However, you cannot transfer licenses between tenants. You must register the VCF Operations instance in the same tenant as the licenses you want to add. If you register the VCF Operations in a wrong tenant, you can deactivate the VCF Operations instance and restart the registration in the correct tenant. If you have added licenses, the licenses must first be removed before deactivating the VCF Operations instance.