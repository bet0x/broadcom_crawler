---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/working-with-individual-devices-in-vsan-cluster/mark-devices-as-remote-in-vsan.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Mark Devices as Remote in vSAN
---

# Mark Devices as Remote in vSAN

ESX hosts that use external SAS controllers can share devices.

You can manually mark those shared devices as remote, so that vSAN does not claim the devices when it creates disk groups. In vSAN, you cannot add shared devices to a disk group.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Disk Management.
4. Select a host to view the list of devices.
5. From the Show drop-down menu at the bottom of the page, select Not in Use.
6. Select one or more devices that you want to mark as remote and click the Mark as remote.
7. Click Yes to confirm.