---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform/installing-vcf-identity-broker.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Deploying VCF Identity Broker
---

# Deploying VCF Identity Broker

VCF Identity Broker provides Single Sign-On for VMware Cloud Foundation and VMware vSphere Foundation products. Deploying VCF Identity Broker in appliance mode in fleet management allows users to access VCF management components with a single set of credentials.

Deploying VCF Identity Broker in appliance mode is suitable for environments that require high availability utilizing a multi-node cluster. VCF Identity Broker can also be deployed as an embedded service within the management domain vCenter instance. For more information about VCF Identity Broker models, see [VCF Identity Broker Detailed Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-instance-models.html).

Before starting the appliance deployment, download the VCF Identity Broker install binary to the fleet management appliance. See [Downloading VCF Management Components into Binary Management](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/using-the-overview-tab.html). Then select Fleet ManagementLifecycle and click Add on identity broker.

The deployment moves through the following stages.

1. Deployment

   - Installation type

     |  |  |
     | --- | --- |
     | New Install | Choose this option to perform a fresh installation. |
     | Import | Imports an existing **identity broker** deployment, for example if VCF Identity Broker was removed for troubleshooting. |
   - Version: 9.0.0.0
   - Deployment type: Small. For a small deployment, the cluster requires: 3 VMs, 8 vCPUs per VM, 16 GB RAM per VM, 100 GB disk per VM.
2. Certificate: Select the certificate for deployment. If a certificate is not available, click Add Certificate to create a new one. See [Managing Certificates in VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0.html).
3. Infrastructure

   - Select vCenter.

     vCenter servers with any of the following conditions are not listed:

     - VCF Identity Broker deployed in vCenter using the VCF Operations API.
     - vCenter version greater than 9.0
     - vCenter associated with SDDC Manager
     - vCenter used by another VCF Identity Broker instance. To use the vCenter, delete the associated VCF Identity Broker instance.
   - Select Cluster: Select the cluster in the management domain vCenter for deployment.
   - Select Folder
   - Select Resource Pool
   - Select Network
   - Select Datastore
4. Network

   - Domain Name
   - Domain Search Path
   - DNS Servers: If the required DNS server is not listed, add it.
   - Time Sync Mode: Point to an NTP Server or Host Time
   - IPv4 Details:

     - Default IPv4 Gateway
     - IPv4 Netmask
5. Components

   - Install identity broker:

     - Add Password: If you do not have a password, click Add Password to create a new one. Password must be a minimum of 15 characters.
     - Add Certificate: Select the certificate for deployment. To create a new certificate, click Add Certificate .
   - Component Properties

     - FQDN: Component FQDN
     - Certificate: Accept the automatic selection.
     - Component Password: Needed for the vmware-system-user and the operator account. Password must be a minimum of 15 characters.
   - Components

     - VM Node Prefix: A unique identifier used to name component nodes. To avoid conflicts and maintain proper node identification within the cluster, ensure that the node prefix is unique.
     - Internal Cluster CIDR: IP Address range used for internal cluster communication within the cluster. Choose a range that does not conflict with existing networks in infrastructure.
     - Primary VIP: Used for accessing component services. Should resolve to the Component Properties FQDN
     - Additional VIPs: (optional) Add up to 2 VIPs.
     - Cluster Node IP Pool: The Node IP Pool is a range of IP addresses allocated to cluster nodes. These IP's ensure that each node has a unique address for internal communication within the cluster. Additional IP's from the pool will be used during rolling cluster upgrades.

       - A minimum of 4 IP addresses needed, maximum number of IP’s is 7.
       - Three of these IP addresses will be used for deploying cluster nodes hosting VCF Identity Broker component. Spare IP addresses will be used during rolling upgrades and patches.

To execute the Precheck, click Next.

1. Precheck: If the precheck completes successfully, click Next.
2. Summary: To trigger deployment after reviewing the summary, click Submit.