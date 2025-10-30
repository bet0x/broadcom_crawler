---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/vcf-fleet-management-design-with-multiple-availability-zones/planning-and-preparing-for-vcf-fleet-in-a-single-site.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Planning and Preparation for VCF Fleet in a Single Site
---

# Planning and Preparation for VCF Fleet in a Single Site

Before you start the implementation of the VCF Fleet in a Single Site Blueprint, you should follow the procedures in the table below to ensure a smooth deployment.

## High Level Deployment Requirements

The following is a high level overview of the requirements to deploy this blueprint. To fully size and gather input requirements refer to the Planning and Preparation for the VCF Fleet section.

| Aspect | Requirements |
| --- | --- |
| Physical Hosts | 7x hosts   - 4 for the management domain cluster - 3 for each cluster within a workload domain |
| Physical VLANs, Networks and IP allocations | 13x VLANS (with a physical network gateway interface attached)  - 2x ESX Management Network (7 IPs)    - 1 IP per management domain host (x4 hosts)   - 1 IP per workload domain host (x3 hosts) - 1x Management Domain VM Management Network (19 IPs)    - Fleet Management (1 IP)   - VCF Operations (3 IPs)   - VCF Operations Collector (1 IP)   - VCF Automation VIP (1 IP)   - VCF Automation Node IPs (4 IPs) \*   - NSX Manager (6 IPs)   - vCenter (2 IPs)   - SDDC Manager (1 IP) - 1x Workload Domain VM Management Network (7 IPs)    - Edge VMs (2 IPs)   - Supervisor Control Plane (5 consecutive IPs) \* - 2x vSAN Network (or NFS if using NFS storage model) (7 IPs)    - 1 IP per Management Domain host (x4 hosts)   - 1 IP per Workload Domain host (x3 hosts) - 2x vMotion Network (7 IPs)    - 1 IP per Management Domain host (x4 hosts)   - 1 IP per Workload Domain host (x3 hosts) - 2x Host TEP network (14 IPs)    - 2 IPs per Management Domain host (x4 hosts)   - 2 IPs per Workload Domain host (x3 hosts) - 1x Workload Domain Edge TEP network (8 IPs)    - 2 IPs per Edge VM (x4 Edge VMs) - 2x Edge Uplink Network (4 IPs)    - 2 IPs per Edge VM (x2 Edge VMs)   All IP addresses should have forward and reverse DNS entries configured in your managed DNS server apart from those marked with a \* |
| Virtual Networking | - Supervisor Service CIDR    - e.g. 10.96.0.0/23 - VPC Private IP Block (Control Plane) - TGW Private IP Block (Control Plane) - External IP Block (Control Plane & Workload/Organizations) - Private VPC Block for each Organization’s VPCs - Private TGW IP Block for each Organization |

## Planning and Preparation for the VCF Fleet

| Procedure Grouping | Procedure | Information |
| --- | --- | --- |
| Planning and Preparation | Download the Planning and Preparation Workbook. | The Planning and Preparation Workbook is located on the Broadcom Technical Documentation site. |
| Pre-Requisites | Review and ensure compliance with the items listed in the Prerequisite Checklist tab of the Planning and Preparation Workbook. | This will ensure that the all hardware, network and infrastructural pre-requisites are met before commencing deployment. |
| Sizing | In a distinct copy of the Planning and Preparation Workbook, populate the Management Domain Sizing tab. | This will ensure that the management domain is adequately sized to host your VCF Fleet deployment. |
| Management Domain | In the same Planning and Preparation Workbook, select the following options on the VCF & VVF Planning tab:   - VMware Cloud Foundation Deployment Version: 9.0.0.0 - Deployment Specification: VMware Cloud Foundation - Instance to perform operation on: First Instance - Operation to be performed: Deploy a new VCF fleet   Populate the Management Domain Creation tab. | This will gather all the required physical network, IP Addressing and infrastructural details required to perform the deployment of the management domain. |
| Workload Domain | In the same Planning and Preparation Workbook populate the following tabs:   - Populate the Workload Domain Creation tab - Stretched Cluster section of the Workload Domain Post Deploy tab | This will gather all the required physical network, IP Addressing and infrastructural details required to perform the deployment of the first workload domain and subsequently stretch the workload domain cluster. |

Note: This is a template that can be reused in subsequent blueprints. In those blueprints, we will add additional rows / tables for the deployment of workload domains and additional VCF Instances (as appropriate), guiding the user on which options to choose in the Planning and Preparation Workbook and which tab to populate for the operation chosen.