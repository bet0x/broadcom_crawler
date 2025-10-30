---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/log-messages-and-error-codes/add-syslog-servers-for-nsx-nodes.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add Syslog Servers for NSX Nodes
---

# Add Syslog Servers for NSX Nodes

You can use the Node Profiles page in NSX Manager to add syslog servers for NSX Manager and NSX Edge nodes.

By default, the node profile is
applied to all nodes, unless the node is configured to not accept such configuration
from the NSX Manager. To prevent a node from accepting the node profile, use the CLI
command set node central-config disabled on that node.

1. From your browser, log in with
   admin privileges to an NSX Manager at
   https://nsx-manager-ip-address.
2. Select SystemFabricProfiles.
3. Click the Node
   Profiles tab.
4. Click All NSX
   Nodes in the Name column.
5. In the Syslog
   Servers section, click Add to add a
   Syslog server.
   1. Enter the FQDN or IP
      address of the Syslog server.
   2. Specify a port
      number.
   3. Select a protocol.

      The available protocols are TCP,
      UDP, and LI (Log
      Insight).
   4. Select a log
      level.

      The available levels are Emergency,
      Alert, Critical,
      Error, Warning,
      Notice, Information,
      and Debug.

      When you choose a level,
      you will also see the logs for all the previous levels (starting
      with the Emergency level). For example, if
      you choose Emergency, you will see
      Emergency-level logs. If you choose
      Critical, you will see logs for
      Emergency, Alert
      and Critical. If you choose
      Information, you will see logs for
      Emergency, Alert,
      Critical, Error,
      Warning, Notice,
      and Information. If you choose
      Debug, you will see messages for all log
      levels.
   5. Click
      Add.
6. Repeat step 5 to add more syslog
   servers, if required.