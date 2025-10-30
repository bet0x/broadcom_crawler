---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster/introduction-to-stretched-clusters/vsan-stretched-clusters-networking-design.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN Stretched Clusters Network Design
---

# vSAN Stretched Clusters Network Design

All three sites in a vSAN stretched cluster communicate across the management network and across the vSAN network. The virtual machines in both data sites communicate across a common virtual machine network.

A vSAN stretched cluster must meet certain basic networking requirements.

- Management network requires connectivity across all three sites, using a Layer 2 stretched network or a Layer 3 network.
- The vSAN network requires connectivity across all three sites. It must have independent routing and connectivity between the data sites and the witness host. vSAN supports both Layer 2 and Layer 3 between the two data sites, and Layer 3 between the data sites and the witness host.
- VM network requires connectivity between the data sites, but not the witness host. Use a Layer 2 stretched network or Layer 3 network between the data sites. In the event of a failure, the virtual machines do not require a new IP address to work on the remote site.
- vMotion network requires connectivity between the data sites, but not the witness host. Use a Layer 2 stretched or a Layer 3 network between data sites.

vSAN over RDMA is not supported on vSAN stretched clusters or two-node vSAN clusters.

## Override Default Gateway for a vSAN VMKernel Adapater

If you use a single default gateway on ESX hosts, each ESX host contains a default TCP/IP stack that has a single default gateway. The default route is typically associated with the management network TCP/IP stack.

The management network and the vSAN network might be isolated from one another. For example, the management network might use vmk0 on physical NIC 0, while the vSAN network uses vmk2 on physical NIC 1 (separate network adapters for two distinct TCP/IP stacks). This configuration implies that the vSAN network has no default gateway.

You can override the default gateway for the vSAN VMkernel adapter on each host, and configure a gateway address for the vSAN network. You can override the default gateway when the vSAN network uses a different subnet than the management network. In vSAN stretched clusters, data sites and the witness hosts can reside on separate networks. A dedicated vSAN gateway allows traffic to reach the witness host without static routes, simplifying network configuration. For more information on overriding default gateway, see [Override the Default Gateway of VMKernel Adapter](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-networking/setting-up-vmkernel-networking/overriding-the-default-gateway-of-a-vmkernel-adapter.html).

You also can use static routes to communicate across networks. Consider a vSAN network that is stretched over two data sites on a Layer 2 broadcast domain (for example, 172.10.0.0) and the witness host is on another broadcast domain (for example, 172.30.0.0). If the VMkernel adapters on a data site try to connect to the vSAN network on the witness host, the connection fails because the default gateway on the ESX host is associated with the management network. There is no route from the management network to the vSAN network.

Define a new routing entry that indicates which path to follow to reach a particular network. For a vSAN network on a vSAN stretched cluster, you can add static routes to ensure proper communication across all hosts.

For example, you can add a static route to the hosts on each data site, so requests to reach the 172.30.0.0 witness network are routed through the 172.10.0.0 interface. Also add a static route to the witness host so that requests to reach the 172.10.0.0 network for the data sites are routed through the 172.30.0.0 interface.

If you use static routes, you must manually add the static routes for new ESX hosts added to either site before those hosts can communicate across the cluster. If you replace the witness host, you must update the static route configuration.

Use the esxcli network ip route command to add static routes.