---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrading-management-components.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrading Management Components with VMware Aria Suite Lifecycle to Version 9
---

# Upgrading Management Components with VMware Aria Suite Lifecycle to Version 9

You can upgrade your version 8 VMware Aria components, deployed as part of a VCF 5.x or vSphere 8.x environments, to version 9. The upgrade procedure uses both the VMware Aria Suite Lifecycle 8.18 appliance and the VCF Operations fleet management appliance that is deployed as part of the VMware Aria Operations upgrade to VCF Operations version 9.0.

Version 8 Aria Component Upgrade Scenarios

The following Aria component versions are supported for upgrade using the VMware Aria Suite Lifecycle 8.18 appliance. An outline of the upgrade path is provided for each deployment scenario.



| Aria component deployed | Supported versions for upgrade | Upgrade path |
| --- | --- | --- |
| VMware Aria Operations only | VMware Aria Operations 8.14 or later. | 1. Download and apply VMware Aria Suite Lifecycle 8.18 Patch 2 or later. 2. Use VMware Aria Suite Lifecycle to upgrade to VCF Operations and install the fleet management appliance. |
| VMware Aria Automation only | VMware Aria Automation 8.18 or later | 1. Install VMware Aria Operations 8.18 2. Download and apply VMware Aria Suite Lifecycle 8.18 Patch 2 or later. 3. Use VMware Aria Suite Lifecycle to upgrade to VCF Operations and install the fleet management appliance. 4. Use the fleet management appliance to upgrade to VCF Automation. |
| VMware Aria Operations for Networks with VMware Aria Operations and VMware Aria Automation | VMware Aria Operations 8.14 or later.  VMware Aria Automation 8.18 or later  VMware Aria Operations for Networks 6.13 or later | 1. Download and apply VMware Aria Suite Lifecycle 8.18 Patch 2 or later. 2. Use VMware Aria Suite Lifecycle to upgrade to VCF Operations and install the fleet management appliance. 3. Use the fleet management appliance to upgrade to VCF Automation and VCF Operations for networks. |

Because you will use the VCF Operations fleet management appliance to upgrade management components, you must have VMware Aria Operations installed in your environment so that you can upgrade it to VCF Operations. If VMware Aria Operations is not installed, follow these instructions to add it to your VMware Aria Suite Lifecycle environment: [Add a product to an existing private cloud environment](https://techdocs.broadcom.com/us/en/vmware-cis/aria/aria-suite-lifecycle/8-18/vmware-aria-suite-lifecycle-installation-upgrade-and-management-8-18/managing-environments/add-a-product-to-an-existing-private-cloud-environment.html).

After upgrading your existing VMware Aria components, you must deploy any missing management components before upgrading your management domain. See [Deploy VCF Operations for VMware Cloud Foundation 9 Core Components Upgrade](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/preparing-to-upgrade-to-vmware-cloud-foundation.html).

VMware Aria Operations for Logs and Workspace One Access (formerly VMware Identity Manager) cannot be upgraded to version 9 and must be manually deployed after VCF Operations is at version 9. See [Completing the Deployment of Your Platform](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform.html). VMware Aria Operations for Logs users who want to migrate data from version 8 to version 9 can perform the migration after installing VCF Operations for logs.