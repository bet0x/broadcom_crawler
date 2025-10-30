---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/working-with-events-and-alarms/troubleshooting-communication-alarms-between-your-nsx-manager-and-host.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Troubleshooting Communication Alarms Between Your NSX Manager and Host
---

# Troubleshooting Communication Alarms Between Your NSX Manager and Host

You
may experience a loss of communication alarm between the NSX Manager and the host. Heartbeats are sent every minute from the
manager node to the host node. This alarm notifies you of a heartbeat loss which is an
indication of the last time NSX Manager
and the host communicated.

If the host loses connectivity to the NSX Manager or to the controller service, a
full configuration or runtime state synchronization, respectively, gets sent to the host
when connectivity is restored.

Alarm information is displayed in several
locations within the NSX Manager
interface. For a complete list of events, see NSX Event Catalog. For example, alarms display on the Alarms page of
the NSX Manager UI. Every alarm
contains a recommended action. Use this action and the information in this topic to
troubleshoot your alarm.

The following table describes the IP protocol
used, channel health check mechanism and related timers, authentication, security, and
communication channel health check validations. It also provides insights into the
several common issues that lead to degraded fabric health.

To validate the health of the communication
channels, use the NSX Manager Health Monitoring table details.

NSX Manager Health
Monitoring



| Communication | IP Protocol and Port | Channel | Authentication | Health Check |
| --- | --- | --- | --- | --- |
| Management Plane Appliance Proxy Hub (MP APH) to host connectivity | TCP:1234 | TLS between Manager and host | Mutual TLS authentication based on self-signed or CA certificates between clients (hosts/transport nodes) and server (APH in MP) | To determine the connectivity status between transport node and managers, use get managers CLI command on the transport node. Various alarms get raised when communication channels between MP and Host are in a disconnected state.   - management\_channel\_to\_transport\_node\_down   alarm gets raised when MP and host are disconnected for more   than 5 minutes. Alarm description mentions transport node   name and IP address: management channel to transport node   {transport\_node\_name} ({transport\_node\_address}) is down for   5 minutes. - management\_channel\_to\_transport\_node\_down\_long   alarm gets raised when MP and host are   disconnected for more than 15 minutes. Alarm description   mentions transport node name and IP address: management   channel to transport node {transport\_node\_name}   ({transport\_node\_address}) is down for 15. - network\_latency\_high alarm gets   raised when the latency between MP and host is more than 150   ms for a duration of 5 minutes. Alarm description mentions   transport node name and IP address: The average network   latency between manager nodes and host {transport\_node\_name}   ({transport\_node\_address}) is more than 150 ms for 5   minutes.   If the host gets detached for any reason the alarms are cleared. |
| Central Control Plane (CCP) to host (NSX-Proxy) connectivity | TCP: 1235 | TLS between CCP and host | Mutual TLS authentication based on self-signed or CA certificates between client (hosts/transport nodes) and server (CCP) | To determine the connectivity status between the transport node and CCP, use get controllers CLI command.  Various alarms get raised when communication channels between MP and host are in a disconnected state.  - control\_channel\_to\_manager\_node\_down   alarm gets raised when host and CCP are disconnected for   more than 3 minutes. Alarm description: The transport   node {entity\_id} control plane connection to manager   node {appliance\_address} is down for at least   {timeout\_in\_minutes} minutes from the transport node’s   point of view. - control\_channel\_to\_manager\_node\_down\_too\_long   alarm gets raised when host and CCP are disconnected for   more than 15 minutes. Alarm description: The transport   node {entity\_id} control plane connection to manager   node {appliance\_address} is down for at least   {timeout\_in\_minutes} minutes from the transport node’s   point of view. |