---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-instance-types/deployment.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Deployment Pattern 3: External-Facing deployment of VCF Automation
---

# Deployment Pattern 3: External-Facing deployment of VCF Automation

External-Facing Deployment of VCF Automation refers to implementing VCF Automation to seamlessly interact with external networks or services in a secure manner.

External Facing deployment of VCF Automation

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/cd135dc4-76bf-423c-a77f-a264bba15487.original.png)

This deployment pattern helps to minimize the attack surface, contain potential security breaches, and provides the necessary controls for meeting various security and compliance standards for VCF Automation.

The DMZ VPC accommodates external facing services (like load balancers) and serve as a security barrier between the internet and the internal application network. To provide an additional layer of network isolation, this deployment pattern also uses a second VPC for the VCF Automation instances. The Transit Gateway routes traffic between the two VPCs and to the upstream network, enabling safe channels of communication.

The Tier-0 Gateway provides north and south routing as well as stateful firewall features. This offers a reliable and secure design for hosting VCF Automation that is accessible over the internet. Provider Admin can apply East - West firewall on the Mgmt App VPC to protect access to VCF Automation appliances and limit lateral movement.

| Benefits | Drawbacks |
| --- | --- |
| - Easier to manage and update one set of VCF Automation appliances. Reduces operational overhead. - Limits lateral movement and isolates external-facing services from core management and workloads. - Micro-segmentation approach securely exposes services through DMZ VPC, Load Balancer, and T0 Gateway for strong protection - Distributes traffic efficiently across multiple automation appliance instances for scale and availability. | - Needs robust security (firewalls, WAF, and API security in place). - Load balancer misconfigurations could cause downtime or abnormal traffic routing. - Adds network complexity; managing routing, firewall rules, and subnet allocations needs careful planning for each orgnizations or tenants. |