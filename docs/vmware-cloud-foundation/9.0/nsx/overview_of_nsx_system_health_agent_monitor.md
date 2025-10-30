---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/monitoring-nsx-host-transport-nodes-container-topic/overview-of-nsx-system-health-agent-monitor.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Overview of NSX System Health Agent Monitor
---

# Overview of NSX System Health Agent Monitor

Learn about the basic concepts of a SHA monitor, which is a component that is introduced in the System Health Agent (SHA) framework.

SHA is the distributed system health agent in NSX. This framework monitors statistics (metrics) of various NSX components, such as ESX hosts, NSX edges, NSX Manager appliance, and so on. SHA monitors the component statistics, analyzes them, alerts abnormality, and triggers remediation actions when specific conditions are met.

Monitor
:   A monitor is a component of the SHA framework that monitors various statistics (metrics) about the system health and takes corresponding action. For instance, it exports statistics to a destination for users to view the system health, triggers alarms to notify users, and dumps statistics to a file for offline analysis. A monitor replaces the SHA plug-ins, which were introduced in an earlier NSX release. A monitor provides detailed descriptions of the statistics so that users know the purpose of each statistic, and how to control the monitor when required.

    For example, the esx-obsrv-stats-monitor contains descriptions of all the observability statistics that are collected from an ESX host transport node.

    Currently, a monitor supports exporting statistics to a single destination, which is the NSX Manager.

Monitor profile
:   A monitor profile helps you to control the monitor by configuring a set of properties.

    For example, some configuration properties in the monitor profile are:

    - enable
    - check\_interval
    - applied\_to\_group\_paths

    Only a few configuration properties are listed here. To learn about all the configuration properties in a monitor profile, see the schema of the SHA monitor profile in the NSX API Guide at:

    ```
    GET https://<nsx-mgr>/policy/api/v1/infra/sha/monitors/<monitor-id>/profiles/<profile-id>
    ```

    You can access the monitor and monitor profiles only with NSX APIs. Currently, these components are not exposed in the NSX Manager UI.

    To get the list of all monitor IDs, use the following API:

    ```
    GET https://<nsx-mgr>/policy/api/v1/infra/sha/monitors
    ```

    To get the list of all profiles for a specific monitor, use the following API:

    ```
    GET https://<nsx-mgr>/policy/api/v1/infra/sha/monitors/<monitor-id>/profiles
    ```

    In a multi-tenant NSX deployment, users in projects and NSX VPCs cannot consume the monitor and monitor profile APIs. These APIs are currently available for consumption only to users in the default space.

    Each monitor has a system-created default profile. For instance, the default profile of the esx-obsrv-stats-monitor is applied to all the host transport nodes in the system where this monitor runs. When you update the configuration of the default profile, the change affects all the nodes. The default profile cannot be deleted.

    You can create a user-defined (custom) profile to override the default profile for a specific group of host transport nodes. If multiple profiles are applied to the monitor on a host transport node, the last applied profile will override the other profiles. The default profile has the lowest priority.

    Regardless of whether you are configuring the default profile or a custom profile of the monitor, certain properties in the profile cannot be edited.

    For example:

    - The default profile of the esx-obsrv-stats-monitor is applied to the system-created default group, which contains all the host transport nodes in the system. You cannot edit the applied\_to\_group\_paths property of the default profile.
    - You cannot deactivate the esx-obsrv-alarms-monitor by setting the enable property in the profile to false. This monitor reports alarms in the system and is always activated.

## Types of Monitors

The SHA framework contains two main types of monitors.

Metric-exporter monitors
:   These monitors are used to export metrics (statistics) to a destination, such as NSX Manager. For example, esx-obsrv-stats-monitor.

    For a metric-exporter monitor, the system supports only one user-defined (custom) profile.

Standard monitors
:   These monitors are used to do tasks other than exporting metrics, such as reporting alarms to NSX Manager, dumping statistics to a file, and so on. For example, esx-obsrv-alarms-monitor, esx-obsrv-segment-stats-file-dump-monitor.

    For a standard monitor, there is no restriction on the number of user-defined (custom) profiles that you can create.

A monitor defines a high level category of statistics (metrics) that it controls. The statistics in a monitor are organized in multiple sub-categories. A sub-monitor is defined to control individual sub-categories. By default, the configuration that is defined for the parent monitor is applied to all the sub-monitors in the parent monitor. If required, you can edit the configuration of the sub-monitors.

For example:

The esx-obsrv-stats-monitor is a metric-exporter type of monitor. It contains two sub-monitors of metric-exporter type, which are called esx-obsrv-datapath-traffic-stats-monitor and esx-obsrv-datapath-infra-stats-monitor.

The advantage of categorizing the statistics in a monitor with multiple sub-monitors is that you can control all sub-monitors together with the parent monitor. You don't need to run separate API calls for the individual sub-monitors to configure their properties.