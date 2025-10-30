---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/managing-the-nsx-manager-cluster/resize-an-nsx-manager-node.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Resize an NSX Manager Node
---

# Resize an NSX Manager Node

You can change the memory and CPU resources of an NSX Manager node in a cluster.

- Verify that the new size satisfies the memory and CPU resources system requirements for a manager node. .
- Familiarize yourself with how to run CLI commands. For more information, see the[NSX Command-Line Interface Reference](https://developer.broadcom.com/xapis/nsx-cli-guide/latest/). Also familiarize yourself with how to change the memory and CPU resources of a VM. For more information, see the vSphere documentation.

Note that in normal operating conditions all three manager nodes must have the same CPU and memory resources. A mismatch of CPU or memory between NSX Managers in an NSX Manager cluster should only be done when transitioning from one size of NSX Manager to another size.

If you have configured resource allocation reservation for the NSX Manager VMs in vCenter, you might need to adjust the reservation. For more information, see the vSphere documentation.

| Resizing Effort | Form Factors | Description |
| --- | --- | --- |
| Less effort | Small, Medium or Large | NSX requires that two managers are available at all times. If you have cluster VIP (virtual IP) configured, there will be a brief outage when the VIP switches to another node in the cluster. You can access the other two nodes directly during the outage if the VIP-assigned node is shut down for resizing. If you have deployed a load balancer for the manager nodes, health checks will be triggered when a manager goes offline. The load balancer should direct traffic to another node. |

- Resize an NSX manager node (Applicable to Small, Medium or Large form factor only. Do not use Small for Global Manager.)

  Change the CPU and memory of the existing NSX Manager nodes. You must make the change to one manager at a time so that two managers are available at all times. For form factor details, see Prerequisites.

  This procedure does not support the resizing of NSX Managers from or to the Extra Large form factor.

  This procedure remains the same if the NSX Manager nodes are deployed manually and the cluster is formed using join node CLI or if the NSX Manager nodes are deployed and the cluster is formed using NSX Manager UI.

  1. Log in to a manager's CLI as admin and run the shutdown command.
  2. From NSX Manager UI, verify that the state of the manager cluster is DEGRADED.
  3. From VMware vSphere, change the memory and/or CPU resources of the manager VM that was shut down.
  4. From vSphere, power on the VM. From NSX Manager UI, wait for the state of the manager cluster to be STABLE.
  5. Repeat steps 1 to 4 for the other two manager VMs.