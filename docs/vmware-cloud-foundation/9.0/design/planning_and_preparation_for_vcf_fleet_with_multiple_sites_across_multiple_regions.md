---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/blueprint-4/planning-and-preparation-for-vcf-fleet-with-multiple-sites-across-multiple-regions.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Planning and Preparation for VCF Fleet with Multiple Sites across Multiple Regions
---

# Planning and Preparation for VCF Fleet with Multiple Sites across Multiple Regions

Before you start the implementation of the VCF Fleet with Multiple Sites across Multiple Regions blueprint, you should follow the procedures in the table below to ensure a smooth deployment.

## High Level Deployment Requirements

The following is a high level overview of the requirements to deploy this blueprint. To fully size and gather input requirements refer to the Planning and Preparation for the first VCF Instance in the VCF Fleet and Planning and Preparation for additional VCF Instances in the VCF Fleet sections.

| Aspect | Requirements |
| --- | --- |
| Physical Hosts | 14x hosts   - 4x for the management domain cluster (VCF Instance 1) - 3x for the workload domain cluster (VCF Instance 1) - 4x for the management domain cluster (VCF Instance 2) - 3x for the workload domain cluster (VCF Instance 2) |
| Physical VLANs, Networks and IP allocations | 26x VLANS (with a physical network gateway interface attached)  - 4x ESX Management Network (14 IPs)    - 1 IP per VCF Instance 1 Management Domain host (x4 hosts)   - 1 IP per VCF Instance 1 Workload Domain host (x3 hosts)   - 1 IP per VCF Instance 2 Management Domain host (x4 hosts)   - 1 IP per VCF Instance 2 Workload Domain host (x3 hosts) - 1x VCF Instance 1 Management Domain VM Management Network (19 IPs)    - Fleet Management (1 IP)   - VCF Operations (3 IPs)   - VCF Operations Collector (1 IP)   - VCF Automation VIP (1 IP)   - VCF Automation Node IPs (4 IPs) \*   - NSX Manager (6 IPs)   - vCenter (2 IPs)   - SDDC Manager (1 IP) - 1x VCF Instance 1 Workload Domain VM Management Network (7 IPs)    - Edge VMs (2 IPs)   - Supervisor Control Plane (5 consecutive IPs) \* - 1x VCF Instance 2 Management Domain VM Management Network (10 IPs)    - VCF Operations Collector (1 IP)   - NSX Manager (6 IPs)   - vCenter (2 IPs)   - SDDC Manager (1 IP) - 1x VCF Instance 2 Workload Domain VM Management Network (7 IPs)    - Edge VMs (2 IPs)   - Supervisor Control Plane (5 consecutive IPs) \* - 4x vSAN Network (or NFS if using NFS storage model) (14 IPs)    - 1 IP per VCF Instance 1 Management Domain host (x4 hosts)   - 1 IP per VCF Instance 1 Workload Domain host (x3 hosts)   - 1 IP per VCF Instance 2 Management Domain host (x4 hosts)   - 1 IP per VCF Instance 2 Workload Domain host (x3 hosts) - 4x vMotion Network (14 IPs)    - 1 IP per VCF Instance 1 Management Domain host (x4 hosts)   - 1 IP per VCF Instance 1 Workload Domain host (x3 hosts)   - 1 IP per VCF Instance 2 Management Domain host (x4 hosts)   - 1 IP per VCF Instance 2 Workload Domain host (x3 hosts) - 4x Host TEP network (28 IPs)    - 2 IPs per VCF Instance 1 Management Domain host (x4 hosts)   - 2 IPs per VCF Instance 1 Workload Domain host (x3 hosts)   - 2 IPs per VCF Instance 2 Management Domain host (x4 hosts)   - 2 IPs per VCF Instance 2 Workload Domain host (x3 hosts) - 2x Workload Domain Edge TEP network (8 IPs)    - 2 IPs per VCF Instance 1 Edge VM (x2 Edge VMs)   - 2 IPs per VCF Instance 2 Edge VM (x2 Edge VMs) - 4x Edge Uplink Network (8 IPs)    - 2 IPs per VCF Instance 1 Edge VM (x2 Edge VMs)   - 2 IPs per VCF Instance 2 Edge VM (x2 Edge VMs)   All IP addresses should have forward and reverse DNS entries configured in your managed DNS server apart from those marked with a \* |
| Virtual Networking | - Supervisor Service CIDR    - e.g. 10.96.0.0/23 - VPC Private IP Block (Control Plane) - TGW Private IP Block (Control Plane) - External IP Block (Control Plane & Workload/Organizations) - Private VPC Block for each Organization’s VPCs - Private TGW IP Block for each Organization |

## Planning and Preparation for the first VCF Instance in the VCF Fleet

| Procedure Grouping | Procedure | Information |
| --- | --- | --- |
| Planning and Preparation | Download the Planning and Preparation Workbook | The Planning and Preparation Workbook can be located on the Broadcom Technical Documentation site. |
| Pre-Requisites | Review and ensure compliance with the items listed in the Prerequisite Checklist tab of the Planning and Preparation Workbook | This will ensure that the all hardware, network and infrastructural pre-requisites are met before commencing deployment. |
| Sizing | In a distinct copy of the Planning and Preparation Workbook, populate the Management Domain Sizing tab | This will ensure that the management domain for the first VCF Instance is adequately sized to host components of the VCF Fleet that will reside in that instance. |
| Management Domain (First Instance) | In the same Planning and Preparation Workbook, select the following options on the VCF & VVF Planning tab   - VMware Cloud Foundation Deployment Version: 9.0.0.0 - Deployment Specification: VMware Cloud Foundation - Instance to perform operation on: First Instance - Operation to be performed: Deploy a new VCF fleet   Populate the following tabs:   - Populate the Management Domain Creation tab | This will gather all the required physical network, IP Addressing and infrastructural details required to perform the deployment of the management domain in the first VCF Instance. |
| Workload Domain (First Instance) | In the same Planning and Preparation Workbook populate the following tabs:   - Populate the Workload Domain Creation tab | This will gather all the required physical network, IP Addressing and infrastructural details required to perform the deployment of the first workload domain in the first VCF Instance. |

## Planning and Preparation for additional VCF Instances in the VCF Fleet

| Procedure Grouping | Procedure | Information |
| --- | --- | --- |
| Pre-Requisites | Review and ensure compliance with the items listed in the Prerequisite Checklist tab of the Planning and Preparation Workbook | This will ensure that the all hardware, network and infrastructural pre-requisites are met before commencing deployment. |
| Sizing | In a distinct copy of the Planning and Preparation Workbook, populate the Management Domain Sizing tab | This will ensure that the management domain for the additional VCF Instance is adequately sized to host components of the VCF Fleet that will reside in that instance. |
| Management Domain (Additional Instance) | In the same Planning and Preparation Workbook, select the following options on the VCF & VVF Planning tab   - VMware Cloud Foundation Deployment Version: 9.0.0.0 - Deployment Specification: VMware Cloud Foundation - Instance to perform operation on: Additional Instance - Operation to be performed: Deploy a VCF Instance in an existing VCF fleet   Populate the following tabs:   - Populate the Management Domain Creation tab | This will gather all the required physical network, IP Addressing and infrastructural details required to perform the deployment of the management domain of the additional VCF Instance. |
| Workload Domain (Additional Instance) | In the same Planning and Preparation Workbook populate the following tabs:   - Populate the Workload Domain Creation tab | This will gather all the required physical network, IP Addressing and infrastructural details required to perform the deployment of the first workload domain in the additional VCF Instance. |