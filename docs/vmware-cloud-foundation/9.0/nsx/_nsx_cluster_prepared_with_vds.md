---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/managing-nsx-on-a-vsphere-distributed-switch/nsx-t-cluster-prepared-with-vds.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Cluster Prepared with VDS
---

# NSX Cluster Prepared with VDS

An example of an NSX cluster prepared using VDS as the host switch.

![A NSX cluster prepared using a VDS switch.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/0f392958-6607-4544-935c-ee0404bcc25f.original.png)

In the sample topology diagram, two VDS switches are configured to manage NSX traffic and vSphere traffic.

VDS-1 and VDS-2 are configured to manage networking for ESX hosts from Cluster-1, Cluster-2, and Cluster-3. Cluster-1 is prepared to run only vSphere traffic, whereas, Cluster-2 and Cluster-3 are prepared as host transport nodes with these VDS switches.

In vCenter, uplink port groups on VDS switches are assigned physical NICs. In the topology, uplinks on VDS-1 and VDS-2 are assigned to physical NICs. Depending on the hardware configuration of the ESX host, you might want to plan out how many physical NICs to be assigned to the switch. In addition to assiging uplinks to the VDS switch, MTU, NIOC, LLDP, LAG profiles are configured on the VDS switches.

After VDS switches are configured in NSX, add an uplink profile.

When preparing a cluster by applying a transport node profile (on a VDS switch), the uplinks from the transport node profile is mapped to VDS uplinks.

After preparing the clusters, ESX hosts on cluster-2 and Cluster-3 manage NSXtraffic, while cluster-1 manage vSphere traffic.