---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/vcf-automation-deployment-models.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Automation Models
---

# VCF Automation Models

VMware Cloud Foundation uses VCF Automation as the central provisioning platform for your VCF fleet. VCF Automation enables consumption of Kubernetes and cloud infrastructure resources as a service, while maintaining control, security, and compliance.

VCF Automation runs on containers within a Kubernetes cluster, deployed on dedicated virtual appliances. VCF Automation infrastructure is visible in the vCenter inventory as individual nodes. During installation, the fleet management services automatically provision the Kubernetes cluster to orchestrate the deployment of the VCF Automation component containers and services. VCF Operations fleet management transparently manages the Kubernetes cluster.

VCF Automation Models in VMware Cloud Foundation



| Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| [Simple VCF Automation Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-simple-deployment-model.html) | - Single node - Applies to Small appliance size - Can be scaled out to the high availability model by resizing the node to Medium or Large, which also forces the scale out to 3 nodes | - Recommended deployment scenarios:    - Proof of Concept (POC) or evaluation.   - Small-scale, non-critical workloads.   - Development and testing environments. | No application-level high availability. |
| [High Availability VCF Automation Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-high-availability-deployment-model.html) | - Three node cluster. - Applies to Medium or Large node sizes. - Supports use of an external load balancer. | - Recommended deployment scenarios:    - Production environments.   - Mission-critical applications.   - Enterprise deployments.   - Scalable infrastructure, ideal for organizations that anticipate future growth and need the ability to scale their infrastructure resources. - Can be scaled up or down in size as necessary (for example, from medium to large nodes or the reverse). | Provides application-level availability. |

VCF Automation Models in VMware Cloud Foundation

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/a0980e9f-3b61-482c-bcee-3929a53105f4.original.png)