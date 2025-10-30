---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/working-with-individual-devices-in-vsan-cluster/mark-flash-devices-as-cache-in-vsan.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Mark Devices as Flash in vSAN
---

# Mark Devices as Flash in vSAN

When flash devices are not automatically identified as flash by ESX hosts, you can manually mark them as local flash devices.

- Verify that the device is local to your ESX host.
- Verify that the device is not in use.
- Make sure that the virtual machines accessing the device are powered off and the datastore is unmounted.

Flash devices might not be recognized as flash when they are enabled for RAID 0 mode rather than passthrough mode. When devices are not recognized as local flash, they are excluded from the list of devices offered for vSAN and you cannot use them in the vSAN cluster. Marking these devices as local flash makes them available to vSAN.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Disk Management.
4. Select the host to view the list of available devices.
5. From the Show drop-down menu at the bottom of the page, select Not in Use.
6. Select one or more flash devices from the list and click the Mark as Flash Disk.
7. Click Yes to save your changes. 

   The Drive type for the selected devices appears as Flash.