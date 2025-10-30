---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-management-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Shut Down the Management Domain
---

# Shut Down the Management Domain

You shut down the components of the management domain in VCF in a specific order to keep components operational by maintaining the necessary infrastructure, networking, and management services as long as possible before shutdown.

After you shut down the components in all workload domains, you begin shutting down the management domain.

## Shutdown Order for the Management Domain

If your VCF Instance is deployed without workload domains, shut down any customer workloads or additional virtual machines in the management domain before you proceed with the shutdown order of the management components.

You shut down VMware Live Site Recovery after you shut down the management components that can be failed over between the VCF Instances. You also shut VMware Live Site Recovery down as late as possible to have the management virtual machines protected as long as possible if a disaster event occurs. The virtual machines in the paired VCF Instance become unprotected after you shut downVMware Live Site Recovery in the current VCF Instance.

Shutdown Order for the Management Domain



| Shutdown Order | SDDC Component |
| --- | --- |
| 1 | [VCF Automation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-management-domain/shut-down-the-vrealize-automation-cluster.html) |
| 2 | [VCF Operations for Networks](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-management-domain/shut-down-vcf-operations-for-networks.html) |
| 3 | [VCF Operations collector](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-management-domain/shut-down-the-vcf-operations-collector-virtual-machines.html) |
| 4 | [VCF Operations for logs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-management-domain/shut-down-vcf-operations-for-logs.html) |
| 5 | [VCF Identity Broker](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-management-domain/shut-down.html) |
| 6 | [VCF Operations fleet management](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-management-domain/vcf-shut-down-the-vrealize-suite-lifecycle-manager-virtual-machine-in-the-management-domain.html) |
| 7 | [VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-management-domain/shut-down-vcf-operations.html) |
| 8 | [VMware Live Site Recovery](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vvs/9-X/site-protection-and-disaster-recovery-for-vmware-cloud-foundation/operational-guidance-for-site-protection-vvs/pdr-vvs-shutdown-and-startup/shut-down-the-site-recovery-manager-and-vsphere-replication-virtual-machines.html) for the management domain |
| 9 | [NSX Edge nodes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-management-domain/shut-down-the-nsx-t-edge-nodes-in-the-management-domain.html) |
| 10 | [NSX Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-management-domain/shut-down-the-nsx-t-managers-in-the-management-domain.html) |
| 11 | [SDDC Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-management-domain/shut-down-the-sddc-manager-virtual-machine-in-the-management-domain.html) |
| 12 | - [Shut Down vSAN and the ESX Hosts in the Management Domain](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-management-domain/shut-down-the-esx-hosts-in-management-domain/shut-down-vsan-and-the-esx-hosts-in-a-management-domain.html) - [Shut Down ESX Hosts with NFS or Fibre Channel Storage in the Management Domain](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-management-domain/shut-down-the-esx-hosts-in-management-domain/shut-down-esx-hosts-without-vsan-storage.html) |

## Save the Credentials for the ESX Hosts and vCenter for the Management Domain

Before you shut down the management domain, get the credentials for the management domain hosts and vCenter and save them. You need these credentials to shut down the ESX hosts and then to start them and vCenter back up.

## Shutting Down a Management Domain with Infrastructure Services VMs

If the management domain contains virtual machines that are running infrastructure services like Active Directory, NTP, DNS and DHCP servers, stop these virtual machines last, that is, after the vCenter appliance.

- For a vSAN cluster, select I confirm all VMs below are infrastructure VMs in the vSAN shutdown wizard.
- For a non-vSAN cluster, migrate all such virtual machines to the first host with vCenter and shut them down after the vCenter appliance is shut down.