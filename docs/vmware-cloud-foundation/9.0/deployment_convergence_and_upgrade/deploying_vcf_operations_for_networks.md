---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform/installing-vcf-networks.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Deploying VCF Operations for Networks
---

# Deploying VCF Operations for Networks

VCF Operations for networks provides a comprehensive overview of your VMware Cloud Foundation platform network health, issues, and operations all in one place. Deployed as an appliance using VCF Operations fleet management, it consists of Platform and Collector nodes.

Before starting the installation, download the operations-networks binary to the fleet management appliance. See [Downloading VCF management components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/using-the-overview-tab.html). Then select Fleet ManagementLifecycle and click Add on operations-networks.

The deployment moves through the following stages.

1. Deployment

   - Installation type

     |  |  |
     | --- | --- |
     | New Install | Choose this option to perform a fresh installation. |
     | Import | Imports an existing **operations-networks 9.0** deployment. Not applicable for a new installation.  If you have an existing VCF Operations for Networks deployment that is not managed by VMware Aria Suite Lifecycle , you can use this option to import your VCF Operations for networks into VCF Operations then upgrade to VCF Operations for networks. |
     | Import from legacy fleet management | Imports VMware Aria Operations for Networks 6.x for upgrade to operations-networks 9.0. |
   - Version: 9.0.0.0
   - Deployment type: Standard or Cluster
2. Certificate: Select the certificate for deployment. If no certificate is available, you can generate or import one.
3. Infrastructure

   - Select vCenter: Select the vCenter for the Management Domain.
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
   - DNS Servers
   - Time Sync Mode: Use NTP Server, Use Host Time
   - IPv4 Details:

     - Default IPv4 Gateway
     - IPv4 Netmask
5. Component Properties

   - FIPS Compliance Mode: Default is on. If not needed, turn it off.
   - Certificate: Pre-selected from the previous step. To create a new certificate, click Add Certificate.
   - Anti-Affinity/Affinity Rule: Selection is on by default. If selected, choose the DRS Anti-Affinity rule type:

     - Keep virtual machines in separate hosts: For anti-affinity, select this rule type.
     - Keep virtual machines in same host: For affinity, select this rule type.

     If the Anti-Affinity/Affinity Rule selection is deselected, DRS Anti-Affinity rule type does not appear.
   - Component Password: Select a password to be used by admin, support, and console users. If you do not have a password, click Add Password to create a new one. Password must be a minimum of 15 characters.
   - NTP Servers: Pre-selected from previous step. Change as needed.
6. Components

   - Platform VM: Enter the Name, IP Address, and Node Size for the Platform VM
   - Collector VM: Enter the Name, IP Address, and Node Size for the Collector VM

   FQDNs are not required for the VCF Operations for Network deployment, but you should configure DNS records for IP addresses consumed by Platform and Collector VMs on their respective DNS Servers.
7. Precheck: If the precheck completes successfully, click Next.
8. Summary: To trigger deployment after reviewing the summary, click Submit.