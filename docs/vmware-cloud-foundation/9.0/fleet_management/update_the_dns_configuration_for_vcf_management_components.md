---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/configuring-managemnet-appliances/update-dns-configuration.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Update the DNS Configuration for VCF Management Components
---

# Update the DNS Configuration for VCF Management Components

To update the DNS configuration for your VCF management component, you can use the fleet management appliance. The Update DNS Configuration option is supported for VCF Automation and VCF Identity Broker.

Verify that you have a current backup of the nodes in your cluster.

To update the DNS configuration of VCF core components, see [Update the DNS Server Configuration for VCF Core Components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/configuring-managemnet-appliances/update-dns-server-configuration.html).

1. Under Fleet ManagementLifecycleComponents, select the integrated component that you want to update.
2. On the component details screen that appears, click the ellipses (...) and select Update DNS Configuration.
3. The Proceed to DNS Configuration Update pop-up window appears. If you have a taken a backup of your cluster, click Proceed.
4. Review the current configuration of your DNS servers and click Next.
5. On Update DNS Configuration, you can:

   - Click Add New Server to configure a new server with a unique name and IP address. Enter the server details, and click Submit.
   - To change the priority of your servers, click the up or down arrows.

   When finished, click Next.
6. To change DNS server priority, use the up and down arrows for the DNS servers listed and click Next.
7. Click RUN PRECHECK.

   If the data validation is not successful, perform the recommended actions and run the precheck again.
8. After a successful precheck run, review the summary of your add nodes request and click Finish.