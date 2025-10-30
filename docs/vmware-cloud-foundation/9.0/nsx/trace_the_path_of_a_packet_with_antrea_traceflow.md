---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/trace-the-path-of-a-packet-with-antrea-traceflow.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Trace the Path of a Packet with Antrea Traceflow
---

# Trace the Path of a Packet with Antrea Traceflow

You can start a Traceflow session in NSX Manager to trace the path of packet in an Antrea Kubernetes cluster. Antrea Traceflow currently supports tracing the path of only Unicast
traffic. Broadcast and Multicast traffic are not supported.

Antrea Kubernetes cluster is registered to NSX.

In a
multi-tenant NSX
environment, the Antrea Traceflow
feature is currently not supported under projects. You must use this feature in the
Default view (default space) of the NSX environment.

The source of a Traceflow session must be a pod, whereas the
destination can be a pod or a service in the same Antrea Kubernetes cluster. You can trace the path of a packet for
the following types of traffic in an Antrea Kubernetes cluster:

- Pod to pod traffic on the same
  node (intra-node traffic)
- Pod to pod traffic between
  nodes (inter-node traffic)
- Pod to service traffic on the
  same node
- Pod to service traffic between
  nodes
- Pod to an
  arbitrary IP address

Currently, Antrea Traceflow does not support tracing the path of a packet that
travels between Antrea Kubernetes cluster
and NSX overlay network.
However, some workaround is possible. For more information, see [Workaround to Trace the Packet Flow Between an Antrea Kubernetes Cluster and an NSX Overlay Network](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/trace-the-path-of-a-packet-with-antrea-traceflow/workaround-to-trace-the-packet-flow-between-an-antrea-kubernetes-cluster-and-an-nsx-overlay-network.html#GUID-65c3afb6-6f0b-4e2c-b02f-a19587b84408-en).

Traceflow injects a test packet into the Antrea Kubernetes cluster network and monitors the
flow of the packet. As the packet flows from the source to destination, observations
are collected from various components along the path of the packet. These
observations are displayed in the Traceflow output, which shows the various components in the path
of the packet.

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Navigate to Plan & TroubleshootTraffic Analysis.

   NSX Manager UI fetches the
   information about registered Antrea Kubernetes clusters when you start the
   NSX Manager
   application in the browser. If the application UI is already open, it does
   not fetch the Antrea Kubernetes
   cluster registration information automatically. This behavior is expected
   and per the current UI design. If you have registered the first Antrea Kubernetes cluster after the
   NSX Manager
   application is opened, ensure that you refresh the browser after navigating
   to the Traceflow Analysis page. A manual refresh
   ensures that the Antrea Traceflow tab is visible in
   the UI when you reach step 4 of this procedure.

   This manual browser refresh
   is required only once, and not every time after a new Antrea Kubernetes cluster is
   registered to NSX.
3. In the
   Traceflow card, click Get
   Started.
4. Click the Antrea
   Traceflow tab.

   This tab is available only when at least one Antrea Kubernetes cluster is registered to NSX. If this tab is not visible,
   refresh the browser.
5. Specify the configuration
   settings of the Traceflow
   session.

   Field | Description || Cluster | Select an Antrea Kubernetes cluster from the drop-down menu.  Alternatively, enter the first few characters of the cluster name to filter the list, and then select the cluster. |
   | IP Address | Select either IPv4 or IPv6. |
   | Protocol Type | Select any one protocol type: ICMP, TCP, UDP.  For ICMP:  - Optional: Enter the   ICMP identifier. Default is 0. - Optional: Enter the   ICMP sequence number. Default is 0. - Optional: Enter the   TTL. Default is 64. For TCP, UDP:  - Optional: Enter the   source port number. Default is 0. - Optional: Enter the   destination port number. Default is 0. - (Only for TCP): Add   TCP flags, if required. SYN flag is set by default. This flag is   required for the Antrea Traceflow. - Optional: Enter the   TTL. Default is 64. |
   | Source | Only Pod is supported as the source of an Antrea Traceflow.  Pods that use the host network are currently not supported as the source of an Antrea Traceflow. This limitation is a known behavior. For example, Antrea Agent pods are not supported in the source of an Antrea Traceflow.  If you know the pod name, select it directly from the Pod drop-down menu. Otherwise, filter the list of pods by doing these steps: 1. Enter the first    few characters of the node name, or select a value from the    Node drop-down menu. 2. Enter the first    few characters of the namespace, or select a value from the    Namespace drop-down menu. |
   | Destination | 1. Select the type of    destination: Pod,    Service, IP    Address. 2. If you select    Pod or Service    as the destination, use the Node and    Namespace drop-down menus to filter    the list of pods or services. 3. If you select    IP Address as the destination, enter    an IP    address. |
6. Click Trace.

The Traceflow observations are displayed in
a tabular format. For each observation, the table shows the following information.

Observation Type
:   This column takes the
    following values.

    | Observation Type | Description |
    | --- | --- |
    | Delivered | The packet is delivered to destination Pod or Service properly. |
    | Dropped | The packed is dropped by a network policy. |
    | Received | The packet is received from another node in the Kubernetes cluster. |
    | Forwarded | The packet is forwarded to the next logical node or a Kubernetes cluster object. |

Component
:   This column shows the
    components that the test packet had encountered on its path from the
    source to the destination. Sample component values are: IngressRule,
    EgressRule, SpoofGuard, Classification, Output, and so on.

    Click the component name
    to view more information in a pop-up window.

Timestamp
:   The date and time for each
    observation.