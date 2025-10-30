---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-nsx-edge-nodes/edge-node-status-down-and-bfd-tunnel-data-is-missing.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Edge Node Status Down and BFD Tunnel Data is Missing
---

# NSX Edge Node Status Down and BFD Tunnel Data is Missing

This
issue can occur if NSX Edge
dataplane service goes down due to memory leak in certain NSX Edge processes. In this case, certain
NSX Edge CLIs may fail with
error encountered.

1. Run
   admin cli get service dataplane to view the status of
   service.
2. If status is down, run cli start service dataplane.
3. Once service has started, run the following CLIs to view the CPU and Memory
   consumption by NSX Edge
   dataplane module.
4. Get dataplane cpu stats from /var/log/vmware/top-cpu.log
   and top-mem.log to watch for values going above 60% usage.