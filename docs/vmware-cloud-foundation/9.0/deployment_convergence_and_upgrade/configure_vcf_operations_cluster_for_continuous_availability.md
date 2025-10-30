---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-and-configuration-of-components-for-advanced-architectures/configure-vcf-operations-cluster-for-continuous-availability.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Configure VCF Operations Cluster for Continuous Availability
---

# Configure VCF Operations Cluster for Continuous Availability

VCF Installer supports the deployment of VCF Operations in either Simple mode or High Availability mode during the initial VCF deployment. After the initial deployment, the VCF Operations cluster can be converted to a continuous availability architecture

Identify three separate fault domains for the installation of the VCF Operations primary node and data nodes, the VCF Operations primary replica node and data nodes, and the witness node, respectively. The fault domains can be located in either a different workload domain, a separate availability zone, or a different region. In a continuous availability architecture, there must be at least one primary node and one data node within the primary fault domain. Additionally, the replica fault domain should have the same number of nodes as the primary fault domain, and there should be one witness node in the witness fault domain. The VCF Operations nodes in the primary fault domain, the VCF Operations nodes in the replica fault domain, and the witness node in the witness fault domain must be able to communicate over the network, despite being in separate fault domains. Consult the VCF Operations sizing guidelines for the sizing and network latency requirements between the three distinct fault domains.

1. Deploy VCF Operations using VCF Installer in either Simple mode or High Availability mode within the fault domain designated for the primary node.
2. Deploy the witness node in the fault domain designated for it, by following these steps:
   1. Download the VCF Operations ova file from the Broadcom support portal.
   2. Upload the VCF Operations ova file to the vCenter in the fault domain designated for the witness node.
   3. Deploy the VCF Operations OVF template and select Witness as the configuration for deployment.
   4. Note down the IP address and the hostname of the witness node.
   5. Log in to the VCF Operations administrator console in the primary fault domain.
   6. Add the newly deployed witness node to the VCF Operations cluster using the IP address and hostname of the witness node, as recorded in the previous steps.
3. If VCF Operations was deployed in a High Availability architecture during the initial setup, follow the steps below:
   1. Deactivate High Availability in the VCF Operations administrator console.
   2. The primary replica cluster node is converted into a standard data node within the cluster, which can then be removed if an extra data node is not needed. The remaining nodes in the cluster maintain their current roles.
   3. Ensure that the VCF Operations cluster has at-least one primary node and one data node in the primary fault domain. Consult the VCF Operations sizing guidelines for the maximum number of data nodes that can be added in the primary fault domain. Note that the number of VCF Operations nodes in the primary fault domain and the replica fault domain must be equal.
4. Deploy the same number of VCF Operations nodes in the designated replica fault domain as in the primary fault domain, following the steps below:
   1. If the designated replica fault domain is managed by the VCF Operations in the primary fault domain, then use the lifecycle management capability within VCF Operations to add the same number of VCF Operations nodes in the replica fault domain as in the primary fault domain.
   2. If the designated replica fault domain is NOT managed by the VCF Operations in the primary fault domain, then continue with the the steps.
   1. Download the VCF Operations ova file from the Broadcom support portal.
   2. Upload the VCF Operations ova file to the vCenter in the fault domain designated for the replica fault domain.
   3. Use the VCF Operations OVF template to deploy an equal number of VCF Operations nodes as in the primary fault domain, ensuring that the selected size matches that of the nodes deployed in the primary fault domain.
   4. Note down the IP address and the hostname of the VCF Operations nodes deployed in the replica fault domain.
   5. Log in to the VCF Operations administrator console in the primary fault domain.
   6. Add the newly deployed VCF Operations nodes in the replica fault domain using their IP address and hostnames to the VCF Operations cluster in the primary fault domain.
5. Click **Activate CA** in the VCF Operations Admin console.
6. The Continuous Availability wizard opens. The Witness node exists outside the fault domains. The primary node is already assigned to Fault Domain. Perform the following steps:
   1. To pair with the VCF Operations nodes in the primary fault domain, move the VCF Operations data nodes deployed in the replica fault domain to Fault Domain.
   2. Ensure an even distribution of VCF Operations nodes between the primary and replica fault domains to enable Continuous Availability. The number of nodes in both fault domains must be equal.
7. After successfully activating CA, navigate to Lifecycle under Fleet Management within the VCF Operations console and click trigger inventory sync on the Operations component.

The Lifecycle page for the VCF Operations component now displays Continuous Availability as the configuration for the VCF Operations cluster.

**VCF Operations Analytics Node Data Storage and Fault Domain Behavior**

VCF Operations uses a robust architecture to ensure data availability and fault tolerance across analytics nodes. Data is stored in pairs of analytics nodes distributed across two fault domains, ensuring continuous availability and synchronization. Each object is stored in two nodes (primary and replica) across fault domains, providing redundancy and resilience in case of failures.

Key Concepts of Data Storage and Fault Domain Behavior



| Key Concept | Details |
| --- | --- |
| Data Storage and Synchronization | When an object is discovered, VCF Operations determines the primary node to store the data and automatically replicates it to its paired node in the other fault domain. |
| Synchronization between the primary and replica nodes ensures data consistency across fault domains |
| Fault Domain Resilience | Each fault domain contains half of the analytics nodes, and each node has a paired replica in the other fault domain. |
| The cluster continues to function without data loss as long as one node from each pair is available. |
| Continuous Availability | The cluster can tolerate the loss of one fault domain or individual nodes without data loss, but the system will operate in a degraded state until the issue is resolved. |
| Latency and Network Requirements | Latency between fault domains must be <10 ms, with peaks up to 20 ms during 20-second intervals. High latency can impact synchronization but does not stop the process. |
| Witness Node Role | The witness node ensures cluster health and determines which fault domain remains online during communication failures. |

Key Scenario and Behavior



| Scenario | Behavior |
| --- | --- |
| Data Storage | Data is stored in a primary node and replicated to its paired node in the other fault domain. |
| Loss of One Fault Domain | The cluster operates in a degraded state but continues without data loss. The fault domain must be repaired or replaced to restore full functionality. |
| Loss of Two Nodes in One Fault Domain | The cluster continues to operate as long as one node from each pair is available. |
| Loss of Connectivity Between Fault Domains | One fault domain will go offline automatically. Once connectivity is restored, the admin must manually bring the fault domain back online to synchronize data. |
| Witness Node Unavailability | If both fault domains are healthy, the witness node’s unavailability has no impact. If communication issues occur, the witness determines which fault domain remains online. |
| Node Replacement | Use the "Replace nodes of cluster" functionality in the admin UI. Sync time depends on object count, historical data, network bandwidth, and cluster load. |
| Latency Exceeds 20 ms | Synchronization continues but may be delayed. Latency must return to <10 ms for optimal performance. |
| Primary Node Failover | If the primary node becomes unavailable, the primary replica node is promoted. The original primary node becomes the replica when it returns online. |
| Entire Fault Domain Replacement | If a fault domain is unrecoverable, it can be replaced with  newly deployed nodes. The admin UI allows replacing the  primary replica node. |
| Load Balancer Support | Load balancers are supported for continuous availability. |
| Node Reboot or Offline | Nodes automatically resume operation after reboot or being brought offline/online. No additional steps are required. |