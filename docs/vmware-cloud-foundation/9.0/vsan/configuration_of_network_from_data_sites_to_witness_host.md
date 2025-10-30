---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-network-topologies/configuration-of-network-from-data-sites-to-witness-host.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Configuration of Network from Data Sites to Witness Host
---

# Configuration of Network from Data Sites to Witness Host

The host interfaces in the data sites communicate to the witness host over the vSAN network. There are different configuration options available.

This topic discusses how to implement these configurations. It addresses how the interfaces on the hosts in the data sites, which communicate to each other over the vSAN network, communicate with the witness host.

## Option 1: Physical ESX Witness Connected over L3 with Static Routes

The data sites can be connected over a stretched L2 network. Use this also for the data sites’ management network, vSAN network, vMotion network, and virtual machine network.

The physical network router in this network infrastructure does not automatically transfer traffic from the hosts in the data sites (site 1 and site 2) to the host in the witness site (site 3). To configure the vSAN stretched cluster successfully, all hosts in the cluster must communicate. It is possible to deploy a vSAN stretched cluster in this environment.

The solution is to use static routes configured on the ESX hosts, so that the vSAN traffic from site1 and site 2 can reach the witness host in site 3. In the case of the ESX hosts on the data sites, add a static route to the vSAN interface, which redirects traffic to the witness host on site 3 over a specified gateway for that network. In the case of the witness host, the vSAN interface must have a static route added, which redirects vSAN traffic destined for the hosts in the data sites. Use the following command to add a static route on each ESX host in the vSAN stretched cluster: esxcli network ip route ipv4 add -g<gateway>-n <network>

The vCenter must be able to manage the ESX hosts at both the data sites and the witness site. As long as there is direct connectivity from the witness host to vCenter, there are no additional concerns regarding the management network.

There is no need to configure a vMotion network or a VM network, or add any static routes for these networks in the context of a vSAN stretched cluster. VMs are never migrated or deployed to the vSAN witness host. Its purpose is to maintain witness objects only, and does not require either of these networks for this task.

## Option 2: Virtual ESX Witness Appliance Connected over L3 with Static Routes

Since the witness host is a virtual machine that gets deployed on a physical ESX host, which is not part of the vSAN cluster, that physical ESX host must have a minimum of one VM network pre-configured. This VM network must reach both the management network and the vSAN network shared by the ESX hosts on the data sites.

The witness host does not need to be a dedicated host. It can be used for many other VM workloads, while simultaneously hosting the witness.

An alternative option is to have two preconfigured VM networks on the underlying physical ESX host, one for the management network and one for the vSAN network. When the virtual ESX witness is deployed on this physical ESX host, the network needs to be attached and configured accordingly.

Once you have deployed the virtual ESX witness host, configure the static route. Assume that the data sites are connected over a stretched L2 network. Use this also for the data sites’ management network, vSAN network, vMotion network, and virtual machine network. vSAN traffic is not routed from the hosts in the data sites (site 1 and site 2) to the host in the witness site (site 3) over the default gateway. To configure the vSAN stretched cluster successfully, all hosts in the cluster require static routes, so that the vSAN traffic from site 1 and site 2 can reach the witness host in site 3. Use the esxcli network ip route command to add a static route on each ESX host.