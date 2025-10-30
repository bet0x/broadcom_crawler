---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/stateful-servers.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Stateful Servers
---

# Stateful Servers

Integrate host profiles of an ESX
host with NSX on stateful
servers.

A stateful host is a host that retains all configurations and the installed VIBs even
after it is rebooted. While an auto-deploy server is needed for stateless hosts because
the boot up files required to bring up a stateless hosts are stored on the auto-deploy
server, a stateful host does not need a similar infrastructure. Because the boot up
files required to bring up a stateful host is stored on its hard drive.

In this procedure, the reference host is
outside of the stateful cluster and the target hosts in the cluster. A target host can
be within a cluster or a standalone host outside of the cluster. Prepare a cluster by
applying host profile and transport node profile (TN profile) , so that any new target
hosts joining the cluster is automatically prepared with NSX VIBs. Configure the target host as a
transport node. Similarly, for a standalone host, apply the host profile and configure
NSX to install NSX VIBs and when NSX configuration is complete, it becomes a
transport node.

NSX VIBs are installed from TN profile and ESX host configurations are applied by the
Host Profiles.