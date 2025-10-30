---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects/monitoring-and-troubleshooting-within-projects.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Monitoring and Troubleshooting within NSX Projects
---

# Monitoring and Troubleshooting within NSX Projects

NSX supports the monitoring of network traffic
within Projects for debugging or troubleshooting purposes. You can also view alarms raised
for a Project.

An Enterprise Admin can view alarms within
the default space and across all projects while the Project Admin can only view
project-specifc alarms.

## Traceflow

An Enterprise Admin and the Project Admin
can use the Traceflow tool to inspect the path of a packet. While an Enterprise
administrator can run a trace across the default space and across all projects, the
Project Admin can perform a trace only within a project. Traceflow can be run on VMs
and ports that are a part of the same Local Manager site.

To run a trace across projects as an
Enterprise Admin, ensure that you select All Projects from
the project switcher menu. The UI workflow for performing a Traceflow in a project
remains the same as it currently exists for the Default view
(default space) of your NSX
deployment.

For more information on Traceflow, see
[Perform a Traceflow](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/perform-a-traceflow.html).

To perform a trace as a Project Admin,
navigate to Plan & TroubleshootTraffic AnalysisTraceflow Get Started in your project space.

Specify the source and destination
information according to the traffic type and click Trace.
The output includes a table listing the observed packets. Details of entities that
belong to the default project and encountered during the trace, are hidden from view
in the Traceflow output for the project.

## Port Mirroring

Only the Enterprise Admin can configure
port mirroring from the default space for VMs in a project. This feature is
currently unavailable to the Project Admin and only the Enterprise Admin can view
the results in the default space.

To configure port mirroring for a
project, create appropriate groups in the default space and add your tagged VMs from
the project to these groups.

Navigate to Plan & TroubleshootPort Mirroring, select the session type, and set the groups as
Source and Destination.

For more information on port mirroring,
see [Add a Port Mirroring Session](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/add-a-port-mirroring-session.html).

## IPFIX

Only the Enterprise Admin can configure
IPFIX from the default space for VMs in a project. This feature is currently
unavailable to the Project Admin and only the Enterprise Admin can view the results
in the default space.

To configure IPFIX for a project, create
appropriate groups in the default space and add your tagged VMs from the project to
these groups.

Navigate to Plan & TroubleshootIPFIX, select the appropriate group under Applied To
for your IPFIX profile.

For more information on IPFIX, see [Network Monitoring](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring.html).