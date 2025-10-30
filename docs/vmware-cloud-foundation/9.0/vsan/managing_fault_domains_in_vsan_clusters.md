---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/managing-fault-domains-in-vsan-clusters.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Managing Fault Domains in vSAN Clusters
---

# Managing Fault Domains in vSAN Clusters

Fault domains enable you to protect against rack or chassis failure if your vSAN cluster spans across multiple racks or blade server chassis.

You can create fault domains and add one or more hosts to each fault domain. A fault domain consists of one or more vSAN hosts grouped according to their physical location in the data center. When configured, fault domains enable vSAN to tolerate failures of entire physical racks as well as failures of a single host, capacity device, network link, or a network switch dedicated to a fault domain.

The Failures to tolerate policy for the cluster depends on the number of failures a virtual machine is provisioned to tolerate. When a virtual machine is configured with the Failures to tolerate set to 1 (FTT=1), vSAN can tolerate a single failure of any kind and of any component in a fault domain, including the failure of an entire rack.

When you configure fault domains on a rack and provision a new virtual machine, vSAN ensures that protection objects, such as replicas and witnesses, are placed in different fault domains. For example, if a virtual machine's storage policy has the Failures to tolerate set to N (FTT=n), vSAN requires a minimum of 2\*n+1 fault domains in the cluster. When virtual machines are provisioned in a cluster with fault domains using this policy, the copies of the associated virtual machine objects are stored across separate racks.

A minimum of three fault domains are required to support FTT=1. For best results, configure four or more fault domains in the cluster. A cluster with three fault domains has the same restrictions that a three host cluster has, such as the inability to reprotect data after a failure and the inability to use the Full data migration mode. For information about designing and sizing fault domains, see [Designing and Sizing vSAN Fault Domains](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/designing-and-sizing-virtual-san-fault-domains.html).

Consider a scenario where you have a vSAN cluster with 16 hosts. The hosts are spread across four racks, that is, four hosts per rack. To tolerate an entire rack failure, create a fault domain for each rack. You can configure a cluster of such capacity with the Failures to tolerate set to 1. If you want the Failures to tolerate set to 2, configure five fault domains in the cluster.

When a rack fails, all resources including the CPU, memory in the rack become unavailable to the cluster. To reduce the impact of a potential rack failure, configure fault domains of smaller sizes. Increasing the number of fault domains increases the total amount of resource availability in the cluster after a rack failure.

When working with fault domains, follow these best practices.

- Configure a minimum of three fault domains in the vSAN cluster. For best results, configure four or more fault domains.
- A host not included in any fault domain is considered to reside in its own single-host fault domain.
- You do not need to assign every vSAN host to a fault domain. If you decide to use fault domains to protect the vSAN environment, consider creating equal sized fault domains.
- When moved to another cluster, vSAN hosts retain their fault domain assignments.
- When designing a fault domain, place a uniform number of hosts in each fault domain.
- You can add any number of hosts to a fault domain. Each fault domain must contain at least one host.