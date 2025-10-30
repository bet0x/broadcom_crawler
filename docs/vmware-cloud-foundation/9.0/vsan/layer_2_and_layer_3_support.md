---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking/network-requirements-for-vsan/layer-2-and-layer-3-support.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Layer 2 and Layer 3 Support
---

# Layer 2 and Layer 3 Support

VMware recommends Layer 2 connectivity for vSAN deployed on a single site. For vSAN deployed across multiple racks, you can use Layer 2 or Layer 3. VMware recommends Layer 3 for data site to data site communication

vSAN also supports deployments using routed Layer 3 connectivity between vSAN hosts. You must consider the number of hops and additional latency incurred while the traffic gets routed.

Layer 2 and Layer 3 Support



| Cluster Type | L2 Supported | L3 Supported | Considerations |
| --- | --- | --- | --- |
| Hybrid Cluster | Yes | Yes | L2 for single site and single rack is recommended. L2 or L3 for single site, if vSAN cluster is deployed across multiple rack and/or using vSAN fault domains. |
| All-Flash Cluster | Yes | Yes | L2 is recommended and L3 is supported. |
| vSAN Stretched Cluster Data | Yes | Yes | Both L2 and L3 between data sites are supported. Layer 3 is recommended to isolate faults per site. Layer 3 networking is preferred for vSAN stretched clusters as it helps avoid issues with Spanning Tree Protocol (STP) redirecting the traffic across less desirable links. |
| vSAN Stretched Cluster Witness | No | Yes | L3 is supported. L2 between data and witness sites is not supported. |
| Two-Node vSAN Cluster | Yes | Yes | Both L2 and L3 between data sites are supported. |
| vSAN Stretched Compute Cluster | Yes | Yes | Both L2 and L3 between data sites are supported. |
| vSAN Compute Client Traffic | Yes | Yes | Both L2 and L3 between data sites are supported. |
| vSAN Storage Cluster | Yes | Yes | L2 is recommended and L3 is supported. |
| vSAN Stretched Storage Cluster | Yes | Yes | Both L2 and L3 between data sites are supported. Layer 3 is recommended to isolate faults per site. Layer 3 networking is preferred for vSAN stretched storage clusters as it helps avoid issues with Spanning Tree Protocol (STP) redirecting the traffic across less desirable links. |