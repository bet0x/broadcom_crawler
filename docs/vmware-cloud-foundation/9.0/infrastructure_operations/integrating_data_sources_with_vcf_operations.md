---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Integrating Data Sources with VCF Operations
---

# Integrating Data Sources with VCF Operations

You can extend the monitoring capabilities of VCF Operations by installing and configuring integrations in VCF Operations to connect to, and analyze data from external data sources in your environment. Once connected, you can use VCF Operations to monitor and manage objects in your environment. These integrations are also referenced as Management Packs.

An integration can be a connection to a data source, or include predefined dashboards, widgets, alerts, and views.

Integrations include accounts, dashboards, reports, alerts, and other content. The cloud accounts and other accounts comprise of adapters, using which VCF Operations manages communication and integration with other products, applications, and functions. When an integration is installed and the accounts are configured, you can use the VCF Operations analytics and alerting tools to manage the objects in your environment.

VMware integrations include native, non-native, and external management packs.

For a fresh deployment of VCF Operations, the activation status of integrations are as follows:

Integration Activation Status



| Integration Name | Activated by Default? | Can be Deactivated? |
| --- | --- | --- |
| vCenter | Yes | No |
| VMware Cloud Foundation | Yes | Yes |
| vSphere Supervisor | Yes | No |
| vSAN | Yes | No |
| Service Discovery | Yes | No |
| VCF Automation for VM Apps Organization | No | Yes |
| VCF Automation for All Apps Organization | No | Yes |
| OS and Application Monitoring | Yes | No |
| VCF for Networks | No | Yes |
| NSX | Yes | No |
| Ping | No | Yes |
| PCI Compliance | No | Yes |
| ISO Compliance | No | Yes |
| HIPAA Compliance | No | Yes |
| FISMA Compliance | No | Yes |
| DISA Compliance | No | Yes |
| CIS Compliance | No | Yes |

The list of activated and available integrations, accounts, and repository are all available from a central Integrations page in VCF Operations . This page can be accessed from the left menu by clicking AdministrationIntegrations.

## Non-Native Management Packs and Management Pack Builder

If there’s a technology without a current, native, management pack, you have the option to install a non-native pack or build your own using VCF Operations Management Pack Builder.

With the Management Pack Builder, you can create custom management packs for use in VCF Operations. This is a no-code solution for bringing in data from an external API and either creating new resources or extending your VMware and third party resources with new data, relationships, and events. For more information, see [Management Pack Builder.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/extending-monitoring-capabilities/cloud-foundation-operations-configuration-guide-management-pack-builder.html)

## Upgrade Considerations

The native integrations in VCF Operations are reinstalled if VCF Operations is upgraded.