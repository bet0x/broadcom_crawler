---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-industrial-vswitch-segment-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Understanding Industrial vSwitch Segment Profile
---

# Understanding Industrial vSwitch Segment Profile

The Industrial vSwitch (IvS) is an EDP (Enhanced Data Path) Dedicated mode switch that can facilitate real-time PROFINET communication between PROFINET devices in an industrial Ethernet network.

The IvS aims to deliver deterministic, low-latency, and highly available connectivity between vPLCs and IO devices in industrial networks. It is not meant to support high-performance, high-throughput workloads and networks.

The IvS Segment Profile can only be enabled on VLAN Transport Zones. It can be configured to enable support for PROFINET protocol on vNICs connected to applications that require PROFINET and PROFINET-RT, such as virtual programmable logic controllers (vPLCs). VLANs/segments configured with the IvS Segment Profile, can have the following capabilities:

- Allows for the vPLCs to be discovered by other PROFINET devices using Discovery and Basic Configuration Protocol (DCP).
- Enables the option to retain Priority Code Point (PCP) value from the 802.1Q VLAN tag in PROFINET RT packets sent by the vPLCs and PROFINET IO devices.
- Enables packet latency measurement for TX/RX traffic between the vNICs and the physical uplinks, and therefore allows the administrator to monitor and alert on the critical latency metrics for PROFINET traffic to and from the vPLCs.
- Enables Parallel Redundancy Protocol (PRP) to be configured on the segment and provides for the vPLC to behave like a vDAN in a PRP domain.

The default IvS Segment Profile has all settings disabled and does not impact the operations of vNICs attached with such profile.