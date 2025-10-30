---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/trigger-auto-deployment-on-target-hosts/apply-tnp-on-stateless-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Apply TNP on Stateless Cluster
---

# Apply TNP on Stateless Cluster

NSX configuration and installation only happens on the target hosts when TNP is applied to the cluster.

1. Note down the settings extracted in the Host Profile from the reference host. The corresponding entities in the TNP profile must have the same value. For example, the VDS name used in the Host Profile and TNP must be the same.

   For more information on extracted host profile settings, see [Extract and Verify the Host Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/extract-and-verify-the-host-profile.html).
2. Add a TNP.
3. Add a TNP by entering all required field. 

   Ensure that values of the following parameters are the same on both the new TNP profile and the existing Host Profile.

   On a VDS switch, migration of VMkernel adapters and physical NIC migration is not supported.

   - Transport Zone: Ensure transport zone referenced in Host Profile and TNP is the same.
   - VDS Name: Ensure VDS name referenced in Host Profile and TNP is the same.
   - Uplink Profile: Ensure uplink profile referenced in Host Profile and TNP is the same.
   - Teaming Policy:
     - (On a VDS switch) In vCenter, when creating VDS uplinks, verify the NIC used in the Host Profile and map that physical NIC to the VDS uplink. In NSX-T, you map NSX uplinks to VDS uplinks. So, verify the configuration on the VDS switch in vCenter.

   After applying TNP on target nodes, if the TNP configuration does not match Host Profile configuration, the node might not come up because of compliance errors.
4. Verify that the TNP profile is successfully created.
5. Apply TNP profile to the target cluster and click Save.
6. Verify that the TNP profile is successfully applied to the target cluster. It means that NSX is successfully configured on all nodes of the cluster.
7. In NSX, verify that the ESX host is configured successfully as a transport node.

Alternatively, you can reboot a target host after applying TNP to the cluster. See [Reboot Hosts After Applying TNP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/trigger-auto-deployment-on-target-hosts/reboot-hosts-after-applying-tnp.html#GUID-52fa9a09-bd76-424e-8c89-f361c4dfe122).