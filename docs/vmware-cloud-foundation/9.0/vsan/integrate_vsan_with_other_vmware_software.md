---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/what-is-vsan/integrating-with-other-vmware-products.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Integrate vSAN with Other VMware Software
---

# Integrate vSAN with Other VMware Software

After you have vSAN up and running, it is integrated with the rest of the VMware software stack.

You can do most of what you can do with traditional storage by using vSphere components and features including vSphere vMotion, snapshots, clones, vSphere DRS, vSphere HA, VMware Live Site Recovery, and more.

## vSphere HA

You can enable vSphere HA and vSAN on the same cluster. As with traditional datastores, vSphere HA provides the same level of protection for virtual machines on vSAN datastores. This level of protection imposes specific restrictions when vSphere HA and vSAN interact. For specific considerations about integrating vSphere HA and vSAN, see [Using vSAN and vSphere HA](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/using-virtual-san-and-vsphere-ha.html).