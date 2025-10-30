---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrade-vsan-on-disk-format-versions.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrade vSAN On-Disk Format Versions
---

# Upgrade vSAN On-Disk Format Versions

[Optional] Upgrade the vSAN on-disk format version using the vSphere Client to take advantage of features that are available only in the later versions.

- ESX and vCenter upgrades are completed
- Verify that the disks are in a healthy state. Navigate to the Disk Management page to verify the object status.
- Verify that your ESX hosts are not in maintenance mode. When upgrading the disk format, do not place the ESX hosts in maintenance mode.
- Verify that there are no component rebuilding tasks currently in progress in the vSAN cluster. For information about vSAN resynchronization, see vSphere Monitoring and Performance.

- The upgrade may cause temporary resynchronization traffic and use additional space by moving data or rebuilding object components to a new data structure.

1. In the vSphere Client, navigate to the vSAN cluster.
2. Click the Configure tab.
3. Under vSAN, select Disk Management.
4. Click Pre-check Upgrade. The upgrade pre-check analyzes the cluster to uncover any issues that might prevent a successful upgrade. Some of the items checked are host status, disk status, network status, and object status. Upgrade issues are displayed in the Disk pre-check status text box.
5. Click Upgrade.
6. Click Yes on the Upgrade dialog box to perform the upgrade of the on-disk format.

vSAN successfully upgrades the on-disk format. The On-disk Format Version column displays the disk format version of storage devices in the cluster.