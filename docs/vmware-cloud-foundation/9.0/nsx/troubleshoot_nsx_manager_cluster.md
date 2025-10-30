---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshoot-nsx-manager-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Troubleshoot NSX Manager Cluster
---

# Troubleshoot NSX Manager Cluster

You
must configure a three-node NSX Manager
cluster and only one of the nodes can fail at any given time for the cluster to
self-heal.

For an NSX Manager cluster to self-recover from a node failure, the majority of
nodes must not have failed (the number of active nodes must be greater than the failed
nodes) otherwise the entire cluster becomes unavailable. It means that all write
operations are blocked, all clustering related API/CLIs fail. However, local API/CLI
commands continue to work.

NSX Manager logs are written into /var/log/syslog,
directory.

## Admin CLI

To activate Admin CLI, log in as an
admin to a NSX Manager. But if you
login as root, you can run singleton admin CLI directly from the root shell using
the su admin –c <cmd-to-run> command. You can switch on
interactive mode of admin CLI using the su admin command and
then run admin commands.