---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/configure-an-online-depot-for-a-vcf-instance.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Connect to an Online Depot for a VCF Instance
---

# Connect to an Online Depot for a VCF Instance

Connect to an online depot for your VCF Instance to access upgrade, patch, and install binaries.

- To connect to an online depot, SDDC Manager must be able to access the internet, either directly or through a proxy server. See [Configure a Proxy Server for SDDC Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/configure-an-online-depot-for-a-vcf-instance/configure-a-proxy-server-for-a-vcf-instance.html).
- If your environment is using a TSL interception and / or TSL termination proxy with a custom CA certificate to connect to the internet, you must import the proxy's CA certificate to the SDDC Manager trust store. See [KB 316056](https://knowledge.broadcom.com/external/article/316056).
- Generate a download token on the Broadcom Support Portal.
- See [Public URL list for SDDC Manager](https://knowledge.broadcom.com/external/article/327186) for information about the URLs that must be accessible to download binaries.

SDDC Manager supports two types of software depots:

- Online depot
- Offline depot

You can only connect SDDC Manager to one type of depot. If SDDC Manager is connected to an online depot and you configure a connection to an offline depot, the online depot connection is disabled and deleted.

If you configured an online depot in VCF Installer, the VCF Instance inherits the depot settings.

1. In VCF Operations, click Fleet ManagementLifecycle.
2. Click VCF Instances and click the name of a VCF Instance.
3. Click Depot Settings.
4. Click Authenticate to set up an online depot.
5. Paste the download token that you generated on the Broadcom Support Portal in the text box and click Authenticate.

   SDDC Manager attempts to connect to the depot. If the connection is successful, SDDC Manager starts looking for available binaries. To view available binaries, click the Binary Management tab. It may take some time for all available binaries to appear.