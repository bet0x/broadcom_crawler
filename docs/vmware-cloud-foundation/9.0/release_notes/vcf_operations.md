---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-ops.html
product: vmware-cloud-foundation
version: 9.0
section: Release Notes
breadcrumb: Release Notes > VCF Operations
---

# VCF Operations

This document contains the following sections

- [VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-ops.html#GUID-78debcd3-65e3-4f20-9aec-9bc7e56138e4-en_id-76fcd972-0a92-46d1-a6a5-09787b3ddd20)
- [Building Cloud Infrastructure](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-ops.html#GUID-78debcd3-65e3-4f20-9aec-9bc7e56138e4-en_id-27578375-9d8e-43f4-a2a8-d68eb7f4e0d9)
- [Lifecycle Management](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-ops.html#GUID-78debcd3-65e3-4f20-9aec-9bc7e56138e4-en_id-6665ba3d-2786-44e6-a8b4-c1c8765bfbeb)
- [Fleet Management](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-ops.html#GUID-78debcd3-65e3-4f20-9aec-9bc7e56138e4-en_id-8ccfb31a-0a9f-44aa-bdb1-d1a476ddaa27)
- [Infrastructure Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-ops.html#GUID-78debcd3-65e3-4f20-9aec-9bc7e56138e4-en_id-6611071f-d808-44bb-96c1-23ca0611ac75)
- [Workload Monitoring and Observability](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-ops.html#GUID-78debcd3-65e3-4f20-9aec-9bc7e56138e4-en_id-097a5b15-dd18-43b0-ad18-dd497e62e3ff)
- [Cost and Capacity Management](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-ops.html#GUID-78debcd3-65e3-4f20-9aec-9bc7e56138e4-en_id-30babe03-d099-4ce9-947a-767b1ba8d9de)
- [Workload Mobility](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-ops.html#GUID-78debcd3-65e3-4f20-9aec-9bc7e56138e4-en_id-f70a98af-9f21-4c15-bfc9-4244c6379088)
- [Security and Compliance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-ops.html#GUID-78debcd3-65e3-4f20-9aec-9bc7e56138e4-en_id-42bb4d27-0e51-49bd-acf4-c1fa3eb07fb0)

## VCF Operations

VMware Cloud Foundation Operations helps organizations build, manage, operate and secure their private cloud infrastructure by deploying and maintaining its fleet-level components, providing unified visibility and enhanced performance across the workload and infrastructure stack, and helping stay compliant with regulatory standards and organizational guidelines.

VCF Operations provides a single, unified interface to build, operate and secure the private cloud, significantly enhancing the cloud admin experience and eliminating operational silos. It is purpose-built for operationalizing VCF at scale while reducing complexity and operational overhead. From infrastructure provisioning to lifecycle management, everything is centralized in a single view, enabling faster deployments, streamlined upgrades, and more predictable operations. VCF Operations empowers IT teams to focus on delivering value, rather than managing infrastructure complexity.

VCF Operations includes the following major capabilities:

- Building Cloud Infrastructure
- Lifecycle Management
- Fleet Management
- Infrastructure Operations
- Workload Monitoring and Observability
- Cost and Capacity Management
- Workload Mobility
- Security and Compliance

**Licensing VCF Operations**

To license your VCF Operations instance, you can either register VCF Operations with Broadcom and add a license of VCF or vSphere Foundation, or add a licensed vCenter instance to the list of integrations. Until the VCF Operations instance is licensed, it can be used for up to 90 days in evaluation mode.

Get started today at

[https://www.vmware.com/products/cloud-infrastructure/ cloud-foundation-operations](https://www.vmware.com/products/cloud-infrastructure/).

## Building Cloud Infrastructure

Workload Domains are generally used to run customer workloads within a VCF environment. It includes a vCenter and NSX Manager, which can be shared with other workload domains, and one or more vSphere clusters with ESX hosts.

- **Introduction of new UI for Workload Domain deployment**

  Deployment of a Workload Domain with new or existing components can now be performed from the VCF Operations UI and is located under Inventory > select VCF Instance > Add Workload Domains.
- **vSphere Supervisor Enablement**

  vSphere Supervisor deployment and configuration can now be performed during workload domain creation.
- **Distributed or Centralized Network Connectivity**

  Distributed or Centralized Network deployment and configuration can now be performed during workload domain creation.

## Lifecycle Management

Manage the lifecycle of the whole VMware Cloud Foundation environment, including performing pre-checks, downloading installation and upgrade bundles, upgrading the workload domains, and monitoring your upgrade.

- **Combined ESX and NSX Host Component Upgrade**

  NSX host component upgrade bundles are included in ESX upgrade bundles and are not available separately. NSX host components are now upgraded as part of the ESX upgrade.
- **Automated Upgrade of the vSAN Witness Host for vSAN Stretched Clusters**

  vSphere clusters, based on vSphere Lifecycle Manager images, automatically upgrade the vSAN stretched cluster virtual witness host during ESX upgrades.
- **Operational Agility for vSphere Cluster Upgrades**

  - vSphere cluster upgrades can be initiated or scheduled even if there is a different vSphere cluster upgrade scheduled for or in progress at the specified time.
  - Failed vSphere cluster upgrades do not affect remaining in-progress cluster upgrades. After a failed upgrade, the vSphere cluster can now be remediated and the upgrade restarted without waiting for the rest of the cluster upgrades to complete.

## Fleet Management

Fleet Management enables operational consistency and efficient resource management of the VCF infrastructure at scale. It centralizes management functions across the integrated VCF components, streamlining tasks like licenses, identity access, certificates, passwords, configurations, and tags, across the VCF instances in a VCF fleet.

Key capabilities include:

- **License management**

  - License management allows organizations to control how they use VCF licenses while maintaining visibility and control over their licensing costs and compliance.

    You can seamlessly manage your licenses in the VCF Operations console.

    With intuitive controls, it dynamically enables features based on licensing, ensuring a hassle-free experience without the need for manual intervention. You can upgrade your licenses and unlock the full potential of VCF, maximizing the value of your investment. You can choose when and how to monitor VCF assets across the entire VCF stack, ensuring complete control and visibility at your convenience. VCF provides license management in two modes: for online environments as well as for air-gapped environments.

    For more information, see [Licensing Overview](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_839&appid=vcf-9-0&language=&format=rendered).
- **Identity and Access Management**

  - VCF simplifies identity and access management by enabling single-source configuration through VCF Operations. This eliminates the need for separate configurations across VCF components, offering Single sign-on and centralized management of federated access, enhancing both flexibility and user experience.

    VCF supports day-2 operations, allowing configuration through embedded vCenter or the VCF Identity Broker. It offers high availability and automation for tenant identity management, simplifying the overall management process ensuring continuity across multiple geolocations.

    Feature Highlights:

    For more information, see [VCF Single Sign-On](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_859&appid=vcf-9-0&language=&format=rendered).

    - Support for industry standards such as OIDC, SAML, LDAP and SCIM.
    - Workflow-based single identity source configuration for Active Directory, OpenLDAP, Okta, Microsoft Entra ID, Ping Federate, ADFS, and any SAML 2.0 compliant Identity provider.
    - MFA (Multi-factor Authentication) support is expected to be configured on the identity provider.
    - User and Groups provisioning is supported with JIT (Just-in-Time), direct AD integration, and SCIM.
    - Auto-configuration of VCF components for seamless integration with the identity source, with the option for manual configuration of some components.
    - Seamless Single Sign-On experience across VCF components.
- **Certificate Management**

  - VCF Operations introduces a unified, non-disruptive TLS certificate management system, allowing centralized control of certificates across all components in the VCF private cloud. With automated workflows, integration with various certificate authorities, and auto-renewal capabilities, it enhances security while minimizing manual effort. The following capabilities are supported:

    For more information, see [Managing Certificates in VMware Cloud Foundation](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcf_235&appid=vcf-9-0&language=&format=rendered).

    - Auto-renewal of certificates issued by VMCA, MSCA, or Open SSL CA that also support non-disruptive certificate update.
    - Replacement of default certificates with a trusted enterprise CA-signed certificate.
    - Certificate expiry notifications across your VCF infrastructure.
- **Password Management**

  - Unified password management in VCF Operations centralizes break-glass account password management of all components of the VCF private cloud. It offers a consolidated view of accounts, their statuses, and remediation needs. This ensures a consistent password management process and improves user experience by efficiently handling expiring or soon-to-expire passwords. The following capabilities are supported:

    For more information, see [Managing Passwords for VMware Cloud Foundation Components](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcf_250&appid=vcf-9-0&language=&format=rendered).

    - Update of passwords from a single console.
    - Remediate passwords to prevent account lockout.
    - Password expiry notifications across VCF infrastructure.
- **Configuration Management**

  - Unified configuration management provides features like scheduled drift detection for vCenter and cluster objects, enabling proactive detection of configuration deviations from the desired state. Users can now manage global templates across vCenter Instances, integrate with Git, and schedule drift detection through Automation/Orchestration service. The following capabilities are supported:

    For more information, see [Scheduling Drift Detection](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_873&appid=vcf-9-0&language=&format=rendered), [Configuring Source Control in VCF Operations](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_825&appid=vcf-9-0&language=&format=rendered), and [Managing Config Templates in VCF Operations](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_777&appid=vcf-9-0&language=&format=rendered).

    - Create desired state templates
    - Schedule Drift Detection
    - Download the Drift Status Report
    - Git Repo Integration
    - vSphere Configuration Profile-Enabled Cluster Status
    - Edit Configuration Templates
- **Tag Management**

  - Unified tag management provides a single pane of glass to manage tags across VCF components. It resolves issues of inconsistency, scalability, and dynamic tag assignment by offering centralized control of tags, ensuring a uniform tagging system across the entire fleet, and simplifying management at scale. The following capabilities are supported:

    For more information, see [Tags and Categories Overview](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_832&appid=vcf-9-0&language=&format=rendered).

    - **Consolidated View:** Obtain a single pane of glass view for Brownfield vCenter tags through their import into the common VCF Operations platform.
    - **Scale effectively:** Scale effectively by creating new tags in VCF Operations and pushing them to multiple vCenter instances at the same time.
    - **Tag Persistence:** Maintain tag persistence during vMotion for tags originating from VCF Operations.
    - **Conflict Resolution:** Review tag conflicts across vCenter Instances and learn how to resolve conflicting tags.
    - **Export tags:** Export tags via a JSON for use in automation purposes.

## Infrastructure Operations

**VCF Health**

VCF Health continuously monitors the operational state of the VCF components in your environment to ensure they are functioning as expected. By proactively identifying potential issues such as expired certificates, NTP drifts, DNS misconfigurations, and configuration errors, you can take preventative actions before these issues escalate into significant problems. Proactive monitoring empowers you to maintain a stable, secure, and efficient environment, reducing the risk of downtime and operational disruptions.

For more information, see [What is VCF Health](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_787&appid=vcf-9-0&language=&format=rendered).

**Diagnostics**

Diagnostics automatically detects known issues and critical vulnerabilities within the VCF software stack, providing detailed descriptions, root cause insights, and actionable remediation steps to resolve problems and mitigate risks.

- Diagnostics Findings

  The Diagnostics Findings feature offers a consolidated view of known product issues, VMSA-based security exposures, and best-practice recommendations across your VCF environment. Diagnostic Findings helps VCF administrators gain enhanced visibility into potential issues and risks, prioritize resolution efforts, and achieve uninterrupted operations. Key enhancements include:

  - Allows you to export discovered findings to CSV.
  - Offers parity with signatures that were previously part of Skyline Health Diagnostics and Skyline Advisor.
  - Allows you to view all signatures in the Findings Catalog.
- Log Assist

  - Log Assist streamlines the process of manually gathering and uploading support bundles used by VMware Technical Support Engineers (TSEs) to help solve customer technical issues. With the Log Assist feature, users can transfer support bundles to Broadcom Support from VCF Operations for the purpose of troubleshooting an open support case.

For more information, see [Using VCF Operations diagnostics](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/using-vcf-operations-diagnostics.html).

**Analyze Logs**

Log Analysis facilitates a deep dive into infrastructure logs, with powerful query and filtering options to troubleshoot issues across your virtualized environment. You can analyze and visualize log data and create custom queries for ongoing monitoring.

VCF Operations 9.0 introduces an integrated log management solution enabling you to explore logs, configure log-based alerts, and create dashboards directly within VCF Operations. For other log configurations and legacy log functionalities other than ones described above, continue using the standalone VCF Operations for logs UI.

Key capabilities include:

- **Centralized Log Collection and Standardization**

  The new centralised log collection feature allows users to manage log collection for several VCF components from a single UI. It simplifies the log collection process across the following areas:

  - Pre-installation of agents and centralized collection configuration.

    - The VCF Operations for logs Agent is now pre-installed for VCF Operations for network.
    - Log collection: With centralized log collection configuration page, you can enable and disable log collection for vCenter, ESX, VCF Operations (including operations-networks appliance).
  - Standardized Log format.

    - Logs generated by the following VCF components are now standardized in RFC 5424 format:

      - VCF Identity Broker
      - VCF Operations for network
      - VCF Operations

      For more information, see [Overview of Log Standardization](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_868&appid=vcf-9-0&language=&format=rendered).
- **Log Analysis**

  - Users can effectively search log statements with easy access to the following attributes:

    - Saved queries
    - Extracted Fields
    - Event Types
    - Event Trends
  - Side by side comparison of different log queries
  - Alerts and symptoms based on logs.
  - Dashboards based on logs.
  - Improved scale and performance to support 6TB of storage per node.

    For more information, see [Viewing Logs, Queries, and Fields](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_869&appid=vcf-9-0&language=&format=rendered).
- **Unified Cloud Proxy for Log Collection**

  From VCF 9.0, unified cloud proxy offers the log collection functionality. Cloud proxies that were previously enabled with the Log Forwarding feature are not functional after you upgrade to VCF 9.0.
- **Deployment Best Practices for VCF Log Solution**

  To ensure a smooth transition to the native log solution, follow these recommendations:

  - Deployment Location: Deploy the log solution within the same VCF management domain as your VCF Operations Analytics cluster.
  - Certificates: Install a custom SSL certificate signed by a certificate authority or internal root CA. Add these authoritative certificates or intermediate certificates to the log sources so that the log sources can establish trust with the log solution without manual intervention.
  - Log Source Configuration:

    - Use Fully Qualified Domain Names (FQDNs) for log source configuration instead of Virtual IPs (VIPs).
    - Use VIPs only if DNS is not supported.
    - Avoid configuring log sources with the IP addresses or FQDNs of individual log solution appliances.

**Network Operations**

View and manage the operational state of your VCF networking, allowing for streamlined troubleshooting and ensuring network performance is optimized.

Key capabilities include:

- Overview and summary of vSphere networking and NSX inventory.
- Visibility into network alerts and their trends.
- Monitoring of NSX health.\*
- Monitoring of Virtual Private Clouds (VPCs).\*
- Discover applications based on network flows.\*
- Traffic summary across the VCF environment for the past 24 hours.\*

\*Requires VCF Operations for networks to be deployed and attached.

For more information, see [Network Operations](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_892&appid=vcf-9-0&language=&format=rendered).

- **New NSX Project and VPC dashboards**

  View operational details and statistics for NSX Projects, VPCs, and  Transit Gateways with new dashboards.

  For more information, see [NSX Projects and VPCs](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_893&appid=vcf-9-0&language=&format=rendered).
- **Ability to access Flow information when DFW is not available**

  VCF Operations for networks can now fetch flow information even when firewall entitlement is not present or when DFW is deactivated. This is achieved by using the NSX Switch IPFIX mechanism.

  No special action is needed by the customer, apart from activating IPFIX for the NSX-T data source.

  When DFW is not activated or present, the following flow properties and dashboards will render no data.

  Flow properties:

  - Firewall Rule / Rule Id
  - Firewall Action
  - Protection Status
  - Flow Action
- **Dashboards**

  - Flow Insights > Recent Flows > New Firewall Rule Hits
  - Application > What's New > New Unprotected Members
  - Application > Flows > Top Application flows by rule (in the last 24 hours)
  - Plan and assess > Security Planning > Selecting 'All Unprotected flows' from 'Flow type' drop down
  - NSX-T Manager dashboard > Firewall Hit Count widget
- **Enhanced troubleshooting capabilities for NSX edge transport node metrics**

  NSX edge transport nodes export the metrics and statuses to VCF Operations for networks. These enhancements include:

  - Granular metrics for edge transport nodes, which are collected every 20 seconds.
  - View new statuses like VTEP State, DataPath IPC Thread Status, Edge Agent Status, and so on for the NSX Edge transport node.
  - Enhanced NSX-T Edge node monitoring with new edge node metrics sub-groups:

    - Non Data Path CPU Core Metrics
    - Tier0 Gateway Metrics
    - Uplink Router Interface Metrics
    - Node Process Metrics

**Storage Operations**

View and manage the operational state of your VCF storage, allowing visibility into storage capacity and performance. Provides a single point of access for monitoring storage across your virtualized infrastructure. Storage Operations provides the following capabilities:

- Single pane of glass view of storage inventory, capacity utilization, and key performance statistics.
- Visibility into the health of vSAN clusters, and drill down experience for further analysis.
- Visibility into vSAN deduplication and compression for both vSAN ESA and OSA deployments. Key highlights include:

  - Space efficiency metrics
  - New deduplication dashboards
  - Health alerts
- vSAN Performance Diagnostics

  vSAN Performance Diagnostics provides the following capabilities:

  - Improves the performance of your vSAN cluster by running vSAN performance benchmark tests for a desired performance outcome.

    - Maximize Throughput
    - Maximize IOPs
    - Minimize Latency
  - Troubleshoots performance issues and provides guided remediation of the issues. The diagnostic tests can be run on both vSAN OSA and ESA HCI architectures.

For more information, see [Monitoring Storage Operations](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_855&appid=vcf-9-0&language=&format=rendered).

**Data Protection and Recovery**

VCF Operations 9.0 simplifies disaster and cyber recovery with VMware Live Recovery, providing automated and centralized monitoring. Real-time insights, intuitive navigation, and a unified dashboard enable faster response to disasters and ransomware, ensuring continuous protection and improved efficiency.

**Marketplace and Integrations**

- **In-product Marketplace**

  Introducing a new Marketplace feature in VCF Operations 9.0 that allows you to find, download, and install integrations.

  For more information, see [Adding and Managing Management Packs from VMware Marketplace](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_872&appid=vcf-9-0&language=&format=rendered).
- **Management Pack Builder**

  You can create a Custom Management Pack in the Admin console of VCF Operations. The following features have been added:

  - Design, test, and install custom management packs.
  - Support for JSON and XML REST APIs.
  - Extend existing objects with new metrics and relationships.

  For more information, see [Management Pack Builder](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_867&appid=vcf-9-0&language=&format=rendered).
- **Management Packs**

  See the VMware Cloud Foundation Operations for Integrations 9.0 Release Notes under VCF Operations in the [Async Releases](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-async-releases.html) section.

**Others**

**vCenter Linking**

Use vCenter linking to obtain a single-pane-of-glass view across vCenter functionalities. Linking vCenter instances provides you with the following capabilities:

- A quick workflow to group up to 15 vCenter instances.
- Single pane of glass view of inventory management, unified alarms, tasks, and other functions replicated within grouped vCenter instances.
- Note: If you use Enhanced Linked Mode (ELM), vCenter linking maintains parity with ELM across all capabilities, except for roles/permissions and tag replication.

For more information, see [Linking vCenter Instances in VCF Operations](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_830&appid=vcf-9-0&language=&format=rendered).

## Workload Monitoring and Observability

VCF Operations provides tools and capabilities to manage, monitor and troubleshoot the performance of Virtual Machines, applications, and other infrastructure components within VCF's workload domains.

**Workload Operations**

Business applications are enhanced to include application discovery based on Network Flows

**Troubleshooting Workbench**

- **Enhanced Object Relationship Graph/Tree**

  The Object Relationship Advanced Widget (both Tree and Graph modes) has been refactored to improve performance and usability. With object grouping, pagination,   search, and the ability to hide unnecessary branches, you can now handle larger environments more effectively. Improved tooltips and back-end optimizations ensure better visibility, noise reduction, and support for more objects. For more information, see [Object Relationship (Advanced) Widget](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_249&appid=vcf-9-0&language=&format=rendered).
- **Run Custom Script**

  You can now run custom scripts directly on Virtual Machine (VM) objects from the Troubleshooting Workbench without the need to enable the Service Discovery plug-in.

  This new action, available via the Actions menu (right-click the three-dot ellipsis), allows scripts to run on VMs to gather diagnostic information and remediate issues. The feature is also accessible in the Inventory view.
- **vGPU monitoring added for Virtual Machines (PAIF)**

  New metrics have been added from ESX to VCF Operations.

**Platform Monitoring Improvements with VCF Operations**

Native integration with VCF Operations and Management to monitor Supervisor and VKS clusters.

The VCF 9.0 release brings a new, native integration with VCF Operations to monitor metrics for the Supervisor and VKS clusters. This integration enables the automatic discovery of Supervisor and VKS clusters for monitoring in VCF Operations. You can leverage the Telegraf agent to send metrics to VCF Operations and Management and gain visibility into the Supervisor cluster components, VKS clusters, and the Kubernetes resources created in them.

For more information, see [vSphere Supervisor Monitoring](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_891&appid=vcf-9-0&language=&format=rendered).

## Cost and Capacity Management

- **Cost Navigation**

  With VCF Operations, there has been a significant enhancement to Cost Management through the introduction of a new **Cost** home page in VCF Operations. This streamlined landing page serves as a centralized hub for all aspects of cost visualization.

  Simple and efficient design, offering a one-stop-shop experience where dashboards are embedded natively, enabling faster decision-making and more intuitive navigation.

  Access to key cost insights such as cost overview, analysis, optimization, showback, chargeback, and billing, from a unified interface.

  Key capabilities include:
- **Cost Management**

  Cost Management now includes the following capabilities:

  - Ability to change the currency after it has been configured.
  - Better cost analysis by comparing cost across objects, metrics, and timelines.
  - Support for cost on the basis of the current licensing offering.
  - Configuration of additional cost based on the Guest OS.
  - API to add new server models for costing.

  For more information, see [List of Global Settings](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_354&appid=vcf-9-0&language=&format=rendered), [New or Edit Cost Analysis](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_724&appid=vcf-9-0&language=&format=rendered), [Edit Monthly Cost of License](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_412&appid=vcf-9-0&language=&format=rendered), and [Editing Additional Costs](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_423&appid=vcf-9-0&language=&format=rendered).
- **Chargeback**

  Chargeback capabilities of VMware Cloud Director and Tenant App are now integrated into VCF. Native Chargeback capabilities are now available in the product and allow providers to:

  1. Configure rate cards as per the new supervisor cluster-based architecture.
  2. Generate and share bills with tenants.

  For more information, see [Performing VCF Automation Based Multitenancy in VCF Operations](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_870&appid=vcf-9-0&language=&format=rendered) .

  Chargeback for VMware Cloud Director will no longer be supported in VCF Operations and related capabilities and APIs will be removed. Going forward, Chargeback is going to be available on VCF Automation tenancy model and the capabilities and APIs will be made available around the same.
- **Capacity Management**

  With capacity management, you can now perform the following actions:

  - Exclude storage capacity from influencing the overall capacity of a cluster.
  - Execute What-If scenarios on a new cluster.
  - Export results of What-If scenarios as a report.
  - Exclude data from anomalous occurrences from influencing capacity projections.

  For more information, see [Viewing Object Capacity in the Capacity Tab](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_427&appid=vcf-9-0&language=&format=rendered) , [What-If Analysis - Workload Planning: Traditional](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_431&appid=vcf-9-0&language=&format=rendered) , and [What-If Analysis: Modeling Workload, Capacity, or Migration Planning](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_865&appid=vcf-9-0&language=&format=rendered).
- **Green Score**

  The Green Score capability and dashboards have the following updates:

  1. Sustainability has been renamed to Green Score.
  2. Definitions and formulas are updated in the information and Read Me sections.
  3. Reference standards have been updated to the 2025 values.
  4. Monetary equivalents of power, using the global average cost of power, has been removed.
  5. Equivalents of trees to offset carbon emissions have been removed.
  6. Dashboards have been renamed to emphasize power usage optimizations. The dashboards are now called Energy Efficiency with Virtualization, Energy Efficient Clusters, Energy Efficient Infrastructure, and Environmental Impact of Idle VMs.

  For more information, see [Configuring Green Score](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_871&appid=vcf-9-0&language=&format=rendered).

## Workload Mobility

VCF Operations HCX offers a flexible and secure platform for workload mobility within and across VCF private cloud environments. VCF Operations HCX 9.0 introduces integration with VCF while reducing operational complexity related to workload mobility through the following new features and capabilities:

- VCF Integration will include VCF licensing, authentication, and certificate management.
- New NSX destination constructs, including NSX VPC, NSX Global Segments, and NSX VLANs.
- Migrating workloads into vSphere Supervisor clusters.
- New VCF Workload Mobility Migration Planning will incorporate VCF Operations for network capabilities, working in conjunction with VCF Operations, and send the plans to a designated HCX Manager for migration.
- Single streamlined VCF Operations HCX appliance deployed at both source and destination locations.

**Licensing**

To license VCF Operations HCX, assign the VCF license to your vCenter instance from VCF Operations. When VCF Operations HCX is connected to that vCenter instance it becomes licensed automatically. Until VCF Operations HCX is licensed, it can be used for up to 90 days in evaluation mode.

## Security and Compliance

- **Security Operations**

  The Security Operations dashboard is designed to provide a comprehensive view of your security posture in VCF. This dashboard consolidates key elements related to user and infrastructure security to help you identify areas that may require attention and tightening based on your security exposure. It complements the Compliance capability within VCF Operations by surfacing core aspects of VCF security in one place.

  For more information, see [Monitoring Security Operations](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_810&appid=vcf-9-0&language=&format=rendered).
- **Compliance**

  Ensure compliance for your VCF infrastructure with a wide range of regulatory frameworks through latest upgraded and newly introduced compliance packs.

  For more information, see [Measuring Compliance of Objects](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_477&appid=vcf-9-0&language=&format=rendered).
- **Audit Events**

  VCF Operations allows you to view, monitor and search through activities across all the vCenter Instances in your VCF environment. Audit events enhance operational efficiency, transparency, and accountability. Using Audit Events, you can quickly track user activities and identify any anomalies.

  For more information, see [Viewing and Configuring Audit Events](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_768&appid=vcf-9-0&language=&format=rendered).