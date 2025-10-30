---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/distributed-load-balancer/understanding-traffic-flow-with-a-distributed-load-balancer.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Understanding Traffic Flow with a Distributed Load Balancer
---

# Understanding Traffic Flow with a Distributed Load Balancer

Understand how traffic flows between VMs that are connected to an instance of a
distributed load balancer (DLB).

![Diagram of traffic flow with a DLB.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/dc40b430-6fbf-4ec3-aeb2-29e8725423df.original.png)

As an administrator ensure:

- Virtual IP addresses and pool members connected to a DLB instance must have unique
  IP address for traffic to be routed correctly.

Traffic flow between Web VM1 and APP VM2.

1. When Web VM1 sends out a packet to
   APP VM2 it is received by the VIP-APP.

   The DLB APP is attached to the
   policy group consisting of Web tier VMs. Similarly, DLB-APP hosting VIP-DB
   must be attached to the policy group consisting of App tier VMs.
2. The VIP-APP hosted on DLB APP receives the request from Web VM1.
3. Before reaching the destination VM
   group, the packet is filtered by distributed firewall rules.
4. After the packets are filtered
   based on the firewall rules, it is sent to the Tier-1 router.
5. It is further routed to the the
   physical router.
6. The route is completed when the
   packet is delivered to the destination App VM2 group.

As DLB VIPs can only be accessed from VMs connected to downlinks of Tier-0 or
Tier-1 logical routers, DLB provides load balancing services to east-west traffic.

A DLB instance can co-exist with an instance of DFW. With DLB and DFW enabled on a
virtual interface of a hypervisor, first the traffic is load balanced based on the
configuration in DLB and then DFW rules are applied on traffic flowing from a VM to the
hypervisor. DLB rules are applied on traffic originating from downlinks of a Tier-0 or
Tier-1 logical routers going to the destination hypervisor. DLB rules cannot be applied
on traffic flowing in the reverse direction - originating from outside the host going to
a destination VM.

For example, if the DLB instance is load balancing traffic from Web-VMs to App-VMs, then
to allow such traffic to pass through DFW, ensure that the DFW rule is set to value
"Source=Web-VMs, Destination=App-VMs, Action=Allow".