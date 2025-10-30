---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/troubleshooting-antrea-to-nsx-integration-issues/collect-support-bundles-for-an-antrea-kubernetes-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Collect Support Bundles for an Antrea Kubernetes Cluster
---

# Collect Support Bundles for an Antrea Kubernetes Cluster

You can use the Support Bundle feature in NSX to collect log files from Antrea Kubernetes cluster nodes for detailed troubleshooting and
diagnostic purposes.

Antrea Kubernetes clusters are registered
to NSX.

NSX can upload the support bundles
to an NSX Manager node from where
you triggered the support bundle collection request, or it can upload the support
bundles to a remote file server that you specified in the request. If the support
bundles are uploaded to an NSX Manager node, you can download them to your local computer.

This documentation uses the term
"Antrea Kubernetes cluster" to mean Kubernetes clusters with Antrea CNI. The term "Kubernetes cluster" is a
generic term, which represents Tanzu Kubernetes Grid (TKG) clusters with Antrea CNI, OpenShift clusters with Antrea CNI, or do it yourself (DIY) Kubernetes clusters with
Antrea CNI.

The UI use the term "Antrea
container cluster" for a few UI fields or labels. In the Procedure section of
this documentation, the term "Antrea container cluster" is retained for those UI
fields or labels. For all free-form text, the term "Antrea Kubernetes cluster"
is used.

A support bundle for an Antrea Kubernetes cluster contains log files for
the following components:

- Antrea Controller
- Antrea Agent
- Management Plane Adapter
- Central Control Plane Adapter
- Open vSwitch

Supported and Unsupported Features
:   - From
      an NSX Manager
      node, you can start only a single support bundle collection request.
      But, you can collect support bundles for multiple Antrea Kubernetes clusters with a
      single collection request.
    - If you are using an
      NSX Manager
      cluster with three Management nodes, you can start a separate
      support bundle collection request simultaneously from each
      NSX Manager
      node. However, the Antrea
      Kubernetes cluster that you select in each collection request must
      be different.

      For
      example, assume that you have started a support bundle
      collection request on NSX Manager node A. In this collection request,
      you selected cluster nodes 1 and 2 from Antrea Kubernetes cluster X.
      Simultaneously, if you start a second collection request on
      NSX Manager node B for the cluster nodes 3 and 4
      in the Antrea
      Kubernetes cluster X, one of these two collection requests will
      fail. You must wait for the first collection request to complete
      before triggering the second request for the same Antrea Kubernetes
      cluster.
    - Collection of support
      bundles from NSX Manager Central CLI is currently not supported for
      Antrea Kubernetes
      clusters.

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Navigate to SystemSupport Bundle.

   The Request Bundle  page opens.

   NSX Manager UI fetches the
   information about registered Antrea Kubernetes clusters when you start the
   NSX Manager
   application in the browser. If the application UI is already open, it does
   not fetch the Antrea Kubernetes
   cluster registration information automatically. This behavior is expected
   and per the current UI design. If you have registered the first Antrea Kubernetes cluster after the
   NSX Manager
   application is opened, ensure that you refresh the browser after navigating
   to the Request Bundle page. A manual refresh ensures
   that you can select Antrea
   Kubernetes clusters as the target nodes in the next step of this
   procedure.

   This manual
   browser refresh is required only once, and not every time after a new
   Antrea Kubernetes cluster
   is registered to NSX.
3. Select the target nodes to include in the support bundle request.

   The available types of nodes are:
   - Antrea Container Clusters
   - Management Nodes
   - Edges
   - Hosts

   A single support bundle
   request can include a mix of different types of nodes in the NSX environment. For example, you
   can select nodes from Antrea
   Kubernetes clusters, NSX Manager nodes, and NSX Edge nodes in the same collection request. However,
   the scope of this procedure is to explain the workflow of creating a support
   bundle collection request for only Antrea Kubernetes clusters.
4. From the
   Type drop-down menu, select Antrea
   Container Clusters.
