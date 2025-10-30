---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-and-available-appliances.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Install NSX Manager and Available Appliances
---

# Install NSX Manager and Available Appliances

You use the vSphere Client to deploy NSX Manager virtual appliances. The same OVF file can be used to deploy different types of appliances: NSX Manager, and Global Manager for NSX Federation.

- Verify that the system requirements are met. See System Requirements.
- Verify that the required ports are open. See Ports and Protocols.
- Verify that a datastore is configured and accessible on the ESX host.
- Verify that you have the IP address and gateway, DNS server IP addresses, domain search list, and the NTP Server IP or FQDN for the NSX Managerto use.
- Create a management VDS and target VM port group in vCenter. Place the NSX appliances onto this management VDS port group network. See [Prepare a vSphere Distributed Switch for NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/prepare-a-vsphere-distributed-virtual-switch-for-nsx-t.html).

  Multiple management networks can be used as long as the NSX Manager nodes has consistent connectivity and recommended latency between them.

  If you plan to use Cluster VIP, all NSX Manager appliances should belong to same subnet.
- Plan your NSX Manager IP and NSX Manager Cluster VIP addressing scheme.

  Verify that you have the hostname for NSX Manager to use. The Hostname format must be [[email protected]](/cdn-cgi/l/email-protection). This format is required if NSX installation is dual stack (IPv4, IPv6) and/or if planning to configure CA-signed certificates.

