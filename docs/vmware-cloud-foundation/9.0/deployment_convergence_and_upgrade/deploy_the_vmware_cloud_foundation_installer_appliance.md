---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/deploy-the-vmware-cloud-foundation-installer-appliance.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Deploy the VMware Cloud Foundation Installer Appliance
---

# Deploy the VMware Cloud Foundation Installer Appliance

Deploy the VCF Installer appliance on a network that can access the ESX hosts and VM management network that you plan to use for the deployment. The appliance must be able to access all required external services, such as DNS and NTP.

Before you deploy the VCF Installer appliance, verify that your environment meets the requirements for this process.

|  |  |
| --- | --- |
| Resource Requirements | - 4 vCPUs - 16 GB RAM - 914 GB storage |
| Network Requirements | - Verify that the static IP address and FQDN for the VCF Installer appliance are available. - Verify that connectivity is in place from the VCF Installer appliance and the management VLAN used in the deployment. |
| Deployment Platform | You can deploy the VCF Installer appliance on an ESX host or on a laptop running VMware Workstation or VMware Fusion. |

Where you deploy the VCF Installer appliance impacts how it can be used. You can deploy the appliance:

- Outside of the management infrastructure on any machine with connectivity to the management infrastructure. In this case, you can use the appliance to deploy multiple VCF or VMware vSphere Foundation platforms.
- On one of the ESX hosts that will form the management domain. In this case, you can only use the appliance to deploy a single VCF platform.

This procedure describes how to deploy the VCF Installer appliance directly to an ESX host.

1. In a web browser, log in to the ESX host using the VMware Host Client.
2. In the navigation pane, select Host, and click Create/Register VM.
3. On the Select creation type dialog box, select Deploy a virtual machine from an OVF or OVA file and click Next.
4. On the Select OVF and VMDK files page, enter a name for the virtual machine, browse to the VCF-SDDC-Manager-Appliance-9.0.1.0.<build\_number>.ova file that you downloaded from the Broadcom Support Portal, and click Next.
5. On the Select Storage page, select a datastore and click Next. 

   I'm deploying the VCF Installer appliance... | Storage considerations || Outside of the management infrastructure | Choose any valid datastore. |
   | On one of the ESX hosts that will form the management domain | Choose a local disk. After the management domain storage is configured using the VCF Installer, the VCF Installer appliance is migrated to that storage with Storage vMotion and switched to SDDC Manager mode. The local disk remains empty and is not added to the management domain storage. In this case, the local disk should not be considered when planning for capacity. |
6. On the License agreements dialog box, click I agree and then click Next.
7. On the Deployment options dialog box, enter the following values and click Next. 

   Setting | Value || Network mappings | your\_portgroup |
   | Disk provisioning | Thin |
   | Power on automatically | Selected |
8. On the Additional settings dialog box, expand Application, enter the following values, and click Next. 

   Setting | Details || Root user password/Root user password confirm | The root user password must be a minimum of 15 characters and include at least one uppercase, one lowercase, one digit, and one special character.  Supported special characters: @ ! # $ % ? ^  - Passwords must not contain a dictionary word or part of a dictionary word. - Passwords must not contain the user name or parts of the user name. |
   | Local user password/Local user password confirm | You use the local user account (admin@local) to log in to the VCF Installer.  The local user password must be a minimum of 15 characters and include at least one uppercase, one lowercase, one digit, and one special character.  Supported special characters: @ ! # $ % ? ^  - Passwords must not contain a dictionary word or part of a dictionary word. - Passwords must not contain the user name or parts of the user name. |
   | Host Name | Enter the fully qualified domain name (FQDN) for the VCF Installer appliance.  If you are deploying the VCF Installer on one of the ESX hosts that will form the management domain, the FQDN is used for SDDC Manager after deployment. |
   | NTP Servers | Enter the NTP server(s). Use a comma if entering multiple NTP servers. NTP servers can be entered using FQDNs or IP addresses. |
9. On the Additional settings dialog box, expand Networking Configuration, enter the following values, and click Next. 

   Setting | Details || Network 1 IP Address | Enter the IP address for the VCF Installer appliance. |
   | Network 1 Subnet Mask | Enter the subnet mask for the VCF Installer appliance. |
   | Network Default Gateway | Enter the default gateway for the VCF Installer appliance. |
   | DNS Domain Name | Enter the DNS domain name. For example, rainpole.io. |
   | Domain Search Path | Enter the domain search path(s). Use a comma if entering multiple search paths. For example rainpole.io, sfo.rainpole.io. |
   | Domain Name Servers | Enter the IP address of the primary and secondary DNS servers (comma separated). Do not specify more than two servers. |
10. On the Ready to complete page, review the virtual machine configuration. 

    Make sure your passwords meet the requirements specified above before clicking Finish or your deployment will not succeed.
11. After the VCF Installer appliance is deployed, SSH in to the VM as the vcf user and the local user password provided in step 8.
12. Ensure that you can ping the ESX hosts.
13. Verify that the VCF Installer appliance has access to the required external services, such as DNS and NTP by performing forward and reverse DNS lookups for each host and the specified NTP servers.
14. In a web browser, log in to the VCF Installer appliance administration interface: https://installer\_appliance\_FQDN.

    Enter the admin@local user and the password you provided when you deployed the appliance and then click Log In.