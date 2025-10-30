---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/licensing-overview/pre-version-9-licenses-and-support.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Mixed-Version Environments
---

# Mixed-Version Environments

If you have pre-version 9.0 product components, for example vCenter instances, ESX hosts, NSX, you can continue to use license keys to license capabilities of those components without any changes. If you use a VCF Operations instance for license management, you must update the instance to manage version 9+ licenses.

You can add ESX 8.x hosts that are licensed with license keys to your vCenter instances of version 9. Those ESX hosts must be licensed with a version 8 license. Select a license that has the same feature list as your version 9 license.

In a VMware Cloud Foundation Instance, the management domain of version 9.0 can manage workload domains of version 5.x and 9.0.

Example of Mixed-Version Environment

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/fe65521b-de78-4921-8ad0-adc9316a8902.original.svg)

License usage data is collected for version 9 licenses, and for licenses of earlier versions connected to VCF Operations. You can view both your version 9 and pre-version 9 license usage data by using the usage analytics available in VCF Operations and the VCF Business Services console.

When you upgrade your vCenter instances to version 9, they operate in evaluation mode for up to 90 days. During that period, you must license the vCenter instances with a primary license of version 9+ with sufficient capacity. The license must be for the product you want to use.