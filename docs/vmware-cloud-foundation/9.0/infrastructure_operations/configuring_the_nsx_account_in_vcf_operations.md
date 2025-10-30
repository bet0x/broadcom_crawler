---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/nsx-introduction/configure-nsx-management-pack.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Configuring the NSX Account in VCF Operations
---

# Configuring the NSX Account in VCF Operations

You can configure your NSX account in VCF Operations.

To view the roles and permissions associated with the VIDM users collecting the NSX adapter, see [NSX Introduction](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/nsx-introduction.html#GUID-66a9570c-7fb1-4649-bc9b-782ca949b782-en)

- To use Principal Identities authentication in VCF Operations you must have created a Principal Identity user in NSX.
- Ensure that you have the client certificate and the key to authenticate the Principal Identity users in VCF Operations.

1. From the left menu, click AdministrationIntegrations.
2. On the Accounts tab, click Add, and on the Accounts Types page, select NSX.
3. Configure the adapter instance.

   | Option | Action |
   | --- | --- |
   | Name | Enter the name for the NSX instance as you want it to appear in VCF Operations. |
   | Description | Enter any additional information that helps you manage your instances. |
4. Configure the connection.

   | Option | Action |
   | --- | --- |
   | Virtual IP/ NSX | Enter the FQDN, the IP address, or the Virtual IP of the NSX. Both IPv4 address and IPv6 address formats are supported. |
   | Credential | Select the credential you want to use to sign on to the environment from the drop-down menu. To add new credentials to access the NSX environment, click the plus sign. 1. From the Manage Credential dialog, you can click the Credential Kind drop-down and select NSX Client Certificate Crentials or NSX Credentials. The NSX Client Certificate allows you to use Principal Identities user or certificate-based client for authentication and the NSX Credential allows you to use local administrator or VMware Identity Manager for authentication. 2. Enter the credential details based on your selection. For NSX Credentials, enter the following details.    - Credential Name - The name by which you are identifying the configured credentials.    - User Name - The user name of the NSX instance.    - Password - The password of the NSX instance.  For NSX Client Certificate Credentials, enter the following details.    - Credential Name - The name by which you are identifying the configured credentials.    - Client Certificate Data - Enter the value of the client certificate data associated with the principal user.    - Client Key Data - Enter the value of the client key data associated with the principal user. |
   | Collector /Group | Determine which VCF Operations collector or collector group is used to manage the account. If you have multiple collectors or collector groups in your environment, and you want to distribute the workload to optimize performance, select the collector or collector group to manage the adapter processes for this instance. Review and Accept Untrusted Certificates  When you upgrade VCF Operations, the NSX adapter moves to a warning state and the data collection stops. This happens only when you have an adapter that presents a self-signed certificate, or a certificate signed by an untrusted Certification Authority.  To continue the adapter configuration, you must Validate the Connection, where you are prompted to review and accept the certificate. If you have a multi-node cluster configuration, then you are prompted to review and accept the certificate for each node. |
   | Network Operations | |
   | Network & Flow | Select the option to activate network and flow.  Install the operations-network appliance from Fleet ManagementLifecycle to activate this option |
   | Advanced Settings | |
   | Exclude Resources from Monitoring | Select specific NSX resources that you want to exclude from monitoring in VCF Operations. Once the exclusion is applied, the monitoring for the specified resources will be disabled. Earlier the Management Pack for NSX would collect all the data and monitor all the resource kinds associated with the Management Pack, but now it allows you to exclude specific resources from monitoring. |
   | Exclude Management Services from Monitoring | Select specific NSX management services that you want to exclude from monitoring in VCF Operations. Once the exclusion is applied, the monitoring for the specified services will be disabled. Earlier the Management Pack for NSX would collect all the data and monitor all the services associated with the Management Pack, but now it allows you to exclude specific services from monitoring. |
   | Exclude Logical Router Services from Monitoring | Select the specific router service you want to exclude from monitoring in VCF Operations. Once the exclusion is applied, the monitoring for the specified services will be disabled. |
   | Auto Discovery | Set the Auto Discovery to True or False. - Auto Discovery - True - Activates auto-discovery of the new objects added to the monitored system. By default, this field is set to True. - Auto Discovery - False - Deactivates auto discovery, you must manually discover the objects from the system which you want to monitor. |
   | Import Alerts from NSX | You can directly import alerts from NSX into VCF Operations by setting the Import Alerts from NSX field to True.  Depending on the number of alerts and the system's performance, importing alerts into VCF Operations may take some time.  By default, this field is set to False. |
5. Click Add to save the configurations.

   The adapter instance is added to the list. Newly created NSX accounts do not start monitoring the data automatically and you must manually initiate the data collection.
6. On the Accounts tab, locate the NSX account, click the vertical ellipsis and then click Start Collecting All.

Verify that the adapter is configured and is collecting data.