---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/troubleshooting-upgrade-failures-nsxt/collect-support-bundles.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Collect Support Bundles
---

# Collect Support Bundles

You can collect support bundles on registered cluster and fabric nodes and download the bundles to your machine or upload them to a file server.

If you choose to download the bundles to your machine, you get a single archive file consisting of a manifest file and support bundles for each node. If you choose to upload the bundles to a file server, the manifest file and the individual bundles are uploaded to the file server separately.

1. From your browser, log in as a local admin user to an NSX Manager at https://nsx-manager-ip-address/login.jsp?local=true.
2. Select SystemSupport Bundle
3. Select the target nodes. 

   The available types of nodes are Management Nodes, Edges, and Hosts.
4. Specify log age in days to exclude logs that are older than the specified number of days.
5. Toggle the switch that indicates whether to include or exclude core files and audit logs. 

   Core files and audit logs might contain sensitive information such as passwords or encryption keys.
6. Select the check box to upload the bundles to a remote file server.
7. Click Start Bundle Collection to start collecting support bundles. 

   Depending on how many log files exist, each node might take several minutes.
8. Monitor the status of the collection process. 

   The status tab shows the progress of collecting support bundles.
9. Click Download to download the bundle if the option to send the bundle to a file remote server was not set. 

   The bundle collection may fail for a manager node if there is not enough disk space. If you encounter an error, check whether older support bundles are present on the failed node. Log in to the NSX Manager UI of the failed manager node using its IP address and initiate the bundle collection from that node. When prompted by the NSX Manager, either download the older bundle or delete it.