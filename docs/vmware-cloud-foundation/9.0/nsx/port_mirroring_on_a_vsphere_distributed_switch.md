---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/port-mirroring-on-a-vsphere-distributed-switch.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Port Mirroring on a vSphere Distributed Switch
---

# Port Mirroring on a vSphere Distributed Switch

You can configure port mirroring for port groups, virtual NICs of VMs, and VMs created in NSX and vSphere Distributed Virtual port groups created in vSphere that are connected to a vSphere Distributed Switch (VDS) switch.

In vCenter, configure port mirroring for vSphere Distributed Virtual port groups on a VDS switch.

In NSX Manager, configure port mirroring for segments (in NSX) on a VDS switch.

You cannot edit configuration for a segment created in NSX in vCenter. As an admin, you can view the properties of a port mirroring session to know on which switch it is created.

vSphere Distributed Services Engine provides the ability to offload some of the network operations from your server CPU to a Data Processing Unit (DPU also known as SmartNIC). vSphere 8.0 supports NVIDIA BlueField and AMD Pensando DPU devices only.

For more information about VMware vSphere Distributed Services Engine, see Introducing VMware vSphere® Distributed Services EngineTM and Networking Acceleration by Using DPUs in the VMware vSphere® product documentation.

If you want to configure ERSPAN on DPU backed VDS, you must create vmknic on 'mirror' TCP/IP stack.

To enable port mirroring on vSphere Distributed Virtual port groups, see the vSphere Networking documentation.

The following conditions hold for vSphere port mirroring:

- RSPAN destination will not monitor vNIC ingress traffic.
- RSPAN VLANs should be dedicated VLANs and must not be used as switching VLAN or trunk VLAN.

To enable port mirroring on segments, ports, and groups in NSX from NSX Manager, see [Add a Port Mirroring Session](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/add-a-port-mirroring-session.html#GUID-f0b687ac-3d58-4288-8187-38c2dd15d33f-en).

## Uplink Conflict Between Teaming and Remote SPAN

In vSphere, by default, the Remote SPAN in a teaming policy is set to Disallowed. If you use all the available physical NICs to configure remote SPAN, there are no free uplinks available for the teaming policy to consume. The unavailability of any free uplink means that uplink traffic is not allowed on destination ports, resulting in configuration errors.

However, in NSX, by default, Normal I/O on Destination Ports is set to Allowed. In NSX, port mirroring configured for NSX port groups on VDS switch allows teaming and port mirroring on destination ports. So, uplink configuration errors do not occur in NSX.

To resolve a uplink conflict when configuring teaming and remote SPAN:

- Ensure that a free uplink is available. For example, on an ESX host with 2 physical NICs, do not assign both these uplinks as destination IP addresses in the remote span port mirroring profile to avoid uplink conflicts in configuration. There must be at least one available uplink that can be configured in teaming profile.
- In vCenter, edit the port mirror configuration profile and set the Normal I/O on Destination Ports to Allowed.