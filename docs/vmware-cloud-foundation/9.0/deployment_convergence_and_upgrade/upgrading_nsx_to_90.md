---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrading NSX to 9.0
---

# Upgrading NSX to 9.0

After, you have upgraded SDDC Manager to version 9, you must upgrade your NSX Manager cluster. It is recommended that you upgrade by using the streamlined, orchestrated process by using SDDC Manager. In rare cases the manual option for upgrade by using Upgrade Coordinator is also available.

## Determine Your Upgrade Type

You can select between the following upgrade types for your NSX deployment. The upgrade type you choose determines the method used to perform the upgrade.

| Upgrade Type | Description | Upgrade Method |
| --- | --- | --- |
| Automated Upgrade | - Recommended for most upgrade scenarios. - Upgrades edge nodes in serial order within a cluster. - Upgrades hosts in serial order. - Upgrades NSX VIBs automatically as part of ESX host upgrade. | SDDC Manager |
| Manual Upgrade | - Used for customized upgrade scenarios. - Can upgrade unit groups of edge nodes or groups of hosts in serial or parallel order. Within a cluster or unit group, edge nodes are always upgraded in serial order. - Can alternate between upgrading groups of edge nodes and groups of hosts. - Can upgrade NSX VIBs on hosts separately from ESX upgrade. This option is available only for ESX 8.x hosts. | NSX Manager and SDDC Manager |

## Points to Consider when Upgrading

- Do not perform upgrade tasks in SDDC Manager and at the same time. When an upgrade runs in SDDC Manager, the upgrade coordinator in the UI reflects the progress of the upgrade and vice versa.
- If you are performing an out-of-band upgrade, that is, instead of using VCF operations to perform the upgrade you choose to upgrade through any of the component's console (such as NSX Manager or vCenter) you still must upgrade in the following sequence:
  1. VCF Operations
  2. NSX Upgrade Coordinator
  3. NSX Manager
  4. Edge nodes
  5. vCenter
  6. NSX Finalize Upgrade
  7. ESX

## Checklist for Automated NSX Upgrade

Use the following checklist to track your work through the automated upgrade process.

| Automated Upgrade Task | Instructions |
| --- | --- |
| Evaluate the operational impact of the upgrade. | See [Operational Impact of the Upgrade](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/operational-impact-of-nsx-t-upgrade.html). |
| Run the pre-checks to verify that system components are ready for the upgrade. | See [Run the NSX Upgrade Pre-check Bundle](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/run-the-upgrade-precheck-pub-bundle.html). |
| Complete the pre-upgrade tasks. | See [Pre-Upgrade Tasks for Upgrading NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/pre-upgrade-tasks.html). |
| Verify that the NSX environment is in a healthy state. | See [Verify the Current State of NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/verify-the-nsxt-environment.html). |
| Make the required changes in your system configuration if your deployment contains features that are not supported in the target release. | See [Manage Unsupported Features](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/manage-deprecated-nsx-features.html). |
| In SDDC Manager, upgrade NSX Manager, edge nodes, vCenter, and the hosts. | See:   - [Automated Upgrade to NSX 9 by Using SDDC Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/upgrade-nsx-for-vcf-5-2.html) - [Upgrade to vCenter 9.0 for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrade-vcenter-server-for-vmware-cloud-foundation-5-2.html) - [Upgrade to ESX 9.0 for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrade-esxi-for-vmware-cloud-foundation-5-2-1.html) |
| Verify the upgrade. | See [Verify the Upgrade](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/verify-the-upgrade-nsxt.html). |