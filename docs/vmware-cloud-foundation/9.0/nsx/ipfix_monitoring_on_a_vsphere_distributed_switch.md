---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/ipfix-monitoring-on-a-vsphere-distributed-switch.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > IPFIX Monitoring on a vSphere Distributed Switch
---

# IPFIX Monitoring on a vSphere Distributed Switch

Configure IPFIX monitoring for NSX Distributed Virtual port groups, and vSphere
Distributed Virtual port groups that are connected to a VDS switch enabled to support
NSX networking.

From vSphere, enable IPFIX for Distributed Virtual port groups
(vSphere) and from NSX Manager, enable IPFIX for segments
(NSX) created on a VDS switch.

vSphere Distributed Services Engine provides the ability to offload some of the network operations from your server CPU to a Data Processing Unit (DPU also known as SmartNIC). vSphere 8.0 supports NVIDIA BlueField and AMD Pensando DPU devices only.

For more information about VMware vSphere Distributed Services Engine, see Introducing VMware vSphere® Distributed Services EngineTM and Networking Acceleration by Using DPUs in the VMware vSphere® product documentation.

If you want to configure IPFIX on DPU backed
VDS, you must create vmknic on 'ops' TCP/IP stack.

To enable IPFIX monitoring for Distributed Virtual port groups, see the vSphere Networking
documentation.

To enable IPFIX monitoring for NSX port groups, see [Add a Switch IPFIX Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/add-a-switch-ipfix-profile.html#GUID-57dd8a30-ebf8-4278-9fa0-6121c83b1768-en).

A VDS switch enabled for NSX displays
the following behavior:

- Both non-uplink and uplink ports support bidirectional traffic incoming and
  outgoing on:
  - Ports, port groups, VMs on vSphere.
  - Segments, segment ports, and groups on NSX
- IPFIX profile samples packets on uplink ports when are coming from or going to
  non-uplink ports that are IPFIX enabled. For example, consider that
  VM-A and VM-B are connected to
  non-uplink ports (port-1, port-2), where port-1 connected to
  VM-A is IPFIX enabled, and port-2 connected to
  VM-B is not IPFIX enabled. When you send traffic from
  VM-A and VM-B traffic to port-1, only
  packets from VM-A are sampled because IPFIX is enabled only
  on the port that VM-A is connected to. IPFIX does not sample
  packets coming from the port-2 associated to VM-B because
  IPFIX is not enabled on that port.
- Packet count exported to the IPFIX collector is the total count based on a
  sampling rate, not the sampled packets. For example, IPFIX calculates the
  count of total packets and exports the info. For 100 incoming packets, IPFIX
  might sample 9–11 packets. It exports 90 or 110 packets to the IPFIX
  collector.