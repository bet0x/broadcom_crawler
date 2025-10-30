---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-network-topologies/vsan-stretched-cluster-deployments.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN Stretched Cluster Deployments
---

# vSAN Stretched Cluster Deployments

vSAN supports stretched cluster deployments that span two locations.

## Supported vSAN Stretched Cluster Configurations

vSAN supports stretched cluster configurations.

The following configuration prevent traffic from Site 1 being routed to Site 2 through the witness host, in the event of a failure on either of the data sites' network. This configuration avoids performance degradation. To ensure that data traffic is not switched through the witness host, use the following network topology.

Between Site 1 and Site 2, implement a stretched Layer 2 switched configuration or a Layer 3 routed configuration. Both configurations are supported. VMware recommends Layer 3 for fault isolation and easier troubleshooting

Between Site 1 and the witness host, implement a Layer 3 routed configuration.

Between Site 2 and the witness host, implement a Layer 3 routed configuration.

We shall examine a stretched Layer 2 network between the data sites and a Layer 3 routed network to the witness site. To demonstrate a combination of Layer 2 and Layer 3 as simply as possible, use a combination of switches and routers in the topologies.

## Stretched Layer 2 Between Data Sites, Layer 3 to Witness Host

vSAN supports stretched Layer 2 configurations between data sites.

![Stretched L2 to data hosts, L3 to witness host diagram](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c2535d7e-0f09-4766-b852-ce9ce7c44552.original.png)

## Layer 3 Everywhere

In this vSAN stretched cluster configuration, the data traffic is routed between the data sites and the witness host.

To implement Layer 3 everywhere as simply as possible, use routers or routing switches in the topologies.

vSAN does not require IGMP snooping or PIM because all the routed traffic is unicast.

![Layer 3 vSAN stretched cluster diagram](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/620dd852-150e-4c10-b9df-c5390827a12b.original.png)

You can configure a vSAN stretched cluster in a Layer 2 network, but this configuration is not recommended.

## Separating Witness Traffic on vSAN Stretched Clusters

vSAN supports separating witness traffic on stretched clusters.

You can separate witness traffic from vSAN traffic in two-node configurations. This means that the two vSAN hosts can be directly connected without a 10 GbE switch.

This witness traffic separation is only supported on two-node deployments in vSAN. Separating the witness traffic on vSAN stretched clusters is supported in vSAN.