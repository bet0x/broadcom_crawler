---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/vcf-operations-for-logs-deployment-models/simple-vcf-operations-for-logs-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Simple VCF Operations for Logs Model
---

# Simple VCF Operations for Logs Model

A single VCF Operations for logs node deployed in a vSphere cluster. Availability is provided by the native vSphere HA functionality within the vSphere cluster.

**Simple VCF Operations for Logs Model**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ae726688-f973-4db7-9509-ef51cde41934.original.svg)

## Simple VCF Operations for Logs Model Attributes

A Simple VCF Operations for Logs Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Centralized management | Provides a centralized log management framework for vCenter, ESX, NSX, VCF Operations, VCF Automation, and VCF Identity Broker. |
| Availability | Relies on vSphere HA to restart the nodes in the event of an ESX host failure. |
| Scalability | Supports scale-up and scale-out. |
| Recoverability | Restore through a backup. |

## Simple VCF Operations for Logs Model Options

A Simple VCF Operations for Logs Model can leverage options from the design areas listed below, depending on objectives.

| Design Area | Options |
| --- | --- |
| Appliance Size | - Small - Medium - Large |

## Simple VCF Operations for Logs Model Design Requirements

Simple VCF Operations for Logs Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-LOGS-REQD-SIM-001 | Deploy VCF Operations for logs as a single node - one primary node with an integrated load balancer, in the default management vSphere cluster. | - Supports the simple deployment objective. - Supports scale-out to a high availability model. | None. |

## Simple VCF Operations for Logs Model Design Recommendations

Common VCF Operations for Logs Design Recommendations for All Models



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-LOGS-RCMD-COM-001 | Install the content pack for NSX from the Marketplace. | Enables log analysis of NSX based logs. | Internet access is required to access the Marketplace. |
| VCF-LOGS-RCMD-COM-002 | Configure a retention period for VCF Operations for logs  according to your design objectives. | Accommodates logs from the expected number of logging sources in VMware Cloud Foundation platform. | None. |
| VCF-LOGS-RCMD-COM-003 | Configure alert notifications. | Activates alerts from VCF Operations for logs sent to administrators and operators. | If using email for notifications, you must configure the SMTP server settings in VCF Operations for logs. |
| VCF-LOGS-RCMD-COM-004 | Enable vCenter adapter for VCF Operations for Logs | To gather logs from vCenter the Logs adapter needs to be manually enabled. It is not enabled by default. | Requires manually enabling per adapter. |