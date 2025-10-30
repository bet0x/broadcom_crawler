---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/single-rack-storage-models.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Single-Rack Cluster Storage Models
---

# Single-Rack Cluster Storage Models

A single rack vSAN storage architecture refers to a vSAN cluster deployed within a single physical rack or rack enclosure. This approach leverages the local vSAN compatible storage devices within the ESX hosts housed in that rack to create a shared, distributed datastore accessible to all hosts in a vSphere cluster. The following sections describe single-rack cluster models, A single-rack cluster can either be based on a vSAN ESA or OSA architecture, and can be deployed as vSAN storage cluster or a vSAN compute cluster.