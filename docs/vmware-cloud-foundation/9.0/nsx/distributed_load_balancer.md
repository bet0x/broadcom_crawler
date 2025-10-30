---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/distributed-load-balancer.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Distributed Load Balancer
---

# Distributed Load Balancer

A Distributed Load Balancer configured in NSX can help you effectively load balance East-West traffic and scale
traffic because it runs on each ESX
host.

Distributed Load
Balancer is supported only for Kubernetes (K8s) cluster IPs managed by vSphere with Kubernetes. Distributed Load
Balancer is not supported for any other workload types. As an administrator, you
cannot use NSX Manager GUI to
create or modify Distributed Load Balancer objects. These objects are pushed by
vCenter through
NSX API when K8 cluster IPs
are created in vCenter.

In traditional networks, a central load
balancer deployed on an NSX Edge node is
configured to distribute traffic load managed by virtual servers that are configured on
the load balancer.

If you are using a central balancer,
increasing the number of virtual servers in the load balancer pool might not always meet
scale or performance criteria for a multi-tier distributed application. A distributed
load balancer is realized on each hypervisor where load balancing workloads, such as
clients and servers are deployed, ensuring traffic is load balanced on each hypervisor
in a distributed way.

A distributed load balancer can be configured on the NSX network along with a central load balancer.

![A logical topology of ESX hosts
                    configured using Distributed Load Balancer.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/4eb34b8b-511a-4e5f-ba8d-f885d1b07544.original.png)

In the diagram, an instance of the Distributed
Load Balancer is attached to a VM group. As the VMs are downlinks to the distributed
logical router, Distributed Load Balancer only load balances east-west traffic. In
contrast, the central load balancer, manages north-south traffic.

To cater load balancing requirements of each
component or module of an application, a distributed load balancer can be attached to
each tier of an application. For example, to serve a user request, a frontend of the
application needs to reach out to the middle module to get data. However, the middle
layer might not be deployed to serve the final data to the user, so it needs to reach
out the backend layer to get additional data. For a complex application, many modules
might need to interact with each other to get information. Along with complexity, when
the number of user request increase exponentially, a distributed load balancer can
efficiently meet the user needs without taking a performance hit. Configuring a
Distributed Load Balancer on every host achieves issues of scale and packet transmission
efficiency.

Enable DFW for DLB workloads. Disabling DFW either globally or through the DFW
Exclusion List will cause an outage on DLB workloads.