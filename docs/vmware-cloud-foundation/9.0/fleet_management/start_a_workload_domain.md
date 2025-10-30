---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-virtual-infrastructure-workload-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Start a Workload Domain
---

# Start a Workload Domain

You start the management components for a workload domain in a specific order to provide the necessary infrastructure, networking, and management services.

You start the management components for the management domain first. Then, you start the management components for the workload domains and the customer workloads.

If the NSX Manager cluster and NSX Edge cluster are shared across workload domains, follow this general order:

1. Start the other workload domains.
2. Start the workload domain that runs the shared NSX Edge nodes.
3. Start the customer workloads that rely on NSX services.

## Startup Order for a Workload Domain

Startup Order for a Workload Domain



| Startup Order | SDDC Component |
| --- | --- |
| 1 | [vCenter](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-virtual-infrastructure-workload-domain/start-vcenter-server-in-the-virtual-infrastructure-workload-domain.html) for the workload domain |
| 2 | [ESX hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-virtual-infrastructure-workload-domain/start-vsan-and-the-esxi-hosts-in-a-vi-workload-domain.html) for the workload domain |
| 3 | [Restart Clusters](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-virtual-infrastructure-workload-domain/start-the-esx-hosts.html) for the workload domain |
| 5 | [NSX Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-virtual-infrastructure-workload-domain/start-the-nsx-t-manager-virtual-machines-in-the-vi-workload-domain-vcf-4-5.html) nodes for the workload domain |
| 6 | [NSX Edge](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-virtual-infrastructure-workload-domain/start-the-nsx-t-edge-nodes-in-the-vi-workload-domain-vcf-4-5.html) nodes for the workload domain |
| 8 | [VMware Live Site Recovery](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vvs/9-X/site-protection-and-disaster-recovery-for-vmware-cloud-foundation/operational-guidance-for-site-protection-vvs/pdr-vvs-shutdown-and-startup/start-the-srm-and-vr-virtual-machines.html) for the workload domain |
| 9 | Virtualized customer workloads |