---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance/connect-to-an-online-depot-to-download-binaries.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Connect to an Online Depot to Download Binaries
---

# Connect to an Online Depot to Download Binaries

If the VCF Installer can connect to the internet (either directly or through a proxy server), you can connect to an online depot and download the binaries using your Broadcom Support Portal account.

- See [KB 327186](https://knowledge.broadcom.com/external/article/327186) for information about the URLs that must be accessible to download bundles.
- Obtain a download token from the Broadcom Support Portal.

You can only connect the VCF Installer appliance to one type of depot. If the appliance is connected to an online depot and you configure a connection to an offline depot, the online depot connection is disabled and deleted.

1. In a web browser, log in to the VMware Cloud Foundation Installer appliance administration interface: https://installer\_appliance\_FQDN. 

   Enter the admin@local user and password you provided when you deployed the appliance and then click Log In.
2. Click Depot Settings and Binary Management .
3. Click Configure to connect to the online depot
4. Enter the download token you obtained from the Broadcom Support Portal.
5. To configure a proxy server, toggle the Enable proxy server setting to the on position.
   1. Select HTTP  or HTTPS.
   2. Enter the proxy server FQDN/IP address and port number.
   3. If your proxy server requires authentication, toggle the Authenticated setting to the on position and enter the user name and password. 

      VMware Cloud Foundation does not support proxy servers with NTLMv2 authentication.
6. Click Configure.

You are now ready to download binaries.