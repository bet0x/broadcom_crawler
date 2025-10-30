---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking/vsan-network-characteristics/using-unicast-in-vsan-network/intra-cluster-traffic/intra-cluster-traffic-in-a-stretched-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Intra-Cluster Traffic in a vSAN Stretched Cluster
---

# Intra-Cluster Traffic in a vSAN Stretched Cluster

In a vSAN stretched cluster, the primary node is located at the preferred site.

In a vSAN stretched cluster configuration, vSAN data is synchronously replicated bidirectionally between the preferred site and the secondary site. vSAN read I/O is local to each site. As a result write I/O bandwidth between the sites depend on many factors such as number of vSAN nodes on each site, the aggregate physical NIC bandwidth of the combined hosts between each site, and the number of vSAN objects that are using site to site replication. To calculate bandwidth requirements for vSAN OSA and vSAN ESA, see [VMware vSAN Design and Sizing Guide](https://www.vmware.com/docs/vmware-vsan-design-guide).

![Unicast intra-cluster traffic in stretched cluster](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/a4132276-e6bd-4a57-9873-f2dce1a65e4b.original.png)

With the unicast traffic, there is no change in the witness site traffic requirements.