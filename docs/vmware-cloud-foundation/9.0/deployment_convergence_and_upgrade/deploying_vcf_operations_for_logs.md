---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform/installing-vcf-logs.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Deploying VCF Operations for logs
---

# Deploying VCF Operations for logs

VCF Operations for logs is designed to help you collect, analyze, and visualize logs from across your VMware Cloud Foundation platform.

You deploy the VCF Operations for logs appliance by using VCF Operations fleet management. This provides:

- Centralized log aggregation: Collect logs from all VCF components, such as vCenter, ESX, NSX, vSAN, VCF Automation, VCF Operations, VCF Identity Broker, VCF Operations for networks, and VCF Operations HCX
- Real-time analytics: Search and filter logs instantly for troubleshooting or auditing.
- Dashboards and alerts: Content packs for VCF components offer pre-built dashboards, alerts, and queries.

Before starting the installation, download the operations-logs binary to the fleet management appliance. See [Downloading VCF management components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/using-the-overview-tab.html). Then select Fleet ManagementLifecycle and click Add on operations-logs.

The deployment moves through the following stages.

1. Deployment

   - Installation type

     |  |  |
     | --- | --- |
     | New Install | Choose this option to perform a fresh installation**.** |
     | Import | Imports an existing **operations-logs 9.0** or later deployment. Not applicable for a new installation. |
   - Version: 9.0.0.0
   - Deployment type: Standard or Cluster
2. Certificate: Select the certificate for deployment. If no suitable certificate is available, you can generate or import one.
3. Infrastructure

   - Select vCenter: Lists management domains for deployment.
   - Select Cluster
   - Select Folder (optional)
   - Select Resource Pool (optional)
   - Select Network
   - Select Datastore
   - Select Disk Mode
   - Use Content Library
4. Network

   - Domain Name
   - Domain Search Path
   - DNS Servers: If none exist, then add one and select it.
   - Time Sync Mode: Use NTP Server, Use Host Time
   - IPv4 Details:

     - Default IPv4 Gateway
     - IPv4 Netmask
5. Components

   - Enter Component Properties

     - Node Size: Select Small, Medium or Large. Medium is the minimum size recommended for production, testing, or development-type deployments.
     - FIPS Compliance Mode: Default is on. If not needed, turn it off.
     - Certificate: Pre-selected from the previous step. To create a new certificate, click Add Certificate.
     - Set Affinity & Anti-Affinity rule if needed. If selected choose the DRS Anti-Affinity rule type:

       - Keep virtual machines in separate hosts: For anti-affinity, select this rule type.
       - Keep virtual machines in same host: For affinity, select this rule type.
     - Configure Cluster VIP: If set to YES, the Cluster VIP section appears. Enter:

       - FQDN of the of the Cluster VIP
       - IP address that points to the FQDN of the Cluster VIP
     - Upgrade VM Compatibility
     - Always Use English
     - Admin Email
     - Component Password: Select a password to be used by root and admin local accounts. If you do not have a password, click Add Password to create a new one. Password must be a minimum of 15 characters.
     - Time Sync Mode: Preselected.
   - Enter Component/Node properties

     - VM Name
     - FQDN
     - IP Address
6. Precheck: If the precheck completes successfully, click Next.
7. Summary: To trigger deployment after reviewing the summary, click Submit.