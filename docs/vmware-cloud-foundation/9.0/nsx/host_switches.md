---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Host Switches
---

# Host Switches

A host switch managed object is a virtual network switch that provides networking services to the various hosts in the network. It is instantiated on every host that participates in NSX networking.

A host switch is a virtual switch that implements the networking data plane on various ESX hosts. The NSX host switch is based on the vSphere Distributed Switch (VDS), centrally managed by vCenter. The VDS switch is enhanced with some NSX capabilities and is centrally managed by the NSX Manager.

The NSX Virtual Distributed Switch (NVDS) was another NSX host switch option for the ESX host. It was deprecated in NSX 4.0.