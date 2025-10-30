---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/upgrade-workload-domains-to-vcf-5-2.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Upgrading VMware Cloud Foundation 5.x Workload Domains to 9.0
---

# Upgrading VMware Cloud Foundation 5.x Workload Domains to 9.0

To upgrade to a VMware Cloud Foundation 5.x workload domain to 9.0, all workload domains must be at VMware Cloud Foundation 5.0 or higher. If any workload domain is at a version lower than 5.0, you must upgrade it to 5.0 and then upgrade to 9.0.

You can use VCF Operations or the SDDC Manager UI to upgrade your VMware Cloud Foundation 5.x workload domains to 9.0. The following procedures use the SDDC Manager UI.

The SDDC Manager UI is being deprecated and will be removed in a future release. After upgrading your workload domains to 9.0, use VCF Operations to perform lifecycle management of VMware Cloud Foundation components.

The steps and the order of steps to upgrade a workload domain are similar to the steps to upgrade the management domain.

| Task | Procedure |
| --- | --- |
| 1. Plan the upgrade. | [Plan a Workload Domain Upgrade](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/upgrade-workload-domains-to-vcf-5-2/plan-workload-domain-upgrade.html) |
| 2. Perform an update precheck. | [Perform Update Precheck in SDDC Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/perform-upgrade-precheck.html) |
| 3. Upgrade NSX in a federated environment. | [Upgrading NSX in a Federated Environment](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/upgrade-nsx-in-a-federated-environment.html) |
| 4. Upgrade NSX. | [Upgrading NSX to 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9.html) |
| 5. Upgrade vCenter. | [Upgrade to vCenter 9.0 for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrade-vcenter-server-for-vmware-cloud-foundation-5-2.html) |
| 6. Transition from vLCM baselines to vLCM images. | [Transitioning from vSphere Lifecycle Manager Baselines to vSphere Lifecycle Manager Images](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/vlcm-baseline-to-vlcm-image-cluster-transition-.html) |
| 7. Upgrade ESX. | [Upgrade to ESX 9.0 for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrade-esxi-for-vmware-cloud-foundation-5-2-1.html) |
| 8. Upgrade vSphere Supervisor on clusters that have Workload Management enabled. | See "Updating vSphere Supervisor" in the vSphere documentation. |
| 9. Upgrade vSphere Distributed Switch version | [Upgrade vSphere Distributed Switch Versions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrade-vsphere-distributed-switch-versions.html) |
| 10. Upgrade vSAN on-disk format versions. | [Upgrade vSAN On-Disk Format Versions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrade-vsan-on-disk-format-versions.html) |
| 11. Post upgrade steps for NFS-based workload domains | [Post Upgrade Steps for NFS-Based Workload Domains](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/upgrade-workload-domains-to-vcf-5-2/post-upgrade-steps-for-nfs-based-workload-domains.html) |

After all upgrades have completed successfully:

1. Remove the VM snapshots you took before starting the update.
2. Take a backup of the newly installed components.