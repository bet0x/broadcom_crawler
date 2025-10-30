---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vrealize-automation-8-x/advanced-workload-placement-for-allocation-model.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Advanced Workload Placement for Allocation Model
---

# Advanced Workload Placement for Allocation Model

VCF Operations supports allocation aware advanced workload placement between VCF Automation for VM Apps Organization tenant and VCF Operations for initial placement of virtual machines. The placement recommendation is based on allocation settings that are defined in the VCF Operations policy. The advanced workload placement awareness for allocation works with the existing demand model.

## Need for Allocation Model Awareness

The advanced workload placement based on demand model, depends on the actual demand for resources in a cluster and datastore. If the allocation is based only on the utilization of resources, then it might result in over allocation or over provisioning of resources in clusters. To avoid this, VCF Operations provides allocation model awareness. Allocation model awareness addresses issues related to over allocation or over provisioning by providing you the option of setting the appropriate overcommit ratios in the VCF Operations policy.

The advanced workload placement feature uses the demand model by default and cannot be turned off. To activate the allocation model in addition to the demand model, in VCF Operations configure the appropriate overcommit ratios in policy settings for the preferred clusters, datastores, and datastore clusters.

## Prerequisites

- VCF Operations is configured as an endpoint in VCF Automation for VM Apps Organization tenant. This happens automatically in case of VCF Operations.
- Advanced placement policy in the cloud zone must be activated.
- vCenter Cloud account instance on which the initial provision is done should be same acrossVCF Operations and VCF Automation for VM Apps Organization tenant.
- Overcommit ratios in VCF Operations policy must be configured for the following:

  - For CPU and Memory overcommit ratio - Cluster Compute Resource.
  - For Disk overcommit ratio - Datastore and Datastore Cluster.

## How to Activate Advanced Placement Policy

To activate the advanced placement policy, in VCF Automation Cloud Assembly Service, navigate to Infrastructure > Cloud Zone > Summary tab and set the placement policy to ADVANCED.

If VCF Operations returns no recommendations, then under the placement policy, you can specify if you want VCF Automation for VM Apps Organization tenant to fall back to its default placement using the toggle option.

## How to Activate Allocation Awareness in Advanced Workload Placement Feature

To activate Allocation awareness in VCF Operations perform the following actions.

1. From the left menu, click Infrastructure OperationsConfigurations, and then click the Policy Definition tile.
2. Select the Active policy which is assigned to the Cluster Compute resource under Cloud Zones and make the required changes.
3. Click Edit Policy and navigate to the Capacity tile.
4. Select the Object Type as Cluster Compute Resource and activate the Allocation Model.
5. Set the overcommit ratio as per your requirement and click Save.
6. Repeat Step 3 to Step 5 for datastore cluster, vSAN datastores and local datastores.

After the configuration is completed, VCF Automation makes a provisioning request to VCF Operations , and the advanced workload placement engine calculates the recommendation and shares it with VCF Automation for VM Apps Organization tenant. To know the changes after the configuration, view the Allocation metrics and Demand metrics for the cluster.

The allocation model awareness enhancement is limited to advanced workload placement feature. This capability is not extended to workload optimization feature.