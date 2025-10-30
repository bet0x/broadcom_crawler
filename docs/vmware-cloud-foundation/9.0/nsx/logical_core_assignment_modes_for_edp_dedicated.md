---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/enhanced-data-path-optional-configurations/automatically-assign-ens-logical-cores.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Logical Core Assignment Modes for EDP Dedicated
---

# Logical Core Assignment Modes for EDP Dedicated

Automatically assign logical cores to vNICs such that dedicated logical cores manage the incoming traffic to and outgoing traffic from vNICs.

With a host switch configured in EDP Dedicated mode, if a single logical core is associated to a vNIC, then that logical core processes bidirectional traffic coming into or going out of a vNIC. When multiple logical cores are configured, the host automatically determines which logical core must process a vNIC's traffic.

Logical cores are assigned to vNICs based on one of these parameters.

- CPU-usage: Host predicts the CPU usage to transmit incoming or outgoing traffic at each vNIC direction by using internal statistics. Based on the usage of CPU to transmit traffic, host changes the logical core assignments to balance load among logical cores. The CPU usage mode is more efficient with resources than vNIC-count but vNIC to LCORE assignments may need to be adjusted more frequently. This is the default mode EDP will run in.
- vNIC-count: Host assumes transmission of incoming or outgoing traffic for a vNIC direction requires the same amount of the CPU resource. Each logical core is assigned the same number of vNICs based on the available pool of logical cores. The vNIC-count mode has performance consistency but is less efficient with resources, but is not optimal for asymmetric traffic.

  Note: EDP Standard host switches operate in CPU-usage mode by default. vNIC-count mode is not supported on EDP Standard.

Refer to the following procedure.

1. To switch from one core assignment mode to another mode, run the following command.

   ```
   set ens lcore-assignment-mode<hs-name-arg><ens-lc-mode-arg>
   ```

   Where, <ens-lc-mode-arg> refers to the ENS logical core assignment mode name. This argument can be set to the mode vNIC-count or cpu-usage.

   vNIC-count is the logical core assignment based on vNIC/Direction count.

   cpu-usage is the logical core assignment based on CPU usage.

   Where, <hs-name-arg> refers to the host switch name.

   For example:

   esx-1> set ens lcore-assignment-mode nsxvswitch cpu-usage