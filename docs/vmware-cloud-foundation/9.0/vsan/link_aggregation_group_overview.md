---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/advanced-nic-teaming/link-aggregation-group-overview.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Link Aggregation Group Overview
---

# Link Aggregation Group Overview

By using the LACP protocol, a network device can negotiate an automatic bundling of links by sending LACP packets to a peer.

A Link Aggregation Group (LAG) states that Link Aggregation allows one or more links to be aggregated together to form a Link Aggregation Group.

LAG can be configured as either static (manual) or dynamic by using LACP to negotiate the LAG formation. LACP can be configured as follows:

Active
:   Devices immediately send LACP messages when the port comes up. End devices with LACP enabled (for example, ESX hosts and physical switches) send and receive frames called LACP messages to each other to negotiate the creation of a LAG.

Passive
:   Devices place a port into a passive negotiating state, in which the port only responds to received LACP messages, but do not initiate negotiation.

If the host and switch are both in passive mode, the LAG does not initialize, because an active part is required to trigger the linking. At least one must be Active.

For more information about LACP support on a vSphere Distributed Switch, see the [vSphere Networking](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-networking.html) guide.

The number of LAGs you can use depends on the capabilities of the underlying physical environment and the topology of the virtual network.