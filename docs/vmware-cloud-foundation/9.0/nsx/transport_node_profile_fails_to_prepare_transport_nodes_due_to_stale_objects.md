---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-host-transport-nodes/transport-node-profile-fails-to-prepare-transport-nodes.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Transport node profile Fails to Prepare Transport Nodes Due to Stale Objects
---

# Transport node profile Fails to Prepare Transport Nodes Due to Stale Objects

Transport node profile (TNP) fails
to prepare transport nodes due to stale objects in TNP.

NSX
displays the following error when TNP fails to prepare hosts into transport nodes:
The requested object <uuid> could not be found. Object
identifiers are case sensitive. Please make the appropriate changes and reapply
the configuration.

This issue can occur if any configuration
specified in the TNP does not exist in NSX Manager or vCenter.

1. Search the UUID in NSX Manager to find out the object
   being referred to in the error.
2. Edit the Transport Node Profile
   to remove the referenced stale object (could be TNP itself, IP Pool, Profile
   etc) and then retrigger host configuration.