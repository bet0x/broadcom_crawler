---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/getting-started-with-federation/federation-requirements.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > NSX Federation Requirements
---

# NSX Federation Requirements

To support NSX Federation, your environment must meet various requirements, including round-trip time, software versions, and ports.

- There must be a maximum round-trip time of 500 ms between the following nodes:
  - Active Global Manager and standby Global Manager.
  - Global Manager and Local Manager.
  - Local Manager and remote Local Manager if you have cross-location security configuration only and VMware NSX® Edge™ Nodes RTEP and remote Edge Nodes RTEP if you have cross-network configurations.
- The Global Manager and Local Manager appliances must all have NSX 3.1.0 or later installed. All appliances in an NSX Federation environment must have the same version installed.
- The required ports must be open to allow communication between the Global Manager and Local Manager. See VMware Ports and Protocols at <https://ports.broadcom.com/home/NSX>.
- There must be connectivity without NAT between the following nodes:
  - Global Manager and Local Manager.
  - Local Manager and remote Local Manager.
  - Edge node RTEP and remote Edge node RTEP.
- Verify that each location has a default overlay transport zone configured. From each Local Manager, select System > Fabric > Transport Zones. Select an overlay transport zone, and click Actions > Set as Default Transport Zone.
- Global Manager supports only Policy Mode. NSX Federation does not support Manager Mode. See

An NSX Federation environment has the following configuration maximums:

- For most configurations, the Local Manager cluster has the same configuration maximums as an NSX Manager cluster. Go to [VMware Configuration Maximums tool](https://configmax.vmware.com/home) and select NSX.

  Select the NSX Federation category for NSX in the [VMware Configuration Maximums tool](https://configmax.vmware.com/home) for exceptions and other NSX Federation-specific values.
- For a given location, the following configurations contribute to the configuration maximum:
  - Objects that were created on the Local Manager.
  - Objects that were created on the Global Manager and include the location in its span.

  You can view the capacity and usage on each Local Manager. See View the Usage and Capacity of Categories of Objects in the NSX Administration Guide.

  You can view the capacity and usage on each Local Manager. See View the Usage and Capacity of Categories of Objects in the NSX Administration Guide.