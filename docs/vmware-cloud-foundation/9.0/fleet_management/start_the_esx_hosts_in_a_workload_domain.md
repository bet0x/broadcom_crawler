---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-virtual-infrastructure-workload-domain/start-vsan-and-the-esxi-hosts-in-a-vi-workload-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Start the ESX Hosts in a Workload Domain
---

# Start the ESX Hosts in a Workload Domain

You start the ESX hosts using an out-of-band management interface, such as, ILO or iDRAC to connect to the hosts and power them on.

If you are using non-vSAN storage, the storage must be started and accessible.

1. Power on the first ESX host in the workload domain.
   1. Log in to the first ESX host in the workload domain by using the out-of-band management interface.
   2. Power on the ESX host according to the documentation from the hardware vendor.
2. Repeat the step to start all the remaining ESX hosts in the workload domain.

   This operation takes several minutes to complete.