---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/working-with-site-recovery-manager-and-federation.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Working with Site Recovery Manager and NSX Federation
---

# Working with Site Recovery Manager and NSX Federation

You can use VMware Live Site Recovery™ with NSX Federation for disaster recovery use cases.

Site Recovery Manager supports the following workflows with NSX Federation:

- NSX Federation Global Manager (GM) VMs support full and test recovery of GM VMs (supported with or without NSX Federation management cluster VIP).
- Compute VMs support full and test recovery of compute VMs. Recovered VMs in the disaster recovery site have their NSX tags and firewall rules based on these NSX tags or not such as IP addresses and VM names.

To ensure that groups and firewall rules replicate at the disaster recovery location during recovery, the NSXLocal Manager managing the disaster recovery location must have the NSX tags present at recovery time.

In NSX Federation, two fields support storage array replication: replication \_type and tag\_delay\_delete\_time. If you use storage array replication from your primary site to your recovery site in SRM, then create or update the tag replication policy replication type as STORAGE\_ARRAY\_REPLICATION.

Running a protection plan on SRM to migrate virtual machines using disaster recovery or planned migration options from your primary site to your recovery site will move the virtual machines to the recovery site and delete the virtual machines from primary site. When the concerned virtual machines are deleted from primary site and appear on recovery site within the tag\_delay\_delete\_time setting, then tags from primary site get replicated on the virtual machines on recovery site. For storage array replication, the time for VMs to appear on the recovery site after they are deleted from the primary site depends on the VM count configured to failover, storage array performance, and ESX host.

If vSphere replication is being used to replicate VMs from primary site to recovery site in SRM, then the virtual machine is not deleted from primary site. Therefore, there is no need to specify replication\_type or tag\_delay\_delete\_time in the tag replication policy.

For Global Manager, if replication types VSPHERE\_REPLICATION or OTHER options are used, then the tag\_delay\_time value gets set to 0. The replication\_type is set to default value of enum (invalid) and the tag\_delay\_delete\_time is set to 0 minutes.

Configure VM Tag Replication across LMs using GM API

In NSX Federation, to configure VM tag replication across Local Managers, run the following Global Manager API:

```
PUT https://{{gm}}/global-manager/api/v1/global-infra/vm-tag-replication-policies/policy1
{
   "display_name":"vm tag replication policy Paris to London",
   "description":"vm tag replication policy1",
   "protected_site": "/global-infra/sites/LM_Paris",
   "replication_type": "STORAGE_ARRAY_REPLICATION",
   "tag_delay_delete_time": 30,
   "recovery_sites": [
       "/global-infra/sites/LM_London"
   ],
   "groups":[
       "/global-infra/domains/default/groups/Web-VM-Group",
       "/global-infra/domains/default/groups/DB-VM-Group"
   ],
   "vm_match_criteria": "MATCH_BIOS_UUID_NAME"
```

For NSX Federation, to configure VM tag replication across Local Managers, run the following Global Manager API:

```
PUT https://{{gm}}/global-manager/api/v1/global-infra/vm-tag-replication-policies/policy1
{
   "display_name":"vm tag replication policy Paris to London",
   "description":"vm tag replication policy1",
   "protected_site": "/global-infra/sites/LM_Paris",
   "recovery_sites": [
       "/global-infra/sites/LM_London"
   ],
   "groups":[
       "/global-infra/domains/default/groups/Web-VM-Group",
       "/global-infra/domains/default/groups/DB-VM-Group"
   ],
   "vm_match_criteria": "MATCH_BIOS_UUID_NAME"
```

LM\_Paris sends the tag information of the VMs for the BIOS UUID of the VMs in the groups Web-VM-Group + DB-VM-Group to LM\_London. Before the recovery of the London VMs by SRM, LM\_London does not have the VMs with the BIOS UUID and the VMs are not visible in LM\_London yet. However, when SRM recovers the VMs in London, LM\_London sees those VMs with the BIOS UUID and applies their NSX tags on them. The VMs get their security based on NSX tags.

vm\_match\_criteria has two possible values MATCH\_BIOS\_UUID\_NAME or MATCH\_NSX\_ATTACHMENT\_ID. At the recovery, SRM copies both so any configuration is valid with SRM. However, if another product completes VM replication and copies one, but not the other value, then configure GM with the appropriate vm\_match\_criteria value.

To estimate how much time it might take for the VM to disappear from the primary site and appear on the protected site, you can perform a test on the protection plan and measure the time interval between the end of the Synchronize storage and completion of the Power on priority X VMs steps. Set your tag\_delay\_delete\_time to be more than this estimated time. Another tip is to run the protection plan in VMware Live Site Recovery and set the tag\_delay\_delete\_time to always be more than time it takes between the step Shut Down VMs at the protected site and to complete the step to Power on priority X VMs while doing run on protection plan in SRM.

Check VM Tag Replication across LMs using GM API

To get details on VM tag replication across Local Managers run the following Global Manager API :

```
GET https://{{gm}}/global-manager/api/v1/global-infra/vm-tag-replication-policies
```

The output returns something similar to:

```
{
 "protected_site": "/global-infra/sites/LM_Paris",
 "recovery_sites": [
   "/global-infra/sites/LM_London"
 ],
 "vm_match_criteria": "MATCH_BIOS_UUID_NAME",
 "groups": [
   "/global-infra/domains/default/groups/Web-VM-Group",
   "/global-infra/domains/default/groups/DB-VM-Group"
 ],
 "resource_type": "VMTagReplicationPolicy",
 "id": "policy1",
 "display_name": "vm tag replication policy Paris to London",
 "description": "vm tag replication policy1",
 "path": "/global-infra/vm-tag-replication-policies/policy1",
 "relative_path": "policy1",
 "parent_path": "/global-infra",
 "unique_id": "9ee18586-5480-41d9-8223-690c9226d763",
 "marked_for_delete": false,
 "overridden": false,
 "_create_time": 1638413861377,
 "_create_user": "admin",
 "_last_modified_time": 1638413861377,
 "_last_modified_user": "admin",
 "_system_owned": false,
 "_protection": "NOT_PROTECTED",
 "_revision": 0
}
```

NSX supports only one entry from recovery sites. For details, see the vm-tag-replication-policies/policy-name API in the NSX Global Manager REST API Guide.