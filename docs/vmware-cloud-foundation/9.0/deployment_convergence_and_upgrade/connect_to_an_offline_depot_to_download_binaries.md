---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance/connect-to-an-offline-depot-to-download-binaries.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Connect to an Offline Depot to Download Binaries
---

# Connect to an Offline Depot to Download Binaries

If the VCF Installer appliance cannot connect to the internet, you can connect to an offline depot.

You must set up an offline depot before you can connect to it. See [Set Up an Offline Depot Web Server for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance/connect-to-an-offline-depot-to-download-binaries/set-up-an-offline-depot-web-server-for-vmware-cloud-foundation.html).

You can only connect the VCF Installer appliance to one type of depot. If the appliance is connected to an online depot and you configure a connection to an offline depot, the online depot connection is disabled and deleted.

1. In a web browser, log in to the VMware Cloud Foundation Installer appliance administration interface: https://installer\_appliance\_FQDN. 

   Enter the admin@local user and password you provided when you deployed the appliance and then click Log In.
2. Click Depot Settings and Binary Management .
3. Click Configure to connect to the offline depot
4. Enter the following information for the offline depot: 

   - FQDN or IP address
   - Port
   - User name
   - Password
5. Click Configure.

You are now ready to download binaries.