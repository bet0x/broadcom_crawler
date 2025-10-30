---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/network-design-options.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Network Design Options for VCF Automation Instance Deployment
---

# Network Design Options for VCF Automation Instance Deployment

Each customer has different use cases and network requirements to place VCF Automation on VMware Cloud Foundation management domain. VMware Cloud Foundation provides flexibility of network segment options for our customers to design their private cloud. Below are the design options to choose which best fits your requirements.

| Network Design Options | Justification | Implication |
| --- | --- | --- |
| Deploy on the default VCF Management DVPG network | - Default deployment through VCF Installer - Quick and easy deployment as it uses the default management network - Does not require separate network or VLAN. | - Management network will need to have enough available IP addresses to support the VCF Automation deployment. - Moving to a separate network from the default management network may require a redeployment of VCF Automation. |
| Deploy on a dedicated DVPG network | - Would like to separate user facing networks from management networks to meet regulatory and security requirements. - Additional VLAN required. | - If this option is chosen, VCF Automation deployment cannot happen through VCF Installer. - VCF Automation installation must be deployed through VCF Operations fleet management. - VLAN will need to be created prior to VCF Automation deployment |
| Deploy on a separate NSX overlay network | - Would like to separate user facing networks from management networks to meet regulatory and security requirements. - Future DR Ready. - Additional Segment needed in NSX VPC | - If this option is chosen, VCF Automation deployment cannot happen through VCF Installer. - VCF Automation installation must be deployed through VCF Operations fleet management - Overlay network will need to be created prior to VCF Automation deployment - VCF automation can be deployed via API call. |