---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/vcf-fleet-basic-management-design/preparing-for.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Planning and Preparation Preparing for VCF Fleet in a Single Site with Minimal Footprint
---

# Planning and Preparation Preparing for VCF Fleet in a Single Site with Minimal Footprint

Before you start the implementation of the VCF Fleet in a Single Site with Minimal Footprint Blueprint, you should follow the procedures in the table below to ensure a smooth deployment.

## High Level Deployment Requirements

The following is a high level overview of the requirements to deploy this blueprint. To fully size and gather input requirements refer to the Planning and Preparation for the VCF Fleet section.

| Aspect | Requirements |
| --- | --- |
| Physical Hosts | - 4 for initial management domain cluster - 3 for second management domain cluster to support Self-Service Consumption via VCF Automation [optional]\*\* |
| Physical VLANs, Networks and IP allocations | 7x VLANS (with a physical network gateway interface attached)   - 1x ESX Management Network (7 IPs)    - 1 IP per host (x7 hosts) - 1x VM Management Network (16 IPs)    - Fleet Management (1 IP)   - VCF Operations (1 IP)   - VCF Operations Collector (1 IP)   - VCF Automation VIP (1 IP) \*\*   - VCF Automation Node IPs (2 IPs) \*, \*\*   - NSX Manager (1 IP)   - vCenter (1 IP)   - SDDC Manager (1 IP)   - Edge VMs (2 IPs) \*\*   - Supervisor Control Plane (5 consecutive IPs) \*, \*\* - 1x vSAN Network (or NFS if using NFS storage model) (7 IPs)    - 1 IP per host (x7 hosts) - 1x vMotion Network (7 IPs)    - 1 IP per host (x7 hosts) - 1x Host TEP Network (14 IPs)    - 2 IPs per host (x7 hosts) - 1x Edge TEP Network (4 IPs)    - 2 IPs per Edge VM (x2 Edge VMs) \*\* - 1x Edge Uplink Network (2 IPs)    - 1 IP per Edge VM (x2 Edge VMs) \*\*   All IP addresses should have forward and reverse DNS entries configured in your managed DNS server apart from those marked with a \* |
| Virtual Networking \*\* | - Supervisor Service CIDR    - e.g. 10.96.0.0/23 - VPC Private IP Block (Control Plane) - Distributed Transist Gateway Private IP Block (Control Plane) - External IP Block (Control Plane & Workload/Organizations) - Private VPC Block for each Organization’s VPCs - Private TGW IP Block for each Organization |

## Planning and Preparation for the VCF Fleet

| Procedure Grouping | Procedure | Information |
| --- | --- | --- |
| Planning and Preparation | Download the Planning and Preparation Workbook. | The Planning and Preparation Workbook can be located on the Broadcom Technical Documentation site. |
| Prerequisites | Review and ensure compliance with the items listed in the Prerequisite Checklist tab of the Planning and Preparation Workbook. | This will ensure that the all hardware, network and infrastructural prerequisites are met before commencing deployment. |
| Sizing | In a distinct copy of the Planning and Preparation Workbook, populate the Management Domain Sizing tab. | This will ensure that the management domain is adequately sized to host your VCF Fleet deployment. |
| Management Domain | In the same Planning and Preparation Workbook, select the following options on the VCF & VVF Planning tab:   - VMware Cloud Foundation   Deployment Version: 9.0.0.0 - Deployment Specification: VMware Cloud FoundationInstance to perform operation on: First Instance - Operation to be performed: Deploy a new VCF fleet   Populate the Management Domain Creation tab. | This will gather all the required physical network, IP Addressing and infrastructural details required to perform the deployment of the management domain. |