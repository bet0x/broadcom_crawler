---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Start the Management Domain
---

# Start the Management Domain

You start the management components for the management domain in a specific order to provide the necessary infrastructure, networking, and management services before powering on the components for cloud management.

You start the management components for the management domain first. Then, you start the management components for the workload domains and the customer workloads.

## Startup Order for the Management Domain

You start the virtual infrastructure of the management domain that hosts VCF Operations and VCF Automation first.

Startup Order for the Management Domain



| Startup Order | SDDC Component |
| --- | --- |
| 1 | - [Start vSAN and the ESX Hosts in the Management Domain](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain/start-the-esx-hosts-and-vcenter-server-in-management-domain/start-vsan-and-the-esxi-hosts-in-the-management-domain.html) - [Start ESX Hosts with NFS or Fibre Channel Storage in the Management Domain](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain/start-the-esx-hosts-and-vcenter-server-in-management-domain/start-esx-hosts-without-vsan-storage-in-the-management-domain.html) |
| 2 | [SDDC Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain/start-the-sddc-manager-virtual-machine-in-the-management-domain.html) |
| 3 | [NSX Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain/start-the-nsx-t-manager-virtual-machines-in-the-management-domain.html) |
| 4 | [NSX Edge](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain/start-the-nsx-t-edge-nodes-in-the-management-domain.html) |
| 5 | [VMware Live Site Recovery](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vvs/9-X/site-protection-and-disaster-recovery-for-vmware-cloud-foundation/operational-guidance-for-site-protection-vvs/pdr-vvs-shutdown-and-startup/start-the-srm-and-vr-virtual-machines.html) |
| 6 | [VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain/start-the-vcf-operations.html) |
|  | [VCF Operations fleet management](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain/start-the-vcf-operations-fleet-management-virtual-machine.html) |
|  | [VCF Identity Broker](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain/shut-down(1).html) |
| 7 | [VCF Operations for logs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain/start-the-vcf-operations-for-logs.html) |
| 8 | [VCF Operations collector](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain/start-the-vcf-operations-collector.html) |
| 9 | [VCF Operations for Networks](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain/vrni.html) |
| 10 | [VCF Automation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain/start-the-vrealize-automation-cluster.html) |