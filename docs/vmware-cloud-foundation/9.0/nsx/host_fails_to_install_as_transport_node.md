---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-host-transport-nodes/host-fails-to-install-as-transport-node.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Host Fails to Install as Transport Node
---

# Host Fails to Install as Transport Node

When many
hosts are are prepared simultaneously (in non vLCM way) some hosts may fail in the
internal step of downloading nsx lcp bundle to the host. Error seen is "Failed to
download NSX components on host.

1. Check the host connectivity and
   ensure that the "/tmp" folder has enough space.
2. If it is fine then check if there are many hosts getting prepared at this time.
   Wait for host prep of other hosts to complete.
3. Follow the usual error resolution steps from the UI or API to re trigger the
   operation on the failed host.