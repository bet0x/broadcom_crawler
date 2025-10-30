---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/vcf-operations-for-logs-deployment-models/high-availability-vcf-operations-for-logs-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > High Availability VCF Operations for Logs Model
---

# High Availability VCF Operations for Logs Model

The High Availability VCF Operations for logs model consists of a three-node deployment behind and internal load balancer. This model provides resiliency at both the application level through the clustered deployment as well as the vSphere cluster level through vSphere HA and vSphere DRS functionality.

**High Availability VCF Operations for Logs Model**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/4fc9d3ff-0cc2-4420-a1fe-2a2531d07f04.original.svg)

## High Availability VCF Operations for Logs Model Attributes

A High Availability VCF Operations for Logs has the following attributes.

| Attribute | Detail |
| --- | --- |
| Centralized management | Provides a centralized log management framework for vCenter, ESX, NSX, VCF Operations, VCF Automation, and VCF Identity Broker. |
| Availability | Relies on cluster technology in the event of an outage or ESX HA technology in the case of a host failure. |
| Scalability | Supports scale-up and scale-out. |
| Recoverability | Restore through a backup. |

## High Availability VCF Operations for Logs Model Options

A High Availability VCF Operations for Logs Model can leverage options from the design areas listed below, depending on objectives.

| Design Area | Options |
| --- | --- |
| Appliance Size | - Small - Medium - Large |

## High Availability VCF Operations for Logs Model Design Requirements

High Availability VCF Operations for Logs Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-LOGS-REQD-HA-001 | Deploy VCF Operations for logs as a three node cluster - one primary and two worker nodes with an integrated load balancer, in the default management vSphere cluster. | - Provides high availability. - Using the integrated load balancer prevents a single point of failure. - Using the integrated load balancer simplifies the VCF Operations for logs deployment and subsequent integration. | - You must deploy a minimum of three appropriately sized nodes. - You must size all nodes identically. - If the capacity of your VCF Operations for logscluster must expand, identical capacity must be added to each node. |
| VCF-LOGS-REQD-HA-002 | Protect all VCF Operations for logs cluster nodes by using vSphere High Availability. | Supports the availability objectives for VCF Operations for logs without requiring manual intervention during an ESX host failure event. | None. |
| VCF-LOGS-REQD-HA-003 | Apply a vSphere Distributed Resource Scheduler (DRS) anti-affinity rule to the VCF Operations for logs cluster nodes. | Using vSphere DRS prevents the VCF Operations for logs cluster nodes from running on the same ESXhost and risking the high availability of the cluster. | None. |

## High Availability VCF Operations for Logs Model Design Recommendations

Common VCF Operations for Logs Design Recommendations for All Models



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-LOGS-RCMD-COM-001 | Install the content pack for NSX from the Marketplace. | Enables log analysis of NSX based logs. | Internet access is required to access the Marketplace. |
| VCF-LOGS-RCMD-COM-002 | Configure a retention period for VCF Operations for logs  according to your design objectives. | Accommodates logs from the expected number of logging sources in VMware Cloud Foundation platform. | None. |
| VCF-LOGS-RCMD-COM-003 | Configure alert notifications. | Activates alerts from VCF Operations for logs sent to administrators and operators. | If using email for notifications, you must configure the SMTP server settings in VCF Operations for logs. |
| VCF-LOGS-RCMD-COM-004 | Enable vCenter adapter for VCF Operations for Logs | To gather logs from vCenter the Logs adapter needs to be manually enabled. It is not enabled by default. | Requires manually enabling per adapter. |