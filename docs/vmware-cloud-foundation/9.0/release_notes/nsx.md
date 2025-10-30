---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-nsx.html
product: vmware-cloud-foundation
version: 9.0
section: Release Notes
breadcrumb: Release Notes > NSX
---

# NSX

This document contains the following sections

- [Licensing](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-nsx.html#GUID-7708800a-6da7-4c0c-af6f-0ed05a00ff4e-en_id-6625daa2-66b6-4b6c-982d-409be8bf96cb)
- [Virtual Private Cloud (VPC) Networking](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-nsx.html#GUID-7708800a-6da7-4c0c-af6f-0ed05a00ff4e-en_id-8c1b8423-e8db-4093-81d1-5806444dc474)
- [Enhanced Data Path and Performance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-nsx.html#GUID-7708800a-6da7-4c0c-af6f-0ed05a00ff4e-en_id-5a569f61-e94a-4d37-9992-2f6f0d54461d)
- [Edge Platform](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-nsx.html#GUID-7708800a-6da7-4c0c-af6f-0ed05a00ff4e-en_id-9d33dd6e-5b75-4d50-9b62-d814bdda1d4d)
- [Installation and Upgrade - LCM](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-nsx.html#GUID-7708800a-6da7-4c0c-af6f-0ed05a00ff4e-en_id-109c955e-7f13-47bd-9a05-c16dcd95767f)
- [Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-nsx.html#GUID-7708800a-6da7-4c0c-af6f-0ed05a00ff4e-en_id-3376ee22-5d61-4725-9779-5e1298fc2c9f)
- [Monitoring](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-nsx.html#GUID-7708800a-6da7-4c0c-af6f-0ed05a00ff4e-en_id-6472bb08-ed30-4d93-ad5c-8fa930bf34ae)
- [Platform Security](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-nsx.html#GUID-7708800a-6da7-4c0c-af6f-0ed05a00ff4e-en_id-f651cefa-d7e0-45bd-ac48-32da8e56b31e)

## Licensing

To license NSX, assign the VCF license to your vCenter instance from VCF Operations. When NSX is connected to that vCenter it will become licensed automatically. Until NSX is licensed, it can be used for up to 90 days in evaluation mode.

## Virtual Private Cloud (VPC) Networking

**Virtual Private Cloud (VPC) in vCenter**

VCF 9.0 supports a common networking framework aligned with industry standards for consumption from vCenter, VKS NSX, and VCF Automation. This feature allows administrators to consume natively from vCenter Networking pane virtual networks through VPCs.

VPC in vCenter provides the ability to create VPCs, and subnets inside those VPCs which can be private or publicly advertised (public network), exposing VMs to the outside through External IPs.

**Virtual Private Cloud (VPC) in VCF Automation**

VCF 9.0 provides a common networking framework aligned with industry standards for consumption from vCenter, VKS NSX, and VCF Automation.

VPCs are the fundamental networking building blocks, allowing networking consumption from cloud users consuming VCF Automation for both VMs and Containers. This feature offers self service networking, isolation, and ability to asign multiple namespaces to a given VPC.

**Virtual Private Cloud (VPC) in Supervisor**

VPCs are fundamental in the Supervisor Service and bring a Cloud consumption model for networking in VCF. Inside a VPC users can deploy resources including StaticRoute, SecurityPolicy, K8s NetworkPolicy, TKG Cluster, PodVM and VM.

**Virtual Private Cloud (VPC) Simplification**

In VCF 9.0, [VPCs are enhanced](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=nsx6&appid=vcf-9-0&language=&format=rendered) with Connectivity and Service Profiles, which allows for defining outside connectivity and services in a centralized place. These enhancements help to simplify the process of defining VPCs and their connection to Transit Gateway. Realization of the VPC itself is also improved by directly creating the object instead of creating it inside Tier-1 for improved performance.

**Transit Gateways for VPCs**

[NSX VPC Transit Gateways (TGWs)](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=nsx8&appid=vcf-9-0&language=&format=rendered) simplify and streamline inter-VPC and VPC-to-external network communication by acting as a central hub for routing traffic. The TGW provides an abstraction layer, eliminating the need for tenants to configure infrastructure components directly thus avoiding misconfigurations. Tenants can attach external connections based on their needs, with support for both centralized (CTGW) and distributed (DTGW) connection types.

**Transit Gateways with Distributed VLAN Connectivity**

The NSX Transit Gateway with Distributed VLAN Connectivity (DTGW) simplifies network communication by providing a direct, high-performance datapath from ESX hosts to the network fabric. As a result, reliance on additional infrastructure components is reduced, resource usage is optimized, and deployment is simplified. Key benefits include direct host-to-fabric connectivity for enhanced performance, reduced resources and complexity for easier setup, and non-blocking network performance for improved throughput and lower latency. The solution also features a simplified external connectivity model that does not require deploying edge nodes or advanced routing configurations, reducing overall network complexity.

**VPC-Ready Workload Domains**

When a workload domain is created, all the prerequisites for consuming a Virtual Private Cloud (VPC) are fulfilled. This provides for the deployment of applications in a VPC onset of the deployment in NSX, vCenter and VCF Automation.

**Virtual Private Cloud (VPC) DHCP Enhancements:**

VCF 9.0 introduces advanced [DHCP configurations within VPCs](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=nsx11&appid=vcf-9-0&language=&format=rendered), extending beyond the basic use cases to offer greater flexibility and functionality. Additionally, a new VPC model is introduced, supporting both centralized and distributed Transit Gateways.

**Terraform Support for VPC**

This feature extends the widely used NSX Terraform Provider to support Transit Gateway, VPCs, and new related constructs, allowing Cloud networking consumption from Terraform. For information about the Terraform provider, see <https://registry.terraform.io/providers/vmware/nsxt/latest>.

## Enhanced Data Path and Performance

**Enhanced Datapath Path (EDP) Standard as Default Mode**

EDP Standard is a packet forwarding stack designed to provide superior performance in terms of throughput, packet rate, latency, and CPU utilization. This stack provides a performant alternative to the the Standard stack, which is the currently default mode.

In VCF 9.0, EDP Standard is the default host switch mode of operation for new VCF Workload Domains and for new installations of NSX. Upgraded, Imported, and Converted Workload Domains will continue using the legacy Standard stack until the mode is explicitly changed. See [Enhanced Data Path](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=nsx12&appid=vcf-9-0&language=&format=rendered).

**NSX Switch Port Analyzer (SPAN) in EDP**

Enhanced Data Path (EDP) provides a performant "fast path" for network flow processing. This release makes the EDP Fast Path available for NSX Switch Port Analyzer (SPAN) mirrored traffic.

**Real-Time Monitoring for EDP**

Enhanced Data Path (EDP) provides a performant "fast path" for network flow processing. This release makes the EDP Fast Path available for Live Traffic Analysis, the real-time monitoring tool in NSX.

**Real-Time Virtual Switch**

The Industrial vSwitch adds an EDP deployment mode to NSX. The EDP deployment mode is optimized for the requirements of industrial automation environments and SCADA systems. This mode provides predictable latency and supports the zero delay path switching with the Parallel Redundancy Protocol (PRP). See [Configure an Industrial Switch](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=nsx13&appid=vcf-9-0&language=&format=rendered).

## Edge Platform

**Edge Host Affinity**

The Edge Host Affinity feature introduces improvements for managing traffic sent through the Edge Node during host upgrade using vSphere Life Cycle Manager, which can help minimize disruption to network operations of the Edge Node. Instead of leveraging vMotion to migrate Edge nodes, the feature relies on higher-level protocols to seamlessly failover traffic between Edges. This feature helps to improve Edge Cluster High Availability.

**NSX Edge Platform Usability**

The installation and configuration of NSX Edge Nodes and Edge Clusters have been significantly streamlined through vCenter. [This enhancement](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=nsx2&appid=vcf-9-0&language=&format=rendered) simplifies workflows, reduces complexity, and improves operational efficiency for VPC environments.

**Gateway Firewall Disabled by Default**

Starting with NSX 9.0, Gateway Firewall is automatically disabled by default for all greenfield deployments of Tier-0 (T0) or Tier-1 (T1) Gateways. This update can enhance performance and optimize resource utilization in modern network environments.

## Installation and Upgrade - LCM

**NSX upgrade and install is part of the VCF 9.0 deploy, converge, and upgrade process**

Starting with NSX 9.0, a standalone upgrade or fresh installation of NSX is not supported. You must use the VCF BOM and follow the recommended process to upgrade NSX 4.x to VCF 9.0. For more information about deploying a new instance and upgrading to VCF 9.0, see [Overview of Deploy, Converge, and Upgrade](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/overview-of-deploy--converge--and-upgrade.html).

**NSX Installation with VMware Cloud Foundation 9.0**

NSX is a component of Broadcom's VMware Cloud Foundation solution. As such, NSX Manager gets installed as part of VCF or when a workload domain is created so that VCF enables customers to use virtual networking features, such as VPCs.

**NSX VIBs Included with ESX and Live Patch Support**

Virtual networking ESX kernel modules (VIBs) are included with ESX by default. This reduces the complexity and time required to install and upgrade virtual networking features. With this change, NSX VIBs on ESX Hosts now support ESX Live Patch in addition to the ESX maintenance upgrade. With Live Patch, the upgrades can happen without the need to put hosts into maintenance mode, and with no impact on vMotion or DRS operations.

**Unified Configuration Management**

With this release, the NSX configuration is integrated with vSphere Config Profiles (VCP), which allows for unified configuration management for ESX, VDS, and NSX at the cluster level. The ownership of NSX-specific configurations remains with NSX as part of the Transport Node Profile. But with this integration, users can manage the NSX configuration (at a cluster level) across these two solutions from one central place, allowing for ease of management and configuration compliance at a cluster level. In essence, this change provides a single-pane-of-glass solution for configuration. See [Guidelines for Upgrading NSX](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=nsx14&appid=vcf-9-0&language=&format=rendered).

**Virtual Networking TEPs on Management VMkernel Interface**

To provide virtual networking, NSX requires a tunnel end point (TEP) to encapsulate and de-encapsulate Ethernet frames into IP packets. Each of these TEPs requires an IP address to create a network fabric between transport nodes. With this new functionality, a cloud administrator uses the VMkernel (VMK0) interface and its associated IP address as a TEP in addition to having a dedicated VMkernel interface for TEPs. By using an existing VMkernel interface, customers can avoid having to allocate and manage additional IP addresses on hosts. See [Prepare Individual Hosts as Transport Nodes](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=nsxt-322&appid=vcf-9-0&language=&format=rendered).

**Single NSX Manager Support**

VCF 9.0 supports deploying a single NSX Manager for customers who want to have a reduced set of resource requirements and do not have the need for the high availability that the NSX management clustering technology provides.

For the highest level of availability, you must deploy a cluster of three NSX Managers.

**NSX Upgrade Alignment:**

VCF 9.0 aligns the NSX and vSphere upgrade processes to minimize downtime, unify upgrade cycles, provide testing, documentation,and ensure scalability, and adaptability. See [Guidelines for Upgrading NSX](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=nsx14&appid=vcf-9-0&language=&format=rendered).

**Hitless NSX Upgrade**

Hitless NSX Upgrade provides a faster and more efficient NSX Manager upgrades. NSX now accurately assesses whether or not a host can be successfully put in maintenance mode and avoid the post-operation timeout. See [Operational Impact of the NSX Upgrade](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=nsx15&appid=vcf-9-0&language=&format=rendered).

## Operations

**Serviceability Improvements to Grouping and Tagging**

User-generated tags can now be assigned to Segments and Segment Ports up to the maximum number of tags supported per object, without taking into account system-generated tags.

**Serviceability Improvements to Inventory**

Serviceability enhancements have been made in the **NSX Inventory** category:

- The connectivity between Transport Nodes and the NSX Manager is improved, leadig to fewer inventory loss issues, faster sync between nodes, and lesser CPU cycle usage in maintaining inventory, which frees up CPU resources for workload processing.
- The handling of alarms, raised due to lack of connectivity between NSX Manager and vCenters is more efficient, which reduces false alarms.

**Enhancements to Online Diagnostic System in NSX**

This enhancement makes improvements to NSX ODS runbooks:

- ODS is automatically invoked by the NSX components, such as SHA plug-ins, when an error occurs. This results in reduced reliance on out-of-the-box platforms for monitoring NSX and triggering ODS for troubleshooting.
- Automatic runtime troubleshooting is supported/activated in cases of BFD flaps on ESX. BGP/BFD issues sometimes need live debugging because support bundels might lack essential runtime information..

## Monitoring

**Logical Switch IPFIX for VCF Networking only Customers**

VCF Operations for Networks has an alternative way of gathering IPFIX flows in NSX. This feature introduces a new ConnectionTrack module that holds the necessary traffic connection information inside the NSX networking such as sessionFlags, RetransmissionCount, flowDirection, and averageLatency. NSX Switch IPFIX leverages ConnectionTrack to refactor and build a new user-space exporter to export flow records using new templates.

**NSX System Health Monitoring Improvement and Integration with VCF Operations**

The NSX UI features a **System Health** page for centralized monitoring of the overall health of management cluster, transport nodes, and edge nodes, giving users quick insight to items such as status, alarms, resource utilization, API usage, and compute manager reachability. See [Using VCF Operations to Monitor NSX System Health](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=nsx16&appid=vcf-9-0&language=&format=rendered).

**NSX Edge Monitoring Documentation Enhancement:**

The metrics for NSX Edge monitoring and troubleshooting include a detailed description for better understanding of monitoring information. This updated information can be found in the NSX API documentation.

## Platform Security

**Certificate Management**

It is best practice to run the CARR script prior to upgrading NSX Manager. The goal of running the CARR script is to ensure that the Transport Node (TN) certificates are not expiring within 825 days. If any TN certificate expires within 825 days, the CARR script can be invoked again to replace the certificate. See Broadcom KB article [369034](https://knowledge.broadcom.com/external/article?articleId=369034).