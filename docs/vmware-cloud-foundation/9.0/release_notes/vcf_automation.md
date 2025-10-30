---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-automation.html
product: vmware-cloud-foundation
version: 9.0
section: Release Notes
breadcrumb: Release Notes > VCF Automation
---

# VCF Automation

This document contains the following sections

- [Overview](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-automation.html#GUID-9892d5c0-36fa-462e-9396-38ce57cae783-en_id-5cf20cd4-adac-4228-a50d-650afa98d951)
- [Licensing](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-automation.html#GUID-9892d5c0-36fa-462e-9396-38ce57cae783-en_id-4ed397b0-6c66-4d63-8f7c-246ccc1a04d3)
- [Cloud Services](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-automation.html#GUID-9892d5c0-36fa-462e-9396-38ce57cae783-en_id-0734dd00-2768-4517-a37f-b3d1a3bfb4db)
- [Cloud Administration](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-automation.html#GUID-9892d5c0-36fa-462e-9396-38ce57cae783-en_id-4acd1dc6-e71f-4e7f-ad3c-7a19e823e367)
- [vSphere Supervisor](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-automation.html#GUID-9892d5c0-36fa-462e-9396-38ce57cae783-en_id-e91a0642-4042-4c1b-ad8a-ebff07b512f6)
- [Improvements for VMware Aria Automation users in VCF Automation 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-automation.html#GUID-9892d5c0-36fa-462e-9396-38ce57cae783-en_id-c278531b-23e3-44de-b84b-b40c684846ff)

## Overview

VCF Automation 9.0 allows IT teams and Cloud Service Providers to deliver a self-service private cloud for application teams, based on the vSphere Supervisor Platform. The self-service private cloud comes built-in with a rich set of cloud services to provision VMs, Kubernetes, networking, volumes, Secret Store, databases, Harbor Container Registries, external DNS, certificates and AI workloads.

VCF Automation 9.0 introduces new design innovations that underpin the next generation of private cloud

- Application teams can use cloud services to provision resources like VMs and Kubernetes clusters through self-service user interfaces, APIs, CLI, and gain access to a rich set of metrics to monitor the performance and health of the infrastructure.
- Cloud Admins can now centrally manage data center infrastructure resources, quotas, networks in a multi-tenant fashion and enable a rich set of VCF and third party cloud services for Lines of Businesses and Tenants.
- Lines Of Businesses and Tenants can achieve better control over resource utilization through policy-based governance and gain insights into operational metrics, while enabling application teams to utilize on-demand cloud services.

For more information on VCF Automation, see the [official documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9/what-is-vmware-cloud-foundation-and-vmware-vsphere-foundation/vcf-automation-overview.html).

## Licensing

To license VCF Automation, assign the VCF license to your vCenter instance  from VCF Operations.  When VCF Automation is connected to that vCenter instance it becomes licensed automatically.

For more information on VCF licensing, see the [official documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing.html).

## Cloud Services

**Cloud Services Overview**

VCF Automation 9.0 offers a comprehensive set of cloud services to meet the needs of Application Teams.

- Virtual Machine Service is a built-in solution that allows for self-service deployment and management of virtual machines on vSphere in a declarative manner with options to customize guest OSs through in-line sysprep and cloud-init.
- vSphere Kubernetes Service (VKS) is a fully integrated solution that enables the deployment and lifecycle management of Kubernetes clusters directly in vSphere.

  - A set of packages are automatically included with the cluster including pinniped, Antrea, kapp-controller, guest-cluster-auth-service, gateway-api, secret-gen controller, vSphere-pv-csi, Calico, vSphere-cpi and metrics-server.
  - Other packages like Countour, Harbor, Velero, Istio, Windows gMSA, CertManager, Telegraf, Prometheus, FluentBit, External DNS, Cluster Autoscaler and vSphere PV CSI WH can be optionally installed.
- Network Service allows for self-service of network configurations, such as subnets, static routes, and load balancers.
- Volume Service provides block and file storage services for VM and Kubernetes based workloads to consume storage through policies, persistent volume claims (PVCs), and snapshots that are backed by vSphere datastores and governed by quotas
- Data Services allow for self-service deployment and management of databases (PostgreSQL and MySQL) with rich APIs and empower IT teams with centralized and automated Day 0,1,2 data services operations.
- Secret Store securely stores and manages sensitive data such as passwords, tokens, and certificates for workloads running in vSphere Namespaces, allowing seamless and secure injection of secrets into VMs and Kubernetes applications without exposing them in plain text or requiring external secret managers.
- External DNS automates the registration and life-cycle management of DNS records for workloads running in vSphere Namespaces, allowing seamless integration with external DNS providers and ensuring that services remain discoverable as IPs or endpoints change.

These cloud services can be provisioned through web-based user interfaces, declarative API or CLI. The VCF Automation CLI is integrated with the kubectl command which allows for modern deployment patterns of using declarative YAML-based manifests to provision these cloud services.

Additionally, Catalogs, which are backed by pre-configured workload templates known as Blueprints,  can be used to provision VMs and Kubernetes clusters on a self-service basis. Blueprints are designed and published as Catalog items by Administrators

The Instances menu in VCF Automation 9.0 provides a comprehensive view of resources being consumed from a single location. Application teams can manage their workloads through a set of Day-2 actions and also gain insights into utilization (CPU & memory) for VMs and VKS clusters. Advanced operational metrics such as contention for CPU, memory and network contention and availability are also available for VKS clusters.

For more information on Cloud Services, see the [official documentation](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcfa_115&appid=vcf-9-0&language=&format=rendered).

**Virtual Machine Service**

VCF Automation now includes the following Virtual Machine Service improvements;

- SRM and VADP support for VM Service VMs: by using the same backup and restore vendor workflow used for full VM restores, you can now restore either an entire VM that already exists on in vSphere Supervisor or a subset of disks from its backup.
- Deploy a VM from ISO by using the VM Service: the VM Service now supports deploying a VM from an ISO image alongside the already supported workflow for deploying a VM from an OVF template. You can deploy a VM from an ISO image by using the VM Service deploy a VM workflow in the vSphere Client. If you want to perform guest customization on a deployed VM, deploy the VM from an ISO image and perform guest customization through the CLI workflow.

**Volume Service**

VCF Automation now includes the following Volume Service improvements:

- Ability to create a snapshot: you can now create a snapshot of the PVC attached to a VM created through the VM Service. You can create a snapshot be using either the CLI or the Local Consumption Interface (LCI). A new volume can be created from this snapshot using the API or CLI commands.
- RWX support on vSAN storage clusters.

**vSphere Kubernetes Service (formerly TKG Service)**

This release bundles vSphere Kubernetes Service (VKS) 3.3.1. VKS 3.3.1 builds on top of the capabilities released in VKS 3.3.0. You can review the detailed release notes for [VKS 3.3.0](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-supervisor/8-0/release-notes/vmware-tanzu-kubernetes-grid-service-release-notes.html#GUID-4e548863-c753-46af-b78a-c308d560981d-en_id-9a8726db-dc10-44f5-8a7c-a030c6366c94) and [VKS 3.3.1](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-supervisor/8-0/release-notes/vmware-tanzu-kubernetes-grid-service-release-notes.html#GUID-4e548863-c753-46af-b78a-c308d560981d-en_id-d980858e-865c-4182-bc2d-6270521e9a19).  Here are some of the most important capabilities that VKS 3.3.1 brings to VCF 9.0.

- **Support for VKr1.32:** this release adds support for VKr version 1.32 and drops the compatibility for VKr 1.27.x. This release also drops compatibility for 1.31.1 and adds support for 1.31.4. To upgrade to VKS 3.3.0 or later, all VKS clusters must be running VKr 1.28 or later. For more information, see the [interoperability matrix](https://interopmatrix.broadcom.com/Interoperability?col=820,&row=1794,&isHidePatch=true&isHideLegacyReleases=false).
- **Support for NSX-T VPC Network**: vSphere Supervisor 9.0 introduces support for NSX-T VPC networks. For you to leverage this capability of vSphere in Kubernetes Service, you should ensure you are on VKS 3.3.1 or later.
- **Support for Management and Workload Infrastructure Isolation**: vSphere Supervisor allows you to isolate management and workload infrastructure. For you to leverage this capability of vSphere Supervisor in Kubernetes Service, you should ensure you are on VKS 3.3.1 or later
- **Support for VCF CLI**: use the VCF Consumption CLI in order to authenticate and context-switch between vSphere Namespaces and discover available plug-ins and deploy VKS Standard Packages, using standard Kubernetes client tools such as Kubectl.
- **Ability to enable OS FIPS mode:** this release provides a configuration option to enable Operating System FIPS on the VKS cluster nodes during the creation of the VKS clusters. Refer to the documentation to make these configuration changes for different operating systems (Photon OS, Ubuntu, Windows). Ubuntu Pro subscription is required when using a Ubuntu based VKS cluster.
- **Ability to configure a Windows node pool to use Group Managed Service Accounts**: this release supports the joining of Windows nodes to on-premises Active Directory infrastructure to make use of Group Managed Service Accounts. The service automates the joining of Windows nodes to an Active Directory domain within a particular organizational unit, and adding nodes to a security group that can be delegated to for access to group managed service accounts.
- **Support for migration from TKC API to Cluster API**: Deprecation of TanzuKubernetesCluster (TKC) API was announced in vSphere Kubernetes Service release 3.2. The TKC API will be removed in a future release. Customers are encouraged to use Cluster API's Cluster API to bootstrap, configure and manage the lifecycle of the Kubernetes clusters. This release provides a means to retire the TKC API and continue managing existing VKS clusters using the Cluster API's Cluster API.
- **Cluster Autoscaler supports scaling from zero or to zero**: This release removes the no scaling from zero or to zero limitation for the autoscaler for clusters running VKr 1.31.4 or later. You must have the autoscaler standard package installed.
- **Support for Multiple Content Library:** VKS clusters can now be deployed from multiple content libraries in the same vSphere Namespace allowing for customer node images (windows) and Broadcom provided images to be leveraged.

## Cloud Administration

**Provider Management**

The Provider Management capability in VCF Automation allows IT teams and Cloud Service Providers to effectively manage, deliver, and scale cloud services across multiple vCenter and VCF instances.

- **Multi-tenancy:** multi-tenancy is natively available in VCF Automation through the concept of Organizations. The new multi-tenancy model ensures that each Organization representing a Line Of Business or a Tenant nad operates in a secure and isolated environment with access only to allocated services and resources.
- **Setting up Organizations:** a Quick Setup workflow is available which sets up the first Organization and assigns the necessary infrastructure quota. Organizations are created with predefined roles to meet the needs of Organization Administrators and Application Teams.
- **Centralized resource allocation and service provisioning:** IT teams and Cloud Service Providers can allocate shared data center resources, define cloud service tiers, and apply resource quotas to Organizations from a centralized location, while maintaining consistent performance and service availability across the infrastructure.
- **Networking:** IT teams and Cloud Service Providers can manage shared networking infrastructure, including IP addresses and Provider Gateways and assign portions of this infrastructure to one or more Organizations.

  - IP spaces offer a structured quota based approach for allocation of IP addresses to different Organizations.
  - Provider Gateways establish external network connectivity for Organizations. A Provider Gateway leverages VCF networking Tier 0 Virtual Routing and Forwarding (VRFs) and associates them with IP addresses from IP spaces. A Provider Gateway can be assigned to one or more Organizations.
  - Edge clusters: provides a view of utilization of a shared pool of NSX edge clusters which are used to offer cloud networking services such as NAT and north-south routing for workloads in the context of NSX Virtual Private Clouds (VPC).
- **Scalable content management:** IT teams and Cloud Service Providers can create Content Libraries in VCF Automation, which can be shared with all Organizations. Additionally, content such as Blueprints and Orchestration workflows can also be developed and shared with Organizations.
- **Maintain a rich ecosystem of cloud services:** VCF Automation introduces the ability to install, upgrade, configure, and publish cloud services like Secret Store and Data Services Manager from VCF and enable services from partners and ISVs.
- **Customized Organization experience:** Organization experiences can be tailored with custom themes and branding
- **Identity Provider Integration:** IT Teams and Cloud Service Providers can integrate with Identity Providers of their choice, enabling centralized authentication and Single Sign-On (SSO)
- **Chargeback:** chargeback and showback for managing IT costs at an Organization level can be retrieved from VCF Operations.

For more information on Provider Management, see the [official documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/provider-management.html).

**Organization Management**

VCF Automation provides a rich set of capabilities that enable the Organization Administrator of a Line of Business or Tenant to further organize and govern resources allocated to them among Application Teams.

- **Resources for Application Teams:** Organization Administrators can create logical representations of Application Teams through the use of constructs called Projects. A default Project is created when an Organization is created. Organization Administrators can further create and assign resource envelopes to Projects in the form of vSphere Namespaces. vSphere Namespaces provide a fine grained set of controls over resource utilization limits, CPU and Memory reservations and storage classes.
- **Centralized content management:** The Content Hub is a new centralized capability that allows Organization Administrators to discover and utilize Content Libraries, Blueprints, and Orchestration workflows that are shared with them. Additionally, Organization Administrators can also create and maintain their own Content Libraries, Blueprints and Orchestration workflows.

  - Networking: Organization Administrators can visualize and manage Organization specific networking infrastructure like Virtual Private Clouds (VPC), Transit Gateways and IP addresses.

    - Virtual Private Clouds (VPCs): VPCs provide an isolated domain of networking resources for Application teams. Configuration of new VPCs can be simplified through the use of VPC connectivity profiles.
- **Transit Gateways (TGWs):** TGWs enable inter-VPC connectivity. TGWs also connect to external gateways to enable connectivity outside of the Organization boundaries.
- **IP address management:** Organization Administrators can view external IP address blocks that are assigned to them. They can also create and view private-TGW IP address blocks for the entire Organization to use. They can view private-VPC IP address blocks that are applicable to specific VPCs. Finally, Organization Administrators can also view and update IP quotas for external and private-TGW IP blocks that apply to one or more VPCs.
- **Orchestration and Extensibility:**

  - VCF Automation provides built-in Orchestration capabilities powered by VCF Operations orchestrator. IT Teams and Cloud Service Providers can utilize this built-in capability to share workflows with Organizations, promoting reuse. Organization Administrators can achieve additional integration with external instances of VCF Operations orchestrator, offering better flexibility to develop and maintain their own workflows.
  - VCF Operations orchestrator now supports nested workflows in the workflow editor. This significantly improves the ease of developing complex orchestration workflows.
  - VCF Operations supports the ability to build custom resources which can be included to XaaS (Anything as a service) in Blueprints. Custom resources can now be created without the need for Orchestrator dynamic types.
  - Event subscriptions are available when creating, updating, and deleting VMs.
- **Utilization Metrics:** Organization Administrators can gain insights into resource utilization across Projects and on a per-Project basis through intuitive dashboards.

  - Billing: an overview of all expenses incurred for resource usage across the organization is also available.
- **Policy-based Governance:** VCF Automation Policy management helps Organization Administrators to apply governance on resources provisioned from Catalogs, through policies such as Approval, Lease and Day-2 Actions. VCF Automation also supports a YAML-based Policy-As-Code approach to govern usage of VCF cloud services including VMs and Kubernetes clusters. Organization Administrators can apply policies selectively across Projects while gaining insights on enforcements and violations.
- **Identity Provider Integration:** Organization Administrators can integrate with Identity Providers of their choice for centralized management of authentication.

For more information on Organization Management, see the [official documentation.](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/organization-management.html)

## vSphere Supervisor

**vSphere Supervisor Overview**

vSphere Supervisor is the cornerstone of VCF consumption and can be enabled during workload domain creation or directly in vCenter. It transforms vSphere clusters into modern application platforms by embedding a platform-level Kubernetes control plane directly into ESX hosts, exposing a unified declarative API surface. This integration allows users to provision and manage workloads, including VMs, containers via vSphere Pods, full Kubernetes clusters through VKS, OCI image registries, and data services through a consistent API interface.

The Supervisor maintains enterprise-grade governance, security, and operational consistency through vCenter, VCF Operations, and VCF Automation. It powers vSphere Namespaces, providing the foundation for multi-tenancy, enables GitOps-based workflows, and delivers cloud-like self-service in private data centers, bridging the consumption gap between public cloud and on-premises infrastructure.

For an overview of vSphere Supervisor concepts and how they apply in VCF Automation, see the [official documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsphere-supervisor-installation-and-configuration.html).

**Important considerations**

When using vSphere Supervisor, keep the following consideration in mind:

- **Use NSX Virtual Private Clouds (VPC) workload networks:** while other workload network types are supported, such as VDS and NSX Tier-0/Tier-1 segments, the use of VPC workload networks is essential to unlock the full capabilities of VCF 9.0. The combination of a vSphere Namespace and a Virtual Private Cloud delivers a robust multi-tenancy model that enables secure, frictionless self-service consumption of infrastructure and services. This configuration is a prerequisite for leveraging VCF Automation’s All-Apps Organizations.
- **Determine if single zone or multi-zone is required:** a Supervisor deployed in a single-zone configuration cannot be converted to a multi-zone deployment after enablement. It is critical to determine the desired deployment model before initiating the Supervisor enablement process.

**Getting started with vSphere Supervisor**

When getting started with vSphere Supervisor, you must select what type of deployment you want to use:

- **Single-zone deployment:** A single-zone Supervisor deployment utilizes a single vSphere cluster to host both workloads and Supervisor management components. It can be enabled either during the workload domain creation process or through the Supervisor enablement workflow in vCenter. Additional vSphere zones can be added after initial enablement. However, these zones will be used exclusively for workload placement and will not host Supervisor control plane components.
- **Multi-zone deployment:** A multi-zone Supervisor deployment leverages three vSphere clusters, separating each cluster into a vSphere zone. The zones are leveraged by workloads and Supervisor management components to deliver high availability and expose each cluster as an independent, consumable availability zone. This configuration enables a resilient, HA-capable platform. Multi-zone Supervisor enablement is only available through the Supervisor enablement workflow in vCenter. Additional vSphere zones can be added after initial enablement. However, these post-enabled zones will be available for workload consumption only, not for Supervisor control plane components.
- **Single host**: A single-zone Supervisor deployment with a single Control Plane VM deployed to a single ESX host, with vSphere High Availability deactivated. While it shares the same characteristics as other single-zone deployments, this configuration introduces a key limitation: any host failure will result in downtime for the Supervisor control plane and potentially for associated workloads.
- **Simplified deployment flow:** This is a single-zone Supervisor deployment that uses VDS-based workload networking, designed as a fast and simple starting point for proof-of-concept environments and production deployments leveraging VDS. The simplified deployment flow can be enabled directly from vCenter by right-clicking a vSphere cluster and selecting Activate Supervisor. This simplified deployment consists of: one vSphere Supervisor control plane VM, a shared network for both workload and management traffic, and no load balancer, limiting support to VM deployments only. Additional services such as vSphere Kubernetes Service (VKS) can be enabled by configuring a load balancer after the initial deployment. For more information on using this deployment method, see [Deploying Supervisor with a Simplified Deployment Flow](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsphere-supervisor-installation-and-configuration/deploying-easy-supervisor.html).

**New vSphere Supervisor capabilities**

The following is a list of the new vSphere Supervisor capabilities available in VCF 9.0:

- **Embedded Supervisor Kubernetes versions:** this release embeds VMware vSphere Supervisor version 9.0 in vCenter. This version of vSphere Supervisor packages Supervisor Kubernetes versions 1.28, 1.29, and 1.30. If you are upgrading from an existing vCenter, please ensure the current Supervisor version is at least 1.28. Auto upgrade from Supervisor Kubernetes version is not allowed for both VCF and VVF environments.
- **Import a VM into vSphere Namespace:** as a vSphere administrator, you can import an existing VM that runs in vSphere into a vSphere Namespace on vSphere Supervisor and have this VM managed by the VM Service. In VCF 9.0, the imported VM undergoes a change in its network identity that might cause disruption during the import operation.
- **Enable the Foundation Load Balancer:** Supervisors using a VDS workload network can now use the new Foundation Load Balancer, available out of the box. This load balancer is fully integrated and supported for Supervisor workloads.
- **Support VPC networking for workloads:** vSphere Supervisor now supports the use of VPC networks for vSphere Namespaces. This functionality provides a logically isolated, self-contained networking environment for Supervisor workloads and enables consumers to leverage subnets to control routing for their workloads.
- **Enable Supervisor admin role:** provides vSphere Administrators with the ability to delegate responsibility for Supervisor life-cycle and resource management to a Platform Administrator or another team in their organization.
- **Support for workload management isolation:** allows administrators to expose additional vSphere clusters to vSphere Namespace consumers through a vSphere Zone. These clusters can be isolated and dedicated for workload use only. This functionality supports use cases, such as GPU-based workloads that require dedicated resources, all managed and accessed from a single Supervisor.
- **Ability to independently deliver and update vSphere Supervisor:** this release provides you with the flexibility to update the Supervisor version independently of vCenter by using the Supervisor Content Library. This way, you can access the newest versions of the Supervisor and install them without updating the vCenter version. This capability, together with the independent update of the vSphere Kubernetes Service introduced in vSphere 8 U3, simplifies the life-cycle operations of upgrading the platform and Kubernetes versions for administrators and developers.

VCF 9.0 only introduces the ability to independently deliver vSphere Supervisor. VSphere Supervisor 9.0 is already embedded in vCenter 9.0. When the first version of Independent Supervisor is released in future, it will be accessible from the Supervisor Content Library.

- **Single host Supervisor:** deploy a Supervisor to a single ESX host, the Supervisor will consist of a single control plane VM.
- **Expose 4K native emulated virtual disks:** 4K native emulated virtual disks improve performance and compatibility for modern workloads by aligning with the physical storage sector size used in most enterprise arrays. This reduces I/O inefficiencies, enhances durability for write-heavy applications, such as databases, and ensures better integration with advanced storage systems making it ideal for production-grade VMs and Kubernetes clusters.
- **Enable the vSphere administrator to manage size quotas of Supervisor PV snapshots:** storage quotas set on a vSphere Namespace now apply to Supervisor Persistent Volume (PV) snapshots, ensuring that consumers cannot exceed their allocated storage when using volume snapshots.
- **Increase total number of supported persistent volumes:** CNS now supports a total of 30k volumes per Supervisor, which is an increase from 10K volumes in previous releases.
- **Identifying Supervisor PV/PVCs from deleted VKS clusters:** easily identify which PVCs, both RWO and RWX, are associated with VKS clusters. Based on this information, you can easily determine whether a VKS cluster no longer exists and whether the volumes (PVCs) are safe to delete.
- **Enhanced datastore de-commissioning workflows:** leverage the CNS (Cloud Native Storage) interface to migrate detached CNS volumes as recommended during datastore maintenance operations. When a datastore is placed into maintenance mode, attached volumes are automatically migrated, while detached volumes must be manually moved using the CNS interface. Additionally, CNS automatically blocks new volume provisioning on datastores that are entering or already in maintenance mode.

## Improvements for VMware Aria Automation users in VCF Automation 9.0

**Improved user experience**

The user interfaces for Assembler, Service Broker and Orchestrator services are now merged into the main user interface. Users no longer must switch between these services from tiles on the homepage. The new Consume menu in the UI hosts the Catalog and Deployment experiences. The new Design menu in the UI hosts Blueprints, Property Groups, Custom Resources and Resource Actions. The Content & Policies menu in UI hosts Content Sources, Content, Policies, and Notifications. The Service Broker and Assembler services remain untouched in the backend and therefore there are no changes to role-based access control of these services.

**Embedded VCF Operations orchestrator**

The Orchestrator tab hosts a fully embedded version of VCF Operations orchestrator (previously known as VMware Aria Automation Orchestrator). Management of roles for VCF Operations orchestrator is now available from the Access Control menu in the UI.

**Identity provider integration**

Organization Administrators can integrate with identity providers of their choice for centralized management of authentication.

**Certificate management**

Organization Administrators can use the built-in certificate management capability to manage the certificates of servers that VCF Automation has trusted communication with.