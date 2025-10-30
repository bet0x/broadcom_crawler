---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Stretched Cluster Storage Models
---

# Stretched Cluster Storage Models

A vSAN Stretched Cluster provides a highly resilient and available storage architecture by distributing data and services across multiple locations,leveraging synchronous replication over a low-latency inter-site link A stretched cluster spans two distinct physical locations, acting as active-active sites for data storage. This means that data is synchronously replicated between the sites, providing redundancy in case of a site failure. The following vSAN cluster models can be deployed in a stretched cluster configuration, A vSAN HCI Cluster, a vSAN storage cluster or vSAN compute cluster.