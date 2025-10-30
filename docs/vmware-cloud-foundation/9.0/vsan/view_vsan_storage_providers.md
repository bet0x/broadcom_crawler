---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-vsan-policies/view-vsan-storage-providers.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > View vSAN Storage Providers
---

# View vSAN Storage Providers

Enabling vSAN automatically configures and registers a vSAN storage provider in the vSAN cluster.

vSAN storage providers are built-in software components that communicate datastore capabilities to vCenter. A storage capability typically is represented by a key-value pair, where the key is a specific property offered by the datastore. The value is a number or range that the datastore can provide for a provisioned object, such as a virtual machine home namespace object or a virtual disk. You can also use tags to create user-defined storage capabilities and reference them when defining a storage policy for a virtual machine.

1. In the vSphere Client, navigate to vCenter.
2. Click the Configure tab, and click Storage Providers.

The storage provider for vSAN appears on the list.

You cannot manually unregister storage providers used by vSAN. To remove or unregister the vSAN storage providers, remove corresponding ESX hosts from the vSAN cluster and then add the ESX hosts back. Make sure that at least one storage provider is active.