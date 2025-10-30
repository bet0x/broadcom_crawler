---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/enhanced-datapath/enabling-enhanced-data-path-standard-in-new-environment.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Enabling Enhanced Data Path Standard in New Environment
---

# Enabling Enhanced Data Path Standard in New Environment

EDP Standard can be enabled in a “new environment” as a way to maximize or future-proof a cluster’s packet processing capabilities.

## What qualifies as a new environment in this context?

- New VCF Workload Domains.
- Created VCF environments that will utilize a new NSX Manager.

## Overview of enabling EDP Standard in a new environment

1. Confirm pNIC Driver & Firmware compatibility with EDP Standard.
2. Understand the Requirements, Restrictions & Limitations in [Enhanced Data Path](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/enhanced-datapath-1.html).
3. In VCF deployments, no manual intervention is required. When configuring workload domains, EDP Standard is selected by default as the virtual switch operational mode in the Switch configuration page. See Add a vSphere Cluster to a Workload Domain using the SDDC Manager UI.

## About the datapath modes

- **Standard**: This mode is compatible with the broadest set of hardware but does not offer the latest performance improvements.
- **Enhanced Datapath - Standard**: This mode runs an improved packet forwarding stack with the latest network performance advancements. This is recommended for general compute environments and NSX Edge clusters. This mode dynamically and efficiently allocates CPU resources.

  This is the default virtual switch mode.
- **Enhanced Datapath - Dedicated**: This is the datapath operation dedicated to telco applications and virtual network functions. This mode requires preallocated and dedicated CPU cores.