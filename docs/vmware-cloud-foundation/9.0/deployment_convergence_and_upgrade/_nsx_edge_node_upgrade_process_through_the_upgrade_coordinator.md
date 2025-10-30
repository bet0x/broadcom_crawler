---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/nsx-edge-node-upgrade-process-by-the-upgrade-coordinator.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade >   NSX Edge Node Upgrade Process Through the Upgrade Coordinator
---

# NSX Edge Node Upgrade Process Through the Upgrade Coordinator

The upgrade process for edge cluster nodes depends on how and when the edge nodes were deployed.

## Upgrade Process for Auto Deployed Edge Nodes

For auto deployed edge nodes managed by NSX Manager, the upgrade coordinator checks the edge node configuration settings and updates them if the settings do not match the standard values from the current NSX version.

When an NSX version introduces an improvement to the edge node configuration, that improvement only applies to edge nodes deployed after the upgrade. Edge nodes deployed prior to the NSX upgrade are not automatically updated. You can use the upgrade coordinator to update auto deployed edge nodes to the latest configuration settings.

The upgrade workflow for auto deployed edge nodes is as follows:

1. The upgrade bundle file is uploaded and prepared by the upgrade coordinator.
2. The edge node is placed into maintenance mode.
3. The OS is downloaded to the edge node.
4. The OS is installed on the edge node.
5. The OS switch is performed on the edge node.
6. Using vSphere APIs, the edge node virtual machine is powered off.

   VMware vCenter should be running and reachable during this workflow.
7. Upgrade coordinator updates the edge node virtual machine configuration parameters and the allocation of CPU cores and memory.

   The following edge virtual machine configuration attributes are added or updated before powering on an edge virtual machine in the operating system:

   - VMX file properties:

     ```
        "ethernet0.ctxPerDev":"3",
        "ethernet1.ctxPerDev":"3",
        "ethernet2.ctxPerDev":"3",
        "ethernet3.ctxPerDev":"3",
        "ethernet4.ctxPerDev":"3",
        "ethernet0.udpRSS":"1",
        "ethernet1.udpRSS":"1",
        "ethernet2.udpRSS":"1",
        "ethernet3.udpRSS":"1",
        "ethernet4.udpRSS":"1",
        "ethernet0.pnicFeatures":"4",
        "ethernet1.pnicFeatures":"4",
        "ethernet2.pnicFeatures":"4",
        "ethernet3.pnicFeatures":"4",
        "ethernet4.pnicFeatures":"4",
        "featMask.vm.cpuid.PDPE1GB":"Val:1",
        "snapshot.maxSnapshots":"0"
     ```
   - OVF file property:

     ```
     "memoryReservationLockedToMax":"true"
     ```
   - CPU
   - Memory

   For the allocation of CPU cores, memory, and storage, the upgrade coordinator changes the edge node values to match the standard form factor values.

   The edge node CPU core and memory values are only changed to match the form factor values if the existing edge node values are less than the form factor values. If the edge node values are greater than the form factor values, then no changes are made. Ensure that there are sufficient resources in the vSphere resource pool and cluster.

   Supported Edge Form Factors for Upgrade



   | Edge Form Factor | Memory | CPU Cores | Disk Space |
   | --- | --- | --- | --- |
   | Small Form Factor | 4 GB | 2 | 200 GB |
   | Medium Form Factor | 8 GB | 4 | 200 GB |
   | Large Form Factor | 32 GB | 8 | 200 GB |
   | Extra Large Form | 64 GB | 16 | 200 GB |
8. The edge node virtual machine is powered on.
9. Check for required reboot if there is a GRUB update, and if required, the OS is rebooted into the updated GRUB.
10. Upgrade coordinator verifies edge node version.
11. Users from the old OS are migrated to the edge node.
12. The edge node exits maintenance mode.
13. The upgrade process is completed and the edge node upgrade is marked as successful.

## Upgrade Process for Manually Deployed Edge Nodes

For manually deployed edge nodes, the upgrade coordinator only updates the OS and does not change the edge parameters or CPU core and memory values.

The upgrade workflow for manually deployed edge nodes is as follows:

1. The upgrade bundle file is uploaded and prepared by the upgrade coordinator.
2. The edge node is placed into maintenance mode.
3. The OS is downloaded to the edge node.
4. The OS is installed on the edge node.
5. The OS switch is performed on the edge node.
6. The edge node reboots into the new OS.
7. Upgrade coordinator verifies edge node version.
8. The edge node exits maintenance mode.

Before upgrading manually deployed edge nodes, it is important to set the VMX file property "featMask.vm.cpuid.PDPE1GB":"Val:1" of the edge node virtual machine in order to prevent upgrade failure.