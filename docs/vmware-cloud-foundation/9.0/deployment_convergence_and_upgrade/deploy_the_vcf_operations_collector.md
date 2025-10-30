---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/finish-configuring-newly-deployed-vcf-operations-instance-as-part-of-upgrade/deploy-the-cloud-proxy.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Deploy the VCF Operations collector
---

# Deploy the VCF Operations collector

Use VCF Operations fleet management to deploy the VCF Operations collector. After the deployment completes, reconfigure the VCF Instance to use the collector for new and existing domains.

Verify that the VCF Operations binary is downloaded and available. When the VCF Operations binary is downloaded, it will also map the binary for the VCF Operations collector. See [Downloading VCF management components into Binary Management](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/using-the-overview-tab.html).

The VCF Operations collector is the same as the VCF Operations Cloud Proxy that appears in the VCF Operations UI.

The following procedure shows how to deploy the VCF Operations collector using VCF Operations fleet management.

Alternatively, you can also deploy the VCF Operations collector using VCF Operations and vCenter. See [Configuring Cloud Proxies in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/configuring-cloud-proxies-in-vrealize-operations-cloud.html).

1. Log in to VCF Operations.
2. Select Fleet ManagementLifecycle and click the Components tab.
3. Under Integrated Components, click operations.
4. On the operations details page, click Add Nodes.

   The Proceed to Add Nodes dialog box appears.
5. Click Trigger Inventory Sync to synchronize the VCF Operations fleet management appliance with the latest data from the cluster.
   1. Click Submit to start the inventory sync.
   2. When the inventory sync completes, click Proceed.
6. On the Infrastructure page, review the existing infrastructure and click Next.
7. On the Network page, review the existing network information, add DNS and NTP servers, and click Next.
8. On the Components page, click the plus sign to add a cloud proxy (collector).
   1. VM Name: Enter a display name of the cloud proxy.
   2. Enter the FQDN of the cloud proxy.
   3. Enter the IP Address of the cloud proxy.
   4. Select the deployment type:

      - Small Unified
      - Standard Unified

      For information about cloud proxy types, see [Collecting Data with Cloud Proxy in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud.html).
9. To run prechecks, click Next.
10. On the Summary page, click Submit to deploy the cloud proxy (collector).
11. After the deployments completes, update the VCF instance integration to use the new collector for new workload domains.
    1. Select AdministrationIntegrations and click Accounts.
    2. Expand **VMware Cloud Foundation** and expand the integration that you want to configure.
    3. At the VCF instance level, click the vertical ellipsis and click **Edit**.
    4. On the Cloud Account Information page, from the Collector / Group drop-down menu, select the newly deployed collector, click Validate Connection, and click Save.
12. For the existing domains of the same VCF Instance, update the integrations for all vCenter instances to use the new collector/collector group.
    1. Select AdministrationIntegrations and click Accounts.
    2. Expand **VMware Cloud Foundation** and expand the integration that you want to configure.
    3. At the domain level, click the vertical ellipsis and click **Edit**.
    4. On the Connect vCenter page, from the Collector / Group drop-down menu, select the newly deployed collector, click Validate Connection, and click Save.
    5. Repeat the step for all remaining workload domains in that VCF instance.