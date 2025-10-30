---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/logging-user-account-changes.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Logging User Account Changes
---

# Logging User Account Changes

Changes to a user's role assignment
are automatically written to syslog and the audit log.

For more information about syslog and the
audit log, see [Log Messages and Error Codes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/log-messages-and-error-codes.html#GUID-df9e6850-3d60-4e76-8249-c80181dad07b-en).

An example of a log message when assigning a
role to a vIDM user:

```
2020-09-24T16:05:51.244Z nsxmanager-14663974-1-CertKB-FS NSX 5519 - [nsx@6876 audit="true" comp="nsx-manager" entId="e3c2af75-9d0f-4020-90cc-f2f00d6af255" level="INFO" reqId="b27711c6-0590-4b39-b8b6-f0980a0597f0" subcomp="policy" update="true" username="admin"] UserName="admin", ModuleName="AAA", Operation="CreateRoleBinding", Operation status="success", New value=[{"name":"[email protected]","type":"remote_user","identity_source_type":"VIDM","roles":[{"role":"auditor"}],"id":"bba634c9-cfbd-4806-a831-e63ec195e1f9","_protection":"UNKNOWN"}]
```

An example of a log message when updating the
role of a vIDM user:

```
2020-09-24T16:12:51.217Z nsxmanager-14663974-1-CertKB-FS NSX 5519 - [nsx@6876 audit="true" comp="nsx-manager" entId="e3c2af75-9d0f-4020-90cc-f2f00d6af255" level="INFO" reqId="973faed4-f4b5-443d-bd79-7d995c027183" subcomp="policy" update="true" username="admin"] UserName="admin", ModuleName="AAA", Operation="UpdateRoleBinding", Operation status="success", New value=["e3c2af75-9d0f-4020-90cc-f2f00d6af255" {"name":"[email protected]","type":"remote_user","identity_source_type":"VIDM","roles":[{"role":"security_admin"}],"_protection":"UNKNOWN"}]
```

An example of a log message when assigning a
role to an LDAP user:

```
2020-09-24T16:06:28.663Z nsxmanager-14663974-1-CertKB-FS NSX 5519 - [nsx@6876 audit="true" comp="nsx-manager" entId="35e45569-6da6-4dcd-b4a1-75747cdd6cf8" level="INFO" reqId="db27f4ae-25a7-4482-b3f4-49228d12960b" subcomp="policy" update="true" username="admin"] UserName="admin", ModuleName="AAA", Operation="CreateRoleBinding", Operation status="success", New value=[{"name":"[email protected]","type":"remote_user","identity_source_type":"LDAP","identity_source_id":"ldap","roles":[{"role":"auditor"}],"id":"dd8d3675-c574-454b-975e-300b65462827","_protection":"UNKNOWN"}]
```

An example of a log message when updating the
role of an LDAP user:

```
2020-09-24T16:12:37.449Z nsxmanager-14663974-1-CertKB-FS NSX 5519 - [nsx@6876 audit="true" comp="nsx-manager" entId="35e45569-6da6-4dcd-b4a1-75747cdd6cf8" level="INFO" reqId="d7cdd3de-75a1-4d29-9fea-27e1dda4b5e2" subcomp="policy" update="true" username="admin"] UserName="admin", ModuleName="AAA", Operation="UpdateRoleBinding", Operation status="success", New value=["35e45569-6da6-4dcd-b4a1-75747cdd6cf8" {"name":"[email protected]","type":"remote_user","identity_source_type":"LDAP","identity_source_id":"ldap","roles":[{"role":"network_admin"}],"_protection":"UNKNOWN"}]
```