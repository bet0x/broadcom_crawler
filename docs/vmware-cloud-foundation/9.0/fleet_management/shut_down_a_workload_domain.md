---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-virtual-infrastructure-workload-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Shut Down a Workload Domain
---

# Shut Down a Workload Domain

You shut down the components of a workload domain that runs virtualized workloads in VCF in a specific order to keep components operational by maintaining the necessary infrastructure, networking, and management services as long as possible before shutdown.

You shut down the management components for the workload domains before you shut down the components for the management domain.

If the NSX Manager cluster and NSX Edge cluster are shared with other workload domains, follow this general order:

1. Shut down the consumer workloads in all workload domains that share the NSX Manager instance. Otherwise, all NSX networking services in the consumer workloads will be interrupted when you shut down NSX Manager.
2. Shut down the workload domain that runs the shared NSX Edge nodes.
3. Shut down the other workload domains.

## Shutdown Order for a Workload Domain

Shutdown Order for a Workload Domain



| Shutdown Order | SDDC Component |
| --- | --- |
| 1 | Virtualized customer workloads |
| 2 | [VMware Live Recovery](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vvs/9-X/site-protection-and-disaster-recovery-for-vmware-cloud-foundation/operational-guidance-for-site-protection-vvs/pdr-vvs-shutdown-and-startup/shut-down-the-site-recovery-manager-and-vsphere-replication-virtual-machines.html) for the workload domain |
| 4 | [NSX Edge node](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-virtual-infrastructure-workload-domain/shut-down-the-nsx-t-edge-nodes-in-the-vi-workload-domain-vcf-4-5.html)s for the workload domain |
| 5 | [NSX Manager nodes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-virtual-infrastructure-workload-domain/shut-down-the-nsx-t-managers-in-the-vi-workload-domain-vcf-4-5.html) for the workload domain |
| 7 | [ESX hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-virtual-infrastructure-workload-domain/shut-down-the-esx-hosts.html) in the workload domain |
| 8 | [vCenter Server](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-virtual-infrastructure-workload-domain/shut-down-the-vcenter-server-instance-in-the-virtual-infrastructure-workload-domain.html) for the workload domain |