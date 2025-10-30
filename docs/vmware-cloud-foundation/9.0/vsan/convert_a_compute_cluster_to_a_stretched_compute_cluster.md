---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-vsan-stretched-compute-cluster/convert-a-vsan-compute-cluster-to-a-vsan-stretched-compute-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Convert a Compute Cluster to a Stretched Compute Cluster
---

# Convert a Compute Cluster to a Stretched Compute Cluster

If you have an existing compute cluster, you can convert the compute cluster to a stretched compute cluster. Once converted, the stretched compute cluster can mount remote datastores from a vSAN stretched cluster.

1. In the vSphere Client, navigate to the existing compute cluster.
2. Click the Configure tab.
3. Under vSAN, select Fault Domains.
4. Click Configure to open the Configure Stretched Compute Cluster dialog.
5. Select the hosts that you want to be part of the first and the second fault domain. You can move hosts between fault domains or rename the fault domain name.
6. Click Apply.