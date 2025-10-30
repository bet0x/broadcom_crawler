---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/licensing-overview/offerings-and-components.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > 9.0 Products and Product Components
---

# 9.0 Products and Product Components

VMware Cloud Foundation and vSphere Foundation include different sets of product components. You purchase a subscription for a specific product. With the provided default primary license, you license all product components by using a registered VCF Operations instance.

For example, when you purchase a subscription for VCF, with the license you receive and assign to a vCenter instance, all components connected to that vCenter instance are licensed automatically. With your subscription for a product, you also receive license keys for the earlier version of the product and product components. You can decide which version of the product to deploy and license, but your total license usage must not exceed your purchased subscription capacity.

| Purchased Product | **Pre-Version 9 License Key Examples** | **Version 9 License Equivalent** |
| --- | --- | --- |
| VMware Cloud Foundation (VCF) | - VMware Aria Operations Networks - VMware Aria Suite Enterprise 8.14 for Cloud Foundation - VMware Cloud Director - VMware HCX Enterprise - VMware HCX Advanced - VMware NSX Networking for Cloud Foundation - VMware SDDC Manager 5.x for Cloud Foundation - VMware vCenter Server 8 Standard Term License per Instance - VMware vSphere 8 Enterprise Plus for Cloud Foundation (Supports vCenter Server 8.0.0a and above) - VMware Tanzu Kubernetes Grid for vSphere Foundation | VMware Cloud Foundation (cores) |
| VMware vSAN 8 for Foundation (Supports vCenter Server 8.0u3 and above) | VMware vSAN (TiB) |

Additionally, you can purchase subscriptions for add-ons which are compatible with your products. For information about available add-ons for each product, contact your sales team. Add-ons do not necessarily follow the licensing model that VCF and vSphere Foundation have. You can find information about how to license a specific add-on within their respective documentation.

To use VCF Operations for logs, you must integrate it with a vCenter instance of version 9 that is licensed with a VMware vSphere Foundation license or a VMware Cloud Foundation license. At least one vCenter integration must be configured to collect logs directly into a VCF Operations for logs cluster, as opposed to collecting logs by using a collector or a collector group.