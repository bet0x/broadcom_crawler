---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform/vcf-operations-for-logs-for-vvf-clients.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Deploying the VCF Operations for logs Appliance for VMware vSphere Foundation
---

# Deploying the VCF Operations for logs Appliance for VMware vSphere Foundation

Download the virtual appliance to deploy VCF Operations for logs for VMware vSphere Foundation (VVF) . VMware distributes the VCF Operations for logs virtual appliance as an .ova file. Deploy the VCF Operations for logs virtual appliance for VMware vSphere Foundation (VVF) by using the vSphere Client.

- Verify that you have a VMware vSphere Foundation (VVF) license.
- Verify that you have a copy of the VCF Operations for logs virtual appliance .ova file.
- Verify that you have permissions to deploy OVF templates to the inventory.
- Verify that you can log in to the VCF Operations UI.

1. In the vSphere Client, select FileDeploy OVF Template.
2. Follow the prompts in the Deploy OVF Template wizard.
3. On the Select Configuration page, select the size of the VCF Operations for logs virtual appliance based on the size of the environment for which you intend to collect logs. 

   Small is the minimum requirement for production environments.

   VCF Operations for logs provides preset VM (virtual machine) sizes that you can select from to meet the ingestion requirements of your environment. These presets are certified size combinations of compute and disk resources, though you can add extra resources afterward. A small configuration is suitable only for demos.

   If you select Large, you must upgrade the virtual hardware on the VCF Operations for logs virtual machine after the deployment.
4. On the Select Storage page, select a disk format. 
   - Thick Provision Lazy Zeroed creates a virtual disk in a default thick format. Space required for the virtual disk is allocated when the virtual disk is created. The data remaining on the physical device is not erased during creation, but is zeroed out on demand later, on first write from the virtual appliance.
   - Thick Provision Eager Zeroed creates a type of thick virtual disk that supports clustering features such as Fault Tolerance. Space required for the virtual disk is allocated at creation time. In contrast to the flat format, the data remaining on the physical device is zeroed out when the virtual disk is created. It might take much longer to create disks in this format than to create other types of disks.

     Deploy the VCF Operations for logs virtual appliance with thick provisioned eager zeroed disks whenever possible for better performance and operation of the virtual appliance.
   - Thin Provision creates a disk in thin format. The disk expands as the amount of data saved on it increases. If your storage device does not support thick provisioning disks or you want to conserve unused disk space on the VCF Operations for logs virtual appliance, deploy the virtual appliance with thin provisioned disks.

   Shrinking disks on the VCF Operations for logs virtual appliance is not supported and might result in data corruption or data loss.
5. On the Select Networks page, set the networking parameters for the VCF Operations for logs virtual appliance. You can select the IPv4 or IPv6 protocol.

   If you do not provide network settings, such as an IP address, DNS servers, and gateway information, VCF Operations for logs uses DHCP to set those settings.

   Do not specify more than two domain name servers. If you specify more than two domain name servers, all configured domain name servers are ignored in the VCF Operations for logs virtual appliance.

   Use a comma-separated list to specify domain name servers.
6. On the Customize template page, set network properties if you are not using DHCP.

   Under Application, select the Prefer IPv6 addresses check box if you want to run the virtual machine in a dual stack network.

   Do not select the Prefer IPv6 addresses check box if you want to use pure IPv4 even with IPv6 supported in your network. Select the check box only if your network has a dual stack or pure stack support for IPv6.
7. On the Customize template page, select Other Properties and set the root password for the VCF Operations for logs virtual appliance. 

   The root password is required for SSH. You can also set this password through the VMware Remote Console.
8. Follow the prompts to complete the deployment. 

   After you power on the virtual appliance, an initialization process begins. The initialization process takes several minutes to complete. At the end of the process, the virtual appliance restarts.
9. Navigate to the Console tab and verify the IP address of the VCF Operations for logs virtual appliance. 

   IP Address Prefix | Description || https:// | The DHCP configuration on the virtual appliance is correct. |
   | http:// | The DHCP configuration on the virtual appliance failed. 1. Power off the VCF Operations for logs virtual appliance. 2. Right-click the virtual appliance and select Edit Settings. 3. Set a static IP address for the virtual appliance. |

- Log in to the VCF Operations UI to configure vCenter instances to pull tasks, events, and alerts. For more information, see [Configuring Log Sources](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/log-analysis/getting-started-with-log-analysis/configuring-log-sources.html).

- In the VCF Operations UI, navigate to AdministrationControl Panel and click the Operations-Logs Appliance Integration tile. Enter the address, username and password of the VCF Operations for logs deployment. This completes the VCF Operations integration with VCF Operations for logs.

  The VCF Operations for logs Web interface is available at https://operations-for-logs-host/ where operations-for-logs-host is the IP address or host name of the VCF Operations for logs virtual appliance.

- If you want to join an existing deployment, see [Join an Existing Deployment](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf-logs/vcf-operations-for-logs-90.pdf).
- Download the VCF Operations for logs 9.0 documentation from [here](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf-logs/vcf-operations-for-logs-90.pdf).