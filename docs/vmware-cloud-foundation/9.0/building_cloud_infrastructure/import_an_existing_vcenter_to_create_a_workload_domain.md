---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/import-an-existing-vcenter-to-create-a-workload-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Import an Existing vCenter to Create a Workload Domain
---

# Import an Existing vCenter to Create a Workload Domain

If you have an existing vCenter instance, with or without NSX Manager, you can use VCF Operations to import it to a VCF instance as a workload domain. If NSX Manager is not present, you deploy a new instance during the import procedure.

Verify that your existing vSphere infrastructure satisfies the requirements and supported configurations listed below.

All vSphere clusters in the existing vCenter are imported as part of this process. You cannot select a subset of clusters.

**Minimum Component Versions**

- VCF 9.0.x instance from which to perform the import
- vCenter 8.0 Update 1 or later
- ESX 8.0 Update 1 or later
- NSX Manager 4.1.0.2 or later

The following table lists supported and not supported configurations for importing your existing infrastructure to a workload domain.

Supported Configurations



| Category | Supported | Not Supported |
| --- | --- | --- |
| Storage | - Enough free space for the full deployment of VMware Cloud Foundation, according to the Planning and Preparation Workbook - Datastore shared across all hosts in the cluster, accessible from all hosts in the cluster, and writable by all hosts in the cluster - Any supported vSphere storage type.  If the default cluster includes multiple datastore types, VCF determines the primary datastore using the following priority:   1. vSAN   2. NFS v3   3. VMFS   4. NFS 4.1   5. iSCSI   6. vVols\* If you are using a JSON specification file to converge, you can use the existingDatastoreName property to override the priority order and use a specific datastore.  - vSAN Stretched Clusters (ESA, OSA, or ESA storage clusters) with at least 3 ESX hosts in each availability zone and a witness host deployed in a vSAN witness zone that is different from the availability zones - Two-node vSAN clusters for remote offices/branch offices (ROBO) with two ESX hosts and one witness host for VCF simple deployments   For two-node vSAN clusters, the admission control policy should be configured to >= 50% for both memory and CPU.   - vSAN OSA clusters, where deduplication and compression are either both activated or both deactivated - vSAN OSA clusters with activated compression only |  |
| Network | - Virtual Distributed Switch (VDS) 8.0 or later You can move to a vSphere Distributed Switch. See [Migrating from Standard to Distributed vSwitch](https://techdocs.broadcom.com/us/en/vmware-cis/vsan/vsan/8-0/vsan-network-design/migrating-from-standard-to-distributed-vswitch.html). - Ports aligned with [VMware Ports and Protocols](https://ports.broadcom.com/) - Multiple VMkernel interfaces for vMotion traffic - vCenter instance with temporary IP address - Statically assigned VMkernel IP addresses - Dedicated network for VMware vMotion - vSphere Distributed Switches (VDS) with enabled link aggregation control protocol (LACP) - ESX hosts with a combination of standard switches and VDS - ESX hosts with multiple physical uplinks of minimum of 10Gbps, that are assigned to a vSphere Distributed Switch - ESX hosts with a single pNIC with a minimum of 10 Gbps speed, that is connected to a standard switch - Clusters using shared vSphere Distributed Switches - NSX Manager instance that is shared across multiple vCenter instances without ELM If no NSX Manager instance is connected to the vCenter environment, during the import operation, a cluster of 3x NSX Managers is deployed. - NSX Manager instance that is on the same network segment as the imported vCenter appliance without ELM - Starting with VCF 9.0.1, vCenter instances without ELM and with existing NSX Local Managers that are part of an NSX Federation configuration - ESX hosts with a single Physical Network Adapter (pNIC) - DNS server with forward and reverse DNS records   - DNS erver must be configured for all management domain components   - All FQDNs used for the different components must be resolvable to an unique IP | - Cisco virtual switches - vCenter instances without a vSphere Distributed Switch - Custom vCenter ports for client connections - Environments using ports not aligned with [VMware Ports and Protocols](https://ports.broadcom.com/) - Dynamically allocated VMkernel IP addresses You can move to statically assigned IP addresses. See [Edit a VMkernel Adapter Configuration](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-networking-8-0/setting-up-vmkernel-networking/edit-vmkernel-networking-on-a-vsphere-standard-switch-in-the-vsphere-web-client.html). - Shared networks for VMware vMotion - Multiple NSX Manager instances in a vCenter instance - NSX Bare Metal Edge nodes |
| Compute | - Virtual machine of vCenter instance hosted on one of the clusters that is managed by the same instance You can move the virtual machine to a supported location by using VMware vMotion. See [Migrating Virtual Machines Between vCenter Systems](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/migrating-virtual-machines-host-management/vmotion-across-vcenter-server-systems-host-management.html). - Virtual machine of vCenter instance hosted on the default cluster in the management domain - Clusters using vSphere Configuration Profiles - Clusters using vSphere Lifecycle Manager images You can convert clusters that use baselines to use images before upgrading to ESX 9.0. See [Convert a Cluster or a Host That Uses Baselines Into a Cluster or a Host That Uses vSphere Lifecycle Manager Images](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/managing-host-and-cluster-lifecycle-8-0/using-images-to-install-and-update-esxi-hosts-and-clusters/switching-from-baselines-to-images.html#GUID-B54663AB-B1D1-4E87-8B8C-76FF2998A477-en). - Clusters using fully automated Dynamic Resource Scheduler (DRS) - Standalone ESX hosts and single ESX host clusters, if your vCenter instance has an additional cluster that meets the cluster requirements You can manually perform the lifecycle management of the standalone ESX hosts and single ESX host clusters by using the vSphere Client.  - Clusters using fully automated Dynamic Resource Scheduler (DRS) | - Clusters managed by Dell VxRail - vCenter instances with ELM If your vCenter instance does not have existing NSX registrations, you can manually upgrade your vCenter instances to version 9.0.x and then break ELM for all vCenter instances. See [Deactivate Enhanced Link Mode from vCenter Using the cmsso-util break-elm Utililty](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/points-to-consider-while-setting-up-vmware-cloud-foundation-sso/how-to-deactivate-enhanced-link-mode-in-vcenter-without-downtime.html). - Clusters using baselines for lifecycle management - Clusters using manual or partially automated Dynamic Resource Scheduler (DRS) You can set the automation level to fully automated. See [Edit Cluster Settings](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-resource-management-8-0/creating-a-drs-cluster.html#GUID-755AB944-F3D0-43DD-82CD-8CDDDF8674E8-en). - Password Management of imported ESX hosts via the Password Management Console of VCF Operations. - Adding hosts to imported clusters without the use of the vSphere Client - Partial import of clusters   - All clusters managed by a vCenter instance are imported together - Clusters that use vCenter High Availability (VCHA) |

\* vSphere Virtual Volumes (vVols) framework is deprecated in version 9 and using it is not recommended.

1. In VCF Operations, select InventoryDetailed View.
2. Expand VCF Instances and browse to the VCF Instance into which you want to import a workload domain.
3. Click Add Workload DomainImport a vCenter.
4. Enter a workload domain name and click Next.
5. Select a vCenter and optionally an NSX Manager instance to import as a workload domain and click Next.

   | Option | Description |
   | --- | --- |
   | Select an existing standalone vCenter from the inventory | Select an existing vCenter from the table.  If the vCenter is connected to an NSX Manager instance, activate the toggle and enter the following details: - NSX Manager VIP FQDN - NSX Administrator Password - NSX Root Password - NSX Audit Password  If your existing NSX Manager instance is version 9.0 or higher and has one or more Edge clusters, the import process adds the discovered Edge node VMs to the VCF inventory, including their user credentials. During the import process, the Edge node credential passwords will be reset. You can retrieve the updated passwords from the VCF credential store.  Select the Enable Edge cluster sync and import NSX Edge node VMs check box to perform the password reset operation for all the nodes in the existing Edge cluster, as well as for any nodes added later. |
   | Specify an external vCenter | Enter the following details for the external vCenter: - vCenter server FQDN - vCenter Server Root Password - SSO user name - SSO user password If the vCenter is connected to an NSX Manager instance, activate the toggle and enter the following details: - NSX Manager VIP FQDN - NSX Administrator Password - NSX Root Password - NSX Audit Password  If your existing NSX Manager instance is version 9.0 or higher and has one or more Edge clusters, the import process adds the discovered Edge node VMs to the VCF inventory, including their user credentials. During the import process, the Edge node credential passwords will be reset. You can retrieve the updated passwords from the VCF credential store.  Select the Enable Edge cluster sync and import NSX Edge node VMs check box to perform the password reset operation for all the nodes in the existing Edge cluster, as well as for any nodes added later. |
6. Confirm the certificate thumbprints and click Next.

   This includes vCenter, NSX Manager (if you are using an existing instance), and additional thumbprints.
7. Run the prechecks and resolve any issues.
8. If you are not importing an NSX Manager instance that is connected to your vCenter, enter the NSX Manager instance details and click Next.

   Choose whether to create a new NSX Manager instance or join an existing NSX Manager instance. If you already have an NSX Manager instance for a different workload domain, you can reuse that NSX Manager instance or create a new one.

   You cannot join the existing NSX Manager instance for an imported or newly deployed management domain.

   If you are using an existing NSX Manager instance, select it. If you are creating a new NSX Manager instance, enter the following information.

   | Option | Description |
   | --- | --- |
   | Deployment Size | - Standard: Deploys single-node NSX Manager requiring fewer resources. You can choose a standard deployment size only when importing a vCenter 9.0 and later instance. - High-Availability (recommended): Deploys a three-node NSX Manager cluster to enhance the availability of management and control plane functions, as well as minimize downtime during upgrades. |
   | Appliance Size | - Medium - Large - Extra Large |
   | Appliance 1 FQDN | Enter the FQDN for the first NSX Manager node. |
   | Appliance 2 FQDN | Enter the FQDN for the second NSX Manager node. |
   | Appliance 3 FQDN | Enter the FQDN for the third NSX Manager node.  This is not applicable if you chose Standard deployment size. |
   | Appliance Cluster FQDN | Enter the NSX Manager cluster FQDN. |
   | Administrator Password | Enter and confirm an NSX administrator password and enable auto-generated passwords.  Requirements: - At least five different characters. - At least one lowercase character. - At least one digit. - No more than four monotonic or sequential characters. - At least 12 characters. - Cannot be palindrome. - At least one special character. - At least one uppercase character. - No dictionary words. |
   | Auditor Password | Enter and confirm an NSX administrator password or enable auto-generated passwords.  Requirements: - At least five different characters. - At least one lowercase character. - At least one digit. - No more than four monotonic or sequential characters. - At least 12 characters. - Cannot be palindrome. - At least one special character. - At least one uppercase character. - No dictionary words. |
   | NSX overlay networking | Choose whether or not to use the ESX management VMkernel for NSX overlay networking. |
9. Run the validations and prechecks and click Next. 

   Resolve any issues before proceeding.
10. Review your settings and click Finish.