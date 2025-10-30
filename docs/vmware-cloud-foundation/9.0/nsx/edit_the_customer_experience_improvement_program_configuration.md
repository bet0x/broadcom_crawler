---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/customer-experience-improvement-program-nsx-t/edit-the-customer-experience-improvement-program-configuration.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Edit the Customer Experience Improvement Program Configuration
---

# Edit the Customer Experience Improvement Program Configuration

When you install or upgrade NSX Manager, you can decide to join the CEIP and configure data collection settings.

- Verify that the NSX Manager is connected and can synchronize with your hypervisor.
- Verify that NSX is connected to a public network for uploading data.

You can also edit the existing CEIP configuration to join or leave the CEIP program, define the frequency and the days the information is collected, and proxy server configuration.

1. With admin privileges, log in
   to NSX Manager.
2. Select SystemGeneral SettingsCustomer Program.
3. Click Edit in the Customer Experience Improvement Program section.
4. In the Edit Customer Experience Program dialog box, select the Join the VMware Customer Experience Improvement Program check box.
5. Toggle the Schedule switch to disable or enable the data collection. 

   The schedule is enabled by default.
6. Configure the data collection and upload recurrence settings.
7. Click Save.
8. If you configured the recurrence settings in step 6, you must restart the telemetry service on NSX Manager. If you have an NSX Manager cluster, you must do this on every manager in the cluster.
   1. SSH to NSX Manager and log in as admin.
   2. Run the following command to restart the telemetry service:

      ```
      restart service telemetry
      ```