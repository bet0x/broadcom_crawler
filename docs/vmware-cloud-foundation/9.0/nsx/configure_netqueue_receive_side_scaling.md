---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/enhanced-data-path-optional-configurations/configure-netq-receive-side-scaling.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure NetQueue Receive Side Scaling
---

# Configure NetQueue Receive Side Scaling

Enable NetQueue Receive Side Scaling to enable VM vNIC requests to be offloaded to a physical NIC. It improves packet performance of the receive-side data.

When a pNIC sends packets to a host, Enhanced Data Path distributes data across different processing threads using a NUMA-aligned RSS engine (a pool of Queues allocated for NetQueue RSS). There are a couple of ways to configure these RSS engines.

These two modes are:

- Shared Netqueue RSS

  RSS engine is shared by multiple vNIC queues. In this mode, multiple hardware queues are made available to vNIC queues. This provides a performance improvement over using a single NetQueue (the default behavior for a VM vNIC).
- Dedicated NetQueue RSS

  RSS engine is dedicated to a single vNIC queue: A dedicated RSS engine completely offloads any request coming from a vNIC to the physical NIC. In this mode, a single RSS engine is dedicated to a single vNIC queue. It improves throughput performance as pNIC manages the receive side data and shares it among the available hardware queues to serve the request. The vNIC queues are co-located on the same logical core or fastpath as pnic queues.

  This approach assigns an entire RSS engine to a virtual machine. This option has severe implications (may starve other workloads, or be impossible to use practically in a DRS cluster) .

  While this option is available with EDP Dedicated, it is not considered a best practice.

  This mode is not supported in EDP Standard deployments.

**How to Configure Shared NetQueue RSS**

NetQueue RSS is configured by the Enhanced Datapath driver module. EDP automatically creates NetQueue RSS engines according to the host pNIC’s capabilities. If there was a customized RSS configuration on a server, it should be reset prior to enabling EDP:

|  |  |
| --- | --- |
| Broadcom | esxcli system module parameters set -m bnxtnet -p “” |
| Mellanox | esxcli system module parameters set -m nmlx5\_core -p "" |
| Intel | esxcli system module parameters set -m i40en -p "" |

**Configuring VM vNIC for Shared RSS**

To configure multiple RSS engines to be available to serve RSS requests from vNICs, configure these parameters in the .vmx file of VM:

ethernet.pnicfeatures = '4', which indicates RSS feature is requested by vNICs.

The VMs connected to the vSphere switch are configured for multiple queues. It means multiple logical cores of a NUMA node can process the Tx and Rx traffic coming from vNICs.

When multiple vNICs request RSS offloading, the Enhanced Network Stack (ENS) does not offload their RSS requests to the pnic, but the shared RSS engine processes their requests. For shared RSS, multiple RSS queues are available but co-location of a vNIC queue or a pNIC queue is not guaranteed.

**Configuring VM vNIC for Dedicated RSS**

To configure a dedicated RSS engine to process requests from a vNIC, configure these parameters in the .vmx file of the VM: ethernet.rssoffload=True.

This configuration is provided for completeness, and not currently recommended.

**Verifying RSS with Queue Counters**

Verify that packet flow is distributed on the hardware queues provided by the RSS engine.

Run the following commands. The counters will increment if there is enough activity to distribute traffic across multiple RX queues:

```
vsish
get /net/pNics/vmnicX/stats
```

```
Sample output:
rxq0: pkts=0 bytes=0 toFill=2047 toProc=0 noBuf=0 csumErr=0
rxq1: pkts=0 bytes=0 toFill=2047 toProc=0 noBuf=0 csumErr=0
rxq2: pkts=0 bytes=0 toFill=2047 toProc=0 noBuf=0 csumErr=0
rxq3: pkts=0 bytes=0 toFill=2047 toProc=0 noBuf=0 csumErr=0
rxq4: pkts=0 bytes=0 toFill=2047 toProc=0 noBuf=0 csumErr=0
rxq5: pkts=0 bytes=0 toFill=2047 toProc=0 noBuf=0 csumErr=0
rxq6: pkts=0 bytes=0 toFill=2047 toProc=0 noBuf=0 csumErr=0
rxq7: pkts=0 bytes=0 toFill=2047 toProc=0 noBuf=0 csumErr=0
txq0: pkts=0 bytes=0 toFill=0 toProc=0 dropped=0
txq1: pkts=0 bytes=0 toFill=0 toProc=0 dropped=0
txq2: pkts=0 bytes=0 toFill=0 toProc=0 dropped=0
txq3: pkts=0 bytes=0 toFill=0 toProc=0 dropped=0
txq4: pkts=0 bytes=0 toFill=0 toProc=0 dropped=0
txq5: pkts=0 bytes=0 toFill=0 toProc=0 dropped=0
txq6: pkts=0 bytes=0 toFill=0 toProc=0 dropped=0
txq7: pkts=0 bytes=0 toFill=0 toProc=0 dropped=0
```