---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/workload-domain-deployment-models/management-domain-deployment-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Management Domain Model
---

# Management Domain Model

The management domain in a VCF fleet hosts the management components of the VCF Instance where it is deployed and the management components of the fleet.

**Management Domain Model in VMware Cloud Foundation**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c611c880-bc04-4267-8bd0-56b9ac91b17b.original.svg)

## Management Domain Model Attributes

The Management Domain Model has the following attributes.

| Attribute | Details |
| --- | --- |
| Resource allocation | - VCF fleet management components. - VCF Instance components. - NSX Edge nodes. - Can also run business workloads. |
| VCF fleet management components | - The management domain in the first VCF Instance contains the following fleet-level management components:    - VCF Operations   - VCF Automation - Management domains in additional VCF Instances contain the following instance-level management components:    - VCF Operations collector(s) |
| VCF Instance management components | - Contains the following management appliances for all workload domains:    - ESX hosts   - vCenter   - NSX Manager (dedicated)   - SDDC Manager |

## Management Domain Model Options

According to your objectives, the Management Domain Model can have options from the following design areas.

| Design Area | Options |
| --- | --- |
| Cluster models | - First cluster:    - [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html)   - [Layer 2 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-2-multi-rack-cluster.html)   - [Stretched Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-multiple-availability-zones.html) (Day 2) - Additional clusters:    - All cluster models. |
| VCF Operations models | - [Simple VCF Operations Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/simple.html) - [High Availability VCF Operations Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/ha.html) |
| VCF Automation models | - [Simple VCF Automation Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-simple-deployment-model.html) - [High Availability VCF Automation Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-high-availability-deployment-model.html) |
| NSX Manager models | - Simple NSX Manager Model - High Availability NSX Manager Model |

## Management Domain Model Requirements

Management Domain Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-WLD-REQD-CFG-001 | Deploy a management domain to host all management components for the VCF instance. | - Guarantees sufficient resources for management components. - Enables the use of specific hardware to meet only the needs of the management components. - Enables the use of dedicated physical compute, network and storage separately from those used for additional workloads. - Enables separate life cycle management of management and workload components. | - You must carefully size the management domain to accommodate planned deployments of additional workload domains and management components. - Hardware might not be fully utilized until full-scale deployment has been reached. |

## Management Domain Model Recommendations

Management Domain Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-WLD-RCMD-CFG-001 | If running business workloads in the management domain, configure the following vSphere resource pools to control resource usage by management and business workloads.   - cluster-name-rp-sddc-mgmt - cluster-name-rp-sddc-edge - cluster-name-rp-user-edge - cluster-name-rp-user-vm | Ensures sufficient resources for the management components. | You must manually create the vSphere resource pools and manage their settings over time. |