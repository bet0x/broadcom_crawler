---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-network-connectivity-in-vcenter.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Managing Network Connectivity in vCenter
---

# Managing Network Connectivity in vCenter

Starting with VCF 9.0, a simplified workflow is introduced to set up network connectivity and perform network configuration.

The new NSX-based workflow for network connectivity is available both in vCenter and NSX for you to have a uniform experience of performing network configurations from either of the components. The new workflow leverages many default settings that are recommended by Broadcom for simplifying the deployment process, such as deployment parameters, transport zones, and uplink profile, that reduces the number of user inputs required to perform network configuration. The workflow also provides a topology visualization to correlate your inputs in the user interface. Contextual visualization helps you get a view of the set up before completing the tasks in the workflow.

Based on the kind of network connectivity you have selected, you can create an edge cluster with a centralized gateway or a distributed gateway with VLAN. For more information, see [Workload Networking Detailed Designs](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking.html) and [NSX Edge Cluster Detailed Design](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-nsx-edge-cluster.html).