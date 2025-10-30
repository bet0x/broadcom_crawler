---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-host-transport-nodes/unable-to-power-on-vm-or-vmotion-on-transport-node.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Unable to power on VMs or vMotion VMs on Transport Node
---

# Unable to power on VMs or vMotion VMs on Transport Node

The Virtual Distributed L2 (VDL2) component is down. This component must be up for NSX to successfully complete VM operations that are attaced to a segment on the transport node.

NSX displays the following error message: Currently connected network interface" 'Network adapter 1' uses network 'VM\_NETWORK:vdl2 down)

1. SSH to host and run following command to verify status of vdl2 component, net-dvs | grep "component.vdl2"

   ```
   com.vmware.common.opaqueDvs.status.component.vdl2 = down , propType = RUNTIME
   ```
2. Run net-vdl2 –l to verify VTEP interface is assigned valid IP Address, Gateway and status of each interface is UP.
3. Run esxcfg-vswitch –l to verify minimum MTU of minimum 1600 bytes (minimum 1700 bytes is recommended) is set up on the VDS switch used by NSX and uplinks assigned to VTEP interfaces are UP.
4. To view host switch information, run one of the following transport node state API:
   1. (deprecated) GET api/v1/transport-nodes/<uuid>/state
   2. GET api/v1/infra/sites/<site-id>/enforcement-points/<enforcementpoint-id>/host-transport-nodes/<host-transport-node-id>/state, where default values for enforcementpoint-id and site-id is ‘default’ or GET api/v1/transport-nodes/<uuid>/state (deprecated).

1. Ensure that the configuration details entered in these fields are correct:

   - VTEP IP Pool
   - VTEP VLAN
   - VDS MTU
   - Status of assigned PNIC (must be Up)
2. If VTEP pool is configured using DHCP, verify that DHCP server is assigning valid IP addresses to the VTEP pool.