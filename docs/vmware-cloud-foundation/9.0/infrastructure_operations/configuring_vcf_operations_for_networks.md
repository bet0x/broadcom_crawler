---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vrealize-network-insight/configuring-vmware-vrealize-network-insight.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Configuring VCF Operations for networks
---

# Configuring VCF Operations for networks

Configure an instance of the VCF Operations for networks in VCF Operations.

1. From the left menu, click Administration>Integrations.
2. From the Accounts tab in the Integrations page, click Add Account and then select the VCF for Networks card. You can also activate the management pack from the Repository tab, where you will find the card in the Available Integrations section. After the management pack is activated, click Add Account.
3. Configure the adapter instance.

   Option | Description || Name | Enter a name for the adapter. |
   | Description | Enter a description. |
   | FQDN/IP | The FQDN or the IP address of VCF Operations for networks. |
   | Credential | Select and add the credential you want to use to sign on to the environment from the drop-down menu. To add new credentials to access the environment of this management pack, click the plus sign.  - Credential Kind. Select and configure the Credential Type. You can select either the Local, LDAP, or VIDM  This Management pack supports only the Local, LDAP, and vIDM users that are added in the User Management settings of VCF Operations for networks.    - Local - Network Credentials. Enter the credential name, user name of the local user configured in VCF Operations for networks, and password.   - LDAP - Network Credentials. Enter the credential name, LDAP domain configured in VCF Operations for networks, LDAP user name, and LDAP password.   - vIDM - Network Insight Credentials. Enter the credential name, vIDM FQDN/IP integrated with VCF Operations for networks, vIDM user name, and vIDM password for that vIDM user. Credential Name. |
   | Collector / Group | Select the required collector group. |
   | Validate Connection | Test Connection should be successful. |
4. The VCF Operations for networks instance collects events based on common data sources between VCF Operations and VCF Operations for networks. When you deactivate the Import problem events as based on common data sources option, all the events are imported into the VCF Operations.
5. You can collect user-defined events of VCF Operations for networks as notifications in VCF Operations. To do so, activate the Import User defined events as Notifications.
6. Select the severity of the problem events you want to import. By default, all the problem events with moderate and critical severities are imported.
7. Click Add.

   The VCF Operations for networks instance is added to the list. Newly created VCF Operations for networks accounts do not start monitoring the data automatically and you must manually initiate the data collection.