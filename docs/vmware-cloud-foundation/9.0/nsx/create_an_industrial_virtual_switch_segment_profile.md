---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-industrial-vswitch-segment-profile/create-an-industrial-virtual-switch-segment-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create an Industrial Virtual Switch Segment Profile
---

# Create an Industrial Virtual Switch Segment Profile

You can create an Industrial vSwitch (IvS) Segment Profile to support these switch types.

For a complete description of configuring an IvS for NSX, see [Configure an Industrial vSwitch](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/enhanced-data-path-optional-configurations/configuring-industrial-vswitch.html).

1. With admin privileges, log in to the NSX Manager.
2. Navigate to NetworkingSegmentsProfilesSegment Profiles.
3. Click Add Segment Profile and select Industrial vSwitch and enter Segment Profile name.
4. Complete the segment IvS profile details:

   | Options | Description |
   | --- | --- |
   | Parallel Redundancy Protocol | Enables PRP for the Segment and allows the connected vNICs to behave as vDANs. |
   | Latency Measurement | Turns on or off the vNIC to the uplink latency measurement. This requires the vmxnet driver version 1.9 or newer. |
   | Sampling Rate (Number of packets) | Indicates the frequency to sample packets for latency measurement. A value of 10 means to sample every 10th packet. The default Sampling Rate is 1. |
   | Full Network Path Latency | Set to On for full network path latency. If set to Off, then latency through the guest OS is not measured. |
   | Retain VLAN Priority Field | If set to On, the priority field or Priority Code Point (PCP) priority tag will be retained after VLAN operation. |
   | DCP Multicast Address | Discovery and Configuration Protocol (DCP) is part of the PROFINET protocol suite. It is used to discover IO devices, Identity device information, and configure device settings, such as the device name and IP address.  The default configuration uses a couple of multicast macs - 01:0e:cf:00:00:00, 01:0e:cf:00:00:01. If non-empty set MAC addresses are provided as input, then it will override these default multicast MACs. |
5. Click Save.