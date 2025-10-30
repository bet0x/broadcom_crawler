---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/download-consistency-check-report.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Download the Consistency Check Report
---

# Download the Consistency Check Report

The optional Consistency Check Report allows you to view a list of errors and warnings that occurred during the upgrade so that you can perform remediation actions as needed.

The optional Consistency Check Report is different from the mandatory pre-check operations that run at the start of the upgrade workflow.

The upgrade coordinator in NSX Manager continuously monitors the system during the upgrade process for indicators of possible failure, such as:

- Policy objects that have not upgraded successfully
- Unusual increase in traffic drops in a cluster, indicating a possible failure in the cluster
- Unusual decrease in forwarding throughput in a cluster, indicating a possible failure in the cluster

You can retrieve the Consistency Check Report during or after the upgrade to view the list of possible failures. To retrieve the report, do one of the following:

- In the upgrade coordinator in NSX Manager, click the **Consistency Check Report** button to download the `.csv` report file.
- Call the consistency check API:

  ```
  GET https://{nsx-mgr}/api/v1/upgrade/consistency-report?component_type={MP, EDGE, HOST, ALL}        
  ```

For more information, see the [NSX API Guide](https://developer.broadcom.com/xapis/nsx-t-data-center-rest-api/latest/).