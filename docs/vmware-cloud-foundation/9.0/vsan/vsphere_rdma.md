---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/ip-network-transport-configuration/vsphere-rdma.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > vSphere RDMA
---

# vSphere RDMA

vSAN supports Remote Direct Memory Access (RDMA) communication.

RDMA allows direct memory access from the memory of one computer to the memory of another computer without involving the operating system or CPU. The transfer of memory is offloaded to the RDMA-capable Host Channel Adapters (HCA).

vSAN supports the RoCE v2 protocol. RoCE v2 requires a network configured for lossless operation that is free of congestion. If your network has congestion, certain large I/O workloads might experience lower performance than TCP.

Each vSAN host must have a vSAN certified RDMA-capable NIC, as listed in the vSAN section of the Broadcom Compatibility Guide. Use only the same model network adapters from the same vendor on each end of the connection.

vSphere RDMA is not supported on vSAN stretched clusters, two-node vSAN clusters, vSAN storage clusters, or datastore sharing (HCI Mesh).

All hosts in the cluster must support RDMA. If any host loses RDMA support, the entire vSAN cluster switches to TCP.

vSAN with RDMA supports NIC failover, but does not support LACP or IP-hash-based NIC teaming.