1. Locate and download the NSX OVA file from the My Downloads panel on the [Broadcom Support](https://support.broadcom.com/group/ecx/downloads) page. You can either copy the download URL or download the OVA file.
2. In the vSphere Client, select the ESX host or ESX host cluster on which to install NSX.
3. Right-click Host and select  Deploy OVF template to start the installation wizard.
4. Enter the download OVA URL or navigate to the OVA file, and click Next.
5. Enter a name and a location for the NSX Manager VM, and click Next. 

   The name you enter appears in the vSphere and vCenter inventory.
6. Select a compute resource for the NSX Manager appliance, and click Next. 
   - To install on a ESX host managed by vCenter, select a host on which to deploy the NSX Manager appliance.
   - To install on a standalone ESX host, select the host on which to deploy the NSX Manager appliance.
7. Review and verify the OVF template details, and click Next.
8. Specify the deployment configuration size, and click Next. 

   The Description panel on the right side of the wizard shows details of the selected configuration.
9. Specify storage for the configuration and disk files.
   1. Select the virtual disk format.
   2. Select the VM storage policy.
   3. Specify the datastore to store the NSX Manager appliance files.
   4. Click Next.
10. Select a destination network for each source network.
11. Select the port group or destination network for the NSX Manager.
12. Configure IP Allocation settings.
    1. For IP allocation, specify Static - Manual.
    2. For IP protocol, select IPv4 or IPv6.

       You can ignore the IP Allocation settings. You can select either IPv4 or IPv6. It would not impact ingress or egress network traffic of NSX Manager.
13. Click Next.

    The following steps are all located in the Customize Template section of the Deploy OVF Template wizard.
14. In the Application section, enter the system root, CLI admin, and audit passwords for the NSX Manager. The root and admin credentials are mandatory fields.

    Your passwords must comply with the password strength restrictions.
    - At least 12 characters
    - At least one lower-case letter
    - At least one upper-case letter
    - At least one digit
    - At least one special character
    - At least five different characters
    - Default password complexity rules are enforced by the following Linux PAM module arguments:
      - retry=3: The maximum number of times a new password can be entered, for this argument at the most 3 times, before returning with an error.
      - minlen=12: The minimum acceptable size for the new password. In addition to the number of characters in the new password, credit (of +1 in length) is given for each different kind of character (other, upper, lower and digit).
      - difok=0: The minimum number of bytes that must be different in the new password. Indicates similarity between the old and new password. With a value 0 assigned to difok, there is no requirement for any byte of the old and new password to be different. An exact match is allowed.
      - lcredit=1: The maximum credit for having lower case letters in the new password. If you have less than or 1 lower case letter, each letter will count +1 towards meeting the current minlen value.
      - ucredit=1: The maximum credit for having upper case letters in the new password. If you have less than or 1 upper case letter each letter will count +1 towards meeting the current minlen value.
      - dcredit=1: The maximum credit for having digits in the new password. If you have less than or 1 digit, each digit will count +1 towards meeting the current minlen value.
      - ocredit=1: The maximum credit for having other characters in the new password. If you have less than or 1 other characters, each character will count +1 towards meeting the current minlen value.
      - enforce\_for\_root: The password is set for the root user.

      For more details on Linux PAM module to check the password against dictionary words, refer to the man page.

      For example, avoid simple and systematic passwords such as VMware123!123 or VMware12345. Passwords that meet complexity standards are not simple and systematic but are a combination of letters, alphabets, special characters, and numbers, such as VMware123!45, VMware 1!2345 or VMware@1az23x.
15. In the Optional parameters section, leave the password fields blank. It avoids the risk of compromising passwords set for VMC roles by a user who has access to the vCenter. When deploying VMC for NSX, this field is used internally to set passwords for the Cloud Admin and Cloud Operator roles.
16. In the Network Properties section, enter the hostname of the NSX Manager. 

    The host name must be a valid domain name. Ensure that each part of the host name (domain/subdomain) that is separated by dot starts with an alphabet character. Also, NSX accepts only latin alphabets that do not have an accent mark, as in í, ó, ú, ý.

    If you plan to install NSX in dual stack (IPv4 and IPv6) and/or if you plan to configure CA-signed certificates, then enter a Hostname with valid domain name to NSX Manager VMs and Cluster VIP (if configured).
17. Select a Rolename for the appliance. The default role is NSX Manager.

    - To install an NSX Manager appliance, select the NSX Manager role.
    - To install a Global Manager appliance for a NSX Federation deployment, select the NSX Global Manager role.

      See [Getting Started with NSX Federation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/getting-started-with-federation.html) for details.
18. Enter a default gateway, management network IP address (required), and management network netmask (required). 

    Entering a default gateway is optional. However, you cannot configure it after deploying NSX Manager.
19. In the DNS section, enter DNS Server list and Domain Search list.
20. In the Services Configuration section, enter NTP Server IP or FQDN.

    Optionally, you can enable SSH service and allow root SSH login. But, it is not recommended to allow root access to SSH service.
21. Verify that all your custom OVF template specification is accurate and click Finish to begin installation. 

    The installation might take 7-8 minutes.
22. From the vSphere Client, verify that the VM is powered on. Open the VM console to track the boot process of the node.
23. After the VM node boots a second time, log in to the CLI as admin and run the get interface eth0 command to verify that the IP address was applied as expected.
24. Enter the get services command after waiting for about 5 minutes to verify that all default services are running. 

    The following services are not required by default and do not start automatically.
    - liagent
    - migration-coordinator: This service is used only when running migration coordinator. See the NSX Migration Guide before starting this service.
    - snmp: For information on starting SNMP see Simple Network Management Protocol in the NSX Administration Guide.
    - nsx-message-bus: This service is not used in NSX 3.0 and later releases.
25. After deployment, verify that the NSX Manager UI comes up by accessing the following URL, https://nsx-manager-ip or https://nsx-manager-fqdn.
26. Verify that your NSX Manager,or Global Manager node has the required connectivity. 

    Perform the following tasks:
    - Ping your node from another machine.
    - The node can ping its default gateway.
    - The node can ping the hypervisor hosts that are in the same network using the management interface.
    - The node can ping its DNS server and its NTP Server or FQDN.
    - If you enabled SSH, make sure that you can SSH to your node.

    If connectivity is not established, make sure that the network adapter of the virtual appliance is in the proper network or VLAN.
27. Troubleshooting OVA failures:

    During deployment, if you entered incorrect configuration details, delete the appliance and redeploy with correct configuration.

    1. Verify that the datastore chosen for deployment is mounted on all the hosts that are members of a cluster. Redeploy and choose ESX host instead of vCenter to bypass vCenter cluster related checks.
    2. If a proxy is enabled on vCenter, edit the file /etc/sysconfig/proxy and add the line .\*.domainname to bypass the proxy for ESX hosts. See Knowledge Base article 321922: [Unable to deploy OVF using vSphere Client in vCenter when an HTTPS Proxy is configured](https://knowledge.broadcom.com/external/article?articleNumber=321922).
    3. If the deployment of the appliance through the OVF tool results in the error ovf descriptor not found, view the file contents in terminal cat -A <filepath/filename> and remove hidden formatting characters. Then try again.
28. Troubleshooting issues related to bringing up the appliance. SSH to NSX Manager CLI as admin and run the following commands to troubleshoot:
    1. Run get configuration and verify hostname/name-server/search-domain/ntp settings are correct.
    2. Run get services and verify all required services are running (other than nsx-message-bus, snmp, migration-coordinator). If these services are not running, try restarting the service by running restart service <service-name>.
    3. Run get cluster status and verify all manager cluster components are up. If any component is down, try restarting the service associated to the component by running restart service <associated-component-service-name>.
    4. Run get core-dumps to verify no core dumps generated in /var/log/core or /image/core. If you find any core dumps, contact VMware Support.
    5. Run get filesystem-status to verify that no disk partition is full, especially those partitions that are consumed by NSX.
    6. Alternatively, you can run API commands to know the node and service status.

       GET api/v1/node/status

       GET api/v1/node/services

- Log in to the NSX Manager from a supported web browser. See [Log In to the Newly Installed NSX Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-and-available-appliances/log-in-to-your-newly-created-nsx-manager.html#GUID-06b390a4-50cc-44bb-b8ee-ef608b1165a6).
- [Deploy NSX Manager Nodes to Form a Cluster from the UI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-and-available-appliances/deploy-nsx-manager-nodes-to-form-a-cluster-using-ui.html).