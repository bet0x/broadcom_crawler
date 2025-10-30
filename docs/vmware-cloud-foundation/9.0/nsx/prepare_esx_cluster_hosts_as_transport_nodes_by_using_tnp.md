---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/preparing-esxi-hosts-as-transport-nodes/prepare-esxi-cluster-hosts-as-transport-nodes.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Prepare ESX Cluster Hosts as Transport Nodes by Using TNP
---

# Prepare ESX Cluster Hosts as Transport Nodes by Using TNP

If a cluster of ESX hosts is registered to a vCenter, you can apply transport node profiles on the vCenter cluster to prepare all hosts part of the cluster as NSX transport nodes or you can prepare each host individually.

- Verify all hosts that you want to configure as transport nodes are powered on in vCenter.
- Verify all hosts are members of VDS in vCenter with correct uplinks.
- Verify that the system requirements are met.
- Verify vCenter is added as compute manager to NSX Manager.
- Verify NSX Manager cluster is up and stable.
  - UI: Go to SystemAppliancesNSX Appliances.
  - CLI: SSH to one of the NSX Manager nodes as an admin and run get cluster status.
- The reverse proxy service on all nodes of the NSX Manager cluster must be Up and running.

  To verify, run get service http. If the service is down, restart the service by running restart service http on each NSX Manager node. If the service is still down, contact VMware support.

- Verify that a transport node profile is configured. See [Adding a Transport Node Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/add-a-transport-node-profile.html).

Use the following procedure to apply a TNP to a cluster.

Changing the switch mode when applying a TNP to a cluster can result in data path impact. Refer to Enabling EDP Standard in Active Environments for a non-impactful procedure.

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Select SystemFabricHosts.
3. On the Cluster tab, select a cluster and click Configure NSX.
4. In the NSX Installation pop-up window, from the Transport Node Profile drop-down menu, select the transport node profile to apply to the cluster. If a transport node is not created, click Create New Transport Node Profile to create a new one.

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/b48418f8-55a0-4e63-98c3-75ba2d105b7b.original.png)
5. Click Apply to begin the process of transport node creation of all hosts in the cluster.

   See [Adding a Transport Node Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/add-a-transport-node-profile.html).

To prepare individual hosts, see [Prepare ESX Individual Hosts as Transport Nodes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/preparing-esxi-hosts-as-transport-nodes/prepare-esxi-individual-hosts-as-transport-nodes.html).