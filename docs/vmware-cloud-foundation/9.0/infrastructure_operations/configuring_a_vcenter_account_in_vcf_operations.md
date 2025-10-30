---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Configuring a vCenter Account in VCF Operations
---

# Configuring a vCenter Account in VCF Operations

To manage your vCenter instances in VCF Operations, you must configure an account for each vCenter instance. The account requires the credentials that are used for communication with the target vCenter.

- Verify that you know the vCenter credentials that have sufficient privileges to connect and collect data, see [Privileges Required for Configuring a vCenterAccount](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations/privileges-required-for-configuring-a-vcenter-adapter-instance.html#GUID-fd32d12e-f9d4-443d-9fe7-d7afcbf99e69-en). If the provided credentials have limited access to objects in vCenter, all users, regardless of their vCenter privileges see only the objects that the provided credentials can access. At a minimum, the user account must have Read privileges and the Read privileges must be assigned at the datacenter or vCenter level.
- You must install the VCF Operations for logs appliance for VCF to enable log collection and analysis in VCF Operations. See *Deploy, Converge, Upgrade* for more information on deployment and upgrade. For more information on log analysis in VCF Operations, see [Configuring and Analyzing Logs.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/log-analysis.html)

Any account credentials you add are shared with other account administrators and VCF Operations collector hosts. Other administrators might use these credentials to configure a new account or to move a account to a new host.

1. From the left menu, click AdministrationIntegrations.
2. On the Accounts tab, click Add.
3. On the Accounts Type page, click vCenter.
4. Enter a display name and description for the account.

   Enter the name for the vCenter instance as you want it to appear in VCF Operations. A common practice is to include the IP address so that you can readily identify and differentiate between instances.
5. Select the Physical Data Center you want to associate with the vCenter account.

   If no physical data center is created or if you want to create a new physical data center for your account, you can add a new physical data center. For more information, see [Adding Physical Data Centers in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/-configuring-administration-settings/adding-physical-data-centers.html#GUID-e984d436-eeb5-4d0b-bc61-cc5187d0bc58-en).
6. In the vCenter text box, enter the FQDN or IP address of the vCenter instance to which you are connecting. 

   While configuring VCF Single Sign-On, enter the of the FQDN of the vCenter instance to which you are connecting. vCenter instances configured using IP address are not included in VCF accounts. If you want the vCenter instance to be part of the VCF account, enter the FQDN.
7. To add credentials for the vCenter instance, click the Add icon, and enter the required credentials.

   The vCenter credential must have Performance > Modify intervals permission activated in the target vCenter to collect VM guest metrics. Optionally, you can use alternate user credentials for actions. Enter an Action User Name and Actions Password. If you do not enter an Action User Name and Actions Password, the default user specified is considered for actions.

   Credentials are stored in VCF Operations and can be used for one or more instances of the vCenter.

   To monitor application services and operating systems, it is recommended that you enter action credentials with guest operations privileges. For more information, see [Privileges Required for Configuring a vCenter Account](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations/privileges-required-for-configuring-a-vcenter-adapter-instance.html#GUID-fd32d12e-f9d4-443d-9fe7-d7afcbf99e69-en).
8. Determine which VCF Operations collector or collector group is used to manage the account. If you have multiple collectors or collector groups in your environment, and you want to distribute the workload to optimize performance, select the collector or collector group to manage the adapter processes for this instance.

   The collector for VCF Operations can also be the cloud proxy. Select the cloud proxy you just deployed as the collector for this vCenter account. The vCenter FQDN or IP address must be reachable from the selected collector or collector group.
9. Click Validate Connection to validate the connection with your vCenter instance.
10. In the Review and Accept Certificate dialog box, review the certificate information.
    - If the certificate presented in the dialog box matches the certificate for your target vCenter instance, click OK.
    - If you do not recognize the certificate as valid, click Cancel. The validation test fails and the connection to vCenter instance is incomplete. To complete the adapter configuration, you must provide a valid vCenter URL and verify that the certificate on the vCenter is valid.
11. The account is configured to run actions on objects in vCenter from VCF Operations. If you do not want to run actions, deselect Activate for Operational Actions.
12. To collect logs, click Activate Log Collection. For more information, see [Configuring and Analyzing Logs.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/log-analysis.html)

    When you export vCenter information from one VCF Operations instance and import it to another, the log collection information is not transferred.
13. To collect network and flow, click Activate Network and Flow. For more information, see [Add VMware vCenter Server for VCF Operations for networks](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/network-operationss/working-with-data-sources/adding-a-data-source-in-vrealize-network-insight/supported-vmware-managers/add-vcenter-server.html).
14. To modify the advanced options regarding collectors, object discovery, or change events, expand the Advanced Settings. 

    For information about these advanced settings, see [Configuring Advanced Settings for a vCenter Account](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/account-information-vmware-vsphere-solution-account-options.html#GUID-69a3ab7d-60bd-4fac-b037-a310e51df404-en).
15. Click Add to select an additional option for this vCenter instance.

    License and vSphere Client plug-in management is supported only for vCenter accounts of version 9.0 or later. If your vCenter is 9.0 or later and is not managed by any VCF Operations instance, the current VCF Operations instance takes up the license and vSphere Client plug-in management. If you do not have the required privileges for license and vSphere Client plug-in management, the vCenter account will be added only for monitoring purposes. For more information, see [Use and Configure your vSphere Client](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/using-the-vsphere-client-host-management/working-with-the-vsphere-client-host-management.html#GUID-6E321032-5350-4008-953A-3167B3BF18C1-en).

    After you integrate a vCenter account with a VCF Operations instance for license management, it takes up to 15 minutes before the vCenter account appears in the License tab of VCF Operations.

    If you have an earlier version of vCenter accounts, you can only activate vSphere Client plug-in management. If your vCenter is pre 9.0, and is not managed by any VCF Operations instance, the current VCF Operations instance takes up the vSphere Client plug-in management. If you do not have the required privileges for vSphere Client plug-in management, vCenter account will be added only for monitoring purposes.

    - Add vCenter only for monitoring: Use this option if you want to proceed with the existing VCF Operations integration and use the new vCenter account for monitoring purposes only.
    - Add vCenter for monitoring and license and vSphere Client plug-in management by replacing the current integration: Use this option to replace existing VCF Operations integration with a newer integration.

      For versions 9.0 or later, you can use this option if another VCF Operations provides license and vSphere Client plug-in management for vCenter you are adding and you want to replace it with the current VCF Operations. After you remove the current integration, you must assign new license to this vCenter instance. For more information, see [Assign a Primary License to a vCenter Instance or a VCF Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/assign-a-licenses-to-a-vcenter-instance.html).

      For versions prior to 9.0, license management is not applicable. You can use this option if another VCF Operations provides vSphere Client plug-in management for vCenter you are adding and you want to replace it with the current VCF Operations.

    Newly created vCenter accounts do not start monitoring the data automatically and you must manually initiate the data collection.
16. On the Accounts tab, locate the vCenter account, click the vertical ellipsis and then click Start Collecting.
17. You can use your vCenter account to monitor and manage license and vSphere client plug-in.
    - To bulk activate license and vSphere Client plug-in management for all your vCenter accounts of versions 9.0 or later, select the vCenter account, and click Activate Management.
    - To activate license and vSphere Client plug-in management for a particular vCenter account, select the vCenter account, click the vertical ellipsis, click Edit, and then click Manage Integrations. You must have the required privileges to manage integration. For more information, see [Privileges Required for Configuring a Adapter Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations/privileges-required-for-configuring-a-vcenter-adapter-instance.html).

The vCenter account is added to the list and VCF Operations begins collecting metrics, properties, and events from the vCenter instance. Depending on the number of managed objects, the initial collection can take more than one collection cycle. A standard collection cycle begins every five minutes.

For information about the network port that VCF Operations uses to communicate with a vCenter instance and VCF Operations components, see [VMware Ports and Protocols](https://ports.broadcom.com/).

You can activate vSAN configuration for your account. For more information, see [Configuring a vSAN Account](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsan-overview/configure-a-vsan-adapter-instance.html#GUID-d8e309ca-47a8-4fcc-8a7d-b3d77743cb98-en).

You can use the vCenter for service discovery, see [Configure Service and Application Discovery](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/workload-monitoring-and-observability/about-service-discovery/configure-service-and-application-discovery.html#GUID-4f354d19-bad4-49d2-814d-1a7ce39cf08e-en).