---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-qos-segment-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Understanding QoS Segment Profile
---

# Understanding QoS Segment Profile

QoS provides
high-quality and dedicated network performance for preferred traffic that
requires high bandwidth. The QoS mechanism does this by prioritizing sufficient
bandwidth, controlling latency and jitter, and reducing data loss for preferred
packets even when there is a network congestion. This level of network service
is provided by using the existing network resources efficiently.

For this release, shaping and
traffic marking namely, CoS and DSCP is supported. The Layer 2 Class of Service
(CoS) allows you to specify priority for data packets when traffic is buffered
in the segment due to congestion. The Layer 3 Differentiated Services Code
Point (DSCP) detects packets based on their DSCP values. CoS is always applied
to the data packet irrespective of the trusted mode.

NSX trusts the
DSCP setting applied by a virtual machine or modifying and setting the DSCP
value at the segment level. In each case, the DSCP value is propagated to the
outer IP header of encapsulated frames. This enables the external physical
network to prioritize the traffic based on the DSCP setting on the external
header. When DSCP is in the trusted mode, the DSCP value is copied from the
inner header. When in the untrusted mode, the DSCP value is not preserved for
the inner header.

DSCP settings work only on
tunneled traffic. These settings do not apply to traffic inside the same
hypervisor.

You can use the QoS switching
profile to configure the average ingress and egress bandwidth values to set the
transmit limit rate. The peak bandwidth rate is used to support burst traffic a
segment is allowed to prevent congestion on the northbound network links. These
settings do not guarantee the bandwidth but help limit the use of network
bandwidth. The actual bandwidth you will observe is determined by the link
speed of the port or the values in the switching profile, whichever is lower.

The QoS switching profile
settings are applied to the segment and inherited by the child segment port.