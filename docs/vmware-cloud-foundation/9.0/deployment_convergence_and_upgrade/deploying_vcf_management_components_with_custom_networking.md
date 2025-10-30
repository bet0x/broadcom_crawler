---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-and-configuration-of-components-for-advanced-architectures/deploying-vcf-management-components-with-custom-networking.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Deploying VCF Management Components with Custom Networking
---

# Deploying VCF Management Components with Custom Networking

If you skipped deployment of the VCF management components during initial deployment of a VCF Instance, you can use the SDDC Manager API to deploy them later.

Using the SDDC Manager API, you can deploy the VCF management components to specific vSphere distributed port groups or NSX segment. There are four main options. You can deploy the VCF management components to a:

- Shared management network
- Dedicated management network
- NSX overlay segment
- NSX VLAN segment

You can use custom networking to separate user-facing networks from management networks to meet regulatory and security requirements.

For more information about each of these options, see [Fleet Level Components Networking Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/fleet-level-component-backing-networking-models.html).