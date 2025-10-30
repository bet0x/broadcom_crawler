---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-vsan-stretched-compute-cluster/what-are-vsan-stretched-compute-clusters.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > What is a Stretched Compute Cluster?
---

# What is a Stretched Compute Cluster?

Stretched compute clusters are cluster with compute resources that are distributed across two different sites or data centers. These clusters provide high availability, disaster recovery, and resource management by enabling the cluster to operate in a stretched mode across the sites.

Each site has its fault domain. The fault domain in the stretched compute cluster groups host based on their location and network topology. This ensures that the cluster operates optimally across sites. When configured with two distinct fault domains, stretched compute cluster enters stretched mode allowing the cluster to span two locations and improve redundancy.

## Stretched Compute Clusters and Fault Domains

In a stretched compute cluster, the fault domain organizes the hosts based on the site attributes and the network topologies. You can group hosts based on their physical location. This ensures that the compute resources are distributed across different fault domains and helps you manage the workload during site failure.

With hosts available in two sites, you can configure a stretched compute cluster. You can add additional hosts, as required. Use Disable stretched compute cluster to disable stretched compute cluster that removes the sites and converts a stretched compute cluster to a compute cluster.

## Stretched Compute Clusters Design Considerations

Consider the following guidelines when working on a stretched compute cluster:

- Ensure that the hosts in a compute cluster are placed in separate sites.
- Allow only the stretched compute cluster to mount the datastores from a vSAN stretched cluster.

## Stretched Compute Clusters Network Design

All the sites in a stretched compute cluster communicate across the management network and across the vSAN network. The virtual machines in both the data sites communicate across a common virtual machine network.

A stretched compute cluster must meet certain basic networking requirements:

- Management network requires connectivity across all the sites, using a Layer 3 network.
- The vSAN network requires connectivity across all the sites of the server cluster.
- VM network requires connectivity between the data sites. Use a Layer 3 network between the data sites. In the event of a failure, the virtual machines do not require a new IP address to work on the remote site.
- vMotion network requires connectivity between the data sites. Use a Layer 3 network between the data sites.