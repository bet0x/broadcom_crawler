---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Completing the Deployment of Your Platform
---

# Completing the Deployment of Your Platform

After the automated by VCF Installer deployment of components for your VMware Cloud Foundation or vSphere Foundation platform, you must deploy the remaining components to complete the platform. You deploy the orchestrator appliance manually for both VCF and vSphere Foundation. For VCF you deploy the remaining appliances by using automation provided by VCF Operations. For vSphere Foundation you deploy the operations-logs appliances manually.

Deployment of a three-node VCF Identity Broker is optional per the requirements of your organization. If you do not need the three-node appliance deployment, you can use the same functionality that is embedded in vCenter.

Post-VCF Installer Deployment Scope per Platform



| Component | Component Appliances | VMware Cloud Foundation | | vSphere Foundation |
| --- | --- | --- | --- | --- |
| Simple | High Availability |
| VCF Identity Broker | identity broker (node 1) | No | Yes | No |
| identity broker (node 2) | No | Yes | No |
| identity broker (node 3) | No | Yes | No |
| VCF Operations | operations-networks | Yes | Yes | No |
| operations-networks (collector node 1) | Yes | Yes | No |
| operations-networks (collector node 2) | No | Yes | No |
| operations-logs (primary node) | Yes | Yes | Yes |
| operations-logs (worker node 1) | No | Yes | Yes |
| operations-logs (worker node 2) | No | Yes | Yes |
| operations-orchestrator (primary node) | Yes | Yes | Yes |
| operations-orchestrator (secondary node1) | No | Yes | Yes |
| operations-orchestrator (secondary node2) | No | Yes | Yes |