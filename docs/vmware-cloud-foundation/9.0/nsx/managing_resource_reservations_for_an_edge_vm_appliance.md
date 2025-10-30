---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/managing-resource-reservations-for-an-edge-vm-appliance.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Managing Resource Reservations for an Edge VM Appliance
---

# Managing Resource Reservations for an Edge VM Appliance

NSX uses vSphere resource allocation to reserve resources
for NSX Edge appliances. You can tune the
CPU and memory resources reserved for NSX Edge to ensure optimal use of resources on an NSX Edge.

For maximum performance NSX Edge VM appliance must be assigned 100% of the
available resources. If you customize resources allocated to the NSX Edge VM, turn back the allocation later to
100% to get maximum performance.

For auto-deployed NSX Edge appliances, you can change the resource
allocation from NSX Manager. However,
if an NSX Edge appliance is deployed
from vSphere, you can only manage resource reservations for that NSX Edge VM from vSphere.

As per the resource requirements of the Edge
VM deployed in your environment, there are two ways to manage reservations:

- Default values assigned to give
  100% resource reservations.
- Custom values assigned to give
  0–100% resource reservations.

## Default Reservations

Assumes the NSX Edge set to the
High priority. The level of priority importance defines
the number of vCPU shares and memory assigned to the NSX Edge. To assign custom values, you can
change the relative priority assigned to the NSX Edge.

Resource constraints for different form
factors set with Normal priority:

| Form Factor | Number of vCPUs | vCPU Shares (Normal priority) | RAM (GB) |
| --- | --- | --- | --- |
| Small | 2 | 2000 | 4 |
| Medium | 4 | 4000 | 8 |
| Large | 8 | 8000 | 32 |
| XLarge | 16 | 16000 | 64 |

You can tune reservations of an
NSX Edge appliance by
considering two parameters:

- Relative priority assigned to
  a VM
- Pre-assigned resource
  constraints for a VM form factor

## Custom Reservations

Assign relative priority for an
NSX Edge appliance. You can
change the relative importance of an NSX Edge appliance to assign the following resource requirements:

For an Extra Large form factor, the
releative importance of CPU Reservation Priority, vCPUs and Memory are listed in the
following table:

| Relative Importance | vCPUs | CPU Share value | Memory (shares per MB configured virtual machine memory) |
| --- | --- | --- | --- |
| Extra High | 16 | 34000 | 64 |
| High | 8 | 32000 | 32 |
| Normal | 4 | 16000 | 8 |
| Low | 2 | 8000 | 4 |

For example, a High relative importance
to an NSX Edge appliance deployed
in a medium form factor assigns the following vCPU and memory shares:

- 4 (vCPUs) X 8000 (vCPU share
  value) = 32000 shares of vCPU
- 20 (GB RAM) X 1000 = 20000
  shares of memory

Before assigning a CPU value in MHz
to guarantee the allocated CPU cycles for an NSX EdgeVM, ensure that the relative importance is set to Low. If the
relative importance is set to Normal or High with a custom CPU value in MHz, the VM
deployment might face issues due to resource constraints.