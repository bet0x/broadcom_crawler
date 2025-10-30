---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/install-vcf-automation-as-a-day-n-operation.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Deploying VCF Automation as a Day-N Operation
---

# Deploying VCF Automation as a Day-N Operation

If VCF Automation was not deployed as part of the initial VMware Cloud Foundation deployment or import of an Aria Automation 8.x instance, you can add it as a Day-N operation using VCF Operations fleet management. Deployment of only a single VCF Automation instance is supported.

Download the install binaries for VCF Automation from Binary Management. See [Downloading VCF management components](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/using-the-overview-tab.html).

The following procedure shows how to deploy a new instance of VCF Automation.

1. On the Overview tab under Fleet ManagementLifecycle, click Add on the tile for VCF Automation.
2. Select the options for your deployment.

   - For the Installation type, select New Install.

   - Version: 9.0 (default)
   - Deployment Type: To choose the correct type, click View Sizing Info and review the compute nodes and resources that a Small, Medium, or Large deployment supports. For sizing guidelines, download the [Planning and Preparation Workbook](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-planning-and-preparation-workbook.xlsx) and click the Management Domain Sizing tab. Notes with general guidelines are at the far right of the page.
3. If you select NEW, click + to create a certificate:

   - Enter an FQDN
   - The Common Name and a Subject Alternative Name must include the FQDN
4. Enter the Infrastructure properties.

   - For vCenter, select the Management Domain vCenter
   - Enter information for the primary cluster.
     - Cluster
     - Folder
     - Resource Pool
     - Network
     - Datastore
5. Enter the Network properties.

   - Domain Name: Top-level domain, such as example.com.
   - Domain Search Path: Top-level domain, such as example.com.
   - DNS Servers: To select the DNS server that you want to configure VCF Automation with, click Edit Server Selection. If the DNS server that you want is not available, click Add New Server to add and select it.
   - NTP: To select the NTP server that you want to VCF Automation with, click Edit Server Selection. If the NTP server that you want is not available, click Add New Server to add and select it.
   - IPv4 Details:
     - IPv4 gateway: Default gateway of the network for VCF Automation to join.
     - IPv4 netmask: Netmask of the network for VCF Automation to join.
6. Enter the Component information.

   Component Properties

   - FQDN -- Enter the component FQDN
   - Certificate is prepopulated with the value from the previously added certificate.
   - Component Password -- Select one component password for two accounts:
     - vmware-system-user
     - Provider's admin accountIf you do not have a password, click Add Password to create a new one. Password must be a minimum of 15 characters.

   Cluster VIP

   - Choose internal or external load balancer:
     - For internal load balancer, the FQDN should resolve to the primary VIP address.
     - For an external load balancer or others, the FQDN should resolve to the Virtual Server IP address of the load balancer.

   Components

   - VM Node Prefix**:** A unique identifier used to name component nodes. To avoid conflicts and maintain proper node identification within the cluster, ensure that the node prefix is unique.
   - Internal Cluster CIDR**:** IP Address range used for internal cluster communication within the cluster. Choose a range that does not conflict with existing networks in infrastructure
   - Primary VIP: The Primary Virtual IP Address is used for accessing component services
     - Primary VIP if using internal load balancer

       If using an internal load balancer, this Primary VIP Address should resolve to the component FQDN.

       ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/83fd9ff5-c8af-4c36-988f-a5c28ef30277.original.png)
     - Primary VIP if using external load balancer

       If using an external load balancer, this Primary VIP Address and Additional VIPs should be in or added to the server pool that the load balancer can direct traffic to.

       ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/61d099a4-9d5f-4ca9-8989-b19a5ba6ce1a.original.png)
   - Additional VIP addresses**:** This is optional. Depending on the small, medium, or large deployment type, you may add up to two additional VIPs.
   - VM Node Prefix: Unique identifier used to name component nodes. Ensure this prefix is distinct for a cluster to avoid conflicts and maintain proper node identification
   - Cluster Node IP Pool**:** The Node IP Pool is a range of IP addresses allocated to cluster nodes. These IP's ensure that each node has a unique address for internal communication within the cluster. Additional IP addresses from the pool will be used during rolling cluster upgrades. The pool must contain a minimum of four IP addresses.
   - Cluster CIDR: IP address range used for internal cluster communication within the cluster. Choose a range that does not conflict with existing networks in the infrastructure.
7. Precheck: Click Run Precheck.
8. Summary: To trigger the deployment after reviewing the summary, click Submit.