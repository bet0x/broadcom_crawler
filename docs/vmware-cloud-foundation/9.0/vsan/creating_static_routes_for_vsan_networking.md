---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/designing-the-virtual-san-network/creating-static-routes-for-virtual-san-networking.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Creating Static Routes for vSAN Networking
---

# Creating Static Routes for vSAN Networking

In traditional configurations, where vSphere uses a single default gateway, all routed traffic attempts to reach its destination through this gateway.

In such cases, you might need to create static routes in your vSAN environment.

vSAN enables you to override the default gateway for the vSAN VMkernel adapter on each host, and configure a gateway address for the vSAN network. This offers greater flexibility than static routes and simplifies management.

However, certain vSAN deployments might require static routing. For example, deployments where the witness is on a different network, or the vSAN stretched cluster deployment, where both the data sites and the witness host are on different networks.

To configure static routing on your ESX hosts, use the esxcli command:

esxcli network ip route ipv4 add -g gateway-to-use –n remote-network

remote-network is the remote network that your host must access, and gateway-to-use is the interface to use when traffic is sent to the remote network.

For information about network design for vSAN stretched clusters, see [vSAN Stretched Clusters Network Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster/introduction-to-stretched-clusters/vsan-stretched-clusters-networking-design.html).