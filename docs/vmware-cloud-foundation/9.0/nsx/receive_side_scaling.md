---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/enhanced-data-path-optional-configurations/receive-side-scaling.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Receive Side Scaling
---

# Receive Side Scaling

EDP takes full advantage of RSS to scale out.

Receive Side Scaling allows multiple threads on the receive side for processing incoming traffic for a NIC.

Without RSS, receiving ESX hosts only use one physical queue and hence one lcore (in EDP Dedicated) for packet processing. When the receive side data increases it creates a bottleneck at the single core. The overall throughput performance might decrease. With RSS enabled on the NIC, you can configure multiple hardware queues to process requests to VMs. Before you use a NIC card to leverage the RSS functionality, use the Broadcom Compatibility Guide for I/O to confirm whether the NIC card driver supports RSS.

![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/75d0d58f-a62d-4e17-865d-7a1713b8f2cc.original.png)

You can choose to enable or disable RSS modes:

| RSS Types | EDP Behavior |
| --- | --- |
| Default Queue RSS | Enabled by default. |
| Shared NetQueue RSS | Optional setting. See [Configure NetQueue Receive Side Scaling](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/enhanced-data-path-optional-configurations/configure-netq-receive-side-scaling.html). |
| Dedicated NetQueue RSS | Optional setting. This setting assigns an entire RSS engine to a single virtual machine. It is not considered a best practice to enable this setting. Engage Broadcom for technical guidance. |
| Device RSS | Conceptually similar to Default Queue RSS but applies to all pNIC queues.  This will be seen on devices that do not support NetQueue. EDP does not interact with Device RSS (this type of RSS is managed fully on the driver). |