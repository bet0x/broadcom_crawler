---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/preparing-a-new-or-existing-cluster-for-virtual-san/preparing-hosts-for-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Preparing Your Hosts for vSAN
---

# Preparing Your Hosts for vSAN

As a part of the preparation for enabling vSAN, review the requirements and recommendations about the configuration of hosts for the cluster.

- Verify that the storage devices on the hosts, and the driver and firmware versions for them, are listed in the vSAN section of the Broadcom Compatibility Guide available at: <https://compatibilityguide.broadcom.com/>.
- Make sure that a minimum of three hosts contribute storage to the vSAN datastore.
- For maintenance and remediation operations on failure, add at least four hosts to the cluster.
- Designate hosts that have uniform configuration for best storage balance in the cluster.
- Do not add hosts that have only compute resources to the cluster to avoid unbalanced distribution of storage components on the hosts that contribute storage. Virtual machines that require much storage space and run on compute-only hosts might store a great number of components on individual capacity hosts. As a result, the storage performance in the cluster might be lower.
- Do not configure aggressive CPU power management policies on the hosts for saving power. Certain applications that are sensitive to CPU speed latency might have low performance.
- If your cluster contains blade servers, consider extending the capacity of the datastore with an external storage enclosure that is connected to the blade servers. Make sure the storage enclosure is listed in the vSAN section of the Broadcom Compatibility Guide.
- Consider the configuration of the workloads that you place on vSAN:

  - For high levels of predictable performance, use vSAN ESA based clusters.
  - For balance between performance and older hardware, consider using vSAN OSA