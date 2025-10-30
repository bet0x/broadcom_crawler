---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/preparing-esxi-cluster-hosts-as-transport-nodes-through-vcenter.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Preparing ESX Cluster Hosts as Transport Nodes through vCenter
---

# Preparing ESX Cluster Hosts as Transport Nodes through vCenter

Prior to VCF 9.0, both NSX admin and VI admin were required to perform this task. A VI admin created a VDS and added hosts to proper uplinks and an NSX admin configured TN (or Transport Node Profile at a cluster level) settings through NSX API or UI by defining virtual switches (VDS) and their properties. This required for both the admins to be in a complete sync for creating a transport node successfully.

Starting with VCF 9.0, a vCenter admin (VI admin) can configure ESX hosts as transport nodes (TN) directly from vCenter. After the NSX admin has created a Transport Node Profile (TNP), a VI admin will be able to carry out the entire process of TN creation through vCenter with the Config Manager or vSphere Cluster Profile (VCP) feature. A VI admin will define the Virtual Distributed Switch (VDS) configuration at a cluster level and specify uplinks that the hosts will utilize. Additionally, the VI admin will also set NSX configuration (Transport Node Profile) in the cluster document. This cluster-level configuration ensures uniformity across member hosts through the Config Manager workflow that includes the following stages:

- Validation
- Compliance check
- Impact
- Remediation

The VI admin undertakes the following workflow to prepare an ESX cluster as Transport Nodes.

1. Create a VDS host switch.
2. Create a VCP enabled cluster or enable VCP on an existing cluster.
3. Add hosts to this cluster if required.
4. From the Configure tab of this cluster, create a draft for the cluster from its Config Manager by using any of the following options:

   - Create Draft
   - Import From File
   - Import from Host
5. Run the pre-check and apply changes.
6. Check the compliance.

Once all the steps are completed, transport nodes are prepared for NSX. You can check the progress from vCenter too.

You can also check the progress from NSX Manager by navigating to **System > Fabric > Hosts > Clusters**. A VCP capsule is shown for the VCP-enabled clusters.

Note that on a VCP cluster all the CRUD operations including uninstall are blocked from NSX Manager. These operations on a VCP enabled cluster can only be performed from vCenter.

If you try to change a TNP of a VCP cluster from NSX Manager, you will get an error. To attach a new TNP to a VCP cluster, you will have to perform the following steps.

1. Create a new TNP.
2. Go to vCenter.
3. Go to the Draft tab of the cluster and create a new draft.
4. Once the configuration is completed, update the NSX Config in Cluster Desired Doc.
5. Run the pre-check and apply changes.
6. Check the compliance.

Once these steps are completed successfully, the Transport Node Cluster and TNs are prepared.

Also, from NSX Manager if you update any property of a TNP that is applied to a VCP cluster (say VDS), you will see a “Preparing hosts is pending message” for that cluster. You will have to go to vCenter and complete the remaining steps from there.