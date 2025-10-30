---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-network-topologies/2-host-vsan-deployments.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Two Node vSAN Deployments
---

# Two Node vSAN Deployments

vSAN supports two-node deployments. Two-node vSAN deployments are typically used for remote offices/branch offices (ROBO) that have a small number of workloads, but require high availability.

vSAN two-node deployments use a third witness host, which can be located remotely from the branch office. Often the witness is maintained in the branch office, along with the management components, such as the vCenter.

## Two Node Deployments

vSAN supports two-node deployments.

With vSAN, the two-node vSAN implementation is much simpler. vSAN allows the two hosts at the data site to be directly connected.

![2-node vSAN](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/78064298-6685-4eb0-afc8-53323d7d533d.original.png)

To enable this functionality, the witness traffic is separated completely from the vSAN data traffic. The vSAN data traffic can flow between the two nodes on the direct connect, while the witness traffic can be routed to the witness site over the management network.

The witness appliance can be located remotely from the branch office. For example, the witness might be running back in the main data center, alongside the management infrastructure (vCenter, vROps, Log Insight, and so on). Another supported place where the witness can reside remotely from the branch office is in vCloud Air.

Multiple remote office/branch office two-node deployments are supported on shared witness.

![2-node vSAN all unicast](/content/dam/broadcom/techdocs/us/en/dita/vmware/vcf/vcf-90/vsan/images/multiple2-node-vsan66-backtoback-nomulticast.png)

## Common Considerations for Two Node vSAN Deployments

Two-node vSAN deployments provide support to other topologies. This section describes common configurations.

vSAN requires a minimum 1500 MTU between the witness host and data hosts and the MTUs on the witness and data hosts must match.

For more information about two-node configurations and detailed deployment considerations outside of network, see the vSAN core documentation.

## Running the Witness on Another Two Node vSAN Cluster

vSAN does not support cross hosting the witness on another two-node cluster.

## Witness Running on Another Standard vSAN Deployment

vSAN supports witness running on another standard vSAN deployment.

This configuration is supported. Any failure on the two-node vSAN at the remote site does not impact the availability of the standard vSAN environment at the main data center.

![2-node witness host in another vSAN cluster](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/80875426-e10e-42fb-bf4f-9805f214b789.original.png)