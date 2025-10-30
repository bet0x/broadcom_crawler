---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Understanding vSAN Networking
---

# Understanding vSAN Networking

A vSAN network facilitates the communication between cluster hosts, and must be fast, resilient, and scalable.

vSAN uses the network to communicate between the ESX hosts and for virtual machine disk I/O.

Virtual machines (VMs) on vSAN datastores are made up of a set of objects, and each object can be made up of one or more components. These components are distributed across multiple hosts for resilience to drive and host failures. vSAN maintains and updates these components using the vSAN network.

The following diagram provides a high-level overview of the vSAN network:

![Local vSAN network diagram](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/9666ef22-fdd6-4b49-8147-fa1897e5e90a.original.svg)