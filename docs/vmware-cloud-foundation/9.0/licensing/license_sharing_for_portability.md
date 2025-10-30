---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/license-sharing/license-sharing(1).html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > License Sharing for Portability
---

# License Sharing for Portability

The manual process for sharing a license for portability is now automated.

## License Sharing for Portability Requirements

Apart from the requirements the provider must meet for license management, providers must also be certified for portability with the Broadcom Advantage Partner Program.

## Licenses Eligible for Sharing for Portability

The following licenses are eligible for sharing.

- VCF licenses
- Add-on licenses used with VCF offering. The end customer must have validated licenses for VCF as well.

## High-level License Sharing for Portability Workflow

1. The end customer creates a license of the desired capacity by splitting a default license within available capacity.
2. The provider then validates the license ID and site ID through APIs.
3. Depending on the management of the VCF Operations instance, the provider or/and end customter must have an installed VCF Operations instance and register it in the VCF Business Services console.
4. The VCF Operations instance can be provider managed or customer managed.

   1. If a provider manages the VCF Operations instance, the provider downloads a registration file for the VCF Operations instance in disconnected mode and passes the file to the end customer. The end customer then registers the VCF Operations instance in the tenant that contains the licenses they want to use for portability. After successful registration of the VCF Operations instance, the end customer receives a license file. The end customer must download the file and pass it back to the provider. The provider must upload the license file in the VCF Operations instances in disconnected mode. The provider can then switch to connected mode.
   2. If the end customer manages the VCF Operations instances and workload, after the provider gives the customer access to VCF Operations, the VCF Operations registration and license management are performed by the end customer.
5. The provider deploys VCF usage meter appliance and registers it in the VCF Business Services console for license usage reporting.