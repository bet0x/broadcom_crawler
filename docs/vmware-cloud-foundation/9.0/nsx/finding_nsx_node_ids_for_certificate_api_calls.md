---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/finding-node-ids-for-certificate-api-calls.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Finding NSX Node IDs for Certificate API Calls
---

# Finding NSX Node IDs for Certificate API Calls

Use the NSX UI or CLI to find the node IDs required to import or replace certificates in manager nodes and clusters.

There are several types of node IDs required for certificate replacement. The type of certificate replacement you are performing will determine the type of node ID you need to include in your API call.

- To replace the API certificate of a manager node or other NSX Manager certificate, such as APH-AR, use the Unified Appliance node ID.
- To replace the transport node (TN) or the Edge host certificates, use the transport node ID.

| Task | From the UI | From the CLI |
| --- | --- | --- |
| To get the Unified Appliance node ID. | 1. Go to SystemAppliance. 2. From the NSX Manager tab, click View Details. 3. From the details pop-up, select the UUID icon to copy to clipboard. | Log in to any of the NSX Manager nodes using SSH and run the command: get cluster status. |
| To get the Edge transport node ID. | 1. Go to SystemFabricHostsClusters. 2. Select the ID value of the NSX Edge transport node and copy it to your clipboard. | Log in to the NSX Edge and run the command: get transport-nodes status. |
| To get the host transport node ID. | 1. Go to SystemFabricHostsClusters. 2. Select an NSX Edge cluster by clicking the check box in the first column. 3. Click the menu icon (three dots) and select Copy ID to Clipboard. | Log in to the NSX Edge and run the command: get transport-nodes status. |

If required, retrieve all three NSX Manager appliance node IDs and run the API calls for each appliance certificate replacement. For instructions, refer to [Replace NSX Certificates Using API](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/replace-certificates-through-api.html).