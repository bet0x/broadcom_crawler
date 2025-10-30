---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/using-quickstart-to-configure-a-vsan-cluster/using-quickstart-to-create-a-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Use Quickstart to Configure a vSAN Cluster
---

# Use Quickstart to Configure a vSAN Cluster

You can use the Quickstart workflow to quickly configure a vSAN cluster.

- Verify that hosts are running ESX 9.0 or later.
- Verify that ESX hosts in the cluster do not have any existing vSAN or networking configuration.

If you perform network configuration through Quickstart, then modify those parameters from outside of Quickstart, you cannot use Quickstart to add or configure additional hosts.

1. Navigate to the new cluster in the vSphere Client.
2. Click the Configure tab, and select Configuration > Quickstart.
3. (optional) On the Cluster basics card, click Edit to open the Cluster basics wizard. 
   1. (Optional) Enter a cluster name.
   2. Select basic services, such as DRS, vSphere HA, and vSAN. 

      Check Enable vSAN ESA to use vSAN ESA. vSAN ESA is optimized for high-performance flash storage devices that provide greater performance and efficiency.
   3. Select any option to Choose how to set up the cluster's image.
   4. Select Manage configuration at a cluster level check box to ensure that all the hosts in the cluster have the same settings.
   5. Click Next.
   6. Select an image from the Image Library of Lifecycle Manager.
   7. Click Next and review the cluster details.
   8. Click Finish.
4. On the Add hosts card, click Add to open the Add hosts wizard. 
   1. On the Add hosts page, enter information for new hosts, or click Existing hosts and select from hosts listed in the inventory.
   2. On the Host summary page, verify the host settings.
   3. On the Ready to complete page, click Finish.

   If you are running vCenter on a host, the host cannot be placed into maintenance mode as you add it to a cluster using the Quickstart workflow. All other virtual machines on the host must be powered off.
5. On the Cluster configuration card, click Configure to open the Cluster configuration wizard. 
   1. (vSAN ESA clusters) On the Cluster Type page, enter the HCI cluster type:

      - vSAN HCI provides compute resources and storage resources. The datastore can be shared across data centers and vCenter instances.
      - vSAN storage cluster provides storage resources, but not compute resources. The datastore can be mounted by remote vSAN clusters across data centers and vCenter instances.
   2. On the Configure the distributed switches page, enter networking settings, including distributed switches, port groups, and physical adapters. 

      - In the Distributed switches section, enter the number of distributed switches to configure from the drop-down menu. Enter a name for each distributed switch. Click Use Existing to select an existing distributed switch.

        If the host has a standard virtual switch with the same name as the selected distributed switch, the standard switch is migrated to the corresponding distributed switch.

        Network resource control is enabled and set to version 3. Distributed switches with network resource control version 2 cannot be used.
      - In the Port Groups section, select a distributed switch to use for vMotion and a distributed switch to use for the vSAN network.
      - In the Physical adapters section, select a distributed switch for each physical network adapter. You must assign each distributed switch to at least one physical adapter.

        If the physical adapters chosen are attached to a standard virtual switch with the same name across hosts, the standard switch is migrated to the distributed switch. If the physical adapters chosen are unused, there is no migration from standard switch to distributed switch.

        Network resource control is enabled and set to version 3. Distributed switches with network resource control version 2 cannot be used.
   3. On the vMotion traffic page, enter IP address information for vMotion traffic.
   4. On the Storage traffic page, enter IP address information for storage traffic.
   5. On the Advanced options page, enter information for cluster settings, including DRS, HA, vSAN, host options, and EVC.
   6. On the Claim disks page, select storage devices on each host. For clusters with vSAN OSA, select one cache device and one or more capacity devices. For clusters with vSAN ESA, select flash devices for the host's storage pool.

      Only the vSAN Data Persistence platform can consume vSAN Direct storage. The vSAN Data Persistence platform provides a framework for software technology partners to integrate with VMware infrastructure. Each partner must develop their own plug-in for VMware customers to receive the benefits of the vSAN Data Persistence platform. The platform is not operational until the partner solution running on top is operational. For more information, see the vSphere Supervisor Concepts guide.
   7. (Optional) On the Create fault domains page, define fault domains for hosts that can fail together. 

      For more information about fault domains, see [Managing Fault Domains in vSAN Clusters](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/managing-fault-domains-in-vsan-clusters.html).
   8. (Optional) On the Proxy setting page, configure the proxy server if your system uses one.
   9. On the Review page, verify the cluster settings, and click Finish.

You can manage the cluster through your vCenter.

You can add hosts to the cluster through Quickstart. For more information. see [Expanding a vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/expanding-a-vsan-cluster.html).