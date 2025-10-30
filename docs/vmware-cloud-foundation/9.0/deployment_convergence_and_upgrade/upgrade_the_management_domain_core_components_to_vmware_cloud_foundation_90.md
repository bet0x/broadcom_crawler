---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrade the Management Domain Core Components to VMware Cloud Foundation 9.0
---

# Upgrade the Management Domain Core Components to VMware Cloud Foundation 9.0

To upgrade to VMware Cloud Foundation 9.0, the management domain must be at VMware Cloud Foundation 5.0 or higher. If your platform is at a version lower than 5.0, you must upgrade the management domain and all workload domains to 5.0 or later before you can upgrade to 9.0.

You can upgrade workload domains before or after upgrading the management domain, as long as all components in the workload domain are compatible.

Upgrade the core components in the management domain in the following order:

1. SDDC Manager and VMware Cloud Foundation services.
2. NSX Manager and NSX Global Manager instances (if applicable).
3. vCenter instance.
4. ESX hosts.

After all upgrades have completed successfully:

1. Remove the VM snapshots you took before starting the update.
2. Back up the newly installed components.