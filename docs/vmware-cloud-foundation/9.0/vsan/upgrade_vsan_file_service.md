---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service/upgrade-vsan-file-service.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Upgrade vSAN File Service
---

# Upgrade vSAN File Service

When you upgrade the file service, the upgrade is performed on a rolling basis.

Ensure that the following are upgraded:

- ESX Hosts
- vCenter
- vSAN disk format

During the upgrade, the file server containers running on the virtual machines which are undergoing upgrade fails over to other virtual machines. The file shares remain accessible during the upgrade. During the upgrade, you might experience some interruptions while accessing the file shares.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Services.
4. Under File Service, click Edit.
5. Click Check upgrade from the list.
6. In the Upgrade File Service dialog box, select one of the following deployment options and then click Upgrade.

   Option | Action || Automatic approach | This is the default option. This option lets the system search and download the OVF. After the upgrade begins, you cannot cancel the task. vSAN requires internet connectivity for this option. |
   | Manual approach | This option allows you to browse and select an OVF that is already available on your local system. After the upgrade begins, you cannot cancel the task. If you select this option, you should upload all the following files: - VMware-vSAN-File-Services-Appliance-x.x.x.x-x\_OVF10.mf - VMware-vSAN-File-Services-Appliance-x.x.x.x-x-x\_OVF10.cert - VMware-vSAN-File-Services-Appliance-x.x.x.x-x-x-system.vmdk - VMware-vSAN-File-Services-Appliance-x.x.x.x-x-cloud-components.vmdk - VMware-vSAN-File-Services-Appliance-x.x.x.x-x-log.vmdk - VMware-vSAN-File-Services-Appliance-x.x.x.x-x\_OVF10.ovf |