---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrading Your VCF Management Domain to VMware Cloud Foundation 9.0
---

# Upgrading Your VCF Management Domain to VMware Cloud Foundation 9.0

As a mandatory part of the upgrade to version 9, you must upgrade your VMware Cloud Foundation management domain to version 9.0. Before you upgrade, it is important to understand how VCF 9.0 is different from earlier versions. Upgrading your workload domains is not a mandatory part of the upgrade and can be performed later as a day N procedure.

VMware Cloud Foundation 9.0 includes additional components that were not required in VCF 5.x.

Prior to 9.0, VCF included the following required components:

- SDDC Manager
- NSX Manager
- vCenter
- ESX

Optionally, you could deploy the management components part of the VMware Aria suite.

Starting with VCF 9, the previously optional management components VCF Operations (Aria Operations), VCF Operations fleet management (Aria Suite Lifecycle), and VCF Automation (Aria Automation) are now mandatory. The full list of required components for VCF 9.0 is:

- Core components (upgraded using SDDC Manager):
  - SDDC Manager
  - NSX Manager
  - vCenter
  - ESX
- Management components (upgraded manually or deployed in version 9 prior to upgrading the core components):

  - VCF Operations
  - VCF Operations fleet management
  - VCF Operations collector (for new deployments, deploy after the SDDC Manager upgrade)
  - VCF Automation

The following upgrade procedures use the SDDC Manager UI to upgrade VCF. The SDDC Manager UI is being deprecated and will be removed in a future release. After your upgrade to VCF 9.0 is complete, use VCF Operations to perform lifecycle management activities.

For information on how to upgrade your workload domains, see [Upgrading VMware Cloud Foundation 5.x Workload Domains to 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/upgrade-workload-domains-to-vcf-5-2.html).

## VMware Cloud Foundation 9.0 Management Domain Upgrade Overview

You can perform a sequential or skip-level upgrade to VCF 9.0 from VCF 5.0 or later. If your platform is at a version earlier than 5.0, you must upgrade the management domain and all workload domains to VCF 5.0 or later before you can upgrade to VCF 9.0.

The process depends on which, if any, VMware Aria management components you have deployed as part of VCF 5.x.

- [Preparing Your Management Components for VCF 9 Core Components Upgrade](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components.html)
- [Upgrade the Management Domain Core Components to VMware Cloud Foundation 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2.html)
- (Optional) [Completing the Deployment of Your Platform](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform.html)