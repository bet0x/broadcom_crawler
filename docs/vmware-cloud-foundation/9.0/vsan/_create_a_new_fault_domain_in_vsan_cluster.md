---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/managing-fault-domains-in-vsan-clusters/create-a-new-fault-domain-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >  Create a New Fault Domain in vSAN Cluster
---

# Create a New Fault Domain in vSAN Cluster

To ensure that the virtual machine objects continue to run smoothly during a rack failure, you can group hosts in different fault domains.

- Choose a unique fault domain name. vSAN does not support duplicate fault domain names in a cluster.
- Verify the version of your ESX hosts.
- Verify that your vSAN hosts are online. You cannot assign hosts to a fault domain that is offline or unavailable due to hardware configuration issue.

When you provision a virtual machine on the vSphere cluster with fault domains, vSAN distributes protection components, such as witnesses and replicas of the virtual machine objects across different fault domains. As a result, the vSAN environment becomes capable of tolerating entire rack failures in addition to a single host, storage disk, or network failure.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Fault Domains.
4. Click the plus icon.

   The New Fault Domain wizard opens.
5. Enter the fault domain name.
6. Select one or more hosts to add to the fault domain. 

   A fault domain cannot be empty. You must select at least one host to include in the fault domain.
7. Click Create. 

   The selected hosts appear in the fault domain. Each fault domain displays the used and reserved capacity information. This enables you to view the capacity distribution across the fault domain.