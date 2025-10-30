---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/enabling-virtual-san/configure-a-cluster-for-vsan-using-the-vsphere-client.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Configure a Cluster for vSAN Using the vSphere Client
---

# Configure a Cluster for vSAN Using the vSphere Client

You can use the vSphere Client to configure vSAN on an existing cluster.

- Verify that your environment meets all requirements. See [Requirements for Enabling vSAN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/requirements-for-creating-a-virtual-san-cluster.html).

- Create a vSphere cluster and add ESX hosts to the vSphere cluster before enabling and configuring vSAN. Configure the port properties on each ESX host to add the vSAN service.

You can use Quickstart to quickly create and configure a vSAN cluster. For more information, see [Use Quickstart to Configure a vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/using-quickstart-to-configure-a-vsan-cluster/using-quickstart-to-create-a-vsan-cluster.html).

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, select Services.
   1. Select an HCI configuration type. 

      - vSAN HCI provides compute resources and storage resources. The datastore can be shared across clusters in the same data center, and across clusters managed by remote vCenter instances.
      - Compute Cluster is a vSphere cluster that can mount a remote datastore from a vSAN storage cluster. These clusters are ESX hosts in a vSphere cluster that only complies with the Broadcom Compatibility Guide at <https://compatibilityguide.broadcom.com/>.
      - vSAN Storage Cluster (deployment model based on vSAN ESA) provides storage resources, but not compute resources. The datastore can be mounted by client vSphere clusters and vSAN clusters in the same data center and from remote vCenter instances.
   2. Select a deployment option (Single site vSAN cluster, Two node vSAN cluster, or vSAN stretched cluster).
   3. Click Configure to open the Configure vSAN wizard.
4. Select vSAN ESA if your cluster is compatible, and click Next.
   - Select vSAN managed disk claim to claim all compatible disks on the existing host cluster. Ensure that the vSAN disks are compatible with the vSAN Hardware Compatibility List.
   - Select Auto-Policy management to optimize capacity utilization based on the cluster size and type.
5. Configure the vSAN services to use, and click Next.

   - Configure data management features, including deduplication and compression, data-at-rest encryption, data-in-transit encryption.
   - Select RDMA (remote direct memory access) if your network supports it.
   - If you configure a vSAN storage cluster, you get the option to Use Storage cluster client network. You can select this option to separate the external VM traffic from the internal storage traffic by utilizing the dedicated VMkernel ports for different traffic types. After enabling this option, you cannot modify the network configuration.
   - Create and assign a default datastore policy for vSAN ESA. This auto-policy management allows best capacity utilization after the cluster configuration is complete.
6. Claim disks for the vSAN cluster, and click Next.

   For vSAN OSA, each ESX host that contribute storage requires at least one flash device for cache, and one or more devices for capacity. For vSAN ESA, each ESX host that contributes storage requires one or more flash devices.
7. (Optional) Create fault domains to group ESX hosts that can fail together.
8. Review the configuration, and click Finish.

Enabling vSAN creates a vSAN datastore and registers the vSAN storage provider. vSAN storage providers are built-in software components that communicate the storage capabilities of the datastore to vCenter.

- Verify that the vSAN datastore has been created. See [View vSAN Datastore](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/view-virtual-san-datastore.html#GUID-d4bffc3d-5659-4acd-83f4-f0ba92d9105a-en).

- Verify the health of the new vSAN cluster created. See [Check vSAN Skyline Health.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitoring-vsan-skyline-health/check-vsan-skyline-health.html)

- Verify that the vSAN storage provider is registered. See [View vSAN Storage Providers.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-vsan-policies/view-vsan-storage-providers.html)