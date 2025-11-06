---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-in-vmware-cloud-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Lifecycle Management in VMware Cloud Foundation
---

# Lifecycle Management in VMware Cloud Foundation

VCF Operations provides a comprehensive set of tools for managing the lifecycle of both VCF management components and VCF core components. You can use VCF Operations to download and manage upgrade, patch, and install binaries. You can also manage ESX components and vSphere Lifecycle Manager images and deploy optional VCF management components.

## VCF Component Classification

VCF components are classified based on the level at which they operate. VCF Management components operate on the fleet level, while VCF core components operate on the instance level.

|  |  |
| --- | --- |
| VCF Management Components | VCF Core Components |
| - VCF Operations - VCF Automation - VCF Operations fleet management - VCF Operations for logs - VCF Operations for networks - VCF Identity Broker | - SDDC Manager - vCenter - NSX Manager - ESX |

## VCF Release Types

The VCF release policy defines four distinct release types, each with a specific purpose, scope, and set of lifecycle rules.

| Type | Description |
| --- | --- |
| Major | A major release, such as 9.0.0.0 or 10.0.0.0, represents the most significant evolution of the VCF platform. It serves as the primary vehicle for introducing major features and changes that can redefine the platform's capabilities. This is the only release type that can introduce breaking changes or remove existing functionality. However, this is governed by a strict deprecation policy designed to protect enterprise stability: a feature must be officially announced for deprecation in a prior major release before it can be removed in a subsequent one.  Major releases are fully synchronized, meaning all VCF components are updated in lockstep as part of a single release. They follow a unified consumption pattern, requiring a full-stack upgrade. |
| Minor | A minor release, such as 9.1.0.0 or 9.2.0.0, is the primary mechanism for delivering new features and enhancements within a major version. These releases include features and are designed to be functionally additive. Minor releases aim to be non-disruptive from a compatibility and API perspective.  Like major releases, minor releases are fully synchronized and follow the unified consumption pattern. The policy that "All components are updated in a major and minor release" applies here, ensuring the entire platform advances to a new, consistent feature level. |
| Maintenance | A maintenance release, such as 9.1.1.0 or 9.1.2.0, is a scheduled, cumulative update, focused on enhancing platform stability and support. Maintenance releases provide bug and security fixes, hardware enablement changes, such as support for servers, CPUs, devices, driver updates, guest OS support, and backward-compatible new features. They are limited in scope to minimize the operational impact. You can pick and choose which components to apply based on the impact on your environment and operational costs. For example, if you run into a critical issue with vCenter, you do not need to apply a patch to ESX that is irrelevant to your environment. Maintenance releases are synchronized among VCF components with a new Bill Of Materials. |
| Patch | Patch releases, such as such as 9.1.1.0100, provide time-sensitive fixes to security and catastrophic issues, impacting business operations, that need to be released between major, minor, and maintenance releases. You can pick and choose which components to apply based on the impact on your environment and operational costs. Patch releases are not synchronized among all VCF components and do not require a new implementation of a Bill Of Materials. |

## Lifecycle Management in VCF Operations

With VFC 9.0 and later, you use VCF Operations to manage major, minor, maintenance, and patch releases for your VCF environment.

The VCF management components and VCF core components are managed separately, although you can configure them with the same online or offline depot. The management components are managed at the VCF fleet level and can manage more than one VCF Instance. The core components are managed at the VCF Instance level.

For upgrading your management domain to VCF 9.0, see [Upgrading Your VCF Management Domain to VMware Cloud Foundation 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation.html).

For upgrading your workload domains to VCF 9.0, see [Upgrading VMware Cloud Foundation 5.x Workload Domains to 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/upgrade-workload-domains-to-vcf-5-2.html).

When you update your VCF environment to a maintenance release version, such as 9.1.1.0 or 9.1.2.0, you first update your management components that operate on the fleet level before you update the core components in your instances. For the management components, start with the VCF Operations fleet management appliance, followed by the VCF Operations instance and then proceed with the remaining components in your preferred order. For the core components, start with SDDC Manager, followed by NSX, vCenter, ESX hosts, and vSAN.