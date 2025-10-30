---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/licensing-overview.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Licensing Overview
---

# Licensing Overview

Starting with version 9.0 of VMware Cloud Foundation (VCF) and VMware vSphere Foundation (vSphere Foundation), you license your environment by using a VCF Operations instance and the VMware Cloud Foundation Business Services console ([vcf.broadcom.com](http://vcf.broadcom.com)). Subscription-based license files replace the use of the 25-character license keys.

## What's New in 9.0?

- License keys are no longer used. To license your environment, you purchase a term-based subscription for a product, with a specified capacity.
- A license is an object that entitles you to use the products that you purchased subscriptions for. A license can span multiple subscriptions or, when you split the default license, a license can be a portion of a subscription.
- The initial license that is automatically created in VCF Business Services console after you purchase a subscription is called a default license. The default license is a pool of capacity from all active subscriptions of the same product in the same Site ID. Available capacity is displayed in the unit of measure for the specific product.

  For example, if you purchase a VCF subscription for 500 cores, you receive a default license for 500 cores of VCF and you also receive a default license of 500 TiBs of vSAN, which are added in a separate license. If, on top of that, you purchase a vSAN add-on subscription for 200 TiBs, the new number of TiBs is added to your default vSAN license, and its capacity becomes 700 TiBs.

For more information about using your Broadcom Site ID, see [knowledge base article 142873](https://knowledge.broadcom.com/external/article/142873/using-your-broadcom-site-ids-for-full-su.html#:~:text=This%20guide%20will%20walk%20you,your%20product%20licenses%20and%20entitlements).

- There are two types of licenses - primary licenses, such as VMware Cloud Foundation and VMware vSphere Foundation licenses, and add-on licenses, such as vSAN add-on capacity or VMware Private AI Foundation with NVIDIA licenses. You no longer license individual components such as NSX, HCX, VCF Automation, and so on. Instead, for VCF and vSphere Foundation, you have a single license capacity provided for that product.

  For example, for VMware Cloud Foundation, the single license capacity provided for that product is VMware Cloud Foundation (cores). This is a primary license and you must assign it to your environment before you can assign an add-on license. Components are licensed automatically after you assign the primary license to a vCenter instance. For VCF and vSphere Foundation, you also receive VMware vSAN (TiB)capacity. You also receive VMware vSAN (TiB) capacity when you purchase vSAN as an add-on. The vSAN TiB license is called an add-on license.
- In VCF 9.0, the two supported add-on licenses using the new licensing system are VMware vSAN (TiB) and VMware Private AI Foundation with NVIDIA (cores).

- To license your environment, you must have an installed VCF Operations instance, register it in the VCF Business Services console, and add licenses with available capacity. You can register VCF Operations to the VCF Business Services console either in connected or in disconnected mode. Internet connection is not required to register but connected registration is recommended because it simplifies license management. You assign licenses only to the vCenter instances. The other product components added to the licensed vCenter instances are then automatically licensed. For more information about products and product components, see [Products and Product Components.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/licensing-overview/offerings-and-components.html)

- License usage reports are required at least once every 180 days to maintain your licenses and you must update your license to confirm that the license usage report was submitted. If VCF Operations is registered in connected mode, this data is sent to the VCF Business Services console automatically, and licenses can be updated with a button click. If VCF Operations is registered in disconnected mode, to report license usage, you generate a usage file and upload it in the VCF Business Services console (vcf.broadcom.com). For detailed instructions for both connected and disconnected registration modes, see [Updating Licenses.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/update-licenses.html)
- License expiration applies if the subscription expires or if usage is not reported and the license is not refreshed:
  - Notifications are displayed before the license expiration.
  - After the license expires, you have 90 days to update your license. License assignments are impacted during this 90 day period and notifications appear in most components, including VCF Operations and vCenter.
  - 90 days after the expiration, your environment is impacted in several ways, including:
    - Management operations of various components might be prevented;
    - ESX hosts disconnect from vCenter, most host management operations are prevented;
    - You cannot create or start workloads.

      Existing workloads are not proactively stopped.
  - You can recover expired environments by downloading an updated license.

- With your subscription for a product, you receive both a version 9.0 default license, and license keys for version 8.x of the product. You can decide which version of the product to deploy and license, but your total usage must not exceed your purchased capacity. For more information, see [Products and Product Components.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/licensing-overview/offerings-and-components.html)
- You can check your license consumption analytics in your VCF Operations instance, and the VCF Business Services console. For more information about usage analytics, see [License Usage Analytics](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/license-usage-analytics.html).