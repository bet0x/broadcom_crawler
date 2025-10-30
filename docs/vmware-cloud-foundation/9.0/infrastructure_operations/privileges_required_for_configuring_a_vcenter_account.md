---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations/privileges-required-for-configuring-a-vcenter-adapter-instance.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Privileges Required for Configuring a vCenter Account
---

# Privileges Required for Configuring a vCenter Account

To configure your vCenter adapter instance in VCF Operations, you need sufficient privileges to monitor and collect data and to perform vCenter actions. You can configure these permissions as a single role in vCenter to be used by a single service account or configure them as two independent roles for two separate service accounts.

The vCenter account requires credentials with the following privileges configured in vCenter to be able to monitor and collect data and performs some actions in the vCenter instance.

The vCenter role is created with a Read Only role with three system-defined privileges: System.Anonymous, System.View, and System.Read. For more information, see [Using vCenter Roles to Assign Privileges](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vc_344&appid=vsphere-9-0&language=&format=rendered).

Privileges for Configuring a vCenter Adapter: Monitoring and Data Collection



| Task | Privilege |
| --- | --- |
| Property Collection | System > Anonymous This privilege is added automatically when you create a user account. However, this privilege is not visible in vSphere. |
| Objects Discovery  Events Collection | Storage views > View  Datastore > Browse datastore  System > View This privilege is added automatically when you create a user account. However, the System > View privilege is not visible in vSphere. |
| Performance Metrics Collection | Performance > Modify intervals  System > Read This privilege is added automatically when you create a user account. However, the System > Read privilege is not visible in vSphere. |
| Service Discovery | For credential-based service discovery Virtual machine > Guest operations > Guest operation alias modification Virtual machine > Guest operations > Guest operation alias query  Virtual machine > Guest operations > Guest operation modifications  Virtual machine > Guest operations > Guest operation program execution  Virtual machine > Guest operations > Guest operation queries |
| For credential-less service discovery Virtual machine > Service configuration > Manage service configurations Virtual machine > Service configuration > Modify service configuration  Virtual machine > Service configuration > Query service configurations  Virtual machine > Service configuration > Read service configuration |
| vSphere Client plug-in | Extension > Register extension  Extension > Unregister extension  Extension > Update extension |
| Orphaned Disk | Datastore > Browse datastore |
| Authentication on VCF Operations using vCenter User and apply actions | privilege.Global.com.vmware.label > vRealize Operations Read Only Role  privilege.Global.com.vmware.label > vRealize Operations Power User Role |
| Optimize Container  Schedule Optimize Container  Automate Optimize Container | - AutoDeploy -> Rule -> Create - AutoDeploy -> Rule -> Delete - AutoDeploy -> Rule -> Edit - AutoDeploy -> RuleSet -> Activate - AutoDeploy -> RuleSet -> Edit - Datastore -> Allocate space - Global -> Global tag - Global -> System tag - Host -> Inventory -> Manage Cluster Lifecyle - Host -> Inventory -> Modify cluster - Resource -> Assign virtual machine to resource pool - Resource -> Migrate powered off virtual machine - Resource -> Migrate powered on virtual machine - Resource -> Query vMotion - Storage views -> Configure service - Storage views -> View - Virtual machine -> Edit inventory > Move   Privilege required for vCenter version 7.x:  - Profile-driven storage -> Profile-driven storage update - Profile-driven storage -> Profile-driven storage view  Privilege required for vCenter version 8.x:  - VM storage policies -> Apply VM storage policies - VM storage policies -> Update VM storage policies - VM storage policies -> VM storage policies edit permissions - VM storage policies -> VM storage policies view permissions - VM storage policies -> View VM storage policies |
| Provide data to vSphere Predictive DRS | External stats provider > Update  External stats provider > Register  External stats provider > Unregister  vSphere Stats Privileges > Collect Stats Data  vSphere Stats Privileges > Modify Stats Configuration  vSphere Stats Privileges > Query Stats Data |
| Tag Collection | Global > Global tag  Global > Health  Global > Manage custom attributes This privilege is required only if the tags are associated with custom attributes.  Global > System tag  Global > Set custom attribute |
| Monitoring Health of vCenter Services using VMware Infrastructure Health | User must be part of the SystemConfiguration.Administrator group or have Administrator permission. |
| Add License to vCenter | Global > Licenses role and be a member of the LicenseService.Administrators Single Sign-On group. |
| Configuration Drift | Administrators Group  User must be part of the Administrators Group. |

Privileges for Configuring a vCenter Adapter: Performing vCenter Actions



| Actions | Privilege |
| --- | --- |
| vCenter Linking | Administer |
| VcTrusts/VcIdentity | Create/Update/Delete (Admins privileges)  Create/Update/Delete (below Admins privileges) |
| Set CPU Count for VM | Virtual machine > Configuration > Change CPU count |
| Set CPU Resources for VM  Set Memory Resources for VM | Virtual machine > Change Configuration > Change resource |
| Set Memory for VM | Virtual machine > Change Configuration > Change Memory |
| Delete Idle VM | Virtual machine > Edit Inventory > Remove |
| Delete Powered Off VM | Virtual machine > Edit Inventory > Remove |
| Create Snapshot for VM | Virtual machine > Snapshot management > Create snapshot |
| Delete Unused Snapshots for Datastore | Virtual machine > Snapshot management > Remove snapshot |
| Delete Unused Snapshot for VM | Virtual machine > Snapshot management > Remove snapshot |
| Execute Custom Script | Localization: Guest operations > Guest operation program execution  Virtual machine > Guest operations query  Localization: Guest operations -> Guest operation queries  - The ESX instance that hosts the VMs where the custom script should be run, must have HTTPS access to port 443 from the collector node on which the vCenter adapter instance is configured. - The user provided in the script must have read and write privileges to the temp directory (execute privilege is also required for this directory in Linux systems). For Windows systems, the path can be taken from the environment variable TEMP. For Linux systems, it is /tmp and/or /var/tmp. |
| Power Off VM | Virtual machine > Interaction > Power off |
| Power On VM | Virtual machine > Interaction > Power on |
| Shut Down Guest OS for VM | Virtual machine > Interaction > Power off |
| Move VM | - Resource > Assign virtual machine to resource pool - Resource > Migrate powered off virtual machine - Resource > Migrate powered on virtual machine - Datastore > Allocate space - Virtual machine -> Edit Inventory > Move   Combining these four permissions allows the service account to perform Storage vMotion and regular vMotion of an object therefore allowing VCF Operations to perform the given operations. |
| Set DRS Automation | Host > Inventory > Modify cluster |
| Provide data to vSphere Predictive DRS | External stats provider > Update  External stats provider > Register  External stats provider > Unregister |
| Reboot Guest OS for VM | Virtual machine > Interaction > Reset |

For more information about tasks and privileges, see [Defined Privileges](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_042&appid=vsphere-9-0&language=&format=rendered).