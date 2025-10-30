---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/create-a-workload-domain-by-using-the-vcf-operations-api/deploy-a-l3-multi-rack-vsan-vi-workload-domain/create-vsan-fault-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Create vSAN Fault Domains
---

# Create vSAN Fault Domains

For vSAN multi-rack clusters with more than one ESX node per rack create a vSAN fault domain for each rack for rack resilience.

1. In the vSphere Client for the workload domain vCenter Server, in the Hosts and clusters inventory, navigate to the multi-rack cluster.
2. On the Configure tab, select vSANFault Domains.
3. Click the plus icon.
4. In the New Fault Domain dialog box, enter the fault domain name, and select the hosts for the fault domain.
5. Click Create.
6. Repeat these steps for the other racks.

During a future cluster expansion, add hosts manually to their respective fault domains.