---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/enhanced-data-path-optional-configurations/configure-multiple-context-on-host-switch.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure VM vNIC RX/TX Scaling
---

# Configure VM vNIC RX/TX Scaling

Provide multiple cores to vNICs by configuring the Multiple Context functionality on a host switch running in Enhanced Datapath mode. It helps improve packet performance.

![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8a09cfd9-55bc-4a61-8f93-b4f2fc3b0f31.original.png)

On a host switch configured to run in the Enhanced Datapath mode, you can configure Multiple Context functionality for vNIC traffic. Multiple Context means that multiple threads can serve Tx (transmit) and Rx (receive) vNIC queues, in contrast to the single context, where only one networking thread serves both the Tx queue and Rx queue.

TX = Transmit scaling achieved with the procedure below.

RX = Multi-Context piggybacks on NetQueue RSS without requiring additional configuration on the VM.

1. To verify that host switch is configured to run in Enhanced Datapath mode:
   1. Navigate the UI based on the NSX version and select a host:

      - SystemFabricHosts and select the Cluster tab.
      - SystemFabricHosts and select the Other Nodes tab.
   2. Select the transport node.
   3. Select the Overview tab and verify Enhanced Datapath Capable parameter is set to Yes.
2. To configure Multiple Context functionality for vNIC traffic managed through Enhanced Datapath mode, edit configuration options of VMs and set the following parameter value. See the latest vSphere Virtual Machine Administration guide for details on how to edit VM configuration options.

   ethernetX.ctxPerDev = "3"

   Where, the value 3 indicates that Multiple Context functionality is applied per vNIC queue.

   Other supported values for contexts are:
   - ethernetX.ctxPerDev =1 indicates that Multiple Context functionality is applied per vNIC.
   - ethernetX.ctxPerDev =2 indicates that Multiple Context functionality is applied per VM (default). If you set the value to 0 - ethernetX.ctxPerDev = 0, the value is configured to 2 (default).

Enhanced Datapath improves packet throughput by using the Multiple Context functionality set for vNIC queues.