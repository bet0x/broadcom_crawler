---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/vsan-compute-cluster-storage-models.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Multi-Rack Cluster Storage Models
---

# Multi-Rack Cluster Storage Models

A multi-rack storage architecture is a configuration of vSAN where the ESX hosts contributing storage to the vSAN cluster are physically located in different racks. This design is primarily used for rack awareness and to provide resilience against the failure of an entire rack. By spreading data across multiple racks, the architecture can tolerate the failure of an entire rack, as workloads can automatically restart affected virtual machines on ESX hosts in other racks. The following sections describe multi-rack cluster models. A multi-rack cluster can either be based on a vSAN ESA or OSA architecture, or a vSAN compute cluster.