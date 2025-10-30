---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/deploy-a-vi-workload-domain-using-the-sddc-manager-ui.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Create a New Workload Domain Using VCF Operations
---

# Create a New Workload Domain Using VCF Operations

Creating a new workload domain adds a logical pool of compute, network, and storage infrastructure to a VCF instance.

General requirements:

- A vSphere Lifecycle Manager cluster image must be available for the default vSphere cluster of the workload domain. See [Managing vSphere Lifecycle Manager Images for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/managing-vsphere-lifecycle-manager-images-for-vmware-cloud-foundation.html).
- Hosts must be commissioned with the target principal storage type. See [Managing ESX Hosts in VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management.html).
- If you are using vVols principal storage type, add a VASA provider to the inventory. See [Add a VASA Provider for vVols Storage in Workload Domains](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/configuring-managemnet-appliances/add-a-vasa-provider.html).

  Starting with VMware Cloud Foundation 9.0 and vSphere Foundation 9.0, the vSphere Virtual Volumes capability, also known as vVols, is deprecated and will be removed in a future release of VMware Cloud Foundation and vSphere Foundation. Support for vSphere Virtual Volumes will continue for critical bug fixes only for versions of vSphere 8.x, VMware Cloud Foundation and vSphere Foundation 5.x, and other supported versions until end-of-support for the respective release.
- If you are using vSAN principal storage type, SSD disks or NVMe disks without pre-existing disk partitions must be available with each host.

Networking requirements:

- A static IP pool or a DHCP server configured and advertising IP addresses on the workload domain's NSX host overlay (HOST TEP) VLAN.
- Each host must have at least one physical NIC, with a minimum of 10 Gbps speed, connected to a standard switch.
- A network pool with free IP addresses must be available.
- The IP addresses and Fully Qualified Domain Names (FQDNs) for the vCenter and NSX Manager instances must be resolvable over DNS

For information about importing an existing vCenter environment as a workload domain, see [Import an Existing vCenter to Create a Workload Domain](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/import-an-existing-vcenter-to-create-a-workload-domain.html).

