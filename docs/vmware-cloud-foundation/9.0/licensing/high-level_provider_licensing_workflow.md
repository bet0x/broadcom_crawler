---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/license-management-for-cloud-services-providers-and-hyperscalers/high-level-cloud-services-provider-and-hyperscalers-licensing-workflow.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > High-Level Provider Licensing Workflow
---

# High-Level Provider Licensing Workflow

1. Install a VCF Operations instance version 9.0, or upgrade your existing Aria Operations instance to VCF Operations 9.0.
2. Register your VCF Operations instance with the VCF Business Services console by using one of the two modes:

   1. Disconnected mode - no Internet connection is required. You must manually exchange registration and license file between the VCF Operations instance and the VCF Business Services console. The file exchange must occur for every license adjustment and every 6 months at a minimum or the environment becomes out of compliance.
   2. Connected mode - Internet connection is required. You use an activation code from the VCF Business Services console to register your VCF Operations instance.
3. Add licenses to the VCF Operations instance from the VCF Business Services console, and update the license list in VCF Operations.
4. Assign licenses to vCenter instances from VCF Operations.
5. Deploy or upgrade a VCF usage meter appliance to version 9.0.