---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/nsx-introduction/support-for-principal-identities-authentication-for-the-nsx-management-pack.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Support for Principal Identities Authentication for NSX
---

# Support for Principal Identities Authentication for NSX

VCF Operations supports authentication of Principal Identities (PI) using NSX . The Principal Identities (PI) are unique users in NSX who can create an object and ensure that the object can only be modified or deleted by the same identity. The authentication of principal identities is only supported through a client certificate. The principal identities authentication is local to NSX and it is possible to assign a predefined Role-based access control (RBAC) role to the principal identity.

Principal Identities are generally used by third-party applications or cloud management platforms such as Open stack, and Pivotal Container Services (PKS) to ensure that an administrator does not modify the NSX configuration which can generate a mismatch between their view of the NSX environment and the actual configuration.