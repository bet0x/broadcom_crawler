---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-manager/security-of-nsx-manager.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Security of NSX Manager
---

# Security of NSX Manager

NSX Manager is a restricted system and has features designed to ensure the integrity of the system and to keep the system secure.

Details of the NSX Manager security features:

- NSX Manager supports session timeouts and user logoff. NSX Manager does not support session lock. To initiate a session lock use the workstation operating system being used to access NSX Manager.
- NSX Manager has one active local account out of the box, admin. You cannot delete or deactivate the admin account.
- There are three default inactive local user accounts: audit and two guest user accounts. In the Enterprise environment, the guestuser1 and the guestuser2 user accounts are available. You can delete, activate, or deactivate them. Starting in NSX 4.1, the admin in the Enterprise environment, as well as any user with the Enterprise Admin role, can add up to 10 more guest user accounts in addition to admin, audit, and two guest users.
- NSX Manager enforces approved authorizations for controlling the flow of management information within the network device based on information flow control policies.
- NSX Manager initiates session auditing upon startup.
- NSX Manager uses its internal system clock to generate time stamps for audit records.
- The NSX Manager user interface includes a user account, which has access rights to all resources, but does not have rights to the operating system to install software and hardware. NSX upgrade files are the only files allowed for installation. You cannot edit the rights of or delete this user.
- All passwords in the system (databases, configuration files, log files, and so on) get encrypted using a strong one-way hashing algorithm with a salt. During authentication, when the user enters the password it gets obfuscated. You can configure the password complexity using the UI, API and CLI. You can reset the node the authentication policy and the password complexity configuration back to their default system settings, if desired.
- FIPS compliance

  - NSX Manager uses FIPS 140 approved algorithms for authentication to a cryptographic module.
  - NSX Manager generates unique session identifiers using a FIPS 140 approved random number generator.
  - NSX Manager uses a FIPS 140 approved cryptographic algorithm to protect the confidentiality of remote maintenance and diagnostic sessions.
  - NSX Manager authenticates SNMP messages using a FIPS-validated Keyed-Hash Message Authentication Code (HMAC).
- NSX Manager recognizes only system-generated session identifiers and invalidates session identifiers upon administrator logout or other session termination.
- An audit log gets generated for events such as logon, logoff, and access to resources. Each audit log contains the timestamp, source, result, and a description of the event. For more information, see [Log Messages and Error Codes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/log-messages-and-error-codes.html#GUID-df9e6850-3d60-4e76-8249-c80181dad07b-en).