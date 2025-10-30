---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/license-management-for-cloud-services-providers-and-hyperscalers/register-vcf-operations-(for-vcsps).html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Register VCF Operations as a Provider
---

# Register VCF Operations as a Provider

If the VCF Operations instance is provider managed, you should register it in connected mode.

Verify that you register the VCF Operations in the correct site and tenant.

The registered VCF Operations instance can be

- fully provider managed
- both customer and provider managed (applicable to white label customers)

If the VCF Operations is fully provider managed, you register the VCF Operations instance in connected or disconnected mode and manage all the licenses for the end customers within the tenant.

If both a customer and provider manage the VCF Operations instance, you must start the registration in disconnected mode and then pass the activation code to the end customer to enter into the VCF Operations instance. For more information, see [Register VCF Operations in Connected Mode](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/register-vcf-operations/register-vcf-operation-in.html) and [Register VCF Operations in Disconnected Mode](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/register-vcf-operations/register-vcf-operations-in-disconnected-mode.html).

When you add licenses in the VCF Business Services console, you can only select from existing licenses. Add only licenses created in the same tenant as the one you register the VCF Operations instance in.