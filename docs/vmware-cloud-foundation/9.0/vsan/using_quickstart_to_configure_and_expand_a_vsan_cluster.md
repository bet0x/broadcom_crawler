---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/using-quickstart-to-configure-a-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Using Quickstart to Configure and Expand a vSAN Cluster
---

# Using Quickstart to Configure and Expand a vSAN Cluster

You can use the Quickstart workflow to quickly create, configure, and expand a vSAN cluster.

Quickstart consolidates the workflow to enable you to quickly configure a new vSAN cluster that uses recommended default settings for common functions such as networking, storage, and services. Quickstart groups common tasks and uses configuration wizards that guide you through the process. Once you enter the required information on each wizard, Quickstart configures the cluster based on your input.

Quickstart uses the vSAN health service to validate the configuration and help you correct configuration issues. Each Quickstart card displays a configuration checklist. You can click a green message, yellow warning, or red failure to display details.

Hosts added to a Quickstart cluster are automatically configured to match the cluster settings. The ESX software and patch levels of new hosts must match those in the cluster. Hosts cannot have any networking or vSAN configuration when added to a cluster using the Quickstart workflow. For more information about adding hosts, see [Expanding a vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/expanding-a-vsan-cluster.html).

If you modify any network settings outside of QuickStart, this hampers your ability to add and configure more hosts to the cluster using the QuickStart workflow.

## Characteristics of a Quickstart Cluster

A vSAN cluster configured using Quickstart has the following characteristics.

- Hosts must have ESX 9.0 or later.
- Host all have similar configuration, including network settings. Quickstart modifies network settings on each host to match the cluster requirements.
- Cluster configuration is based on recommended default settings for networking and services.
- Licenses are allocated to vCenter and gets automatically assigned to the vSAN clusters.

## Managing and Expanding a Quickstart Cluster

Once you complete the Quickstart workflow, you can manage the cluster through vCenter, using the vSphere Client or command-line interface.

You can use the Quickstart workflow to add hosts to the cluster and claim additional disks. But once the cluster is configured through Quickstart, you cannot use Quickstart to modify the cluster configuration.

The Quickstart workflow is available only through the HTML5-based vSphere Client.

## Skipping Quickstart

You can use the Skip Quickstart button to exit the Quickstart workflow, and continue configuring the cluster and its hosts manually. You can add new hosts individually, and manually configure those hosts. Once skipped, you cannot restore the Quickstart workflow for the cluster.

The Quickstart workflow is designed for new clusters. When you upgrade an existing vSAN cluster, the Quickstart workflow appears. Skip the Quickstart workflow and continue to manage the cluster through vCenter.