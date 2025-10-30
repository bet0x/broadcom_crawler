---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/connect-sddc-manager-to-a-software-depot-for-downloading-bundles.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Connect SDDC Manager to a Depot for Accessing Bundles
---

# Connect SDDC Manager to a Depot for Accessing Bundles

Connect to an online or offline depot to access software bundles, compatibility data, and more.

To connect to an online depot, SDDC Manager must be able to access the internet, either directly or through a proxy server. See [Configure a Proxy Server for Accessing VMware Cloud Foundation Bundles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/connect-sddc-manager-to-a-software-depot-for-downloading-bundles/configure-a-proxy-server-to-download-bundles-from-sddc-manager.html). If you have not already done so, you must configure SDDC Manager to use a download token. See [KB 390098](https://knowledge.broadcom.com/external/article/390098).

To connect to an offline depot, you must first configure it. See [KB 312168](https://knowledge.broadcom.com/external/article/312168) for information about the requirements and process for creating an offline depot. To download bundles to an offline depot using the VCF Download Tool, see [Download VMware Cloud Foundation 9.0 Upgrade Bundles to an Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/download-bundles-to-an-offline-depot.html).

See [Public URL list for SDDC Manager](https://knowledge.broadcom.com/external/article/327186) for information about the URLs that must be accessible to download bundles.

SDDC Manager supports two types of software depots:

- Online depot
- Offline depot

You can only connect SDDC Manager to one type of depot. If SDDC Manager is connected to an online depot and you configure a connection to an offline depot, the online depot connection is disabled and deleted.

1. In the navigation pane, click AdministrationDepot Settings.
2. Connect SDDC Manager to an online depot or an offline depot.

   | Depot Type | Configuration Steps |
   | --- | --- |
   | Online | 1. Click Authenticate for the VMware Depot. 2. Type your Broadcom Support Portal user name and password. 3. Click Authenticate |
   | Offline | 1. Click Set Up for the Offline Depot. 2. Enter the following information for the offline depot:    - Hostname    - Port number    - Username    - Password 3. Click Save. |

   SDDC Manager attempts to connect to the depot. If the connection is successful, SDDC Manager starts looking for available bundles. To view available bundles, click Lifecycle ManagementBundle Management and then click the Bundles tab. It may take some time for all available bundles to appear.