5. From the Container
   Cluster list, select the name of a cluster.

   If the list has several clusters to select from, enter the first few
   characters of the cluster name. System filters the list and displays only the
   cluster names that match the characters you have entered.

   All nodes in the selected cluster are displayed in the
   Available list.
6. Select one or multiple nodes from
   the cluster and click the right arrow to move them to the
   Selected list.

   To select nodes from multiple
   clusters in a single collection request, repeat steps 4 and 5 for each
   cluster.
7. In the Log age (days)
    text box, keep the default value or enter the specific number of
   days' worth of logs that you want the support bundle to include. Specify the log
   age as a number of days.
8. To upload the support bundle to a
   remote file server, specify the file server settings.
   1. Enter an IP address or
      the host name of the remote file server.
   2. Enter the file transfer
      protocol and port number. Default port number is 22.
   3. Enter the user name and
      password to access the remote file server.
   4. Enter the path to the
      destination folder where the support bundle file is to be
      uploaded.

   When remote file server settings are not specified, the support bundle is
   uploaded to the NSX Manager
   node from where you triggered the support bundle collection request.
9. Click Start Bundle
   Collection.

   The runtime details of the collection request are displayed on the
   Status page. The collection process takes a few
   minutes. The time taken to create the support bundle depends on the number of
   log files to collect from each node in the container cluster.
10. After the collection process is complete, click
    Download.

    The support bundle file is saved on your local computer. If you had specified
    remote file server settings, the Download button is not
    displayed in the UI.

A support bundle collection request generates a single tape archive (TAR) file with
the following file naming convention:
nsx\_support\_archive\_datestamp\_timestamp.tar

Support bundle collection request can
fail in the following situations:

- If the Antrea NSX Adapter on a
  Kubernetes cluster fails when the support bundle request is in progress, the
  collection of logs fails for that Kubernetes cluster.
- If the NSX Manager Appliance fails or is
  not reachable when the support bundle request is in progress, the collection
  of logs fails. Until the connectivity issue to the NSX Manager is resolved, you can
  use the native command line tool of Antrea (antctl) to collect log files from the
  Antrea Kubernetes
  clusters.

Partial Success Scenario
:   Consider
    that you selected 10 nodes from a single Antrea Kubernetes cluster for the support bundle
    collection. During the collection process, log files were collected
    successfully from five nodes in the Antrea Kubernetes cluster, but were not collected for the
    remaining five nodes. In other words, the collection request succeeded
    partially. In this situation, the collection request status is
    Successful and the support bundle file
    (TAR) contains logs for the five successful
    nodes.

1. Extract the TAR file. The
   following files are displayed.

   | File Name | Description |
   | --- | --- |
   | manifest.json | This file contains a summary of the collection request results and the properties of the collection request.  For example, it contains information about: - The nodes for which the collection   succeeded. - The nodes for which the collection failed. - The cluster IDs and node IDs that were used in   the collection request. |
   | nsx\_antrea\_cluster-id.tgz | A single .tgz archive file is created for each Antrea Kubernetes cluster in the support bundle. |
2. Extract the
   nsx\_antrea\_cluster-id.tgz
   file. The following files are displayed.

   | File Name | Description |
   | --- | --- |
   | adapters.tar.gz | This archive file contains the log files of the Management Plane Adapter and the Central Control Plane Adapter. |
   | agent\_node\_name.tar.gz | This archive file contains the log files of the Antrea Agent and Open vSwitch. One archive file is generated for each Antrea Kubernetes cluster node in the collection request.  On extracting this archive file, you can view the following files: - agentinfo file - Agent logs at   /logs/agent - Open vSwitch logs at   /logs/ovs - OpenFlow dump - IPtables - Route dump |
   | clusterinfo | This file is generated for each Antrea Kubernetes cluster in the support bundle request. The file contains information about the following Kubernetes resources that are collected from the Kubernetes API server: - Pods - Nodes - Deployments - ReplicaSets - DaemonSets |
   | controller.tar.gz | This archive file contains the log files of the Antrea Controller.  On extracting this archive file, you can view the following files: - controllerinfo file - Controller logs at   /logs/controller |