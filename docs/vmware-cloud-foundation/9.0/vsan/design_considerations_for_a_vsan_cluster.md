---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/design-considerations-for-a-virtual-san-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Design Considerations for a vSAN Cluster
---

# Design Considerations for a vSAN Cluster

Design the configuration of hosts and management nodes for best availability and tolerance to consumption growth.

## Sizing the vSAN Cluster for Failures to Tolerate

You configure the Failures to tolerate (FTT) attribute in the VM storage policies to handle host failures. The number of hosts required for the cluster is calculated as follows: 2 \* FTT + 1. The more failures the cluster is configured to tolerate, the more capacity hosts are required.

If the cluster hosts are connected across multiple racks, you can organize the hosts into fault domains to improve resilience against issues such as top-of-rack switch failures and loss of server rack power. See [Designing and Sizing vSAN Fault Domains](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/designing-and-sizing-virtual-san-fault-domains.html#GUID-3085c4a6-e276-4916-b5d7-af9be72ce221-en).

## Limitations of a Two-Host or Three-Host Cluster Configuration

In a three-host configuration, you can tolerate only one host failure by setting the number of failures to tolerate to 1. vSAN saves each of the two required replicas of virtual machine data on separate hosts. The witness object is on a third host. Because of the small number of hosts in the cluster, the following limitations exist:

- When a host fails, vSAN cannot rebuild data on another host to protect against another failure.
- If a host must enter maintenance mode, vSAN cannot evacuate data from the host to maintain policy compliance. While the host is in maintenance mode, data is exposed to a potential failure or inaccessibility if an additional failure occurs.

  You can use only the Ensure data accessibility data evacuation option. Ensure data accessibility guarantees that the object remains available during data migration, although it might be at risk if another failure occurs. vSAN objects on two-host or three-host clusters are not policy compliant. When the host exits maintenance mode, objects are rebuilt to ensure policy compliance.

  In any situation where two-host or three-host cluster has an inaccessible host or disk group, vSAN objects are at risk of becoming inaccessible should another failure occur.

## Nested Fault Domains for Two-Node Clusters

In a two-node configuration, the nested fault domains for two-node clusters allows you to tolerate multiple drive failures within a host. Each two-node cluster must have at least three disk groups and use a vSAN storage policy that leverages the nested fault domains capability. The nested fault domains provide protection against disk group failures within a host by mirroring data within each host in addition to the mirroring between the two hosts.

## Balanced and Unbalanced Cluster Configuration

vSAN works best on hosts with uniform configurations, including storage configurations.

Using hosts with different configurations has the following disadvantages in a vSAN cluster:

- Reduced predictability of storage performance because vSAN does not store the same number of components on each host.
- Different maintenance procedures.
- Reduced performance on hosts in the cluster that have smaller or different types of cache devices.

## Deploying vCenter on vSAN

If the vCenter becomes unavailable, vSAN continues to operate normally and virtual machines continue to run.

If vCenter is deployed on the vSAN datastore, and a problem occurs in the vSAN cluster, you can use a Web browser to access each ESX host and monitor vSAN through the vSphere Host Client. vSAN health information is visible in the Host Client, and also through esxcli commands.