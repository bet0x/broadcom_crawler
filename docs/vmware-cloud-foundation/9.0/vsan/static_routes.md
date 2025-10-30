---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/ip-network-transport-configuration/static-routes.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Static Routes
---

# Static Routes

You can use static routes to allow vSAN network interfaces from hosts on one subnet to reach the hosts on another network.

Most organizations separate the vSAN network from the management network, so the vSAN network does not have a default gateway. In an L3 deployment, hosts that are on different subnets or different L2 segments cannot reach each other over the default gateway, which is typically associated with the management network.

Use static routes to allow the vSAN network interfaces from hosts on one subnet to reach the vSAN networks on hosts on the other network. Static routes instruct a host how to reach a particular network over an interface, rather than using the default gateway.

The following example shows how to add an IPv4 static route to an ESX host. Specify the gateway (-g) and the network (-n) you want to reach through that gateway:

```
esxcli network ip route ipv4 add –g 172.16.10.253 -n 192.168.10.0/24
```

When the static routes have been added, vSAN traffic connectivity is available across all networks, assuming the physical infrastructure allows it. Run the vmkping command to test and confirm communication between the different networks by pinging the IP address or the default gateway of the remote network. You also can check different size packets (-s) and prevent fragmentation (-d) of the packet.

```
vmkping –I vmk3 192.168.10.253
```