---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/expanding-a-vsan-cluster/add-a-host-to-the-virtual-san-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Add an ESX Host to the vSAN Cluster
---

# Add an ESX Host to the vSAN Cluster

You can add ESX hosts to a running vSAN cluster without disrupting any ongoing operations.

- Verify that the resources, including drivers, firmware, and storage I/O controllers, are listed in the Broadcom Compatibility Guide at <https://compatibilityguide.broadcom.com/>.
- VMware recommends creating uniformly configured ESX hosts in the vSAN cluster, so you have an even distribution of components and objects across devices in the cluster. However, there might be situations where the vSAN cluster becomes unevenly balanced, particularly during maintenance or if you overcommit the capacity of the vSAN datastore with excessive virtual machine deployments.
- Verify that you configured the ESX hosts for the vSAN network.

The new ESX host's resources become associated with the cluster.

1. In the vSphere Client, navigate to the cluster.
2. Right-click the vSphere cluster and select Add New or Existing Hosts. The Add hosts wizard appears.

   Option | Description || New hosts | 1. Enter the IP address or FQDN. 2. Enter the username and password associated with the ESX host. |
   | Existing hosts | 1. Select ESX hosts that you previously added to vCenter. |
3. Click Next.
4. View the summary information and click Next.
5. Import an image from the ESX host to set as the new image for the cluster. You can either select an existing image or import an image from one of the ESX hosts.
6. Review the settings and click Finish. 

   The ESX host enters maintenance mode before the ESX host is added to the vSphere cluster.

Verify the vSAN Skyline Health status.

Verify that the vSAN Disk Balance health check is green.

For more information about vSAN cluster configuration and fixing problems, see [vSAN Cluster Configuration Issues.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/vsan-cluster-configuration-issues.html)