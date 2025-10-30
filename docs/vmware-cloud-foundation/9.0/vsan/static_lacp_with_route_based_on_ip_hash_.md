---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/advanced-nic-teaming/link-aggregation-group-overview/static-lacp-with-route-based-on-ip-hash-overview.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Static LACP with Route Based on IP Hash 
---

# Static LACP with Route Based on IP Hash

You can create a vSAN cluster using static LACP with an IP-hash policy. This section focuses on vSphere Standard Switches, but you also can use vSphere Distributed Switches.

You can use the Route based on IP Hash load balancing policy.

Select Route based on IP Hash load balancing policy at a vSwitch or port-group level. Set all uplinks assigned to static channel group to the Active Uplink position on the Teaming and Failover Policies at the virtual switch or port-group level.

When IP Hash is configured on a vSphere port group, the port group uses the Route based on IP Hash policy. The number of ports in the port-channel must be same as the number of uplinks in the team.

![LACP with route based on IP hash](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/dd1fb185-1eb0-4ae9-880c-edafbe6ce449.original.png)

## Pros and Cons of Static LACP with IP Hash

Consider the tradeoffs to using Static LACP with IP Hash.

Pros

- Improves performance and bandwidth. One vSAN host or VMkernel port can communicate with many other vSAN hosts using the IP Hash algorithm.
- Provides network adapter redundancy. If a NIC fails and the link-state fails, the remaining NICs in the team continue to pass traffic.
- Adds flexibility. You can use IP Hash with both vSphere Standard Switches and vSphere Distributed Switches.

Cons

- Physical switch configuration is less flexible. Physical switch ports must be configured in a static port-channel configuration.
- Increased chance of misconfiguration. Static port-channels form without any verification on either end (unlike LACP dynamic port-channel).
- More complex. Introducing full physical redundancy configuration increases complexity when multiple switches are used. Implementations can become quite vendor specific.
- Limited load balancing. If your environment has only a few IP addresses, the virtual switch might consistently pass the traffic through one uplink in the team. This can be especially true for small vSAN clusters.