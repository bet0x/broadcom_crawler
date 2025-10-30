---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/working-with-individual-devices-in-vsan-cluster/mark-devices-as-local-in-vsan.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Mark Devices as Local in vSAN
---

# Mark Devices as Local in vSAN

When ESX hosts are using external SAS enclosures, vSAN might recognize certain devices as remote and might be unable to automatically claim them as local.

Make sure that the storage device is not shared.

In such cases, you can mark the devices as local.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Disk Management.
4. Select a host to view the list of devices.
5. From the Show drop-down menu at the bottom of the page, select Not in Use.
6. From the list of devices, select one or more remote devices that you want to mark as local and click the Mark as local disk.
7. Click Yes to save your changes.