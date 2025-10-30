---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/what-is-vsan/limitations-of-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Limitations of vSAN
---

# Limitations of vSAN

This topic discusses the limitations of vSAN.

When working with vSAN, consider the following limitations:

- vSAN does not support ESX hosts participating in multiple vSAN clusters. However, a vSAN host can access other external storage resources that are shared across clusters.
- vSAN does not support vSphere Distributed Power Management (DPM) and Storage I/O Control.
- vSAN does not support SE Sparse disks.
- vSAN does not support Raw Device Mappings (RDM), VMFS, diagnostic partition, and other device access features.