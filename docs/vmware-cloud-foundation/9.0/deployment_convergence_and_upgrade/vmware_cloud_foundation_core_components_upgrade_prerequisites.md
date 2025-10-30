---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrade-prequisites.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > VMware Cloud Foundation Core Components Upgrade Prerequisites
---

# VMware Cloud Foundation Core Components Upgrade Prerequisites

Before you upgrade the VMware Cloud Foundation management domain, verify that the following prerequisites are satisfied.

You cannot upgrade VMware Cloud Foundation on Dell VxRail to VMware Cloud Foundation 9.0.

Upgrade Prerequisites



| Prerequisite | Additional Information |
| --- | --- |
| Allocate a temporary IP address for each vCenter appliance upgrade. | Required for each vCenter upgrade. Must be allocated from the management subnet. The IP address can be reused. |
| Verify that no vCenter appliance is joined to an Active Directory domain. | See [kB 373004](https://knowledge.broadcom.com/external/article/373004/leave-the-vcenter-server-from-active-dir.html). |
| Verify there are no expired or expiring passwords. | Review the password management dashboard in SDDC Manager. |
| Verify there are no expired or expiring certificates. | Review the Certificates tab in SDDC Manager for each workload domain. |
| Verify ESX host TPM module status. | [Conditional] If ESX hosts have TPM modules in use, verify they are running the latest 2.0 firmware. If not in use they must be disabled in the BIOS. See [KB 312159](https://knowledge.broadcom.com/external/article/312159/) |
| Verify ESX hardware is compatible with target version. | See [ESX Requirements](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/esx-installation-and-setup/installing-and-setting-up-esxi/esxi-requirements.html) and [Broadcom Compatibility Guide](https://compatibilityguide.broadcom.com/). |
| Manually update the vSAN HCL database to ensure that it is up-to-date. | See [KB 2145116](https://knowledge.broadcom.com/external/article?legacyId=2145116) |
| Back up SDDC Manager and all vCenter and NSX Manager instances. | Take file-based backups or image-based backups of SDDC Manager and all vCenter and NSX Manager instances. Take a cold snapshot of SDDC Manager. |
| Verify that there are no failed workflows in your system and none of the SDDC Manager resources are in activating or error state. | If any of these conditions are true, contact Broadcom Support before starting the upgrade. |
| Download the upgrade bundles. | See [Downloading VMware Cloud Foundation Upgrade Bundles for Core Components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles.html). |
| Review the Release Notes for known issues related to upgrades. |  |
| In the vSphere Client, verify there are no active alarms on hosts or vSphere clusters. |  |