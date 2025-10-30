---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster/introduction-to-stretched-clusters/vsan-stretched-cluster-best-practices.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Best Practices for Working with vSAN Stretched Clusters
---

# Best Practices for Working with vSAN Stretched Clusters

When working with vSAN stretched clusters, follow these recommendations for proper performance.

- If one of the sites (fault domains) in a vSAN stretched cluster is inaccessible, new virtual machines can still be provisioned in the subcluster containing the operational site. These new virtual machines are implicitly force provisioned if at least two or three sites are available and are non-compliant until the partitioned site rejoins the cluster. A site here refers to either a data site or the witness host. The objects have no failure tolerance and are susceptible to data loss on any additional failure. They create new virtual machines only if necessary. With the vSAN 9.0 release, the new virtual machines are created to comply with the lower failures to tolerate, specified in the policy. This improves failure tolerance as the policy specifies a lower failures to tolerate of one or more.
- If an entire site goes offline due to a power outage or loss of network connection, restart the site immediately, without much delay. Instead of restarting vSAN hosts one by one, bring all hosts online approximately at the same time, ideally within a span of 10 minutes. By following this process, you avoid resynchronizing a large amount of data across the sites.
- If a host is permanently unavailable, remove the host from the cluster before you perform any reconfiguration tasks.
- If you want to clone a VM witness host to support multiple vSAN stretched clusters, do not configure the VM as a witness host before cloning it. First deploy the VM from OVF, then clone the VM, and configure each clone as a witness host for a different cluster. Or you can deploy as many virtual machines as you need from the OVF, and configure each one as a witness host for a different cluster.