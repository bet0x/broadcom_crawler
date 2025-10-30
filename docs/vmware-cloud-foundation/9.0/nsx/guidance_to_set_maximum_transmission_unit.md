---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/mtu-guidance.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Guidance to Set Maximum Transmission Unit
---

# Guidance to Set Maximum Transmission Unit

Get guidance on how to set the Maximum Transmission Unit (MTU) value in the different objects or profiles in NSX.

## Jumbo Frame Support

The minimum required MTU is 1600 bytes. However, MTU of 1700 bytes is recommended to address the whole possibility of a variety of functions and future proof the environment for an expanding Geneve header. In order to get better performance for applications generating large packets, and for optimal throughput, increase MTU to atleast 9,000 bytes as long as underlay physical infrastructure supports it and is also set to use jumbp frame MTU of 9000 bytes.

## VM MTU

In most of the deployments, the guest VM MTU is set to1500 bytes. So no change is required for the VM MTU if the physical fabric has an MTU of 1700 bytes or higher. To improve the throughput, one can increase the MTU up to 8800 (a estimated number to accommodate bridging and future header expansion) only if underlay physical infrastructure is set to to use 9000 bytes. VM MTU should be set 100 bytes or more (200 preferred) lower than the MTU of the physical fabric.

## MTU Configuration

- Global Tunnel Endpoint MTU: To configure the MTU value, go to SystemSettingsGlobal Fabric Settings. The default value for MTU is 1700 bytes. When you set this MTU value, NSX configures the MTU value for all the N-VDS instances used in NSX Transport Nodes.
- Global Logical Interface MTU: To configure the MTU value, go to NetworkingGlobal Networking Config. The default value for MTU is 1500. When you set this MTU value, NSX configures the MTU value for all the logical router interfaces. If the Global Logical interface MTU value is not specified, the MTU value is taken from the Tier-0 logical router (T-0 Gateway). However, on a specific port, the logical router uplink MTU value can override the Global Logical interface MTU value.
- Uplink Profile MTU: To configure the MTU value, go to SystemProfilesUplink Profiles. When you set this MTU value, NSX configures the MTU value for NSX Transport nodes that use N-VDS switch. This MTU field is optional in the uplink profile. If you do not configure it, NSX takes the value set in the global Tunnel Endpoint MTU.
- (vSphere) VDS MTU: To configure the MTU value, go to the vCenter and modify the VDS directly. When you set this MTU value, NSX configures the MTU value for NSX Transport Nodes that use vSphere VDS. In this case, MTU value set on the attached uplink profile is not used.

## Design Guidance

For optimal throughput, set the Global Tunnel Endpoint MTU , Uplink Profile MTU, and vSphere VDS MTU to at least 9000 bytes as long as:

- The underlying infrastructure supports 9000 bytes.
- The underlying infrastructure is set to use jumbo frame MTU of 9000 bytes.

Otherwise, configure Global TEP MTU, Uplink Profile MTU, and vSphere VDS MTU to minimum 1600 bytes or minimum recommended 1700 bytes.

The Gateway Interface MTU can continue to have default value. If you modified the Gateway Interface MTU, the modified value must be at least 200 bytes less than the Fabric MTU (which refers to Global Tunnel Endpoint MTU or VDS MTU or Uplink Profile MTU).

When adjusting the fabric MTU packet size, you must also configure the entire network path (VMkernel ports, virtual switches, physical switches and routers) to support the same MTU packet size. If a device along the path does not support the required frame size and receives a frame larger than its MTU, the device will drop the frame.