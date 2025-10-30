---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/role-based-access-control.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Role-Based Access Control
---

# Role-Based Access Control

With role-based access control (RBAC), you can restrict system access to authorized users. Users are assigned roles and each role has specific permissions.

To view the built-in and custom roles and their associated permissions, navigate to SystemUser ManagementRoles and expand the row to view details. You can view permissions of all categories by expanding the role's permissions details.

After you have assigned an Active Directory (AD) user a role, if the username is changed on the AD server, you need to assign the role again using the new username.

For Security Intelligence RBAC information, see the Using and Managing Security Intelligence documentation.

## Roles and Permissions

There are four types of permissions. Included in the list are the abbreviations for the permissions that are used in the Roles and Permissions table.

- Full access (FA) - All permissions including Create, Read, Update, and Delete (CRUD)
- Execute (E) - Includes Read and Update
- Read (R)
- None (N)

NSX
 has the following built-in roles. Role names in the UI can be different in the API.In NSX, if you have permission, you can clone an existing role, add a new role, edit newly created roles, or delete newly created roles.

The following table shows the permissions that each built-in role has for different operations. Also included in the list are the abbreviations for the roles that are used.

- Auditor (A)
- Cloud Admin (CA)(Available in the Cloud environment only)
- Cloud Operator (CO) (Available in the Cloud environment only)
- Cloud Partner Admin (CPA)
- Enterprise Admin (EA)
- GI (Guest Introspection ) Partner Administrator (GIPA)
- LB (Load Balancer) Admin (LBA)
- LB Operator (LBO)
- Network Admin (NA)
- Network Operator (NO)
- NETX (Network Introspection) Partner Administrator (NXPA)
- Project Admin (PA) (Refer to note)
- Security Admin (SA)
- Security Operator (SO)
- Support Bundle Collector (SBC)
- VPN Admin (VPNA)

The Roles and Permissions tables do not include the Project Admin role. The Project Admin role has full access to all configurations in a project. The Network Admin, Network Operator, Security Admin, and Security Operator roles in a project have RBAC permissions only within the scope of the project, and not for the entire NSX system.

Roles and Permissions



