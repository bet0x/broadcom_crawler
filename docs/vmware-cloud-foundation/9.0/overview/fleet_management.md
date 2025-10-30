---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9/what-is-vmware-cloud-foundation-and-vmware-vsphere-foundation/vcf-operations-overview/fleet-management.html
product: vmware-cloud-foundation
version: 9.0
section: Overview
breadcrumb: Overview > Fleet Management
---

# Fleet Management

By using the fleet management functionality of VCF Operations, you can manage centrally your VCF components.

## License Management

VCF provides license management in two modes - for connected environments and disconnected environments. You can upgrade your licenses and you can choose when and how to monitor VCF assets across the entire VCF stack.

For more details on license management, see the following resources:

- [Licensing](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing.html) documentation. Explains how to use license management.
- [Licensing - Direct Customer](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-manage-licenses-direct-customer-journey.pdf) and [Licensing - Portability](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-manage-licenses-portability-journey.pdf) journey maps. Represent visual guides to the sequences of license management operations.

## Lifecycle Management

You can download installation and upgrade bundles, perform prechecks, upgrade the workload domains, and monitoring your upgrade operations. By streamlining this process, the environment is always running the latest and most stable software versions.

Lifecycle management simplifies and automates the process of applying updates and patches to the software components within the VCF stack, ensuring that the infrastructure complies with the latest security standards and best practices. It provides tools for planning the updates so that you can schedule maintenance windows and make changes with minimal disruption to services. It helps in managing different versions of the software components, ensuring compatibility and stability across the entire infrastructure.

For more details on lifecycle management, see the following resources:

- [Lifecycle Management](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management.html) documentation. Explains how to use lifecycle management.
- [Manage VCF Lifecycle](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-manage-lifecycle-journey.pdf) journey map. Represents a visual guide to the sequence of lifecycle management operations.

## Identity and Access Management

You can use single-source configuration in VCF Operations for identity and access management. In this way, you can use the same identity configuration across VCF components and across multiple geolocations, offering Single Sign-On (SSO) and centralized management of federated access, enhancing both flexibility and user experience.

For more details on identity and access management, see the following resources:

- [Configuring Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is.html) documentation. Explains how to use identity and access management.
- For information about the detailed sequence of operations you perform, see the [VCF Single Sign-On](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-manage-identity-and-access-journey.pdf) journey map.

## Certificate Management

VCF Operations introduces a unified, non-disruptive TLS certificate management system, allowing centralized control of certificates across all components in the VCF private cloud. The system provides automated workflows, integration with various certificate authorities, and auto-renewal capabilities.

Features include viewing certificates and alerts, auto-renewal for VMCA, MSCA, and OpenSSL CA, replacing default certificates with enterprise CA certificates, CA configuration and CSR generation, and certificate expiry notifications.

For more details on certificate management, see the following resources:

- [Managing Certificates in VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0.html) documentation. Explains how to use certificate management.
- [Infrastructure Management - Certificates](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-manage-certificates-journey.pdf) journey map. Represents a visual guide to the sequence of certificate management operations.

## Password Management

Unified password management in VCF centralizes account password management of all components of the VCF private cloud. It offers a consolidated view of accounts, their statuses, and remediation needs. You can easily identify expiring or soon-to-expire passwords.

For more details on password management, see the following resources:

- [Managing Passwords for VMware Cloud Foundation Components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords.html) documentation. Explains how to use password management.
- [Infrastructure Management - Passwords](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-manage-passwords-journey.pdf) journey map. Represents a visual guide to the sequence of password management operations.

## Configuration Management

Unified configuration management provides features like scheduled drift detection for vCenter and cluster objects, enabling proactive detection of configuration deviations from the desired state.

You can manage global templates across vCenter instances, integrate with Git, and schedule drift detection through the VCF Automation or VCF Operations orchestrator.

Configuration management has the following capabilities:

- Schedule drift detection. Schedule or perform on-demand/repeatable drift detection jobs with the VCF Operations console, viewing active and historical jobs.
- Download a drift status report. Generate a PDF report on template drift status for selected vCenter instances within the retention period.
- Git repository integration. Connect to a Git repository for template versioning. Git becomes the primary template owner when connection is established.
- vSphere Configuration Profile-Enabled cluster status. View aggregated vSphere Configuration Profile (VCP) drift status for activated clusters.
- Edit configuration templates. Edit templates in VCF Operations, adding, removing, or modifying vCenter Schema Configuration items with validation.

For more details on configuration management, see the following resources:

- [Scheduling Drift Detection](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-configuration-management/using-the-configuration-management-dashboard/scheduling-drift-detection.html), [Configuring Source Control in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-configuration-management/git/integrating-with-git.html) and [Managing Configuration Templates in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-configuration-management/creating-a-configuration-template.html#GUID-5c970def-f515-4db6-b6dd-d529e5170f8b-en) documentation. Explains how to use configuration management.

- [Infrastructure Management - Configuration Drift Management](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-manage-configuration-drifts-journey.pdf) journey map. Represents a visual guide to the sequence of configuration management operations.

## Tag Management

By using unified tag management, you can manage tags across VCF components from a central location. You have centralized control of tags to resolve issues of inconsistency, scalability, and dynamic tag assignment, ensuring a uniform tagging system across the entire fleet, and simplifying management at scale.

Tag management has the following capabilities:

- Consolidated view. Obtain a single-pane-of-glass view for existing vCenter tags through their import into the common VCF Operations platform.
- Scale effectively. Scale effectively by creating new tags in VCF Operations and pushing them to multiple vCenter instances at the same time.
- Tag persistence. Maintain tag persistence during vSphere vMotion for tags originating from VCF Operations.
- Conflict resolution. Review tag conflicts across vCenter instances and learn how to resolve conflicting tags.
- Export tags. Export tags in JSON for automation purposes.

For more details on tag management, see the following resources:

- [Tags and Categories Overview](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-tag-management.html) documentation. Explains how to use tag management.
- [Infrastructure Management - Tag Management](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-manage-tags-journey.pdf) journey map. Represents a visual guide to the sequence of tag management operations.