---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking/vsan-network-characteristics/using-unicast-in-vsan-network/intra-cluster-traffic/intra-cluster-traffic-in-a-single-rack.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Intra-Cluster Traffic in a Single Rack
---

# Intra-Cluster Traffic in a Single Rack

If all the nodes in a vSAN cluster are connected to the same top of the rack (TOR) switch, then the total increase in traffic is only between the primary node and the switch.

If a vSAN cluster spans more than one TOR switch, you need to monitor the network traffic bandwidth and network latency to ensure adequate resources are available to satisfy vSAN requirements. If a cluster spans many racks, multiple TORs may be involved. A single L2 can span multiple racks or L3 can be used across multiple TORs. vSAN Fault Domains could be considered with L3 to have a logical and physical fault domain at a rack boundary.

![Unicast intra-cluster traffic in single-site cluster](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/569b076d-5f14-443d-b9c6-ac7d7556a246.original.png)