---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-nsx-edge-nodes/edge-node-status-down-due-to-pnic-bond-status-down.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > NSX Edge Node Status Down Due to PNIC Bond Status Down
---

# NSX Edge Node Status Down Due to PNIC Bond Status Down

NSX
Edge node status is Down because the PNIC bond status is down.

This
issue can occur if one or more Edge interfaces used by host-switch are down.

1. Verify
   if uplinks used by fast path interfaces are not down on the physical server
   hosting the uplinks.
2. If fast-path components are down, verify if dataplane service is running by
   running admin cli get service dataplane.
3. Verify status of Edge VTEP Device via admin cli get
   host-switch to find out vtep device name.
4. Run get physical-port <vtep device> .

   ```
   edge-1> get phy fp-eth0 
   Physical Port 
   ADMIN_STATUS : up <----------------- should be "up" 
   DRIVER : net_vmxnet3 
   DUPLEX : full 
   ID : 0 
   LINK : up <----------------- should be "up"
   ```
5. If VTEP device admin\_status or link is down, fix
   this infrastructure issue.
6. If dataplane service is stopped, start by running start | restart
   service dataplane.
7. After resolving the issue, run admin cli get
   logical-routers on the edge transport node to make sure edge is
   functional again.