| Operation | EA | A | NA | NO | SA | SO | CA | CO | CPA | LBA | LBO | VPNA | GIPA | NXPA | SBC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Networking > Tier-0 Gateways | FA | R | FA | R | R | R | FA | R | R | R | R | R | R | R | N |
| Networking > Tier-1 Gateways | FA | R | FA | R | R | R | FA | R | FA | R | R | R | R | R | N |
| Networking > Network Interface | FA | R | FA | R | R | R | FA | R | FA | R | R | R | R | R | N |
| Networking > Network Static Routes | FA | R | FA | R | R | R | FA | R | FA | R | R | R | R | R | N |
| Networking > Locale Services | FA | R | FA | R | R | R | FA | R | FA | R | R | R | R | R | N |
| Networking > Segments | FA | R | FA | R | R | R | FA | R | FA | R | R | R | R | R | N |
| Networking > Segments > Segment Profiles | FA | R | FA | R | R | R | FA | R | FA | R | R | R | R | R | N |
| Networking > IP Address Pools | FA | R | FA | R | R | R | FA | R | FA | R | R | N | N | N | N |
| Networking Forwarding Policies | FA | R | FA | R | FA | R | FA | R | R | N | N | N | N | N | N |
| Networking > DNS | FA | R | FA | FA | R | R | FA | R | FA | R | R | N | N | N | N |
| Networking > DHCP | FA | R | FA | R | R | R | FA | R | FA | R | R | N | N | N | N |
| Networking > Load Balancing | FA | R | N | N | R | N | FA | R | FA | FA | R | N | N | N | N |
| Networking > NAT | FA | R | FA | R | FA | R | FA | R | FA | R | R | N | N | N | N |
| Networking > VPN | FA | R | FA | R | FA | R | FA | R | FA | N | N | FA | N | N | N |
| Networking > IPv6 Profiles | FA | R | FA | R | R | R | FA | R | FA | R | R | N | N | N | N |
| Security > Distributed Firewall | FA | R | R | R | FA | R | FA | R | FA | R | R | R | R | R | N |
| Security > Gateway Firewall | FA | R | R | R | FA | R | FA | R | FA | N | N | N | N | FA | N |
| Security > Identity Firewall AD | FA | R | FA | R | FA | FA | FA | R | FA | R | R | R | R | R | N |
| Security > Network Introspection | FA | R | R | R | FA | R | FA | R | N | N | N | N | N | FA | N |
| Security > Endpoint Protection Rules | FA | R | R | R | FA | R | FA | R | R | N | N | N | FA | N | N |
| Inventory > Context Profiles | FA | R | R | R | FA | R | R | R | FA | R | R | R | R | R | N |
| Inventory > Virtual Machines | R | R | R | R | R | R | R | R | FA | R | R | R | R | R | N |
| Inventory > Virtual Machines > Create & Assign Tags to VM | FA | R | R | R | FA | R | FA | R | FA | R | R | R | FA | FA | N |
| Inventory > Containers | FA | R | R | R | R | R | N | N | R | N | N | N | N | N | N |
| Inventory > Physical Servers | FA | R | R | R | R | R | R | R | R | R | R | N | N | N | N |
| Plan & Troubleshoot > Port Mirroring | FA | R | FA | R | R | R | FA | R | FA | N | N | N | N | N | N |
| Plan & Troubleshoot > Port Mirroring Binding | FA | R | FA | FA | R | R | FA | R | FA | R | R | R | R | R | N |
| Plan & Troubleshoot > Monitoring Profile Binding | FA | R | FA | FA | R | R | FA | R | FA | R | R | R | R | R | N |
| Plan & Troubleshoot > IPFIX > Firewall IPFIX Profiles | FA | R | FA | R | FA | R | FA | R | FA | R | R | R | R | R | N |
| Plan & Troubleshoot > IPFIX > Switch IPFIX Profiles | FA | R | FA | R | R | R | FA | R | FA | R | R | R | R | R | N |
| Plan & Troubleshoot > Collectors | FA | R | FA | R | R | R | FA | R | FA | R | R | R | R | R | N |
| Plan & Troubleshoot > Traceflow | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | N | N | N | N |
| System > Fabric > Hosts > Clusters | FA | R | R | R | R | R | R | R | R | R | R | N | N | N | R |
| System > Fabric > Hosts > Other Nodes | FA | R | R | R | R | R | R | R | R | R | R | N | N | N | R |
| System > Fabric > Hosts > Standalone | FA | R | R | R | R | R | R | R | R | R | R | N | N | N | R |
| System > Fabric > Hosts > Transport Node Profile | FA | R | R | R | R | R | R | R | R | R | R | N | N | N | R |
| System > Fabric > Hosts | FA | R | R | R | R | R | R | R | R | N | N | N | N | N | N |
| System > Fabric > Nodes | FA | R | FA | R | FA | R | R | R | R | R | R | N | N | N | N |
| System > Fabric > Nodes > Edge Transport Nodes | FA | R | R | R | R | R | R | R | R | N | N | N | N | N | N |
| System > Fabric > Nodes > Edge Clusters | FA | R | FA | R | R | R | R | R | R | N | N | N | N | N | N |
| System > Fabric > Nodes > Container Clusters | FA | R | FA | R | R | R | N | N | R | R | R | N | N | N | N |
| System > Fabric > Nodes > Tunnels | R | R | R | R | R | R | R | R | R | R | R | N | N | N | N |
| System > Fabric > Profiles > Uplink Profiles | FA | R | R | R | R | R | R | R | R | R | R | N | N | N | N |
| System > Fabric > Profiles > Edge Cluster Profiles | FA | R | FA | R | R | R | R | R | R | R | R | N | N | N | N |
| System > Fabric > Profiles > Configuration | FA | R | N | N | N | N | R | R | R | N | N | N | N | N | N |
| System > Fabric > Profiles > Node Profiles | FA | R | R | R | R | R | R | R | R | R | R | N | N | N | N |
| System > Fabric > Transport Zones > Add Zones | FA | R | R | R | R | R | R | R | R | R | R | N | N | N | N |
| System > Fabric > Transport Zones > Health Configuration | FA | R | R | R | R | R | R | R | R | R | R | N | N | N | N |
| System > Fabric > Compute Managers | FA | R | R | R | R | R | R | R | R | N | N | N | R | R | N |
| System > Fabric > Settings | FA | N | N | N | N | N | N | N | R | N | N | N | N | N | N |
| System > Certificates | FA | R | N | N | FA | R | N | N | FA | FA | R | FA | N | N | N |
| System > Service Deployments > Service Instances | FA | R | R | R | FA | R | FA | R | R | N | N | N | FA | FA | N |
| System > Support Bundle | FA | N | N | N | N | N | N | N | N | N | N | N | N | N | FA |
| System > Backup | FA | R | N | N | N | N | N | N | R | N | N | N | N | N | N |
| System > Restore | FA | R | N | N | N | N | N | N | R | N | N | N | N | N | N |
| System > Upgrade | FA | R | R | R | R | R | N | N | R | N | N | N | N | N | N |
| System > Migrate | FA | N | N | N | N | N | N | N | R | N | N | N | N | N | FA |
| System > User Mgt > User Role Assignments | FA | R | N | N | N | N | FA | R | FA | N | N | N | N | N | N |
| System > Local Users | FA | R | N | N | N | N | N | N | R | N | N | N | N | N | N |
| System > Roles | FA | R | FA | R | FA | FA | FA | R | FA | R | R | R | R | R | N |
| System > Authentication Providers | FA | R | FA | R | FA | FA | R | R | FA | R | R | R | R | R | N |
| System > Licenses | FA | R | R | R | R | R | N | N | N | N | N | N | N | N | N |
| System > System Administration | FA | R | R | R | R | R | R | R | R | N | N | N | N | N | N |
| Custom Dashboard Configuration | FA | R | R | R | R | R | FA | R | R | R | R | R | R | R | N |