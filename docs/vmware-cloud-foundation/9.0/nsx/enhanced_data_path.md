---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/enhanced-datapath-1.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Enhanced Data Path
---

# Enhanced Data Path

Enhanced Datapath Path (EDP) is a packet forwarding stack, designed to provide superior performance in terms of throughput, packet rate, latency and CPU utilization.

The EDP network stack is the default stack in VCF 9 deployments, and it provides a performant alternative to the non-EDP standard stack. EDP is suitable for all use cases, from general compute workloads, network workloads, to niche workloads like NSX Edge, and telco NFV solutions. In new VCF 9 deployments virtual switches will operate in the EDP Standard mode by default.

## EDP Standard

EDP Standard is a mode that provides increased network performance and very high packet processing efficiency out of the box, exceeding the performance possible with the non-EDP Standard stack, and without the additional configurations associated with EDP Dedicated. EDP Standard is the recommended mode for maximizing host switch network performance in general compute environments and NSX Edge clusters.

## EDP Dedicated

EDP Dedicated is a prescriptive mode. In this mode, knowledge of workload traffic patterns and specific network requirements is needed to reserve physical resources like Physical CPUs.

## Requirements, Restrictions, and Limitations

- EDP Standard

  New VCF 9.0 Workload Domains will operate using Enhanced Data Path Standard by default.

  Upgrading, Converting or Importing Workload Domains to VCF 9.0 will not change the Virtual Switch mode from Standard to EDP Standard. This mode change is recommended, but should be planned separately.
- EDP Dedicated

  New VCF 9.0 Workload Domains will operate using Enhanced Data Path Standard by default. The virtual switch can be configured to EDP Dedicated mode. VCF 5.2.x and older systems running EDP Dedicated will continue operating in this mode when upgraded, converted or imported.

## EDP Enablement Overview

1. Use NIC cards that support the enhanced data path.

   See Broadcom [KB 343324](https://knowledge.broadcom.com/external/article/343324/download-and-install-async-drivers-in-vm.html) for details on how to download and install async drivers.
2. EDP requires Transport Nodes with Enhanced Data Path enabled. Choose between the following mode options:
   - **Standard**: This mode is compatible with the broadest set of hardware, but does not offer the latest performance improvements.
   - **Enhanced Datapath - Standard**: This mode runs an improved packet forwarding stack, recommended for general compute environments and NSX Edge clusters. This mode dynamically and efficiently allocates CPU resources. This is the default virtual switch mode in new VCF 9.0 environments.
   - **Enhanced Datapath - Dedicated**: This is the datapath operation dedicated to telco applications and virtual network functions. This mode requires preallocated and dedicated CPU cores.
3. In new environments, Enhanced Data Path Standard is the default mode. An option to change the virtual switch mode is presented when a Workload Domain is created.

   Converted, Imported and Upgraded environments running the non-EDP Stardard mode will contineu running the previous mode until EDP is selected in the Transport Node Profile configuration.

   Changing the virtual switch mode to EDP Standard in clusters where vSphere Configuration Profiles (VCP) are enabled is seamless and unimpactful. Simply change the mode in the Transport Node Profile.

   If working with non-VCP clusters, see the Enabling EDP procedures in the Networking section of the Administration Guide.