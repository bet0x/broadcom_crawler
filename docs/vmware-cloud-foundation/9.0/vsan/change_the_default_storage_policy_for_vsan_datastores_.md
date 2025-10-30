---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-vsan-policies/assign-a-default-storage-policy-to-vsan-datastores.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Change the Default Storage Policy for vSAN Datastores 
---

# Change the Default Storage Policy for vSAN Datastores

You can change the default storage policy for a selected vSAN datastore.

Verify that the virtual machine storage policy you want to assign as the default policy to the vSAN datastore meets the requirements of virtual machines in the vSAN cluster.

1. In the vSphere Client, navigate to the vSAN datastore.
2. Click the Configure tab.
3. Under General, click the Default Storage Policy Edit button, and select the storage policy that you want to assign as the default policy to the vSAN datastore.

   You can also edit the Improved Virtual Disk Home Storage Policy. Click Edit and select the home storage policy that you want to assign as the storage policy for the home object.

   You can choose from a list of storage policies that are compatible with the vSAN datastore, such as the vSAN Default Storage Policy and user-defined storage policies that have vSAN rule sets defined.
4. Click OK. The storage policy is applied as the default policy when you provision new virtual machines without explicitly specifying a storage policy for a datastore.

You can define a new storage policy for virtual machines. See [Define a Storage Policy for vSAN Using vSphere Client](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-vsan-policies/define-a-storage-policy-for-virtual-san.html#GUID-9c893c43-f30d-4d3c-ae7a-627c52a8efd7-en).