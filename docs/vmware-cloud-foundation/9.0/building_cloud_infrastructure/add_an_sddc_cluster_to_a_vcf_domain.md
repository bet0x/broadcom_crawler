---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/expand-a-workload-domain/add-a-cluster-to-a-workload-domain-using-the-sddc-manager-ui.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Add an SDDC Cluster to a VCF Domain
---

# Add an SDDC Cluster to a VCF Domain

If you want to add capacity to a VCF domain, you can use the vSphere Client to add an SDDC cluster to a VCF domain.

- Verify that there are unassigned hosts are available in the Hosts inventory. See [View ESX Host Inventory](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/view-host-inventory.html).
- For information on commissioning hosts, see [Commission ESX Hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/commission-hosts.html).
- Ensure that the hosts you want to add to the SDDC cluster are in an active state.
- If you are using DHCP for the NSX Host Overlay Network, a DHCP server must be configured and advertising IP addresses on the NSX Host Overlay VLAN of the VCF domain. When NSX creates TEPs for the VCF domain, they are assigned IP addresses from the DHCP server.
- To perform this task in the vSphere Client, you must have access to the management domain vCenter, or your VCF Instance must be configured with VCF SSO and vCenter linking. See [Configuring VCF Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is.html) and [Linking vCenter instances in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/linking-vcenter-systems-in-vmware-cloud-foundation-operations.html). As an alternative, you can perform this task using the SDDC Manager UI (https://<sddc-manager-fqdn>).

If a workload domain has multiple clusters, each cluster can use a different type of principal storage, as long as all hosts within an SDDC cluster use the same type.

You can run multiple add cluster tasks at the same time.

Starting with VMware Cloud Foundation 9.0 and vSphere Foundation 9.0, the vSphere Virtual Volumes capability, also known as vVols, is deprecated and will be removed in a future release of VMware Cloud Foundation and vSphere Foundation. Support for vSphere Virtual Volumes will continue for critical bug fixes only for versions of vSphere 8.x, VMware Cloud Foundation and vSphere Foundation 5.x, and other supported versions until end-of-support for the respective release.

1. In the vSphere Client for the VCF domain vCenter, browse to the VCF instance datacenter in the inventory.
2. Select the datacenter and click ActionsNew ClusterCreate SDDC Cluster.
3. Select the storage type for the SDDC cluster and click Begin.

   Option | Description || vSAN | Select to configure a vSAN-based workload domain.  Select Enable vSAN ESA to configure a vSAN ESA workload domain. If you do not select this option, the workload domain is configured with vSAN OSA. vSAN storage clusters (formerly known as vSAN Max) require vSAN ESA |
   | NFS | Select to configure an NFS-based workload domain. |
   | VMFS on FC | Select to configure a Fibre Channel-based workload domain |
   | vVol | Select to configure a vVol-based workload domain. |
4. Enter a name for the SDDC cluster.
5. Select a cluster image from the drop-down menu.

   If the cluster image contains a different version of a vendor add-on or component than what is installed on the ESXi hosts you add to the cluster, the hosts will be remediated to use the cluster image during cluster creation.
6. Click Next.
7. Enter the vSAN Storage details and click Next.

   This screen only displays if you selected vSAN storage. The vSAN storage options are different for vSAN OSA and vSAN ESA.

   vSAN OSA:

   Option | Description || vSAN Cluster Type | - vSAN HCI: Provides storage and compute resources. - vSAN Compute Cluster: Provides compute resources only. |
   | Failures to Tolerate (vSAN HCI only) | Specify the level of availability you want configured for the cluster. Your selection determines the minimum number of required ESX hosts. |
   | Space efficiency (vSAN HCI only) | Select the check box to enable vSAN deduplication and compression. |
   | Mount Remote Datastore (vSAN Compute Cluster only) | Click Next and choose the remote datastore to provide storage for the new cluster. |

   vSAN ESA:

   Option | Description || vSAN Cluster Type | - vSAN HCI: Provides storage and compute resources. - vSAN Storage: Provides storage resources only. You can mount a vSAN Storage datastore on other vSAN ESA or vSAN compute clusters. |
   | Network Option (vSAN Storage only) | Select the vSAN Storage Client Network checkbox to isolate client or application network traffic from vSAN Storage internal traffic by utilizing dedicated VMkernel ports backed by physical network ports. |
   | Storage Type | Local vSAN datastore. This setting cannot be modified. |
   | Storage Policy | Auto-policy management. This setting cannot be modified.  Based on the type of cluster and number of hosts, vSAN creates and assigns a default datastore policy for best capacity utilization after the cluster configuration is completed. Policy details can be viewed in the vSphere Client (Policies and ProfilesVM Storage Policies). |
8. Enter the NFS Storage details and click Next.

   This screen only displays if you selected NFS storage.

   Option | Description || Datastore Name | Enter a name for the NFS datastore.  The datastore name must contain 3-80 characters and cannot contain any leading or trailing whitespace.  If you using a previously mounted NFS share, the datastore will be automatically renamed to original datastore name. |
   | Folder | Enter the path to the NFS share.  The folder location must contain 3-255 characters and the path cannot contain any whitespace. |
   | NFS Server IP Address | Enter the IP address of the NFS server. |
9. Enter the FC Storage details and click Next.

   This screen only displays if you selected FC storage.

   Option | Description || Datastore Name | Enter the name of the VMFS on FC datastore.  Datastore name must contain 3-80 characters and cannot contain any leading or trailing whitespace. |
10. Enter the vVol Storage details and click Next.

    This screen only displays if you selected vVols storage.

    Option | Description || VASA Protocol Type | Select a VASA protocol type.  vVols supports FC, NFS, and iSCSI storage protocol types. |
    | VASA Provider | Select a VASA provider name.  The VASA Providers list is determined by the selected VASA protocol type. |
    | Storage Container | Select a storage container.  The Storage Containers list is determined by the selected VASA Provider. The list does not display storage containers that are already in use by other clusters. |
    | VASA User | Select a VASA user.  The VASA User list is determined by the selected VASA Provider. |
    | Datastore Name | Enter a datastore name.  The datastore name must contain 3-80 characters and cannot contain any leading or trailing whitespace. |
11. On the Host Selection page, select hosts for the SDDC cluster and click Next.

    You can use the toggle button to turn Skip failed hosts during cluster creation off or on. When this option is off, cluster creation will fail if you select an unhealthy host. When this option is on, cluster creation will succeed if you selected enough healthy hosts to meet the minimum requirements for a new cluster.

    The hosts must be commissioned with the same storage type that you selected for the cluster.

    When you have selected the minimum number of hosts required for this cluster, the Next button is enabled.
12. Enter the Distributed Switch details and click Next.

    Option | Description || Default | This profile is recommended. It provides a unified fabric for all traffic types using a single vSphere Distributed Switch. |
    | Storage Traffic Separation | This profile creates two vSphere Distributed Switches with separate physical NICs. One switch is dedicated for storage traffic, while the other is used for all other traffic. |
    | NSX Traffic Separation | This profile creates two vSphere Distributed Switches with separate physical NICs. One switch is dedicated for NSX Edge and overlay traffic, while the other is used for all other traffic. |
    | Storage Traffic and NSX Traffic Separation | This profile creates three vSphere Distributed Switches with separate physical NICs. One switch is dedicated for NSX Edge and overlay traffic, the second switch is dedicated for storage traffic, while the third is used for all other traffic. |
    | Custom Switch Configuration | Copy from a preconfigured profile or create a new distributed switch configuration. Multiple vSphere Distributed Switches can be configured. Each vSphere Distributed Switch can hold one or more network traffic configurations.  Some network traffic types are mandatory. Switch configuration is incomplete until these mandatory traffic types are configured.  Management, vMotion, vSAN and NSX network types can be configured only once for a cluster.  NSX and Public network traffic types can be configured in multiple vSphere Distributed Switches. |
13. On the Review page, review the vSphere cluster details and click Finish.

To add another cluster in parallel, repeat the above steps.