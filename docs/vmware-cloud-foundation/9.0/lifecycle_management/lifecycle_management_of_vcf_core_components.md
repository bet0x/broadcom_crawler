---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Lifecycle Management of VCF Core Components
---

# Lifecycle Management of VCF Core Components

Use VCF Operations to manage upgrade, patch, and install binaries for SDDC Manager, vCenter, NSX Manager, and ESX.

When you update your VCF environment to a maintenance release version (x.y.z), you first update your management components that operate on the fleet level before you update the core components in your instances. For the management components, start with the VCF Operations fleet management appliance, followed by the VCF Operations instance and then proceed with the remaining components in your preferred order. For the core components, start with SDDC Manager, followed by NSX, vCenter, ESX hosts, and vSAN. See [Lifecycle Management of VCF Management Components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab.html).

Before you can use the binaries for lifecycle management, you must download them to SDDC Manager. The method you use to download binaries depends on how you access the internet in your environment.

- Online depot: The SDDC Manager appliance can connect to the internet, either directly or through a proxy.
- Offline depot: The SDDC Manager appliance cannot connect to the internet, but can connect to a computer with internet access.
- No depot: The SDDC Manager appliance cannot connect to the internet or to a computer with internet access.

You can also use VCF Operations to manage ESX components and vSphere Lifecycle Manager images.