---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/nsx-management-and-control-plane-detailed-design.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > NSX Management and Control Plane Detailed Design
---

# NSX Management and Control Plane Detailed Design

Following the principles of this design and of each product, you determine the size, deploy and configure NSX Manager as part of your VMware Cloud Foundation deployment.

## NSX Manager Model

When you deploy NSX Manager appliances, either with a local or global scope, you deploy the appliance with a size and availability suitable for your environment's scale and availability requirements.

## NSX Global Manager Model

For an environment with multiple VCF Instances, you can use NSX Federation, which requires the manual deployment of NSX Global Manager nodes. Consider the placement requirements for using NSX Global Manager in VCF, and the best practices for having an NSX Global Manager cluster operate in an optimal way, such as the number and size of the nodes and high availability on a standard or stretched management cluster.