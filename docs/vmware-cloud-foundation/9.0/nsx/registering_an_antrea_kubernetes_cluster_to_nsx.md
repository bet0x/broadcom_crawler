---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/registering-an-antrea-kubernetes-cluster-to-nsx.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Registering an Antrea Kubernetes Cluster to NSX
---

# Registering an Antrea Kubernetes Cluster to NSX

The registration process involves two roles or personas: NSX administrator and Kubernetes platform
administrator. In an organization, both roles might be held by the same person or by
different people.

For example, if your organization uses a hosted (managed) Kubernetes service from a
public cloud service provider, such as Azure Kubernetes Service, Google Kubernetes
Service, and so on, the Kubernetes platform administrator is in the cloud service
provider organization, and the NSX
administrator is in your organization. In such a scenario, the Kubernetes platform
administrator and the NSX administrator
can collaborate with each other to exchange information and complete the
registration.