---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vmware-cloud-foundation/configuring-vmware-cloud-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Configuring a VCF Account in VCF Operations
---

# Configuring a VCF Account in VCF Operations

You must configure a VCF account to monitor a VCF Instance. After configuration, all VCF domains are automatically discovered and configured along with their connection details and credentials of underlying adapters for vCenter, vSAN, and NSX.

1. From the left menu, click AdministrationIntegrations.
2. On the Accounts tab, click Add.
3. On the Accounts Types page, click VMware Cloud Foundation.
4. Enter a Name and Description for the account.
5. Select the Physical Data Center you want to associate with the VCF account.

   If no physical data center is created or if you want to create a new physical data center for your account, you can add a new physical data center. For more information, see [Adding Physical Data Centers in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/-configuring-administration-settings/adding-physical-data-centers.html)
6. Enter the FQDN for the SDDC Manager you are trying to connect.
7. To add credentials for the VCF Instance, click the Add icon, and enter the required credentials.

   The credentials must be associated with the admin role in VCF.

   If you are using an AD or domain integrated account for authenticating your VCF Instance, ensure you enter the username as username@domain or domain\username.
8. Determine which VCF Operations collector or collector group or cloud proxy is used to manage the account. If you have multiple collectors or collector groups in your environment, and you want to distribute the workload to optimize performance, select the collector or collector group or cloud proxy to manage the adapter processes for this instance. The SDDC Manager FQDN must be reachable from selected collector or collector group.
9. Click Validate Connection to validate the connection.

   The Review and Accept Certificate wizard appears. Click Accept to continue the validation.
10. Click Advanced Settings.
    - Enable Domain Monitoring on Creation: Change this setting to true to enable data collection and monitoring of newly discovered and configured domains.

      By default, this setting is set to false. If you configure a VCF account with the default setting, data collection and monitoring of domains is disabled. If you edit the VCF account and change this setting to true, data collection and monitoring is enabled but it is done only for the newly discovered domains.
    - VCF Configuration Limit File Name: Enter the name of the file that contains the VCF configuration max soft and hard limits and their configured values in VCF Operations.
11. Click Add and select an add option for this VCF instance.

    License and vSphere Client plug-in management is supported only for VCF accounts of versions 9.0 or later. If your VCF account is 9.0 or later and is not managed by any VCF Operations instance, the current VCF Operations instance takes up the license and vSphere Client plug-in management. If you do not have the required privileges for license and vSphere Client plug-in management, VCF account will be added only for monitoring purposes. For more information, see [Use and Configure your vSphere Client](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/using-the-vsphere-client-host-management/working-with-the-vsphere-client-host-management.html#GUID-6E321032-5350-4008-953A-3167B3BF18C1-en).

    After you integrate a VCF account with a VCF Operations instance for license management, it takes up to 15 minutes before the VCF account appears in the License tab of VCF Operations.

    If your VCF account is a version prior to 9.0, you can only activate vSphere Client plug-in management. If your VCF account is a version prior to 9.0, and is not managed by any VCF Operations instance, the current VCF Operations instance takes up the vSphere Client plug-in management. If you do not have the required privileges for vSphere Client plug-in management, VCF account will be added only for monitoring purposes.

    - Add all associated vCenter systems only for monitoring and fleet management: Use this option if you want multiple VCF Operations instances to monitor and provide fleet management to vCenter systems of the VCF account you are adding.
    - Add all associated vCenter systems for monitoring, fleet management, and license and vSphere Client plug-in management by replacing the current integration: Use this option for version 9.0 or later., if another VCF Operations provides license and vSphere Client plug-in management for the management domain vCenter for the VCF you are adding. All current integration of all associated vCenter systems will be replaced and you must assign new licenses. For more information, see [Assign a Primary License to a vCenter Instance or a VCF Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/assign-a-licenses-to-a-vcenter-instance.html).

      For versions prior to 9.0, license management is not applicable. You can use this option if another VCF Operations provides vSphere Client plug-in management for the management domain vCenter for the VCF account you are adding. All current integration of all associated vCenter systems will be replaced.

    If the management domain vCenter does not have a license and vSphere Client plug-in management, the current VCF Operations starts to manage it automatically.

    For VCF 9.0 and later, the management domain vCenter, vSAN and NSX are created using system managed credentials. Workload domains are configured after one collection cycle.

    If Log Collection and Network and Flow Collection are activated for vCenter and NSX, separate system managed credentials are created for both.

    The VCF account, with the configured domains, is added to the Accounts page. The newly added VCF account does not start monitoring the data automatically and you must manually initiate the data collection.
12. On the Accounts tab, locate the VCF account, click the vertical ellipsis and then click Start Collecting All.

The VCF account is added and starts collecting data in VCF Operations.

You can view the operations of your VCF accounts and their domains from the VCF Health page. For more information, [What is VCF Health](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/using-vcf-operations-diagnostics/how-to-use-vcf-diagnostics-to-monitor-and-correct-your-environment/what-is-vcf-health.html).

If you are using SDDC Manager 9.0 or later, you can also monitor your VCF account and collect data seamlessly using system managed credentials. After you create a VCF account in VCF Operations, you can edit the VCF account and activate System Managed Credentials. Activating system managed credentials for your VCF account does not affect the underlying vCenter and NSX accounts. Newly created vCenter and NSX accounts are automatically configured using system managed credentials if the corresponding vCenter and NSX endpoints are 9.0. For password rotation, click Rotate to rotate your system managed credential password. You must rotate system managed credentials for individual endpoints. For more information, see [Account Management Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-information-security-and-access-design-for-esxi/service-account-design-for-vmware-cloud-foundation.html).

Optionally, you can also configure the vCenter, vSAN, NSX, and Service Discovery instances in the VCF account.

- To configure a vCenter account, see [Configuring a vCenter Account in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations.html).
- To configure a vSAN account, see [Configuring a vSAN Account](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsan-overview/configure-a-vsan-adapter-instance.html).
- To configure the NSX account, see [Configuring the NSX Account in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/nsx-introduction/configure-nsx-management-pack.html).
- To configure Service Discovery, see [Configure Service and Application Discovery](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/workload-monitoring-and-observability/about-service-discovery/configure-service-and-application-discovery.html).