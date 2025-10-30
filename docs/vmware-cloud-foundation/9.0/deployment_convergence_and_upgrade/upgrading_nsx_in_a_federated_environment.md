---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/upgrade-nsx-in-a-federated-environment.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrading NSX in a Federated Environment
---

# Upgrading NSX in a Federated Environment

If NSX Federation is configured between two VCF Instances, VMware Cloud Foundation does not manage the lifecycle of the NSX Global Manager nodes. You must manually upgrade the NSX Global Manager nodes for each instance. Also, note that for a local manager in a federated environment the upgrade path from 4.2.3 to 9.x is not supported.