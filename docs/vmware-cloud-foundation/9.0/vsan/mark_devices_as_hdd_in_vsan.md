---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/working-with-individual-devices-in-vsan-cluster/mark-devices-as-capacity-in-vsan.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Mark Devices as HDD in vSAN
---

# Mark Devices as HDD in vSAN

When local magnetic disks are not automatically identified as HDD devices by ESX hosts, you can manually mark them as local HDD devices.

- Verify that the magnetic disk is local to your ESX host.
- Verify that the magnetic disk is not in use and is empty.
- Verify that the virtual machines accessing the device are powered off.

If you marked a magnetic disk as a flash device, you can change the disk type of the device by marking it as a magnetic disk.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Disk Management.
4. Select the host to view the list of available magnetic disks.
5. From the Show drop-down menu at the bottom of the page, select Not in Use.
6. Select one or more magnetic disks from the list and click Mark as HDD Disk.
7. Click Yes to save. 

   The Drive Type for the selected magnetic disks appears as HDD.