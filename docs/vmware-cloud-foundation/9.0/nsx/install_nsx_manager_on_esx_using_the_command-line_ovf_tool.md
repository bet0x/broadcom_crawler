---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-on-esxi-using-the-command-line-ovf-tool.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Install NSX Manager on ESX Using the Command-Line OVF Tool
---

# Install NSX Manager on ESX Using the Command-Line OVF Tool

If you prefer to automate or use CLI for the NSX Manager installation, you can use the VMware OVF Tool, which is a command-line utility.

- You can download the latest OVF tool from the [Broadcom Support portal](https://support.broadcom.com).
- Verify that the system requirements are met. See [Planning and Preparation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/planning-and-preparation.html).
- Verify that the required ports are open. Refer to [VMware Ports and Protocols](https://ports.broadcom.com/) for more details.
- Verify that a datastore is configured and accessible on the ESX host.
- Verify that you have the IP address and gateway, DNS server IP addresses, domain search list, and the NTP Server IP or FQDN for the NSX Manager to use.
- Create a management VDS and target VM port group in vCenter. Place the NSX appliances onto this management VDS port group network. See [Prepare a vSphere Distributed Switch for NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/prepare-a-vsphere-distributed-virtual-switch-for-nsx-t.html). Multiple management networks can be used as long as the NSX Manager nodes has consistent connectivity and recommended latency between them.

  If you plan to use Cluster VIP, all NSX Manager appliances should belong to same subnet.
- Plan your NSX Manager IP and NSX Manager Cluster VIP addressing scheme.

  Verify that you have the hostname for NSX Manager to use. The Hostname format must be [[email protected]](/cdn-cgi/l/email-protection). This format is required if NSX installation is dual stack (IPv4, IPv6) and/or if planning to configure CA-signed certificates.
- Verify that the system requirements are met. See System Requirements.
- Verify that the required ports are open. See Ports and Protocols.
- Verify that a datastore is configured and accessible on the ESX host.
- Verify that you have the IP address and gateway, DNS server IP addresses, domain search list, and the NTP Server IP or FQDN for the NSX Managerto use.
- Create a management VDS and target VM port group in vCenter. Place the NSX appliances onto this management VDS port group network. See [Prepare a vSphere Distributed Switch for NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/prepare-a-vsphere-distributed-virtual-switch-for-nsx-t.html).

  Multiple management networks can be used as long as the NSX Manager nodes has consistent connectivity and recommended latency between them.

  If you plan to use Cluster VIP, all NSX Manager appliances should belong to same subnet.
- Plan your NSX Manager IP and NSX Manager Cluster VIP addressing scheme.

  Verify that you have the hostname for NSX Manager to use. The Hostname format must be [[email protected]](/cdn-cgi/l/email-protection). This format is required if NSX installation is dual stack (IPv4, IPv6) and/or if planning to configure CA-signed certificates.

By default, nsx\_isSSHEnabled and nsx\_allowSSHRootLogin are both disabled for security reasons. When they are disabled, you cannot SSH or log in to the NSX Manager command line. If you enable nsx\_isSSHEnabled but not nsx\_allowSSHRootLogin, you can SSH to NSX Manager but you cannot log in as root.

1. Run the ovftool command with the appropriate parameters. 

   The process depends on whether the host is standalone or managed by vCenter.
   - For a standalone host:

     On a standalone host, if you enter an incorrect role in the nsx\_role property, then the appliance is deployed in the NSX Manager role.

     - Windows example:

       ```
       C:\Program Files\VMware\VMware OVF Tool>ovftool \
       --name=<nsxmanager>
       --X:injectOvfEnv
       --X:logFile=ovftool.log
       --sourceType=OVA
       --vmFolder='Folder-in-VC'
       --allowExtraConfig
       --datastore=<datastore>
       --net:"<network-name-of-OVF>=<network-name>"
       --acceptAllEulas
       --skipManifestCheck
       --noSSLVerify
       --diskMode=thin
       --quiet
       --hideEula
       --powerOn
       --prop:nsx_ip_0=10.196.176.81
       --prop:nsx_netmask_0=255.255.252.0
       --prop:nsx_gateway_0=10.196.179.253
       --prop:nsx_dns1_0=10.142.7.1
       --prop:nsx_domain_0=eng.yourcompany.com
       --prop:nsx_ntp_0=10.128.243.14
       --prop:nsx_isSSHEnabled=True
       --prop:"nsx_passwd_0=<password>"
       --prop:"nsx_cli_passwd_0=<password-cli>"
       --prop:"nsx_cli_audit_passwd_0=<password-cli-audit>"
       --prop:nsx_hostname=<hostname>
       --prop:mgrhostname01="[email protected]"
       --prop:nsx_allowSSHRootLogin=True
       --prop:nsx_role="NSX Manager"
       --X:logFile=/root/ovftool/<ovf-folder>.log
       --X:logLevel=trivia
       --ipProtocol=IPv4
       --ipAllocationPolicy="fixedPolicy"
       <nsx-unified-applicance>.ova
       'vi://[email protected]:[email protected]/<datacenter>/host/Install/10.196.6.78/'
       ```

       The above Windows code block uses the backslash (\) to indicate the continuation of the command line. In actual use, omit the backslash and put the entire command in a single line.

       In the above example, 10.168.110.51 is the IP address of the host machine where NSX Manager is to be deployed.

       In the above example, --deploymentOption is set to the default size Medium. To learn about other supported sizes, see [Planning and Preparation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/planning-and-preparation.html).
     - Linux example:

       ```
       mgrformfactor="small"
       ipAllocationPolicy="fixedPolicy"
       mgrdatastore="QNAP-Share-VMs"
       mgrnetwork="Management-VLAN-210"

       mgrname01="nsx-manager-01"
       mgrhostname01="nsx-manager-01"
       mgrip01="192.168.210.121"

       mgrnetmask="255.255.255.0"
       mgrgw="192.168.210.254"
       mgrdns="192.168.110.10"
       mgrntp="192.168.210.254"
       mgrpasswd="<password>"
       mgrssh="<True|False>"
       mgrroot="<True|False>"
       logLevel="trivia"

       mgresxhost01="192.168.110.113"

       ovftool
       --name=<nsxmanager>
       --X:injectOvfEnv
       --X:logFile=ovftool.log
       --sourceType=OVA
       --vmFolder='Folder-in-VC'
       --allowExtraConfig
       --datastore=<datastore>
       --net:"<network-name-of-OVF>=<network-name>"
       --acceptAllEulas
       --skipManifestCheck
       --noSSLVerify
       --diskMode=thin
       --quiet
       --hideEula
       --powerOn
       --prop:nsx_ip_0=10.196.176.81
       --prop:nsx_netmask_0=255.255.252.0
       --prop:nsx_gateway_0=10.196.179.253
       --prop:nsx_dns1_0=10.142.7.1
       --prop:nsx_domain_0=eng.yourcompany.com
       --prop:nsx_ntp_0=10.128.243.14
       --prop:nsx_isSSHEnabled=True
       --prop:"nsx_passwd_0=<password>"
       --prop:"nsx_cli_passwd_0=<password-cli>"
       --prop:"nsx_cli_audit_passwd_0=<password-cli-audit>"
       --prop:nsx_hostname=<hostname>
       --prop:mgrhostname01="[email protected]"
       --prop:nsx_allowSSHRootLogin=True
       --prop:nsx_role="NSX Manager"
       --X:logFile=/root/ovftool/<ovf-folder>.log
       --X:logLevel=trivia
       --ipProtocol=IPv4
       --ipAllocationPolicy="fixedPolicy"
       <nsx-unified-applicance>.ova
       'vi://[email protected]:[email protected]/<datacenter>/host/Install/10.196.6.78/'
       ```The result should look something like this:

     ```
     Opening OVA source: nsx-<component>.ova
     The manifest validates
     Source is signed and the certificate validates
     Opening VI target: vi://root:<password>@<esxi-IP-address>
     Deploying to VI: vi://root:<password>@<esxi-IP-address>
     Transfer Completed
     Powering on VM: NSX Manager
     Task Completed
     Completed successfully
     ```
   - For a host managed by vCenter:
     - Windows example:

       ```
       C:\Users\Administrator\Downloads>ovftool
       --name=<nsxmanager>
       --X:injectOvfEnv
       --X:logFile=ovftool.log
       --sourceType=OVA
       --vmFolder='Folder-in-VC'
       --allowExtraConfig
       --datastore=<datastore>
       --net:"<network-name-of-OVF>=<network-name>"
       --acceptAllEulas
       --skipManifestCheck
       --noSSLVerify
       --diskMode=thin
       --quiet
       --hideEula
       --powerOn
       --prop:nsx_ip_0=10.196.176.81
       --prop:nsx_netmask_0=255.255.252.0
       --prop:nsx_gateway_0=10.196.179.253
       --prop:nsx_dns1_0=10.142.7.1
       --prop:nsx_domain_0=eng.yourcompany.com
       --prop:nsx_ntp_0=10.128.243.14
       --prop:nsx_isSSHEnabled=True
       --prop:"nsx_passwd_0=<password>"
       --prop:"nsx_cli_passwd_0=<password-cli>"
       --prop:"nsx_cli_audit_passwd_0=<password-cli-audit>"
       --prop:nsx_hostname=<hostname>
       --prop:mgrhostname01="[email protected]"
       --prop:nsx_allowSSHRootLogin=True
       --prop:nsx_role="NSX Manager"
       --X:logFile=/root/ovftool/<ovf-folder>.log
       --X:logLevel=trivia
       --ipProtocol=IPv4
       --ipAllocationPolicy="fixedPolicy" <nsx-unified-applicance>.ova
       'vi://[email protected]:[email protected]/<datacenter>/host/Install/10.196.6.78/'
       ```

       The above Windows code block uses the backslash (\) to indicate the continuation of the command line. In actual use, omit the backslash and put the entire command in a single line.

       In the above example, --deploymentOption is set to the default size Medium. To learn about other supported sizes, see [Planning and Preparation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/planning-and-preparation.html).
     - Linux example:

       ```
       mgrformfactor="small"
       ipAllocationPolicy="fixedPolicy"
       mgrdatastore="QNAP-Share-VMs"
       mgrnetwork="Management-VLAN-210"

       mgrname01="nsx-manager-01"
       mgrhostname01="nsx-manager-01"
       mgrip01="192.168.210.121"

       mgrnetmask="255.255.255.0"
       mgrgw="192.168.210.254"
       mgrdns="192.168.110.10"
       mgrntp="192.168.210.254"
       mgrpasswd="<password>"
       mgrssh="<True|False>"
       mgrroot="<True|False>"
       logLevel="trivia"

       vcadmin="[email protected]"
       vcpass="<password>"
       vcip="192.168.110.151"
       mgresxhost01="192.168.110.113"

       ovftool
       --name=<nsxmanager>
       --X:injectOvfEnv
       --X:logFile=ovftool.log
       --sourceType=OVA
       --vmFolder='Folder-in-VC'
       --allowExtraConfig
       --datastore=<datastore>
       --net:"<network-name-of-OVF>=<network-name>"
       --acceptAllEulas
       --skipManifestCheck
       --noSSLVerify
       --diskMode=thin
       --quiet
       --hideEula
       --powerOn
       --prop:nsx_ip_0=10.196.176.81
       --prop:nsx_netmask_0=255.255.252.0
       --prop:nsx_gateway_0=10.196.179.253
       --prop:nsx_dns1_0=10.142.7.1
       --prop:nsx_domain_0=eng.yourcompany.com
       --prop:nsx_ntp_0=10.128.243.14
       --prop:nsx_isSSHEnabled=True
       --prop:"nsx_passwd_0=<password>"
       --prop:"nsx_cli_passwd_0=<password-cli>"
       --prop:"nsx_cli_audit_passwd_0=<password-cli-audit>"
       --prop:nsx_hostname=<hostname>
       --prop:mgrhostname01="[email protected]"
       --prop:nsx_allowSSHRootLogin=True
       --prop:nsx_role="NSX Manager"
       --X:logFile=/root/ovftool/<ovf-folder>.log
       --X:logLevel=trivia
       --ipProtocol=IPv4
       --ipAllocationPolicy="fixedPolicy" <nsx-unified-applicance>.ova
       'vi://[email protected]:[email protected]/<datacenter>/host/Install/10.196.6.78/'
       ```The result should look something like this:

     ```
     Opening OVA source: nsx-<component>.ova
     The manifest validates
     Source is signed and the certificate validates
     Opening VI target: vi://[email protected]@<esxi-IP-address:port>/
     Deploying to VI: vi://[email protected]@<esxi-IP-address:port>/
     Transfer Completed
     Powering on VM: NSX Manager
     Task Completed
     Completed successfully
     ```
2. You can also run the OVF tool in Probe mode to view contents of a source. OVA and OVF packages can be probed among a list of other supported source types. You can use the information returned by the Probe mode to configure deployments.

   $> \ovftool --allowExtraConfig <OVA path or URL>
3. For optimal performance, reserve memory for the node.

   Set the reservation to ensure that NSX Manager has sufficient memory to run efficiently. See [Planning and Preparation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/planning-and-preparation.html).
4. From the vSphere Client, verify that the VM is powered on. Open the VM console to track the boot process of the node.
5. After the VM node boots a second time, log in to the CLI as admin and run the get interface eth0 command to verify that the IP address was applied as expected.
6. Enter the get services command after waiting for about 5 minutes to verify that all default services are running. 

   The following services are not required by default and do not start automatically.
   - liagent
   - migration-coordinator: This service is used only when running migration coordinator. See the NSX Migration Guide before starting this service.
   - snmp: For information on starting SNMP see Simple Network Management Protocol in the NSX Administration Guide.
   - nsx-message-bus: This service is not used in NSX 3.0 and later releases.
7. After deployment, verify that the NSX Manager UI comes up by accessing the following URL, https://nsx-manager-ip or https://nsx-manager-fqdn.
8. Verify that your NSX Manager,or Global Manager node has the required connectivity. 

   Perform the following tasks:
   - Ping your node from another machine.
   - The node can ping its default gateway.
   - The node can ping the hypervisor hosts that are in the same network using the management interface.
   - The node can ping its DNS server and its NTP Server or FQDN.
   - If you enabled SSH, make sure that you can SSH to your node.

   If connectivity is not established, make sure that the network adapter of the virtual appliance is in the proper network or VLAN.

- Log in to the NSX Manager from a supported web browser. See [Log In to the Newly Installed NSX Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-and-available-appliances/log-in-to-your-newly-created-nsx-manager.html#GUID-06b390a4-50cc-44bb-b8ee-ef608b1165a6).

  NSX Manager nodes that are removed from the cluster should be powered off or deleted. Do not reuse the same NSX Manager again in your environment.
- If deploying second and third NSX Manager nodes as OVA/OVF, join the manager nodes to first deployed manager node to create NSX Manager Cluster. see [Form an NSX Manager Cluster Using the CLI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-on-esxi-using-the-command-line-ovf-tool/deploy-nsx-manager-nodes-to-form-a-cluster-using-cli.html#GUID-3d870057-b9ef-4f40-8ae6-4151181fe0ad).