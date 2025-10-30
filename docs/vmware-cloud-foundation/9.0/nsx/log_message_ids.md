---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/log-messages-and-error-codes/log-message-categories.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Log Message IDs
---

# Log Message IDs

In a log message,
the message ID field identifies the type of message. You can use the
messageid parameter
in the
set
logging-server command to filter which log messages are sent to a
logging server.

Log Message
IDs



| Message ID | Examples |
| --- | --- |
| FABRIC | Host node  Host preparation  Edge node  Transport zone  Transport node  Uplink profiles  Cluster profiles  Edge cluster |
| SWITCHING | Logical switch  Logical switch ports  Switching profiles  switch security features |
| ROUTING | Logical router  Logical router ports  Static routing  Dynamic routing  NAT |
| FIREWALL | Firewall rules  Firewall rule sections |
| FIREWALL-PKTLOG | Firewall connection logs  Firewall packet logs |
| GROUPING | IP sets  Mac sets  NSGroups  NSServices  NSService groups  VNI Pool  IP Pool |
| DHCP | DHCP relay |
| SYSTEM | Appliance management (remote syslog, ntp, etc)  Cluster management  Trust management  Licensing  User and roles  Task management  Install  Upgrade (NSX Manager, NSX Edge and host-packages upgrades )  Realization  Tags |
| MONITORING? | SNMP  Port connection  Traceflow |
| - | All other log messages. |