VMware Cloud Foundation supports creating workload domains with a vSphere Distributed Switch with link aggregation control protocol (LACP) enabled, but you must use the [SDDC Manager API](https://developer.broadcom.com/xapis/sddc-manager-api/latest/domains/#_usecase_createdomain) to do so.

1. In VCF Operations, select InventoryDetailed View.
2. Expand VCF Instances and browse to the VCF instance in which you want to create a new workload domain.
3. Click Add Workload DomainCreate New.
4. Review the prerequisites, click Select All, and click Proceed.
5. Enter the General Information details and click Next.

   Option | Description || Workload Domain Name | Type a name for the workload domain, such as sfo01. The name must contain between 3 and 20 characters.  It is good practice to include location information in the name since resource object names (such as vSphere Distributed Switch names) are generated based on the workload domain name. |
   | Enable vSphere Supervisor | This setting is activated by default, but can be deactivated.  When activated, the workload domain is enabled for vSphere Supervisor with NSX VPC Networking, creating a Supervisor, a single Supervisor control plane VM, and a single vSphere zone.  After the workload domain is complete, you must deploy an NSX Edge cluster with an active-standby tier-0 gateway to complete Supervisor activation, unless you are using an existing NSX Manager instance with a compatible NSX Edge cluster. See [Configure Centralized Network Connectivity with Edge Clusters](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-network-connectivity-in-vcenter/managing-centralized-network-connectivity-with-edge-clusters.html) for information about deploying an NSX Edge cluster.  Use the vSphere Client to scale out, upgrade, monitor, and configure vSphere Supervisor after deployment.  Click Learn More and review the [vSphere Supervisor documentation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsphere-supervisor-installation-and-configuration.html) for more information. |
   | SSO Domain Name | Enter the vCenter Single Sign-On (SSO) domain name, for example, example.domain.local.  This creates a workload domain that is isolated from the other workload domains in your VCF instance. |
   | Password Creation | Select Auto-generate my passwords for newly installed appliances to generate random complex passwords for any appliances that get deployed during workload domain creation.  You can retrieve auto-generated passwords using the [SDDC Manager API](https://developer.broadcom.com/xapis/sddc-manager-api/latest/credentials/).  If choose not to auto-generate passwords, set and confirm the administration password for the SSO administrator account. This is the password for the user administrator@example.domain.local.  Requirements: - 8-20 characters. - No spaces. - At least one lowercase character. - At least one uppercase character. - At least one digit. - At least one special character. - No dictionary words. |
6. Enter the vCenter details and click Next.

   Option | Description || vCenter FQDN | Enter the FQDN for the workload domain's vCenter.  The vCenter for a workload domain deployed in the management domain. |
   | vCenter Root Password | Enter and confirm a vCenter root password.  Requirements: - No dictionary words. - 15-20 characters. - At least one lowercase character. - At least one digit. - No spaces. - At least one special character. - At least one uppercase character.  This is not required if you chose to auto-generate passwords. |
7. Enter the Cluster details and click Next.

   Option | Description || Cluster Name | Enter a name for the vSphere Cluster. |
   | vSphere Zone Name | If you enabled vSphere Supervisor, enter a vSphere Zone name.  The vSphere Zone is created and the cluster is added to it. This workflow creates a single vSphere Zone. You can use the vSphere Client to create additional zones. |
8. Select a cluster image and click Next.

   If the cluster image contains a different version of a vendor add-on or component than what is installed on the ESX hosts you add to the cluster, the hosts will be remediated to use the cluster image during cluster creation.
9. Enter the NSX Manager details and click Next.

   Choose whether to create a new NSX Manager instance or join an existing NSX Manager instance. If you already have an NSX Manager instance for a different workload domain, you can reuse that NSX Manager instance or create a new one.

   If you are using an existing NSX Manager instance, select it. If you are creating a new NSX Manager instance, enter the following information.

   Option | Description || Deployment Size | - Standard: Deploys single-node NSX Manager requiring fewer resources. - High-Availability (recommended): Deploys a three-node NSX Manager cluster to enhance the availability of management and control plane functions, as well as minimize downtime during upgrades. |
   | Appliance Size | - Medium - Large - Extra Large |
   | Appliance 1 FQDN | Enter the FQDN for the first NSX Manager node. |
   | Appliance 2 FQDN | Enter the FQDN for the second NSX Manager node.  This is not applicable if you chose Standard deployment size. |
   | Appliance 3 FQDN | Enter the FQDN for the third NSX Manager node.  This is not applicable if you chose Standard deployment size. |
   | Appliance Cluster FQDN | Enter the NSX Manager cluster FQDN. |
   | Administrator Password | Enter and confirm an NSX administrator password.  Requirements: - At least five different characters. - At least one lowercase character. - At least one digit. - No more than four monotonic or sequential characters. - At least 12 characters. - Cannot be palindrome. - At least one special character. - At least one uppercase character. - No dictionary words. This is not required if you chose to auto-generate passwords. |
   | Auditor Password | Enter and confirm an NSX auditor password.  Requirements: - At least five different characters. - At least one lowercase character. - At least one digit. - No more than four monotonic or sequential characters. - At least 12 characters. - Cannot be palindrome. - At least one special character. - At least one uppercase character. - No dictionary words. This is not required if you chose to auto-generate passwords. |
   | Configure Network Connectivity and VPC External IP Blocks | Select one of the options: - Centralized Connectivity - Distributed Connectivity vSphere Supervisor requires Centralized Connectivity.  If you select Centralized Connectivity, configure it after the workload domain is created to make it VPC-ready. See [Configure Centralized Network Connectivity with Edge Clusters](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-network-connectivity-in-vcenter/managing-centralized-network-connectivity-with-edge-clusters.html).  If you select Distributed Connectivity, enter the following: - VLAN ID: A dedicated VLAN network is required for the distributed gateway's external connectivity. - Gateway CIDR IPv4 Address: The gateway CIDR IP address should be the same as the VLAN default gateway configured in the external router (TOR). - External IP Block: Advertised CIDRs that allow outside connectivity to VPC workloads either on public subnets or through external IPs. The external IP block must be the same as, or a sub-block of, the configured Gateway CIDRs. - Private - Transit Gateway IP Block: Private CIDRs that are available for inter-VPC (Virtual Private Cloud) communication and are not advertised by the Transit Gateway to the outside datacenter.After the workload domain with distributed connectivity is created, it is VPC-ready.  For more information about VPCs, see [Managing Virtual Private Clouds in vCenter](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-virtual-private-clouds-in-vcenter.html). |
10. Enter the Storage details and click Next.

    Option | Description || vSAN | Select to configure a vSAN-based workload domain.  Select Enable vSAN ESA to configure a vSAN ESA workload domain. If you do not select this option, the workload domain is configured with vSAN OSA. vSAN storage clusters (formerly known as vSAN Max) require vSAN ESA |
    | NFS | Select to configure an NFS-based workload domain. |
    | VMFS on FC | Select to configure a Fibre Channel-based workload domain |
    | vVol | Select to configure a vVol-based workload domain. |
11. Enter the vSAN Storage details and click Next.

    This screen only displays if you selected vSAN storage. The vSAN storage options are different for vSAN OSA and vSAN ESA.

    vSAN OSA:

    Option | Description || Failures to Tolerate | Specify the level of availability you want configured for the cluster. Your selection determines the minimum number of required ESX hosts. |
    | Space efficiency | Select the check box to enable vSAN deduplication and compression |

    vSAN ESA:

    Option | Description || vSAN Cluster Type | - vSAN HCI: Provides storage and compute resources. - vSAN Storage: Provides storage resources only. You can mount a vSAN Storage datastore on other vSAN ESA or vSAN compute clusters. |
    | Network Option (vSAN Storage only) | Select the vSAN Storage Client Network checkbox to isolate client or application network traffic from vSAN Storage internal traffic by utilizing dedicated VMkernel ports backed by physical network ports. |
    | Storage Type | Local vSAN datastore. This setting cannot be modified. |
    | Storage Policy | Auto-policy management. This setting cannot be modified.  Based on the type of cluster and number of hosts, vSAN creates and assigns a default datastore policy for best capacity utilization after the cluster configuration is completed. Policy details can be viewed in the vSphere Client (Policies and ProfilesVM Storage Policies). |
12. Enter the NFS Storage details and click Next.

    This screen only displays if you selected NFS storage.

    Option | Description || Datastore Name | Enter a name for the NFS datastore.  The datastore name must contain 3-80 characters and cannot contain any leading or trailing whitespace.  If you using a previously mounted NFS share, the datastore will be automatically renamed to original datastore name. |
    | Folder | Enter the path to the NFS share.  The folder location must contain 3-255 characters and the path cannot contain any whitespace. |
    | NFS Server IP Address | Enter the IPv4 address of the NFS server. |
13. Enter the FC Storage details and click Next.

    This screen only displays if you selected FC storage.

    Option | Description || Datastore Name | Enter the name of the VMFS on FC datastore.  Datastore name must contain 3-80 characters and cannot contain any leading or trailing whitespace. |
14. Enter the vVol Storage details and click Next.

    This screen only displays if you selected vVols storage.

    Option | Description || VASA Protocol Type | Select a VASA protocol type.  vVols supports FC, NFS, and iSCSI storage protocol types. |
    | VASA Provider | Select a VASA provider name.  The VASA Providers list is determined by the selected VASA protocol type. |
    | Storage Container | Select a storage container.  The Storage Containers list is determined by the selected VASA Provider. The list does not display storage containers that are already in use by other clusters. |
    | VASA User | Select a VASA user.  The VASA User list is determined by the selected VASA Provider. |
    | Datastore Name | Enter a datastore name.  The datastore name must contain 3-80 characters and cannot contain any leading or trailing whitespace. |
15. Select the ESX hosts to use for creating the workload domain and click Next. 

    The ESX hosts must be commissioned with the same storage type as the primary cluster of the workload domain. For example, select hosts commissioned for vSAN ESA storage for a vSAN ESA workload domain.
16. Enter the Distributed Switch details and click Next.

    Option | Description || Default | This profile is recommended. It provides a unified fabric for all traffic types using a single vSphere Distributed Switch. |
    | Storage Traffic Separation | This profile creates two vSphere Distributed Switches with separate physical NICs. One switch is dedicated for storage traffic, while the other is used for all other traffic. |
    | NSX Traffic Separation | This profile creates two vSphere Distributed Switches with separate physical NICs. One switch is dedicated for NSX (Virtual Networking) traffic, while the other is used for all other traffic. |
    | Storage Traffic and NSX Traffic Separation | This profile creates three vSphere Distributed Switches with separate physical NICs. One switch is dedicated for NSX (Virtual Networking) traffic, the second switch is dedicated for storage traffic, while the third is used for all other traffic. |
    | Custom Switch Configuration | Copy from a preconfigured profile or create a new distributed switch configuration. Multiple vSphere Distributed Switches can be configured. Each vSphere Distributed Switch can hold one or more network traffic configurations.  Some network traffic types are mandatory. Switch configuration is incomplete until these mandatory traffic types are configured.  Management, vMotion, vSAN and NSX network types can be configured only once for a cluster.  NSX and Public network traffic types can be configured in multiple vSphere Distributed Switches. |
17. Enter the vSphere Supervisor details and click Next.

    This screen is not displayed if you deactivated the Enable vSphere Supervisor toggle.

    For more information about vSphere Supervisor, click the Learn More link.

    Option | Description || Supervisor Name | Enter a Supervisor name. |
    | Service CIDR | Enter an IP range for Kubernetes cluster services. The range must not overlap with any Supervisor-routable networks. |
    | Use ESXi Management VMK settings | Select the check box to use the ESX Management VMK VLAN ID, subnet mask, gateway, and vSphere Distributed Switch for the management network. |
    | VLAN ID | Enter a VLAN ID for the management network.  This option does not appear if you selected Use ESXi Management VMK settings. |
    | Control Plane IP Range | Enter an IP range with minimum 5 addresses for control plane VMs and management traffic. |
    | Subnet Mask | Enter a network mask to define the IP range size.  This option does not appear if you selected Use ESXi Management VMK settings.  For example: 255.255.255.0 |
    | Gateway | Enter a gateway IP for external communication. This option does not appear if you selected Use ESXi Management VMK settings. |
    | VDS | Select a vSphere Distributed Switch for the management network. This option does not appear if you selected Use ESXi Management VMK settings. |
    | NSX Project | Select an NSX project for system and namespace VPC deployment. This option is not configurable if you are deploying a new NSX Manager instance. |
    | VPC Connectivity Profile | Select a profile for configuring VPC transit gateway connections. This option is not configurable if you are deploying a new NSX Manager instance. |
    | Private (Transit Gateway) CIDR | Enter an IP range for the private transit gateway. |
    | Private CIDR | Enter a non-overlapping IP range for private subnet allocation. |
    | Workload DNS | Enter DNS server addresses for all workload VMs. |
    | Workload NTP | Enter routable NTP server addresses for workload time synchronization. |
18. Review the information about the workload domain and click Finish.

    After successful validation, workload domain creation starts.
19. Click Fleet ManagementTasks to monitor progress.

If you enabled vSphere Supervisor, you must deploy an NSX Edge cluster with an active-standby tier-0 gateway to complete Supervisor activation, unless you are using an existing NSX Manager instance with a compatible NSX Edge cluster. See [Configure Centralized Network Connectivity with Edge Clusters](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-network-connectivity-in-vcenter/managing-centralized-network-connectivity-with-edge-clusters.html) for information about deploying an NSX Edge cluster.