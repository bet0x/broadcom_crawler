---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster/use-quickstart-to-configure-a-vsan-stretched-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Use Quickstart to Configure a vSAN Stretched Cluster or Two-Node vSAN Cluster
---

# Use Quickstart to Configure a vSAN Stretched Cluster or Two-Node vSAN Cluster

You can use the Quickstart workflow to quickly configure a vSAN stretched cluster or two-node vSAN cluster.

- Deploy a host outside of any cluster to use as a witness host.
- Verify that hosts are running ESX 9.0 or later. For a two-node vSAN cluster, verify that hosts are running ESX 9.0 or later.
- Verify that ESX hosts in the cluster do not have any existing vSAN or networking configuration.

When you create a cluster in the vSphere Client, the Quickstart workflow appears. You can use Quickstart to perform basic configuration tasks, such as adding hosts and claiming disks.

1. Navigate to the cluster in the vSphere Client.
2. Click the Configure tab, and select Configuration > Quickstart.
3. On the Cluster basics card, click Edit to open the Cluster basics wizard. 
   1. Enter the cluster name.
   2. Enable the vSAN slider. 

      Select vSAN ESA if your cluster is compatible. You also can enable other features, such as DRS or vSphere HA.
   3. Select any option to Choose how to set up the cluster's image.
   4. (Optional) Select Manage configuration at a cluster level check box to ensure that all the hosts in the cluster have the same settings.
   5. Click Next.
   6. Select an image from the Image Library of Lifecycle Manager.
   7. Click Next and review the cluster details.
   8. Click Finish.
4. On the Add hosts card, click Add to open the Add hosts wizard. 
   1. On the Add hosts page, enter information for new hosts, or click Existing hosts and select from hosts listed in the inventory.
   2. On the Host summary page, verify the host settings.
   3. On the Ready to complete page, click Finish.
5. On the Cluster configuration card, click Configure to open the Cluster configuration wizard. 
   1. (vSAN ESA clusters) On the Cluster Type page, enter the HCI cluster type:

      - vSAN HCI provides compute resources and storage resources. The datastore can be shared across data centers and vCenter instances.
      - vSAN storage clusters provides storage resources, but not compute resources. The datastore can be mounted by remote vSAN clusters across data centers and vCenter instances.
   2. On the Configure the distributed switches page, enter networking settings, including distributed switches, port groups, and physical adapters. 

      - In the Distributed switches section, enter the number of distributed switches to configure from the drop-down menu. Enter a name for each distributed switch. Click Use Existing to select an existing distributed switch.

        If the physical adapters chosen are attached to a standard virtual switch with the same name across hosts, the standard switch is migrated to the distributed switch. If the physical adapters chosen are unused, the standard switch is migrated to the distributed switch.

        Network resource control is enabled and set to version 3. Distributed switches with network resource control version 2 cannot be used.
      - In the Port Groups section, select a distributed switch to use for vMotion and a distributed switch to use for the vSAN network.
      - In the Physical adapters section, select a distributed switch for each physical network adapter. You must assign each distributed switch to at least one physical adapter.

        This mapping of physical NICs to the distributed switches is applied to all hosts in the cluster. If you are using an existing distributed switch, the physical adapter selection can match the mapping of the distributed switch.
   3. On the vMotion traffic page, enter IP address information for vMotion traffic.
   4. On the Storage traffic page, enter IP address information for storage traffic.
   5. On the Advanced options page, enter information for cluster settings, including DRS, HA, vSAN, host options, and EVC. 

      In the vSAN options section, select vSAN Stretched cluster or Two node vSAN cluster as the Deployment type. If you select vSAN Storage, you get the option to Use Storage cluster client network. Once configured, you cannot change the network configuration.
   6. On the Claim disks page, select storage devices to create the vSAN datastore.

      For vSAN OSA, select devices for cache and for capacity. vSAN uses those devices to create disk groups on each host.

      For vSAN ESA, select compatible flash devices or enable I want vSAN to manage the disks. vSAN uses those devices to create storage pools on each host.
   7. (Optional) On the Proxy settings, page, configure the proxy server if your system uses one.
   8. On the Configure fault domains page, define fault domains for the hosts in the Preferred site and the Secondary site. 

      For more information about fault domains, see [Managing Fault Domains in Clusters](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/managing-fault-domains-in-vsan-clusters.html).
   9. On the Select witness host page, select a host to use as a witness host. The witness host cannot be part of the vSAN stretched cluster, and it can have only one VMkernel adapter configured for vSAN data traffic. 

      Before you configure the witness host, verify that it is empty and does not contain any components. A two-node vSAN cluster can share a witness with other two-node vSAN clusters.
   10. On the Claim disks for witness host page, select disks on the witness host.
   11. On the Review page, verify the cluster settings, and click Finish.

You can manage the cluster through vCenter.

You can add hosts to the cluster and modify the configuration through Quickstart. You also can modify the configuration manually with the vSphere Client.