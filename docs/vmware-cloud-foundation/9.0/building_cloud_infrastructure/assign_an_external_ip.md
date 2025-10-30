---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-virtual-private-clouds-in-vcenter/assign-external-ip.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Assign an External IP
---

# Assign an External IP

Learn how to assign an external IP to your virtual machines.

1. In the vSphere Client, navigate to VM.
2. From the **Actions** drop-down menu, select Assign External IP. In the Assign External IP page, enter the settings.

   | **Option** | **Description** |
   | --- | --- |
   | External IP | Click Set to set external IPs for the VMs attached to subnets.  You will need to select the VM, the NIC, and whether to auto assign the IPs or provide IPs from an IP block. |
   | Virtual Machine | Shows the virtual machines that are connected to the private subnets in the VPC. |
   | Network Adapter | Shows the network adapters that are not assigned an external IP and connected to private subnets in the VPC. |