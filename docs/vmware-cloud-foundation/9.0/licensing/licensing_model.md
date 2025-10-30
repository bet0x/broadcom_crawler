---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/licensing-overview/licensing-model.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Licensing Model
---

# Licensing Model

Starting with version 9.0, the licensing model is the same for VCF and vSphere Foundation. You assign licenses only to vCenter instances. The other product components, including ESXi hosts, that are connected to the licensed vCenter instances, are licensed automatically.

## How Capacity Pooling Works

When you purchase multiple subscriptions for the same product, capacity is pooled together in one default license per product. For example, if you purchase a subscription for 200 cores for VCF, and then you purchase another subscription for 300 cores, you have one default license for the product with 500 cores total capacity, instead of two licenses with 200 and 300 cores capacity. If the different subscriptions have different end dates, the number of cores will be reduced on the end date of the subscription, but you can use the capacity for which you have an active subscription.

vSAN capacity, when purchased through VCF, vSphere Foundation, or a vSAN add-on also pools together in one default license. For example, when you purchase a subscription for 300 cores for VCF, and 50 TiBs as a vSAN add-on, you have one default license with 350 TiBs total capacity.

To pool together into the same default license, subscriptions must meet the following requirements:

- Must be for the same product, for example, VCF, or vSphere Foundation.
- Must have the same unit of measure, for example, cores or TiBs.
- Must have the same license (Site ID).
- Must not support overage billing. VMware Cloud Services Provider (VCSP) partner subscriptions are not eligible for pooling.

For some products, you receive multiple default licenses with one subscription. For example, VCF has both a default VMware Cloud Foundation license and a vSAN Enterprise license.

## What Are Primary Licenses

Primary licenses are the licenses for VCF and vSphere Foundation. They are per-core based. The only assets in your environment which consume the capacity of your primary licenses are ESX hosts. To calculate the capacity you need for your environment, you need the total number of the physical CPU cores for each physical CPU on all ESX hosts in your environment. Most products have a minimum consumption rule of 16 cores per physical CPU. CPUs that have fewer than 16 cores consume 16 cores. For example, if you have 1 ESX host in your inventory, with 1 CPU, and 8 CPU cores per CPU, this ESX host will use 16 cores of your license total capacity because it is the minimum license capacity.

| Number of ESX Hosts | Number of CPUs per Host | Cores per CPU | Required License Capacity |
| --- | --- | --- | --- |
| 1 | 1 | 8 | 16 |
| 2 | 2 | 8 | 64 |
| 2 | 2 | 16 | 64 |
| 2 | 2 | 24 | 96 |

For more information about calculating the license capacity you need for your environment, see Broadcom knowledge base article [95927](https://knowledge.broadcom.com/external/article?legacyId=95927).

You assign primary licenses to your vCenter instances. The other components of the product are licensed automatically with the license that you assign to the vCenter instance. For more information about the products and their components, see [Products and Product Components.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/licensing-overview/offerings-and-components.html)

To assign licenses to your vCenter instances, you use a VCF Operations instance. For more information about the licensing workflow, see [High-Level Licensing Workflow](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/licensing-overview/v9-licensing-overview.html).

The difference in the licensing model for VCF Edge and VMware Cloud Foundation is that VCF Edge has an 8 CPU cores per physical CPU minimum, and deployment limitations. For more information about VCF Edge license terms, see the [Specific Program Documentation](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/LegalNotices/VMware-Cloud-Foundation-Edge--VCFE--SPD/24503) for VCF Edge.

## Evaluation Mode

After you install a product or component, it operates in evaluation mode for up to 90 days. During that period, you must license your environment.

ESX hosts that you provision as stateless hosts by using Auto Deploy have no evaluation period in version 9.0.