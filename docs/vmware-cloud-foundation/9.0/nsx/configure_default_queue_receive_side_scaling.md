---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/enhanced-data-path-optional-configurations/configure-default-queue-receive-side-scaling.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure Default Queue Receive Side Scaling
---

# Configure Default Queue Receive Side Scaling

Enhanced Data Path manages the receive-side data arriving at physical NIC cards. A single port on the physical NIC card makes multiple hardware queues available to receive-side data.

![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ea3f455a-1678-46ec-ab52-2e373a840fd3.original.png)

Queues are assigned to packet processing threads from the non-uniform memory access (NUMA) node. When inbound packets - multicast, unknown, or broadcast - arrive at a physical NIC port, they are distributed across several hardware queues. The distribution is based on hashing certain fields (like IP Address, TCP/UDP port) and determining the queue placement based on the hash.

Default Queue RSS reduces bottlenecks from single queue packet processing. DRSS primarily services broadcast, unknown unicast, or multicast (BUM) traffic. Secondarily, DRSS is used as a fallback when single NetQueue and NetQueue RSS placements fail.

Enhanced Data Path configures Default Queue RSS automatically. There are scenarios where Default Queue RSS can be disabled to free up enough physical queues for a NetQueue RSS based configuration. DRSS can be disabled using the module parameter. For example (this command only applies to the intel i40en driver):

esxcli system module parameters set -m i40en -p "DRSS=0,0,0 RSS=8,8,8

The command above is a partial example. Exact steps should be obtained from the the vendor NIC driver documentation.