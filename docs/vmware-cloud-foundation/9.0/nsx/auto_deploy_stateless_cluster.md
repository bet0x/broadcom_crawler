---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Auto Deploy Stateless Cluster
---

# Auto Deploy Stateless Cluster

Stateless hosts do not persist configuration, so they need an auto-deploy server to provide the required start files when hosts power on.

This section helps you to set up a stateless cluster using vSphere Auto Deploy and NSX Transport Node Profile to reprovision a host with a new image profile that contains a different version of ESX and NSX. Hosts that are set up for vSphere Auto Deploy use an auto-deploy server and vSphere host profiles to customize hosts. These hosts can also be set up for NSX Transport Node Profile to configure NSX on the hosts.

So, a stateless host can be set up for vSphere Auto Deploy and NSX Transport Node Profile to reprovision a host with a custom ESX and NSX version.