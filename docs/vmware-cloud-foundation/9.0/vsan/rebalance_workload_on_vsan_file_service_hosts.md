---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service/rebalance-workload-on-vsan-file-service-hosts.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Rebalance Workload on vSAN File Service Hosts
---

# Rebalance Workload on vSAN File Service Hosts

Skyline Health displays the workload balance health status for all the hosts that are part of the vSAN file service Infrastructure.

If there is an imbalance in the workload of a host, you can correct it by rebalancing the workload.

1. In the vSphere Client, navigate to the cluster.
2. Click the Monitor tab.
3. Under vSAN, click Skyline Health.
4. Under Skyline Health, expand File Service and then click Infrastructure Health.

   The Infrastructure Health tab displays a list of all the hosts that are part of the vSAN file service infrastructure. For each host, the status of workload balance is displayed. If there is an imbalance in the workload of a host, an alert is displayed in the Workload Balance column.
5. Click Remidiate Imbalance and then Rebalance to fix the imbalance.

   Before proceeding with rebalancing, consider the following:
   - During rebalancing, containers in the hosts with an imbalanced workload might be moved to other hosts. The rebalancing activity might also impact the other hosts in the cluster.
   - During the rebalance process, the workloads running on NFS shares are not disrupted. However, the I/O to SMB shares located in the containers that have moved are disrupted.

The host workload is balanced and the workload balance status turns green.