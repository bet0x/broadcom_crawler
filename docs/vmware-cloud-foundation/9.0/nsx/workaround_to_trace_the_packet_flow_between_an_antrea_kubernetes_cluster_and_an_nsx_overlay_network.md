---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/trace-the-path-of-a-packet-with-antrea-traceflow/workaround-to-trace-the-packet-flow-between-an-antrea-kubernetes-cluster-and-an-nsx-overlay-network.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Workaround to Trace the Packet Flow Between an Antrea Kubernetes Cluster and an NSX Overlay Network
---

# Workaround to Trace the Packet Flow Between an Antrea Kubernetes Cluster and an NSX Overlay Network

In NSX 4.1, Antrea Traceflow does not support tracing the path of a
packet that travels between Antrea Kubernetes
cluster and NSX overlay network. However, some
workaround is possible, as explained in this documentation.

Before following the workflow instructions in
this documentation, read this important note carefully to ensure that the configuration
of the Protocol Type and Destination Port
fields are done correctly in the NSXTraceflow and Antrea Traceflow sessions.

By default, the
Protocol Type of a Traceflow session is set to ICMP. When you
change it TCP, the Destination Port is
set to 0 by default. Remember to specify the port number of
the Kubernetes service or the NSX Load
Balancer virtual server. This is because the K8s service and NSX Load Balancer virtual server listen on a
specific TCP port. In short, you must specify all the information (IP address,
Protocol Type, and Destination Port) accurately in the Traceflow session to ensure that the injected packet is processed
by the K8s service or the NSX Load
Balancer.

## Trace the Path of a Packet from NSX VM to K8s Pod

If you want to trace the path of a packet from a VM in an NSX overlay network to a pod workload in an
Antrea Kubernetes cluster, do the
following steps:

1. Navigate to Plan & TroubleshootTraffic Analysis, and in the Traceflow card, click
   Get Started.
2. In the
   Source area, select Virtual
   Machine from the Type drop-down
   menu.
3. In the
   Destination area, select
   IP-Mac. Click the Layer 3
   option, and then enter any one of these IP addresses:
   - Kubernetes Ingress IP address
   - LoadBalancer Service IP address
   - Node IP address
   - Pod IP address (if pod IP is routable on the underlying
     network)

NSX
Traceflow will trace the path of the
packet till it leaves the NSX overlay
network.

Currently, the following components are
not suported in the Source of an Antrea Traceflow:

- Kubernetes Service
  (LoadBalancer, NodePort)
- Kubernetes Gateway
- Kubernetes Ingress

Therefore, you cannot trace the path of
the packet after it reaches the Antrea
Kubernetes cluster.

## Trace the Path of a Packet from K8s Pod to NSX VM

If you want to trace the path of a packet
from a pod in an Antrea Kubernetes
cluster to a VM in an NSX overlay
network, do the following steps:

1. Navigate to Plan & TroubleshootTraffic Analysis, and in the Traceflow card, click
   Get Started.
2. Click the Antrea
   Traceflow tab.
3. In the
   Source area, select Pod
   from the Type drop-down menu.
4. In the
   Destination area, select IP
   address from the Type drop-down menu,
   and then enter the IP address of the NSX Load Balancer VM.

   Antrea Traceflow will trace the
   path of the packet till it leaves the Antrea Kubernetes cluster.

   As explained in the
   important note earlier in this documentation, esnure that you all the
   information (IP address, Protocol Type, and Destination Port) accurately
   in the Antrea Traceflow
   session
5. Now, you use the NSXTraceflow feature to trace the
   packet from a tier-0 gateway interface to the destination VM in the
   NSX overlay network.
   Configure the Source in the NSXTraceflow as follows:
   - Type: Port/Interface
   - Attachment: Edge Uplink
   - Port: Select the tier-0 interface from
     the drop-down menu.

   Configure the
   Destination in the NSXTraceflow as follows:
   - Type: IP-Mac
   - Layer: Layer-3 (Network Layer)
   - IP
     Address: Enter the IP address of the
     NSX Load
     Balancer VM.

   The trace result will display how the NSX Load Balancer chooses a VM as
   the destination, and what path the packet has taken from the
   NSX Load Balancer to
   the destination VM.