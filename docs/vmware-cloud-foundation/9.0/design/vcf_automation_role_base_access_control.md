---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-identity-management/role-base-access-control.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Automation Role Base Access Control
---

# VCF Automation Role Base Access Control

Managing multi-tenant cloud environments demands a clearly established role-based access control (RBAC) strategy to guarantee restricted access, tenant separation, and secure operations.

Best Practices for Efficient Role-Based Access Control



| Best Practice | Recommendation |
| --- | --- |
| Principle of Least Privilege | Ensure users are granted only the permissions absolutely necessary for their specific roles, minimizing security risks. |
| Regular Review & Updates | Continuously review and update RBAC assignments to ensure they align with any changes in user roles and responsibilities. |
| Logging & Auditing | Implement logging and auditing to track user access and actions, providing transparency and accountability. |
| User Education | Provide ongoing training on the importance of role-based access and secure credential handling to prevent security breaches. |
| Integrate Third-Party Solutions for RBAC Optimization | Consider using external tools for more streamlined RBAC management, detailed reporting, and enhanced control. |

VCF provides a platform to create and manage secure and multi-tenant environments. Implementing role-based access control for the management components offers the following benefits.

Role-Based Access Control Design for Service Providers



| Attribute | Detail |
| --- | --- |
| Separate Administrator roles | Establish distinct roles for service provider admins, such as managing infrastructure, provisioning resources, and troubleshooting tenant issues. |
| Provider Admin levels | To control access to sensitive areas, differentiate roles for basic resource management, advanced configuration, and network administration . |
| Multi-Factor Authentication for all privileged accounts | Implement Multi-Factor Authentication (MFA) for all privileged accounts, including both tenant and service provider administrators. |

RBAC Design for Tenants



| Attribute | Detail |
| --- | --- |
| Predefined Tenant roles | Create predefined roles such as tenant user, tenant operator, and tenant administrator with permissions based on specific needs. |
| Custom roles for granularity | Implement custom roles for specific workflows, such as a deployment engineer, with permissions to deploy templates without managing infrastructure. |
| Least privilege | Apply the principle of least privilege to grant only the minimum permissions needed for each role to perform their tasks effectively. |

## VCF Automation Default Provider Level Global Roles

These are the default system level roles found in the Provider Admin Portal.

- They are automatically published to all Organizations
- Custom roles can be created at Provider Admin level and then published to one, many, or all Organizations as necessary

VCF Automation Default Provider Level Global Roles



| Role | Description | Published to other Organizations |
| --- | --- | --- |
| Defer to Identity Provider | Rights will be determined based on information received from IdP | Yes, Default - All Organizations |
| Organization Administrator | Owns an Organization and can add users/groups to the organization | Yes, Default - All Organizations |
| Organization Auditor | Audit an Organization | Yes, Default - All Organizations |
| Organization User | Rights given to an organization user | Yes, Default - All Organizations |
| Custom role | Use "new" role button in the Access Control screen to create a custom role as necessary | Can be granularly published to one, many or all Organizations as necessary |

## VCF Automation Default Organization Level Roles

These are the default Organization level roles.

- Organization level roles govern who can log into the Organizational level portal and with what rights
- Organizations can also inherit custom roles created and subsequently published from the Provider Admin level
- Organizations Administrators can also create custom roles at the Organization level

VCF Automation Default Organization Level Roles



| Role | Description | Considerations |
| --- | --- | --- |
| Defer to Identity Provider | Rights will be determined based on information received from IdP | - Inherited from Provider Level Global Roles - Cannot be edited at Organization level |
| Organization Administrator | Owns an Organization and can add users/groups to the organization | - Inherited from Provider Level Global Roles - Cannot be edited at Organization level |
| Organization Auditor | Audit an Organization | - Inherited from Provider Level Global Roles - Cannot be edited at Organization level |
| Organization User | Rights given to an organization user | - Inherited from Provider Level Global Roles - Cannot be edited at Organization level |
| Custom role | Use "new" role button in the Access Control screen to create a custom role as necessary | - Created specifically for the Organization - Cannot be published to other Organizations |

## VCF Automation Default Organization Project Level Roles

Even if a user has access to the Organization portal, they still need to be assigned specific rights at the Project level to access and manage resources.

- Once a Project is created, the administrator must assign users to the a specific role
- The role assigned to the user applies to all Namespaces created within the Project

VCF Automation Default Organization Project Level Roles



| Role | Description |
| --- | --- |
| Project Administrator | Can manage members and catalog content |
| Project Advanced User | Can request catalog items and use IaaS services |
| Project User | Can request catalog items |
| Project Auditor | Can view all project content but cannot request |