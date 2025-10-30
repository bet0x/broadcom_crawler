---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/vlcm-baseline-to-vlcm-image-cluster-transition-.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Transitioning from vSphere Lifecycle Manager Baselines to vSphere Lifecycle Manager Images
---

# Transitioning from vSphere Lifecycle Manager Baselines to vSphere Lifecycle Manager Images

vSphere Lifecycle Manager baselines are not supported with VMware Cloud Foundation 9.0. Before you can upgrade to ESX 9.0, you must transition any clusters that use vSphere Lifecycle Manager baselines to use vSphere Lifecycle Manager images. This applies to both management and VI workload domain clusters.

You can transition to vSphere Lifecycle Manager images using:

- A PowerShell script

  - Menu-driven interface
  - Command-line interface (CLI)
- The SDDC Manager API

You should transition all clusters in the management domain and in all workload domains after SDDC Manager is upgraded to 9.0. If this is not possible, or if you have vSphere Supervisor (Workload Management) enabled, transition any remaining vSphere Lifecycle Manager baseline clusters after upgrading vCenter and before upgrading ESX.

Learn about planning considerations, prerequisites, and tasks for transitioning ESX clusters from vSphere Lifecycle Manager baselines (formerly known as VMware Update Manager or VUM) to vSphere Lifecycle Manager images within a VMware Cloud Foundation workload domain. This process is for transitioning clusters that are already managed by SDDC Manager. For clusters that are not managed by SDDC Manager, you can transition to vSphere Lifecycle Manager images using the vSphere Client. See [Convert a Cluster or a Host That Uses Baselines Into a Cluster or a Host That Uses vSphere Lifecycle Manager Images](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/managing-host-and-cluster-lifecycle/using-images-to-install-and-update-esxi-hosts-and-clusters/switching-from-baselines-to-images.html).

For clusters managed via SDDC Manager, the transition must be performed via SDDC Manager supported mechanisms only.