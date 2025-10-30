---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/support-bundle-cloud-proxy.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Managing Cloud Proxy Support Bundles from the Administration UI
---

# Managing Cloud Proxy Support Bundles from the Administration UI

VCF Operations support bundles contain log and configuration files that help troubleshoot a VCF Operations cloud proxy issue.

Use the Support Bundles (Cloud Proxy) page to create the support bundle on cloud proxy.

Log in to the VCF Operations administration interface at https://master-node-name-or-ip-address/admin and then click SupportSupport Bundles (Cloud Proxy).

## Support Bundle (Cloud Proxy) Options

The options include toolbar and data grid options.

Use the toolbar options to add, download, or remove items.

Support Bundle (Cloud Proxy) Toolbar Options



| Option | Description |
| --- | --- |
| Add | Open a dialog box that guides you through the process of creating a support bundle on cloud proxy. Select the cloud proxy and then click OK to create a support bundle on the selected cloud proxy.  The support bundle is created under the following directory /storage/core/vmware-vrops-cprc/support. |
| Delete | Remove the selected support bundle. |
| Download | Download the support bundle in ZIP format. |
| Reload | Refresh the list of support bundles. |

Use the data grid options to view item details.

Support Bundle (Cloud Proxy) Data Grid Options



| Option | Description |
| --- | --- |
| Bundle | System-generated identifier for the support bundle. |
| Cloud Proxy Name | The name of the cloud proxy on which the support bundle is created. |
| Date and Time Created | Time when support bundle creation began. |
| Status | Progress of support bundle creation. |
| File Size | The size of the support bundles. |

Generation and download of support bundles through the Support Bundles (Cloud Proxy) page works only if the cloud proxy is connected to the cluster.

If there is a disconnect between the cloud proxy and VCF Operations, you can generate a support bundle on cloud proxy manually.

Open an SSH connection with the cloud proxy appliance and run the followng command:

- For 8.3 and 8.4 version: $> cprc-cli -sb
- For 8.5 and later versions: $> cprc-cli -sb IS\_HEAVY, where IS\_HEAVY should be specified as true or false

With cprc-cli -sb true, the support bundle is generated with journal.ctl logs. With cprc-cli -sb false , the support bundle is generated without journal.ctl logs. The support bundle is created in the following path: directory /storage/db/vmware-vrops-cprc/support.

For adding some extra files into the support bundle, you need to modify configuration file available here: /storage/db/vmware-vrops-cprc/configuration/cprc.support.bundle.configuration . Add the path of needed file into cprc.support.bundle.configuration in the files: section. Then generate the support bundle with the cprc-cli -sb or cprc-cli -sb false command, based on the version you are on.

For example if you want to add the /var/log/firstboot/vcopssuitevm.log file into the support bundle, add this path into the files: section of /storage/db/vmware-vrops-cprc/configuration/cprc.support.bundle.configuration. Then generate the support bundle with either the cprc-cli -sb or the cprc-cli -sb false command, based on the version you are on.

Once done, you can download or delete these support bundles from the Support Bundles (Cloud Proxy) page.