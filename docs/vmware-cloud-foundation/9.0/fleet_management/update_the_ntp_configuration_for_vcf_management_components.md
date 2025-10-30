---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/configuring-managemnet-appliances/update-ntp-configuration.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Update the NTP Configuration for VCF Management Components
---

# Update the NTP Configuration for VCF Management Components

To update the NTP configuration for your VCF management component, you can use VCF Operations fleet management. The Update NTP Configuration option is supported for VCF Automation and VCF Identity Broker.

Verify that you have a current backup of the nodes in your cluster. See [Backup and Restore of VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation.html)

To update the NTP configuration of VCF core components, see [Update the NTP Server Configuration for VCF Core Components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/configuring-managemnet-appliances/update-ntp-server-configuration.html).

1. Under Fleet ManagementLifecycleComponents, select the integrated component that you want to update.
2. On the component details screen that appears, click the ellipses (...) and select Update NTP Configuration.
3. The Proceed to NTP Configuration Update pop-up window appears. If you have a taken a backup of your cluster, click Proceed.
4. Review the current configuration of your NTP servers and click Next.
5. On Update NTP Configuration, you can:

   - Click Use Host Time to change the time sync mode of your server to use the ESX NTP server.
   - Click Add New Server to configure a new server with a unique name and FQDN or IP address. Enter the server details, and click Submit.
   - To change the priority of your servers, click the up or down arrows.

   When finished, click Next.
6. To change NTP server priority, use the up and down arrows of the NTP servers listed and click Next.
7. Click RUN PRECHECK.

   If the data validation is not successful, perform the recommended actions and run the precheck again.
8. After a successful precheck run, review the summary of your add nodes request and click Finish.