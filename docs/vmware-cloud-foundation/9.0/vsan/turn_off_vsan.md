---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/disable-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Turn Off vSAN
---

# Turn Off vSAN

You can turn off vSAN for a vSphere cluster when the vCenter managing the vSphere cluster is deployed outside the vSAN cluster.

- Disable vSphere High Availability (HA), if HA is enabled.
- Shutdown all the VMs, unless vCenter is on the cluster. If vCenter is on the cluster, you must migrate vCenter from the cluster that you want to turn off.
- Verify that the ESX hosts are in maintenance mode with 'No Data Migration' selected. For more information, see [Place a Member of vSAN Cluster in Maintenance Mode](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/working-with-members-of-vsan-cluster-in-maintenance-mode/place-a-member-of-vsan-cluster-in-maintenance-mode.html).

When you turn off vSAN for a cluster, all virtual machines and data services located on the vSAN datastore become inaccessible. If you have consumed storage on the vSAN cluster using vSAN Direct, then the vSAN Direct monitoring services, such as health checks, space reporting, and performance monitoring, are not available. If you intend to use virtual machines while vSAN is off, make sure you migrate the virtual machines from vSAN datastore to another datastore before turning off the vSAN cluster.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, select Services.
4. Click Turn Off vSAN.
5. On the Turn Off vSAN dialog, confirm your selection.