---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-high-availability-deployment-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > High Availability VCF Automation Model
---

# High Availability VCF Automation Model

The High Availability VCF Automation Model consists of a three-node deployment. This model provides resiliency at both the application level through the clustered deployment as well as the vSphere cluster level through vSphere HA and vSphere DRS functionality.

The high availability discussion in this section focuses on the VCF Automation appliance level. For discussions on high availability design for components supporting VCF Automation, see the following:

- vSphere Clusters - See [vSphere Cluster Detailed Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models.html) for more details.
- vSphere Supervisor deployments - See [vSphere Supervisor Detailed Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models.html) for more details.
- NSX Edges - See [NSX Edge Cluster Detailed Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster.html) for more details.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/20815db7-e643-4fe0-8e7f-90e672248cce.original.png)

## High Availability VCF Automation Model Attributes

A High Availability VCF Automation Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Availability | - Application level availability provided by the three node cluster - Appliance level level availability provided by vSphere HA |
| Scalability | Supports scale-up and scale-down of node sizes. |
| Recoverability | Restore through a backup. |

## High Availability VCF Automation Model Options

A High Availability VCF Automation Model can leverage options from the design areas listed below, depending on objectives.

| Design Area | Option |
| --- | --- |
| Network Placement | - Deploy on the default VCF Management DVPG network - Deploy on a separate dedicated DVPG network - Deploy on a separate NSX overlay network |
| External Load Balancing | - External load balancer configuration is a post deployment configuration. - The native Kubernetes load balancer is configured automatically during deployment of VCF Automation and cannot be removed. - The external load balancer must be configured to send traffic to the native Kubernetes load balancer configured at deployment. - The external load balancer requires VIP addressing, FQDN, as well as a certificate in addition to those assigned at deployment. |

## High Availability VCF Automation Model Design Requirements

High Availability VCF Automation Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-AUTO-REQD-HA-001 | Deploy VCF Automation as a three node cluster in the default management vSphere cluster. | Supports high availability objectives. | - Analysis will be required to determine which node size is appropriate for your deployment. - Node can be resized after deployment as necessary. |
| VCF-AUTO-REQD-HA-002 | [Deploy VCF Automation in separate DVPG or NSX Overlay](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-and-configuration-of-components-for-advanced-architectures/deploying-vcf-management-components-with-custom-networking/deploy-vcf-management-components-on-an-nsx-overlay-segment.html) as a three node cluster through VCF VCF Operations fleet management. | Supports different network other than default management network for security requirements. | If deployed via VCF Operations fleet management, all the VCF Operations components (to include fleet manager) will need to be fully up and functional prior to starting the VCF Automation deployment. |
| VCF-AUTO-REQD-HA-003 | If VCF Automation is deployed as high availability deployment will default to the medium node size. Review the configuration maximums for the medium node size to determine if it will be sufficient for your use cases | Ensures that the VCF Automation node sizing is appropriate for your use cases. | If your use cases require the large size nodes you will need to perform a scale up action through VCF Operations fleet management post deployment. |
| VCF-AUTO-REQD-HA-004 | Protect all VCF Automation nodes by using vSphere HA. | Supports the high availability objective without requiring manual intervention during an ESX host failure. | None |