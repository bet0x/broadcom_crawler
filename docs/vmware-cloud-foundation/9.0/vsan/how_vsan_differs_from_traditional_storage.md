---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/what-is-vsan/vsan-concepts/virtual-san-and-traditional-storage.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > How vSAN Differs from Traditional Storage
---

# How vSAN Differs from Traditional Storage

Although vSAN shares many characteristics with traditional storage arrays, the overall behavior and function of vSAN is different.

For example, vSAN can manage and work only with ESX hosts, and a single vSAN instance provides a single datastore for the cluster.

vSAN and traditional storage also differ in the following key ways:

- vSAN does not require external networked storage for storing virtual machine files remotely, such as on a Fibre Channel (FC) or Storage Area Network (SAN).
- Using traditional storage, the storage administrator preallocates storage space on different storage systems. vSAN automatically turns the local physical storage resources of the ESX hosts into a single pool of storage. These pools can be divided and assigned to virtual machines and applications according to their quality-of-service requirements.
- vSAN does not behave like traditional storage volumes based on LUNs or NFS shares. The iSCSI target service uses LUNs to enable an initiator on a remote ESX host to transport block-level data to a storage device in the vSAN cluster.
- Some standard storage protocols, such as Fiber Channel Protocol (FCP), do not apply to vSAN.
- vSAN is highly integrated with vSphere. You do not need dedicated plug-ins or a storage console for vSAN, compared to traditional storage. You can deploy, manage, and monitor vSAN by using the vSphere Client.
- A dedicated storage administrator does not need to manage vSAN. Instead a vSphere administrator can manage a vSAN environment.
- With vSAN, virtual machine storage policies are automatically assigned when you deploy new virtual machines. The storage policies can be changed dynamically as needed.