---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/add-a-compute-manager-1/replace-compute-manager.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Replace Compute Manager
---

# Replace Compute Manager

To replace a compute manager (vCenter) with another compute manager (vCenter), determine if the existing compute manager has NSX Manager cluster or NSX Edge nodes registered to it and third-party services running on the NSX cluster.

Before you can replace the vCenter, you must delete any appliances or objects registered with the existing vCenter and then deploy them on the new vCenter.

1. Add a new compute manager. See Add a Compute Manager.
2. Replace NSX Manager cluster deployed from the Add Appliance wizard in the NSX Manager UI.

   Do not follow this procedure to replace NSX Manager appliances deployed from vCenter.

   1. Go to SystemAppliancesAdd NSX Appliance.
   2. Verify whether the status of NSX Manager is stable. If not, ensure the status of NSX Manager is stable before proceeding with the next steps.
   3. Delete an existing NSX Manager on the old compute manager.
   4. Verify status of cluster by running the command, get cluster status.
   5. On the new compute manager, deploy a new NSX Manager.
   6. Once the new NSX Manager is fully operational and has joined the NSX Manager cluster, verify the cluster status.
   7. You can also view the status by running the command, get cluster status.
   8. Repeat these steps till all the existing NSX Manager are replaced by new ones and the cluster status is stable.
3. Add new NSX Edge nodes.
   1. To add Edge node, see Create an NSX Edge Transport Node.
   2. When creating a new NSX Edge node,

      1. In the Name and Descritpion window, enter a new Host Name /FQDN.
      2. In the Configure Deployment window, select a different compute manager.
   3. Verify NSX Edge node is deployed.
   4. Repeat the steps for all the NSX Edge nodes.
   5. All NSX Edge nodes are registered with the new compute manager.
   6. Go to SystemFabricNodesEdge Clusters.
   7. Select the NSX Edge cluster and replace old NSX Edge nodes and add new NSX Edge nodes to the cluster. See Replacing an NSX Edge Transport Node in an NSX Edge Cluster.
   8. Click Save to save the NSX Edge cluster configuration.
4. Deploy third-party services.

   Any third-party services registered with the existing vCenter must be uninstalled from the old vCenter and reinstalled on the new vCenter.

   1. On the old compute manager, uninstall services introspecting east-west traffic. See  Uninstall an East-West Traffic Introspection Service.
   2. On the old compute manager, uninstall services introspecting north-south traffic. See Uninstall a North-South Traffic Introspection Service.
   3. Install third-party services on the new compute manager.

      See Deploy a Service for East-West Traffic Introspection.

      See  Deploy a Service for North-South Traffic Introspection.

The old vCenter is replaced by the new vCenter and all appliances and objects are running on the new vCenter.