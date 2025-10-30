---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/vsphere-cluster-models.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > vSphere Cluster Models
---

# vSphere Cluster Models

VMware Cloud Foundation supports multiple vSphere Cluster Models that provide different levels of availability to the workloads running in a workload domain.

## vSphere Cluster Models

A vSphere Cluster Model is defined and implemented per vSphere cluster and describes the maximum level of availability that can be provided to virtual machines on that vSphere cluster. Each workload domain or VCF Instance can contain a combination of the defined vSphere Cluster Models. You might also may select to deploy a single vSphere Cluster Model in a workload domain or VCF Instance according to your availability objectives.

If a vSphere cluster is part of a workload domain with vSphere Supervisor, the vSphere cluster is a vSphere zone that can be tagged as a vSphere Supervisor management and workload zone.

vSphere Cluster Models in VMware Cloud Foundation



| Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| [Single-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-single-availability-zone.html) | - Single storage fault domain. - Supports Layer 2 networking between ESX hosts. - Protects VMs using vSphere HA. - When using vSAN, can be a:    - HCI cluster   - Storage cluster   - Compute cluster. | - Provides support for the minimal footprint. - Provides support for recovery after host failure events. - Supported in all workload domains. | No protection against a rack failure. |
| [Layer 2 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-2-multi-rack-cluster.html) | - Multiple storage fault domains. - Supports Layer 2 networking between ESX hosts. - Protects VMs using vSphere HA. - When using vSAN, can be a:    - HCI cluster   - Storage cluster   - Compute cluster. | Provides support for recovery after ESX host or physical rack failure events. | - Requires multiple physical racks. - Management domain default cluster supported. |
| [Layer 3 Multi-Rack Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/multi-rack-cluster-detailed-design/layer-3-multi-rack-cluster.html) | - Multiple storage fault domains. - Supports Layer 3 networking between ESX hosts. - Protects VMs using vSphere HA. - When using vSAN, can be a:    - HCI cluster   - Compute cluster. | - Provides support for recovery after ESX host or physical rack failure events. - Provides isolated layer 2 network broadcast domains per rack. | - Requires multiple physical racks. - More complex networking requirements with additional subnets and VLANs per rack. - Management domain default cluster not supported. |
| [Stretched Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-multiple-availability-zones.html) | - Dual storage fault domains. - Protects VMs using vSphere HA. - Can stretch single-rack clusters\* | Provides support for recovery after host and availability zone failure events. | L3 multi-rack clusters cannot be stretched. |

\* You cannot stretch a single-rack storage cluster if that cluster uses vSAN Storage Client traffic separation.

vSphere Cluster Models in a Single VCF Instance

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/f7825f2b-46ba-401c-aeab-4351016078dd.original.png)

You can implement disaster recovery between VCF Instances on any of the above vSphere Cluster Models by following the [Site Protection and Disaster Recovery](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vvs/9-X/site-protection-and-disaster-recovery-for-vmware-cloud-foundation.html) validated solution.