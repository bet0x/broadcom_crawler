---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform/download-and-deploy-the-vco-va.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Deploying VCF Operations orchestrator
---

# Deploying VCF Operations orchestrator

Before you can access the VCF Operations orchestrator content in your VCF environment, deploy the VCF Operations orchestrator appliance.

- Verify that you have a running vCenter instance. The vCenter version must be 9 or later.
- Verify that the host on which you are deploying the VCF Operations orchestrator appliance meets the minimum hardware requirements.

  - 4 CPUs
  - 12 GB of memory
  - 200 GB hard disk

  Do not reduce the default memory size, because the VCF Operations orchestrator server requires at least 8 GB of free memory.
- If your system is isolated and without Internet access, you must download the .ova file for the appliance from the Broadcom support portal.

1. Log in to the vSphere Client as an administrator.
2. Select an inventory object that is a valid parent object of a virtual machine, such as a data center, folder, cluster, resource pool, or host.
3. Select ActionsDeploy OVF Template.
4. Enter the file path or the URL to the .ova file and click Next.
5. Enter a name and location for the VCF Operations orchestrator appliance, and click Next.
6. Select a host, cluster, resource pool, or vApp as a destination on which you want the appliance to run, and click Next.
7. Review the deployment details, and click Next.
8. Accept the terms in the license agreement and click Next.
9. Select the storage format you want to use for the VCF Operations orchestrator appliance.

   Format | Description || Thick Provisioned Lazy Zeroed | Creates a virtual disk in a default thick format. The space required for the virtual disk is allocated when the virtual disk is created. If any data remains on the physical device, it is not erased during creation, but is zeroed out on demand later on first write from the virtual machine. |
   | Thick Provisioned Eager Zeroed | Supports clustering features such as Fault Tolerance. The space required for the virtual disk is allocated when the virtual disk is created. If any data remains on the physical device, it is zeroed out when the virtual disk is created. It might take much longer to create disks in this format than to create disks in other formats. |
   | Thin Provisioned Format | Saves hard disk space. For the thin disk, you provision as much datastore space as the disk requires based on the value that you select for the disk size. The thin disk starts small and, at first, uses only as much datastore space as the disk needs for its initial operations. |
10. Click Next.
11. Configure the network settings and enter the root password.

    When configuring the network settings of the VCF Operations orchestrator appliance, you must use the IPv4 protocol. For both DHCP and Static network configurations, you must add a fully qualified domain name (FQDN) for your VCF Operations orchestrator appliance.

    If the host name displayed in the shell of the deployed VCF Operations orchestrator appliance is photon-machine, the preceding network configuration requirements are not met.
12. Configure additional network settings for the VCF Operations orchestrator appliance, such as enabling SSH access.

    When configuring a Kubernetes network, the values of the internal cluster CIDR and internal service CIDR must allow for at least 1024 hosts. Because of this requirement, the network mask value must be 22 or less. Network mask values higher than 22 are invalid. The Kubernetes network properties have to following default values:

    |  |  |  |
    | --- | --- | --- |
    | Kubernetes network property | Default value | Property description |
    | Kubernetes internal cluster CIDR | 10.244.0.0/22 | The CIDR used for pods running inside the Kubernetes cluster. |
    | Kubernetes internal service CIDR | 10.244.4.0/22 | The CIDR used for Kubernetes services inside the Kubernetes cluster. |

    You can also change the Kubernetes CIDR network properties after deployment.
13. Click Next.
14. Review the Ready to complete page and click Finish.

The VCF Operations orchestrator appliance is successfully deployed.

Log in to the VCF Operations orchestrator appliance command line as root and confirm that you can perform a forward or reverse DNS lookup.

- To perform a forward DNS lookup, run the nslookupyour\_orchestrator\_FQDN command. The command must return the VCF Operations orchestrator appliance IP address.
- To perform a reverse DNS lookup, run the nslookup your\_orchestrator\_IP command. The command must return the VCF Operations orchestrator appliance FQDN.

For information on how to use VCF Operations orchestrator and how to integrate it with different VCF components, go to [Getting Started with VCF Operations orchestrator](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/configuration-of-vmware-cloud-foundation-operations-orchestrator/types-of-orchestrator-instances.html).

If you have not enabled SSH during deployment, you can also perform DNS lookups from the virtual machine console in vSphere Client.

If you encounter problems with your VCF Operations orchestrator deployment, go to [KB 93142](https://knowledge.broadcom.com/external/article?legacyId=93142).