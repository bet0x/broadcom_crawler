---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/manage-deprecated-nsx-features.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Manage Unsupported Features
---

# Manage Unsupported Features

Certain features in the source version of NSX may not be supported in the target version. If your deployment contains an unsupported feature, make the required changes to your system configuration before starting the upgrade. The upgrade precheck step of the upgrade process returns an error if it detects an unsupported feature.

## Multi-NSX

Starting with VCF 9.0, the multi-NSX feature is not supported. Ensure that before upgrading to version 9.0 or later, you have switched off the multi-NSX feature for compute managers added to your NSX Manager, else the NSX Manager pre-check step returns an error.

Alternatively, you can map the NSX Manager instances to individual vCenter instances before upgrading.

## Compute Managers Without Service Accounts

Starting with VCF 9.0, a service account is created on vCenter for NSX to communicate with a registered compute manager. If you are upgrading to VCF 9.0 and any of the registered compute managers do not have a service account enabled, a pre-check error is thrown.

To proceed with the upgrade, you must enable the service account for those compute managers. Note that for compute managers that already have a service account feature enabled, the same service account is used post upgrade for those compute managers. The old privileges are deleted for such a service account and the predefined privileges are added.

## Manager API

Starting with VCF 9.0, the Manager APIs for logical networking and security are removed. Before proceeding with the upgrade, use the Policy promotion tool in the source NSX deployment to migrate any Manager objects in your environment to the equivalent Policy objects.

In addition, perform the following steps for specific use cases.

**Retrieve Manager IDs of logical objects**

After the upgrade, Manager IDs will no longer be available. To ensure the operation of any API that requires the Manager ID of a logical object as an input, perform these steps before starting the upgrade:

1. Create the object using the equivalent Policy API.
2. Retrieve the Unique ID value of the Policy object. The Unique ID is equivalent to the Manager ID of the logical object.
3. Use the retrieved Unique ID as input to the API requiring the Manager ID.

For example, the API for transport node profile creation takes the Manager IDs of IP pool and logical switch objects as inputs. After creating the IP pool and segment objects using Policy APIs, you can input the Unique ID values of these objects to the API for transport node profile creation.

**Perform intermediate upgrade for mixed-mode configurations**

A configuration that contains a combination of policy and manager objects is known as a mixed-mode configuration. Some examples of mixed-mode configurations are:

- NAT rules created through Manager APIs attached to routers created through Policy APIs
- Groups created through Policy APIs used in DFW rules created through Manager APIs

If your source deployment uses mixed-mode configurations, you must use the following workflow to upgrade to VCF 9.0 or later.

1. Upgrade the deployment to NSX 4.2.1 or later.
2. In NSX 4.2.1 or later, use the [Promotion feature](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/administration-guide/operations-and-management/promote-manager-objects-to-policy-objects.html) to promote the mixed-mode objects to policy objects.
3. Upgrade to VCF 9.0 or later.

**Convert mixed-mode IP allocations**

The upgrade precheck process in the NSX Manager upgrade coordinator does not detect mixed-mode IP allocations or warn you of the presence of this unsupported condition.

Before performing the upgrade, verify whether mixed-mode IP allocations exist in your environment. If present, use the [Promotion feature](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/administration-guide/operations-and-management/promote-manager-objects-to-policy-objects.html) in the source NSX deployment to migrate the mixed-mode IP allocations to Policy equivalents.

**Replace member types related to grouping**

Certain member types are deprecated or no longer supported. If your source deployment uses any of these member types, replace them with their supported equivalents which are functionally the same.

| Deprecated or Unsupported Member Type | Supported Equivalent |
| --- | --- |
| IPSET (deprecated) | Group |
| Logical Switch (not supported) | Segment |
| Logical Port (not supported) | Segment Port |

**Remove any remaining Manager objects after the upgrade**

After the upgrade, NSX Manager will raise an alarm if it detects any pure Manager logical objects that have not been migrated to Policy equivalents.