---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/upgrading-the-vsan-cluster/about-the-virtual-san-disk-format/upgrading-vsan-disk-format-using-vsphere-client.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Upgrading vSAN Disk Format Using vSphere Client
---

# Upgrading vSAN Disk Format Using vSphere Client

After you have finished upgrading the vSAN hosts, you can perform the disk format upgrade.

- Verify that you are using the updated version of vCenter.
- Verify that you are using the latest version of ESX hosts.
- Verify that the disks are in a healthy state. Navigate to the Disk Management page to verify the object status.
- Verify that the hardware and software that you plan on using are certified and listed in the Broadcom Compatibility Guide at <https://compatibilityguide.broadcom.com/>.
- Verify that you have enough free space to perform the disk format upgrade.
- Verify that your hosts are not in maintenance mode. When upgrading the disk format, do not place the hosts in maintenance mode. When any member host of a vSAN cluster enters maintenance mode, the member host no longer contributes capacity to the cluster. The cluster capacity is reduced and the cluster upgrade might fail.
- Verify that there are no component rebuilding tasks currently in progress in the vSAN cluster. For information about vSAN resynchronization, see the [vSphere Monitoring and Performance](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-monitoring-and-performance.html) guide.

If you enable encryption or deduplication and compression on an existing vSAN cluster, the on-disk format is automatically upgraded to the latest version. This procedure is not required. See [Edit vSAN Settings](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/enabling-virtual-san/edit-virtual-san-settings.html#GUID-036671bb-dd79-48d2-a59b-5606b2f61c7f-en).

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, select Disk Management.
4. (Optional) Click Pre-check Upgrade. 

   The upgrade pre-check analyzes the cluster to uncover any issues that might prevent a successful upgrade. Some of the items checked are host status, disk status, network status, and object status. Upgrade issues are displayed in the Disk pre-check status text box.
5. Click Upgrade.
6. Click Yes on the Upgrade dialog box to perform the upgrade of the on-disk format.

vSAN successfully upgrades the on-disk format. The On-disk Format Version column displays the disk format version of storage devices in the cluster.

If a failure occurs during the upgrade, you can check the Resyncing Objects page. Wait for all resynchronizations to complete, and run the upgrade again. You also can check the cluster health using the health service. After you have resolved any issues raised by the health checks, you can run the upgrade again.