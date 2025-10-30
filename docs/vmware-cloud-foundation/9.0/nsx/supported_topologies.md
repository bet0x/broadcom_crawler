---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/stateful-services-on-tier-0-and-tier-1-gateways/supported-topologies.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Supported Topologies
---

# Supported Topologies

These are the supported topologies for stateful services on Tier-0 or Tier-1 in
active-active HA mode.

## Greenfield Topologies

In new installations, note the following
considerations when building one of the supported topologies for stateful services
on a NSX Edge cluster:

- Tier-1 stateful active-active
  gateways running stateful services must be connected to Tier-0 stateful
  active-active gateways and must be hosted on the same NSX Edge cluster.
- Tier-1 active-standby gateways
  can be connected to Tier-0 stateful active-active gateways but Tier-1
  gateways must be hosted on a different NSX Edge cluster.

## Brownfield Topologies

In existing installations, note the
following considerations when building one of the supported topologies for stateful
services on a NSX Edge cluster:

- An existing Tier-1 gateway in
  active-standby HA mode cannot be configured to be in active-active HA mode.
  You need to create a new Tier-1 gateway in active-active HA mode.
- Tier-0 active-standby gateways
  cannot be converted to Tier-0 active-active gateways.
- Tier-1 stateless active-active
  gateways can be converted to stateful active-active gateways as long as
  there is no Tier-1 gateway attached to Tier-0 gateways.

## Tier-0 Active-Active and Tier-1 Active-Active HA mode

![Stateful services on Tier-0 Active-Active and Tier-1 Active-Active HA
                        mode.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/af23b884-e234-4641-87d8-3bdd8b9cfb3c.original.png)

## Tier-0 Active-Active and Tier-1 Active-Standby HA mode

![Stateful services on Tier-0 Active-Active and Tier-1 Active-Standby HA
                        mode.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/e80ca71f-57a8-4188-bcbe-763f21a09cdd.original.png)

## Tier-0 Active-Active HA mode (no Tier-1 gateways)

![Stateful services on Tier-0 Active-Active gateways.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/0aab8a9d-91a4-4242-a821-1b913f8e9553.original.png)

## Tier-0 Active-Active and Tier-1 Distributed Router only

![Stateful services on Tier-0 Active-Active and Tier-1 Distributed Router
                        mode.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/913693e8-4758-49d7-bae5-fec2202162cc.original.png)