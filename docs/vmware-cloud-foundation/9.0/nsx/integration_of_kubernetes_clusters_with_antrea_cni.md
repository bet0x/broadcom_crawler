---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Integration of Kubernetes Clusters with Antrea CNI
---

# Integration of Kubernetes Clusters with Antrea CNI

Antrea is a container network interface (CNI) plugin from VMware that provides network connectivity and security features to pods in container clusters that are based on Kubernetes.

Henceforth, this documentation uses
the term "Antrea Kubernetes cluster" to mean Kubernetes clusters with Antrea CNI. The term "Kubernetes cluster" is a
generic term, which represents Tanzu Kubernetes Grid (TKG) clusters with Antrea CNI, OpenShift clusters with Antrea CNI, or do it yourself (DIY) Kubernetes clusters with
Antrea CNI.

The objective is to connect Antrea Kubernetes clusters to the NSX Management Plane and Central Control Plane (CCP). To achieve this integration, you must deploy Antrea NSX Adapter on all the Antrea Kubernetes clusters that you want to integrate to NSX.

## Benefits of Integration

The integration of Antrea Kubernetes clusters to NSX enables the following capabilities:

- View Antrea Kubernetes cluster resources in the NSX Manager UI.
- Centrally manage groups and security policies in NSX that reference Antrea Kubernetes clusters and NSX resources (for example, VMs).
- Distribute the security policies to the Kubernetes clusters for enforcement in the cluster by the Antrea CNI.
- Extend the NSX network diagnostic and troubleshooting features to the Antrea Kubernetes clusters, such as collecting support bundles, monitoring logs, and performing Traceflow operations.
- Monitor the runtime state and health status of Antrea Kubernetes cluster components and Antrea Agents in the NSX Manager UI.

All NSX- Antrea integration features can work when Antrea is either a primary or a secondary CNI in a Kubernetes cluster.

## Interoperability Requirements

For NSX and Antrea integration, specific interoperability requirements must be met. For more details, see [VMware Product Interoperability Matrix](https://interopmatrix.vmware.com/#/Interoperability).

## Antrea CNI in networkPolicyOnly Mode

NSX can be integrated to Antrea Kubernetes clusters in which Antrea CNI is deployed to run in a networkPolicyOnly mode. In such a case, Antrea runs as a secondary CNI and does the task of enforcing network policies in the cluster. The native routed CNI (primary CNI) does the IP address management and pod network connectivity tasks.

To set up Antrea CNI to run in a networkPolicyOnly mode, you need to deploy VMware Container Networking™ with Antrea™ v1.8 or later in your Kubernetes cluster.

All NSX- Antrea integration features that are discussed in this chapter are supported when Antrea CNI is deployed in a networkPolicyOnly mode.