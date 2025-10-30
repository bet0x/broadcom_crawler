---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/create-a-workload-domain-by-using-the-vcf-operations-api/deploy-a-l3-multi-rack-vsan-vi-workload-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Create and Configure a Workload Domain with a Layer 3 Multi-Rack vSAN HCI Cluster
---

# Create and Configure a Workload Domain with a Layer 3 Multi-Rack vSAN HCI Cluster

A workload domain with a layer 3 multi-rack vSAN HCI cluster provides scalability, resilience, and optimal resource usage for workloads.

The clusters in such workload domains have the following configuration:

- Layer 3 network fabric between the racks.
- A dedicated NSX host sub-transport node profile for each rack.
- Each rack can be configured as a vSAN fault domain

Deploy the L3 multi-rack vSAN workload domain so ESX hosts in different racks communicate over the L3 network and vSAN spans those racks. You then disable the vSAN automatic policy management, set and assign a default vSAN storage policy to match availability targets, and create vSAN fault domains to map racks and protect against rack-level failure.

For more information on the layer 3 multi-rack cluster design, see the VMware Cloud Foundation Design Guide.