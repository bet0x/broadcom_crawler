---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/upgrade-workload-domains-to-vcf-5-2/post-upgrade-steps-for-nfs-based-workload-domains.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Post Upgrade Steps for NFS-Based Workload Domains
---

# Post Upgrade Steps for NFS-Based Workload Domains

After upgrading workload domains that use NFS storage, you must add a static route for hosts to access NFS storage over the NFS gateway. This process must be completed before expanding the workload domain.

1. Identify the IP address of the NFS server for the workload domain.
2. Identify the network pool associated with the hosts in the cluster and the NFS gateway for the network pool.
   1. Log in to SDDC Manager.
   2. Click InventoryWorkload Domains and then click the workload domain.
   3. Click the Clusters tab and then click an NFS-based cluster.
   4. Click the Hosts tab and note down the network pool for the hosts.
   5. Click the Info icon next to the network pool name and note down the NFS gateway.
3. Ensure that the NFS server is reachable from the NFS gateway. If a gateway does not exist, create it.
4. Identify the vmknic on each host in the cluster that is configured for NFS traffic.
5. Configure a static route on each host to reach the NFS server from the NFS gateway.

   ```
   esxcli network ip route ipv4 add -g NFS-gateway-IP -n NFS-gateway
   ```
6. Verify that the new route is added to the host using the NFS vmknic.

   ```
   esxcli network ip route ipv4 list
   ```
7. Ensure that the hosts in the NFS cluster can reach the NFS gateway through the NFS vmkernel.

   For example:

   ```
   vmkping -4 -I vmk2 -s 1470 -d -W 5 10.0.22.250
   ```
8. Repeat steps 2 through 7 for each cluster using NFS storage.