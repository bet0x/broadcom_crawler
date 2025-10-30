---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/add-role-assignment-or-principal-identity.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Role Assignment or Principal Identity
---

# Add a Role Assignment or Principal Identity

You can assign roles to users or user
groups if VMware Workspace ONE Access is integrated with NSX, or if you have LDAP as an authentication provider. You can also
assign roles to principal identities.

You must have an authentication provider configured:

- For role assignment for vIDM, verify that a vIDM
  host is associated with NSX. For more information, see [Configure VMware Workspace ONE Access Integration](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-vmware-identity-manager-workspace-one-access/configure-vmware-identity-manager-workspace-one-access-integration.html#GUID-ac2fe6da-466d-4b01-bae8-a79944a07e97-en).
- For role assignment for LDAP, verify that you
  have an LDAP identity source. For more information, see [LDAP Identity Source](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-ldap/ldap-identity-source.html#GUID-e2f67c13-e910-459b-b439-2e3912f60f26-en).

A principal is a component or a third-party application
such as an OpenStack product. With a principal identity, a principal can use the
identity name to create an object and ensure that only an entity with the same
identity name can modify or delete the object. A principal identity has the
following properties:

- Name
- Node ID - this can be any
  alphanumeric value assigned to a principal identity
- Certificate
- RBAC role indicating the access
  rights of this principal

Users (local, remote, or
principal identity) with the Enterprise Administrator role can modify or delete
objects owned by principal identities. Users (local, remote, or principal
identity) without the Enterprise Administrator role cannot modify or delete
protected objects owned by principal identities, but can modify or delete
unprotected objects.

If a principal identity user's certificate expires, you
must import a new certificate and make an API call to update the principal identity
user's certificate (see the procedure below). For more information about the
NSX API, a link to
the API resource is available at <https://code.vmware.com>.

A principal identity user's certificate
must satisfy the following requirements:

- SHA256 based.
- RSA/DSA message algorithm with
  2048 bits or above key size.
- It cannot be a root certificate.

You can delete a principal identity using the API.
However, deleting a principal identity does not automatically delete the
corresponding certificate. You must delete the certificate manually.

Steps to delete a principal identity and
its certificate:

1. Get the details of the
   principal identity to delete and note the
   certificate\_id value in the response.

   GET
   /api/v1/trust-management/principal-identities/<principal-identity-id>
2. Delete the principal
   identity.

   DELETE
   /api/v1/trust-management/principal-identities/<principal-identity-id>
3. Delete the certificate using
   the certificate\_id value obtained in step 1.

   DELETE
   /api/v1/trust-management/certificates/<certificate\_id>

For LDAP, you configure user groups to user roles mapping information; the groups correspond
to the user groups specified in the Active Directory (AD). To grant user permissions
on NSX, add that user to
the mapped group in AD. Starting in NSX 4.2, a single LDAP identity source can add up to 20 groups
to NSX. An error will
result if more than 20 groups are attempted.

1. With admin privileges, log in
   to NSX Manager.
2. Select SystemUser
   Management.
3. To assign roles to users, select
   AddRole Assignment
   for vIDM. 
   1. Select a user or user group.
   2. Select a role.
   3. Click Save.
4. To add a principal
   identity, select
   AddPrincipal Identity with
   Role.
   1. Enter a name for the
      principal identity.
   2. Select a role.
   3. Enter a node ID.
   4. Enter a certificate
      in PEM format.
   5. Click
      Save.
5. To add a role assignment for
   LDAP select Add Role Assignment for LDAP.
   1. Select a domain.
   2. Enter the first few
      characters of the user's name, login ID, or a group name to search the
      LDAP directory, then select a user or group from the list that
      appears.
   3. Select a role.
   4. Click
      Save.
6. If the certificate for the principal
   identity expires, perform the following steps. Do not use this procedure to
   replace Local Manager or
   Global Manager principal
   identity certificates. Instead, to replace those certificates refer to [Replace NSX Certificates Using API](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/replace-certificates-through-api.html) for
   details.
   1. Import a new certificate and
      note the certificate's ID. See [Import a Self-signed or CA-signed Certificate for NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/importing-certificates/import-a-certificate.html#GUID-7c651d93-4af8-45f8-a5a4-0ce67739291c-en).
   2. Call the following API to get
      the ID of the principal identity. 

      GET
      https://<nsx-mgr>/api/v1/trust-management/principal-identities
   3. Call the following API to
      update the principal identity's certificate. You must provide the
      imported certificate's ID and the principal identity user's ID. 

      For example,

      ```
      POST https://<nsx-mgr>/api/v1/trust-management/principal-identities?action=update_certificate
      {
          "principal_identity_id": "ebd3032d-728e-44d4-9914-d4f81c9972cb",
          "certificate_id" : "abd3032d-728e-44d4-9914-d4f81c9972cc"
      }
      ```