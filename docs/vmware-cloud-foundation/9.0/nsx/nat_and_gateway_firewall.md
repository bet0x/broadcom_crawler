---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-address-translation/nat-and-gateway-firewall.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > NAT and Gateway Firewall
---

# NAT and Gateway Firewall

A NAT firewall allows internet traffic to pass through the gateway if a device on the
private network requested it. Any unsolicited requests or data packets are discarded,
preventing communication with potentially dangerous devices.

If a tier-1 gateway has both SNAT and gateway
firewall (GWFW) configured, and if the GWFW is not configured to be stateful, you must
configure NO SNAT for the tier-1 gateway's advertised subnets. Otherwise, traffic to IP
addresses in these subnets will fail.

In the example below, T1-A is the gateway and
there is a SNAT rule configured that translates any traffic from its attached subnet
192.168.1.0/0 to 10.1.1.1.

![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/536f34a7-80d5-4549-be92-66c3d8c829c6.original.png)

Here are some traffic scenarios:

1. Any traffic stream that is
   initiated from VM-A/192.168.1.1 will get translated to 10.1.1.1 as the source
   IP, regardless if gateway firewall is stateful, stateless, or disabled. When the
   traffic from VM-C or VM-B returns for that flow, they will have a destination IP
   of 10.1.1.1; T1-A will match it up with the SNAT flow and translate it correctly
   so that it flows back to VM-A. The SNAT rule works as expected, and there are no
   issues.
2. VM-B/20.1.1.1 initiates a traffic
   flow to VM-A/192.168.1.1. Here, there’s a difference in behavior when T1-A has a
   stateful firewall versus when it has no firewall or stateless firewall. The
   firewall rules permit the traffic between VM-B and VM-A. To have this scenario,
   configure a NO-NAT rule for traffic matching 192.168.1.0/24 to 20.1.1.0/24. When
   this NO-NAT rule exists, then there will be no difference in behavior.
3. If T1-A has stateful firewall, the
   T1-A firewall will create a firewall connection entry for the TCP SYN packet
   from VM-B/20.1.1.1 to VM-A/192.168.1.1. When VM-A replies, T1-A will match the
   reply packet with the stateful connection entry, and forward the traffic from
   VM-A/192.168.1.1 to VM-B/ 20.1.1.1 with no SNAT translation. This is because the
   firewall will skip the SNAT lookup when the return traffic matches up with a
   firewall connection entry.
4. If T1-A has firewall disabled or
   stateless, the T1-A firewall will forward the TCP SYN packet from VM-B/20.1.1.1
   to VM-A/192.168.1.1 without creating a firewall connection entry, because it’s
   either stateless or no firewall. When VM-A/192.168.1.1 replies back to
   VM-B/20.1.1.1, T1-A sees that there’s no firewall connection entry, performs
   SNAT on it, and translates the source IP from VM-A/192.168.1.1 to 10.1.1.1. When
   that reply gets back to VM-B, VM-B will drop the traffic because the source IP
   address is 10.1.1.1 instead of VM-A/192.168.1.1.