---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Shutting Down VMware Cloud Foundation
---

# Shutting Down VMware Cloud Foundation

To avoid data loss and maintain the SDDC components operational, you follow a specific order when shutting down the management virtual machines in VCF.

- Verify that you have complete backups of all management components.
- Verify that the management virtual machines are not running on snapshots.
- If a vSphere Storage APIs for Data Protection (VADP) based backup solution is running on the management clusters, verify that the solution is properly shut down by following the vendor guidance.
- To reduce the startup time before you shut down the management virtual machines, migrate the vCenter instance for the management domain to the first VMware ESX host in the default management cluster in the management domain.

You shut down the customer workloads and the management components for the workload domains before you shut down the components for the management domain. If you have multiple VCF instances you start with the instances that does not run VCF Operations and VCF Automation. The VCF instance running VCF Operations must be the last instance to shut down.

If the NSX Manager cluster and NSX Edge cluster are shared with other workload domains, shut down the NSX Manager and NSX Edge clusters as part of the shutdown of the first workload domain.