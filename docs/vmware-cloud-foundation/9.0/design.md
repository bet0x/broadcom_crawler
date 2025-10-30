---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design
---

# Design

As a cloud architect or VI administrator, understand the supported design options for VCF, and review a set of decision points, justifications, implications, and considerations for designing each component.

## Getting to Know VCF

To apply this documentation, you must be acquainted with the [VCF Product Overview](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9.html) and [VCF Release Notes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes.html). For information about deploying, converging to or upgrading VCF, see [Overview of VCF Deploy, Converge, and Upgrade](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/overview-of-deploy--converge--and-upgrade.html).

## Organization of This Design Guidance

The design content consists of the following sections:

| Section | Description |
| --- | --- |
| [Architecture Options in VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts.html) | Contains an overview of each component of a VCF private cloud with high level comparisons of the benefits and implications of the options available within each component. |
| [Design Blueprints for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints.html) | A collection of design requirements and recommendations based on a defined design profile. It can be used as a full end-to-end design for a VMware Cloud Foundation platform or as a starting point and adjusted to suit your specific objectives by altering the design choices made. |
| [Design Library for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library.html) | Contains detailed design for each component of the VCF private cloud. |

## Design Elements

The VMware Cloud Foundation Design Guide contains requirements and recommendations for the design of each component of the VCF private cloud. In situations where a configuration choice exists, requirements and recommendations are available for each choice. Implement only those that are relevant to your target configuration.

| Design Element | Description |
| --- | --- |
| Design Requirement | Required for the operation of VCF. Deviations are not permitted. |
| Design Recommendation | Recommended as a best practice. Deviations are permitted. |
| Design Choice | You must choose one of a number of options. Could be simple configuration options, or a choice between lower level (more elemental models) from the design library. |

## Scope of This Design Guidance

The VMware Cloud Foundation Design contains:

- An overview of each component of a VCF private cloud with high-level comparisons of the benefits and implications of the available architectural options
- A library of designs for each of the architectural options
- A number of blueprints (defined architecture topologies, based on specific design profiles) to help accelerate time to value when building a new VMware Cloud Foundation platform

The available design blueprints are:

- [VCF Fleet in a Single Site with Minimal Footprint](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/vcf-fleet-basic-management-design.html)
- [VCF Fleet in a Single Site](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/vcf-fleet-management-design-with-multiple-availability-zones.html)
- [VCF Fleet with Multiple Sites in a Single Region](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/vsphere-only-to-vcf-fleet-upgrade-blueprint.html)
- [VCF Fleet with Multiple Sites Across Multiple Regions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/blueprint-4.html)
- [VCF Fleet with Multiple Sites in a Single Region plus Additional Regions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/blueprint-5.html)

## SDKs, APIs, and CLI for VCF Administration

You can build, operate, and manage your VCF private cloud by using the VCF SDK and APIs, and VCF PowerCLI. See [Administration SDKs, APIs, and CLI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/administration-sdks-cli-and-tools.html).