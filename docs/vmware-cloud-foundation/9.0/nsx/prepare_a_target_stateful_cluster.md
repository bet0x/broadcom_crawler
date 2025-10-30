---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/stateful-servers/prepare-a-target-stateful-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Prepare a Target Stateful Cluster
---

# Prepare a Target Stateful Cluster

Prepare a target stateful cluster so that any new host joining the cluster is
automatically deployed with ESX and
NSX VIBs.

You can select a host either within the
cluster or outside of the cluster to be the reference host. You need to create a
reference host because the host profile from the reference host is extracted and
applied to a target host. VDS switch type supports migration of VMkernel
adapters.

In this procedure, as an example the
instructions are to migrate vmk0 (management traffic) and vmk1 (vMotion traffic) to
an VDS switch.

1. On the Reference host, deploy a
   supported ESX build.
   1. In vSphere, add vmk1 adapter. vmk0 is already present to serve
      management traffic.
2. Configure the reference node as a transport node.
   1. Using vSphere Web
      Client, ensure a logical switch is created in NSX.
   2. Using vSphere Web
      Client, ensure that vmk0 and vmk1 are connected to a logical switch on
      VDS switch.
3. Extract the host profile from the reference host.
4. On a target host that is a standalone host:
   1. Attach the host profile to the target host.
   2. Manually configure NSX on the host. When configuring the host as a
      transport node because the host profile on the ESX, ensure the following
      conditions are met.
   3. Host must belong to the same transport zone.
   4. Target host must use the same IP pool that is used by the reference
      host.
   5. Uplink profile, LLDP,
      Networkork mapping for install, VDS configured on the target host must
      be the same as configured on the reference host.
5. On a target host that is part of a cluster:
   1. Attach the host profile to the stateful target cluster.
   2. Create and apply the TN profile on the cluster.
   3. To apply TN profile on the cluster.

Scenarios when VMkernel adapters are migrated with and without host profiles applied
to NSX.