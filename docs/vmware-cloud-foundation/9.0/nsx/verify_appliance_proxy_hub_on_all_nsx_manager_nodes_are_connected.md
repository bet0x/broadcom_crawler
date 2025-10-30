---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/verify-appliance-proxy-hub-on-all-manager-nodes-are-connected.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Verify Appliance Proxy Hub on all NSX Manager Nodes are Connected
---

# Verify Appliance Proxy Hub on all NSX Manager Nodes are Connected

Appliance
Proxy Hub (APH) acts as a communication channel between NSX Manager and a transport node. It runs
as a service on NSX Manager and
provides secure connection between a transport node and NSX Manager.

Before you set a virtual IP (VIP) address
for the cluster nodes, ensure the APH running on each NSX Manager cluster nodes are connected to
each other. If APH on all cluster nodes are not connected, you might face issues
when configuring the VIP for the cluster.

1. To
   verify APH on all the cluster nodes are connected, go to one of the NSX Manager nodes and run the
   GET /api/v1/messaging/cluster-connection/status
   call.

   ```
   {
       "results": [
         {
           "address": "ssl-tcp://192.161.1.52:38522",
           "conn_status": "Connected",
           "node_id": "e85ceb93-df30-43fa-84d7-32d88f68a2ba",
           "node_type": "APPLIANCE_PROXY_HUB"
         },
         {
           "address": "ssl://192.161.1.51:1234",
           "conn_status": "Connected",
           "node_id": "46cc9a95-6194-4d84-94bd-0744fb46e225",
           "node_type": "APPLIANCE_PROXY_HUB"
         }
       ]
   ```
2. Repeat Step 1 on the remaining cluster nodes.
3. Wait for 60 seconds before you set the cluster VIP for the cluster.

When APH on all cluster nodes are
connected to each other, you can proceed to configure VIP for the cluster.

Set up the cluster VIP address.