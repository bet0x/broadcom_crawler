---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9/what-is-vmware-cloud-foundation-and-vmware-vsphere-foundation/vsan.html
product: vmware-cloud-foundation
version: 9.0
section: Overview
breadcrumb: Overview >   vSAN Overview
---

# vSAN Overview

VMware® vSAN™ aggregates local or direct-attached capacity devices of all ESX hosts in a cluster and creates a single storage pool shared across all ESX hosts in the vSAN cluster.

You can use vSphere features that require shared storage, such as vSphere HA, vSphere vMotion, and vSphere DRS, without the need for external shared storage.

## Performance Across Workloads

vSAN delivers high throughput and low latency storage. For best performance, you can use vSAN Express Storage Architecture™ (vSAN ESA) with high performance NVMe-based TLC flash devices.

## Agile Scaling for Deployments of All Sizes

vSAN offers flexible scaling ranging from clusters as small as two nodes (plus witness) to clusters with up to 64 nodes. Whether scaling out by adding nodes to a cluster, scaling up by adding nodes to drives, or scaling compute and storage resources independently with disaggregation, vSAN enables you to customize performance and capacity to optimize storage resources and drive down costs.

## Unified Operations and Lifecycle Management

vSAN provides operational consistency from edge to cloud, with complete visibility and lifecycle management of compute and storage from a single UI.

## Storage Capacity and Efficiency

Improve storage efficiency with optimized compression methods. A single-tier architecture option eliminates the need for a cache tier, further enhancing storage efficiency. vSAN enables you to store data using RAID 5 or RAID 6 for efficiency with performance at the speed of RAID 1.

## Integrated File Services

vSAN enables provisioning of file shares with a single workflow and provides a unified storage control plane for both block and file storage. vSAN file services integrate Active Directory and support Kerberos network authentication and the most common protocols. vSAN file services can be used in two-node deployments and stretched cluster deployments.

## VM-Centric Policy-Based Management

You can perform consistent, VM-centric operations by using policy-based management. Within the vSAN ESA, per-VM policies increase flexibility of management, enabling compression policies, or customize data services on a per-VM basis.

## vSAN Documentation

For more information about the built-in vSAN capabilities, see the [vSAN documentation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring.html).