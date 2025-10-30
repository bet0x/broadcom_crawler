---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/expanding-a-vsan-cluster/use-quickstart-to-add-hosts-to-a-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Use Quickstart to Add ESX Hosts to a vSAN Cluster
---

# Use Quickstart to Add ESX Hosts to a vSAN Cluster

If you configured your vSAN cluster through Quickstart, you can use the Quickstart workflow to add ESX hosts and storage devices to the vSAN cluster.

- The Quickstart workflow must be available for your vSAN cluster.
- Verify that the resources, including drivers, firmware, and storage I/O controllers, are listed in the Broadcom Compatibility Guide at <https://compatibilityguide.broadcom.com/>.
- VMware recommends creating uniformly configured ESX hosts in the vSAN cluster, so you have an even distribution of components and objects across devices in the cluster. However, there might be situations where the vSAN cluster becomes unevenly balanced, particularly during maintenance or if you overcommit the capacity of the vSAN datastore with excessive virtual machine deployments.
- No network configuration performed through the Quickstart workflow has been modified from outside of the Quickstart workflow.

  Networking settings configured while creating the vSAN cluster with Quickstart have not been modified.

When you add new ESX hosts to the vSAN cluster, you can use the Cluster configuration wizard to complete the ESX host configuration. For more information about Quickstart, see [Using Quickstart to Configure and Expand a vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/using-quickstart-to-configure-a-vsan-cluster.html).

If you are running vCenter on an ESX host, the ESX host cannot be placed into maintenance mode as you add it to a vSphere cluster using the Quickstart workflow. All other virtual machines on the ESX host must be powered off.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under Configuration, click Quickstart.
4. On the Add hosts card, click Add to open the Add hosts wizard.
   1. On the Add hosts page, enter information for new hosts, or click Existing hosts and select from hosts listed in the inventory.
   2. On the Host Summary page, verify the host settings.
   3. On the Import Image page, import an image from the ESX host to set as the new image for the cluster. You can either select an existing image or import an image from one of the ESX hosts.
   4. On the Review page, click Finish.
5. On the Configure Cluster card, click Configure to open the Cluster configuration wizard.
   1. On the Configure the distributed switches page, enter networking settings for the new hosts.
   2. (optional) On the Claim disks page, select disks on each new host. If you enable Auto clam at the cluster level for vSAN ESA, all the compatible disks are automatically claimed.
   3. (optional) On the Create fault domains page, move the new hosts into their corresponding fault domains.

      For more information about fault domains, see [Managing Fault Domains in vSAN Clusters](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/managing-fault-domains-in-vsan-clusters.html#GUID-e934bb38-c8b3-468b-bad3-e030ad3ac5c7-en).
   4. On the Ready to complete page, verify the cluster settings, and click Finish.

Verify the vSAN Skyline Health status.