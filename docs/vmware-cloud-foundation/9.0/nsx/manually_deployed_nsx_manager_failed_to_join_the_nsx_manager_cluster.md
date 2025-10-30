---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshoot-nsx-manager-cluster/manually-deployed-nsx-manager-failed-to-join-the-nsx-manager-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Manually deployed NSX Manager failed to join the NSX Manager Cluster
---

# Manually deployed NSX Manager failed to join the NSX Manager Cluster

A
NSX Manager that is manually deployed
in vCenter using OVF or OVA file
failed to join the NSX Manager
cluster.

You
used an incorrect thumbprint value to join the new NSX Manager node to the existing NSX Manager cluster. If NSX VIP is configured, then use the cluster thumbprint command. If
external VIP or no VIP is configured, use the API thumbprint command. Try registering
the NSX Manager node with the cluster
using correct thumbprint.

1. You can manually deploy NSX Manager by running one of the following commands.
   - Run the get
     certificate cluster thumbprint command and then run
     Join management-plane <cluster-vip> username
     <manager-username> password <manager-pwd> thumbprint
     <cluster-thumbprint> command. The procedure to join the
     management node with the cluster is complete. Alternatively, you can use the
     NSX Manager thumbprint, as shown in the following steps to join the NSX
     Manager with the cluster.
   - Or run the get
     certificate api thumbprint command and then run the
     Join management-plane <manager-ip> username
     <manager-username> password <manager-pwd> thumbprint
     <manager-thumbprint> command.