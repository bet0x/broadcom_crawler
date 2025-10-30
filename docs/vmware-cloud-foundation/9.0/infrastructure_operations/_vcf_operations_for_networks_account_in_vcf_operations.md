---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vrealize-network-insight.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations >   VCF Operations for networks Account in VCF Operations
---

# VCF Operations for networks Account in VCF Operations

The VCF Operations for networks adapter activates integration of VCF Operations with VCF Operations for networks. VCF Operations for networks provides network visibility and analytics to minimize risk during application migration, optimize network performance, manage and scale NSX, vCenter on VMware Cloud on AWS, VMware SD-WAN by VeloCloud, and Kubernetes deployments.

- Cloud Integration can be done, when VCF Operations for networks and VCF Operations services are present in the same organization.
- For the cloud integration to be possible, you must have VCF Operations for networks and VCF Operations services in the same geographical location.

This adapter gets problem events from VCF Operations for networks and publishes the alerts in VCF Operations. Alerts are mapped correctly to the common objects between VCF Operations for networks and VCF Operations. Common objects supported in this adapter are vCenter and NSX For the common objects, VCF Operations supports launch-in-context to VCF Operations for networks. This allows the user to perform deep network troubleshooting with the VCF Operations for networks as the context.

The VCF Operations for networks adapter only supports VCF Operations for networks versions 5.2 and above. The VCF Operations for networks adapter can be installed and configured with the on-prem versions of VCF Operations. The VCF Operations for networks adapter does not support cross platform configuration, it should be on-prem VCF Operations to on-prem VCF Operations for networks.