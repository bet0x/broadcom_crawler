---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/configure-a-node-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure a Node Profile
---

# Configure a Node Profile

You can configure settings such
as time zone, NTP servers, SNMP, and syslog servers to apply to all NSX Manager and Edge nodes.

In this release, only one node
profile is supported. This profile represents a collection of time zone, NTP servers,
SNMP configuration and syslog servers. By default, the node profile is applied to all
nodes, unless the node is configured to not accept such configuration from the
NSX Manager. To prevent a node
from accepting the node profile, use the CLI command set node central-config
disabled on that node.

1. With admin privileges, log in
   to NSX Manager.
2. Select SystemFabricProfiles.
3. Click the Node
   Profiles tab.
4. Click All NSX
   Nodes in the Name column.
5. Click
   Edit to configure the time zone and NTP
   servers.
6. In the Syslog
   Servers section, click Add to add a
   Syslog server.
   1. Enter the FQDN or IP
      address of the Syslog server.
   2. Specify a port
      number.
   3. Select a protocol.

      The available protocols are TCP,
      UDP, and LI (Aria Operations for
      Logs).
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
7. In the SNMP
   Polling section, under v2c, click
   Add to add an SNMPv2c community.
   1. Enter a name for the
      community.
   2. Enter a
      Community String value.

      This value is used for authentication.
8. In the SNMP
   Polling section, under v3, click
   Add to add an SNMPv3 user.
   1. Enter a user name.
   2. Enter an authentication
      password.

      You can click the icon on the right to show or hide the
      password.
   3. Enter a private
      password.

      You can click the icon on the right to show or hide the
      password.
9. In the SNMP
   Traps section, under v2c, click
   Add to add an SNMPv2c trap configuration.
   1. Enter a FQDN or IP
      address.
   2. Specify a port
      number.
   3. Enter a name for the
      community.
   4. Enter a
      Community String value.

      This value is used for authentication.
10. In the SNMP
    Traps section, under v3, click
    Add to add an SNMPv3 trap configuration.
    1. Enter a FQDN or IP
       address.
    2. Specify a port
       number.
    3. Enter a user name.

Verify that the profile configurations
are applied to the NSX Manager and
NSX Edge nodes. Log in to the
NSX Manager and NSX Edge nodes with
admin privileges, and run the following commands:

- get clock
- get ntp-server
- get logging-servers
- get snmp v2-targets
- get snmp v3-targets
- get snmp v2-configured
- get snmp v3-configured
- get snmp v3-engine-id
- get snmp v3-protocols
- get snmp v3-users

For more information about these commands including examples, see the NSX Command-Line Interface Reference.

Error situations
:   If the node profile
    configurations are not applied successfully, then there are two
    possibilities:

    - The central
      configuration was not synchronized with the remote node due to
      connectivity issues between NSX Manager and the remote node. In this
      case, you cannot do anything from the central configuration
      side.
    - The central
      configuration was synchronized with the remote node, but the
      command to apply the central configuration failed to run. In
      this case, you can check syslog on the remote node.

      In the logs,
      search for the
      subcomp="central\_node\_config\_update"
      string to look for any errors.

      For example, the
      syslog exporter configuration might fail if the host name
      specified cannot be resolved to IP addresses, or if a second
      VCF Operations for logs server is being configured.

      The following
      example logs show the error messages:

      Log example
      1:

      ```
      2020-05-18T22:56:06.485Z vmw-svc.nsxmanager-sb-36265022-1-rhel NSX 24904 - [nsx@6876 comp="nsx-manager" subcomp="central_node_config_update" username="root" level="INFO"] No change in timezone 2020-05-18T22:56:07.184Z vmw-svc.nsxmanager-sb-36265022-1-rhel NSX 24904 - [nsx@6876 comp="nsx-manager" subcomp="central_node_config_update" username="root" level="INFO"] No change in NTP configuration 2020-05-18T22:56:07.210Z vmw-svc.nsxmanager-sb-36265022-1-rhel NSX 24904 - [nsx@6876 comp="nsx-manager" subcomp="central_node_config_update" username="root" level="INFO"] Updating Syslog configuration 2020-05-18T22:56:08.826Z vmw-svc.nsxmanager-sb-36265022-1-rhel NSX 24904 - [nsx@6876 comp="nsx-manager" subcomp="central_node_config_update" username="root" level="WARNING"] Failed to add syslog exporter {"port": 514, "exporter_name": "264aa005-dfb0-4942-a1c4-f749bfc1a2c4", "protocol": "TCP", "level": "ERR", "server": "vikas.2020.com"}, response: {#012  "error_code": 36569,#012  "error_message": "Error modifying firewall rule due to invalid hostname.",#012  "module_name": "node-services"#012}, status: 400, err: 400 Client Error: Bad Request for url: http://localhost:7441/api/v1/node/services/syslog/exporters
      ```

      Log example
      2:

      ```
      2020-05-18T22:56:08.839Z vmw-svc.nsxmanager-sb-36265022-1-rhel NSX 24904 - [nsx@6876 comp="nsx-manager" subcomp="central_node_config_update" username="root" level="WARNING"] Failed to add syslog exporter {"port": 514, "exporter_name": "f4e088d4-4b45-42fe-ba1d-7f98838c7f61", "protocol": "LI", "level": "INFO", "server": "loginsight.vmware.com"}, response: {#012  "error_code": 36400,#012  "error_message": "Maximum number of loginsight servers exceeded",#012  "module_name": "node-services"#012}, status: 400, err: 400 Client Error: Bad Request for url: http://localhost:7441/api/v1/node/services/syslog/exporters
      ```

      Log example
      3:

      ```
      2020-05-18T22:56:10.639Z vmw-svc.nsxmanager-sb-36265022-1-rhel NSX 24904 - [nsx@6876 comp="nsx-manager" subcomp="central_node_config_update" username="root" level="WARNING"] Failed to add syslog exporter {"port": 514, "exporter_name": "d0dc1797-b5dc-42ba-b07d-fe107dd70111", "protocol": "UDP", "level": "INFO", "server": "logging.vmware.com"}, response: {#012  "error_code": 36569,#012  "error_message": "Error modifying firewall rule due to invalid hostname.",#012  "module_name": "node-services"#012}, status: 400, err: 400 Client Error: Bad Request for url: http://localhost:7441/api/v1/node/services/syslog/exporters
      ```