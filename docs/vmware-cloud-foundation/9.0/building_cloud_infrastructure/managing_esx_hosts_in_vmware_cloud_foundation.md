---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Managing ESX Hosts in VMware Cloud Foundation
---

# Managing ESX Hosts in VMware Cloud Foundation

To add ESX hosts to the global inventory, you must first create a network pool or expand the default network pool created during deployment. Once you have a suitable network pool, you can commission ESX hosts for use in a VCF domain.

During the commissioning process, the ESX hosts are associated with a network pool and added to the global inventory. Newly commissioned ESX hosts appear in the global inventory with a host state of UNASSIGNED. When an ESX host is added to a workload domain, an IP address from the network pool's IP range is assigned to it.

See [VMware Configuration Maximums](https://configmax.broadcom.com/home) for information about ESX host maximums.

VMware Cloud Foundation does not support stateless ESX hosts.