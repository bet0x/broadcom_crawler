---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/troubleshooting-antrea-to-nsx-integration-issues/antrea-kubernetes-cluster-status-is-down.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   Antrea Kubernetes Cluster Status is Down
---

# Antrea Kubernetes Cluster Status is Down

If the status of the Antrea Kubernetes
cluster is down, follow the steps in this documentation either to determine the cause of
this issue and recover from it, or collect the support bundle.

The cluster control plane node is down. The Antrea Kubernetes cluster is disconnected from the Central
Control Plane (CCP).

In the NSX Manager UI, navigate to SystemFabricNodesContainer ClustersAntrea. If required, filter the list of clusters on the
Antrea page with the External ID
field.

Click the Status
column of the problematic cluster. If all the components are down, the possible
causes are:

- The Kubernetes cluster is
  deleted.
- Network connectivity issue with
  the CCP.
- The adapters are crashed or
  deleted for some reason.
- The client certificate of the
  adapters is incorrect.
- The version of the adapters is
  incompatible with the CCP.

If only the Central Control Plane Adapter is down, the
CCP Adapter might have crashed.

1. If the Kubernetes cluster is
   deleted, clean up the leftover registration and inventory data in NSX. See [Clean up Antrea Data from NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/deregister-an-antrea-kubernetes-cluster-from-nsx/clean-up-antrea-data-from-nsx.html#GUID-9bf1c20c-8950-4803-afa4-c6a85c07d6b0-en).
2. Get the kubectl and kubeconfig
   access for the Kubernetes cluster. Use kubectl to retrieve the node name on
   which the interworking pod is running. Start an SSH session to the node and use
   the curl or nc command to connect to every NSX Manager IP on ports 1234 and 1235. If the connection
   cannot be established, the cause is network connectivity issue with the
   CCP.

   Example of the curl command:

   Ensure that you replace NSX-Manager-IP with the IP
   address of NSX Manager in
   your
   environment.

   ```
   curl -v NSX-Manager-IP:1235

   Trying NSX-Manager-IP... 
   Connected to NSX-Manager-IP (NSX-Manager-IP) port 1235 (#0) 
   ... 
   Empty reply from server 
   Connection #0 to host NSX-Manager-IP left intact 
   curl: (52) Empty reply from server
   ```

   Example of the nc
   command:

   ```
   nc -v NSX-Manager-IP 1235 < /dev/null

   Ncat: Version 7.50 (https://nmap.org/ncat)
   Ncat: Connected to NSX-Manager-IP:1235.
   Ncat: 0 bytes sent, 0 bytes received in 0.37 seconds.
   ```
3. Use kubectl to check whether all containers of the interworking pod in the
   vmware-system-antrea namespace are up.

   If any container is down, use kubectl to get logs of the crashed containers
   and check the error message. This step can help you identify failure due to any
   of these reasons:
   - The adapters are crashed or
     deleted for some reason.
   - CCP Adapter is
     crashed.

   Example of the kubectl command for getting the interworking
   pod:

   ```
   kubectl get pod -o wide -l app=antrea-interworking -n vmware-system-antrea
   ```

   Note down the interworking pod
   name.

   Example of the
   kubectl command for getting the detailed state of the interworking
   pod:

   Ensure that you
   replace pod-name with the actual pod
   name.

   ```
   kubectl get pod -o yaml pod-name -n vmware-system-antrea
   ```

   Example of the kubectl command
   for getting container logs:

   Ensure that you replace
   pod-name with the actual pod
   name.

   ```
   kubectl logs pod-name -c mp-adapter -n vmware-system-antrea > mp-adapter.log
   kubectl logs pod-name -c ccp-adapter -n vmware-system-antrea > ccp-adapter.log
   kubectl logs pod-name -c tn-proxy -n vmware-system-antrea > tn-proxy.log
   kubectl logs pod-name -c election-runner -n vmware-system-antrea > election-runner.log
   ```

   If the vmware-system-antrea
   namespace is missing or the interworking pod is missing, the adapters might
   have been deleted from the Kubernetes cluster without running the
   deregistration steps. You can clean up the leftover registration data and
   inventory from the system, and then register the Kubernetes cluster again.
   The cluster ID will be different after reregistering the cluster. If there
   is any Antrea policy applied to
   the cluster, you must apply the policy again after reregistering the
   cluster.

   For instructions about cleaning
   up the leftover registration data, see [Clean up Antrea Data from NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/deregister-an-antrea-kubernetes-cluster-from-nsx/clean-up-antrea-data-from-nsx.html#GUID-9bf1c20c-8950-4803-afa4-c6a85c07d6b0-en).

   For instructions about
   registering an Antrea Kubernetes
   cluster to NSX, see [Registering an Antrea Kubernetes Cluster to NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/registering-an-antrea-kubernetes-cluster-to-nsx.html#GUID-f5e1a6c4-29be-4dca-9124-5a0b38bce33c-en).
4. Use kubectl to get nsx-proxy container logs from the interworking pod, and
   check the error messages.

   This step can help you identify
   failure due to any of these reasons:
   - The client certificate
     of the adapters is incorrect.
   - The version of the
     adapters is incompatible with the CCP.

   For example commands, see step
   3.
5. If the Management Plane Adapter is up,
   use the support bundle feature in NSX to
   collect log files for the Antrea
   Kubernetes cluster.

   For more information, see [Collect Support Bundles for an Antrea Kubernetes Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/troubleshooting-antrea-to-nsx-integration-issues/collect-support-bundles-for-an-antrea-kubernetes-cluster.html#GUID-f29372f4-11a6-4055-a0a7-23e3cae968c6-en).