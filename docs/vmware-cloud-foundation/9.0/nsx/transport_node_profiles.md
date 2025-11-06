---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/preparing-esxi-hosts-as-transport-nodes/transport-node-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Transport Node Profiles
---

# Transport Node Profiles

A Transport Node Profile (TNP) is a template to define networking configuration that
is applied to a cluster.

## Transport Node Profile

Before you create a Transport Node Profile consider these points:

- You can add a maximum of four N-VDS
  or VDS switches for each configuration: enhanced N-VDS or VDS created for
  VLAN transport zone, standard N-VDS or VDS created for overlay transport
  zone, enhanced N-VDS or VDS created for overlay transport zone.
- There is no limit on the number of
  standard N-VDS switches created for VLAN transport zone.
- Each N-VDS switch name must be
  unique. NSX does not allow use of
  duplicate switch names.
- Each transport zone ID associated
  with each N-VDS or VDS host in a transport node configuraiton or transport
  node profile configuration must be unique.

To create a TNP, you configure Host Switches with transport zones, uplink profiles,
mapping uplinks to VDS uplinks (for a VDS switch) and other configurations. TNP can
be created on VDS or N-VDS Host Switches.

![Configure host switches for a Transport Node Profile.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/647e74fd-2188-437c-b8bd-326b6f5d50f1.original.png)

A stretched cluster is a cluster that
extends across multiple TEP subnets. A non-stretched cluster is a cluster that is
confined to a single TEP subnet. In a non-stretched cluster, a single TNP is
sufficient to be applied to a cluster. However, when a cluster is stretched across
multiple subnets or L3 domains, you can create sub-clusters consisting of hosts that
need the same configuration.

While a TNP represents the global
configuration applied to a Host Switch, a sub-TNP represents the local configuration
applied to a sub-cluster. When you apply a sub-TNP to a sub-cluster, all the
configuration from sub-TNP takes precedence over the host switch configuration.

A Sub-TNP can only be created for
vSphere Distributed Switch (VDS) switches.

Transport node creation begins when a
transport node profile is applied to a vCenter cluster. NSX Manager prepares the hosts in the cluster and installs the
NSX components on all the hosts.
Transport nodes for the hosts are created based on the configuration specified in
the transport node profile.

TNP
is not used to prepare standalone hosts.

On a cluster prepared with a transport
node profile, these outcomes are true:

- When you move an unprepared
  host into a cluster applied with a transport node profile, NSX automatically
  prepares the host as a transport node using the transport node profile.
- When you move a transport node
  from the cluster to an unprepared cluster or directly as a standalone host
  under the data center, first the transport node configuration applied to the
  node is removed and then NSX VIBs are removed from the host. See [Uninstall from the vSphere Client](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/triggering-uninstallation-from-the-vsphere-web-client.html#GUID-d9ef4315-b564-4f7a-b0f5-9582cf3efa9c).

To delete a transport node profile, you
must first detach the profile from the associated cluster. The existing transport
nodes are not affected. New hosts added to the cluster are no longer automatically
converted into transport nodes.