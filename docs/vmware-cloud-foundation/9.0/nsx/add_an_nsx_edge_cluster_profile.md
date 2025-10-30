---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/add-an-edge-bridge-profile/add-an-edge-cluster-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an NSX Edge Cluster Profile
---

# Add an NSX Edge Cluster Profile

The NSX Edge cluster profile defines policies for NSX Edge transport nodes that are part of an NSX Edge cluster.

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Select SystemFabricProfilesEdge Cluster ProfilesAdd Profile.
3. Enter the NSX Edge cluster profile details.

   Option | Description || Name and Description | Enter an NSX Edge cluster profile name. Optionally, describe the profile you want to create. For example, Bidirectional Forwarding Detection (BFD) setting for the profile. |
   | BFD Probe Interval | Accept the default setting. BFD is a detection protocol used to identify the forwarding path failures. To detect a forwarding path failure, you can set the interval timing for BFD . |
   | BFD Allowed Hops | Accept the default setting. You can set the maximum number of hops multi-hop BFD sessions can transit. |
   | BFD Declare Dead Multiple | Accept the default setting. You can set the number of times the BFD packet is not received before the session is flagged as down. |
   | Stand By Relocation Threshold | Accept the default setting.  The minimum threshold value must be 10 min.  The recommended threshold value is 30 min. |