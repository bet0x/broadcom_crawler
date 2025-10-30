---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/architecture-of-antrea-kubernetes-cluster-integration-with-nsx.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Architecture of Antrea Kubernetes Cluster Integration with NSX
---

# Architecture of Antrea Kubernetes Cluster Integration with NSX

The integration architecture explains the information exchanged between a Kubernetes
cluster that uses Antrea CNI and the NSX Manager Appliance, which is deployed in
NSX.

This documentation does not explain the
functions of Antrea components in a
Kubernetes (K8s) cluster. To
understand the Antrea architecture and the
functions of Antrea components in a
Kubernetes cluster, see the Antrea
documentation portal at <https://antrea.io/docs>.

This main objective of this documentation is
to understand the functions of the Antrea NSX Adapter that integrates a Kubernetes cluster with Antrea CNI to the NSX Manager Appliance.

## Architecture Diagram

![Information exchanged between Antrea components in a Kubernetes cluster and
                        NSX Manager Appliance.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ab6aee0e-5802-414b-882d-0df512ceca10.original.png)

## Antrea NSX Adapter

This component runs as a
pod on one of the Kubernetes Control
Plane nodes. Antrea NSX Adapter consists of the following two subcomponents:

- Management Plane Adapter (MP
  Adapter)
- Central Control Plane Adapter (CCP
  Adapter)

Management Plane Adapter communicates with the NSX Management
Plane (Policy), Kubernetes API
Server, and Antrea Controller.
Central Control Plane Adapter
communicates with the NSX Central Control Plane (CCP) and Kubernetes API Server.

## Functions of the Management Plane Adapter

- Watches the Kubernetes resource inventory from
  Kubernetes API and
  reports the inventory to NSX Manager. Resource inventory of an Antrea Kubernetes cluster includes
  resources, such as Pods, Ingress, Services, Network Policies, Namespaces,
  and Nodes.
- Responds to the policy
  statistics query from NSX Manager. It receives the statistics from the Antrea Controller API or the
  statistics that are exported by the Antrea Agent on each K8s worker node, and reports the
  statistics to NSX Manager.
- Receives troubleshooting
  operation requests from NSX Manager, sends the requests to Antrea Controller API server,
  collects the results, and returns the information to NSX Manager. Examples of
  troubleshooting operations include Traceflow requests, Support Bundle
  collection requests, log collection requests.
- Watches the runtime state and
  health status of an Antrea
  Kubernetes cluster from the Antrea Monitoring CustomResourceDefinition (CRD) objects and reports the
  status to NSX Manager. The
  status is reported on a per cluster basis. For example, the health status of
  the following components is reported to NSX Manager:
  - Management Plane Adapter
  - Central Control Plane Adapter
  - Antrea Controller
  - Antrea Agents

## Functions of the Central Control Plane Adapter

- Receives the Distributed
  Firewall (DFW) rules and groups from NSX Central Control Plane, translates
  them to Antrea policies, and
  creates Antrea policy CRDs in K8s
  API.
- Watches the policy realization
  status from both K8s network polices and native Antrea policy CRDs and reports the status to NSX Central
  Control Plane.

## Stateless Nature of the Central Control Plane Adapter

The Central Control Plane Adapter is stateless. Each time the adapter
restarts or reconnects to K8s API or NSX Manager, it always synchronizes the state with K8s API and NSX
Central Control Plane. Resynchronization of the state ensures the following:

- The latest Antrea policies are always pushed to K8s
  API as native Antrea policy
  CRDs.
- The stale policy CRDs are
  removed if the corresponding security policies are deleted in NSX.