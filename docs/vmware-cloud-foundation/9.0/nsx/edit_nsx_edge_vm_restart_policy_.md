---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/edit-edge-vm-restart-priority.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Edit NSX Edge VM Restart Policy 
---

# Edit NSX Edge VM Restart Policy

You can set the restart policy for an NSX Edge VM deployed from the vSphere Client at a cluster level using the VM Override property.

- NSX Edge node must be deployed. See the NSX Installation Guide for more details.

Restart priority ensure that NSX Edge VM is restarted first and virtual network infrastructure is up and running before the worload sends North-South traffic to the NSX Edge VM.

When you deploy an NSX Edge node from NSX Manager, redeploy an NSX Edge or upgrade an NSX Edge, restart priority of NSX Edge VM is automatically set to Highest.

To validate NSX Edge restart policy is set to Highest, go to the

1. With admin privileges, log in to the vSphere Client.
2. At the cluster lever, vSphere HA is enabled.
3. To verify the NSX Edge restart policy, perform the following steps:
   1. Select a cluster.
   2. Select ConfigurevSphere Availability.
   3. Verify that vSphere HA is turned on.
   4. In the Edit Cluster Settings window, expand Host Failure Response section and verify that Failure Response is set to Restart VMs and Default VM Restrart Priority is set to Highest.

When an NSX Edge node fails, it is restarted as per the configured restart priority. If you set the priority to Highest, NSX Edge node comes back up before other hosts in the cluster.