---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters/deploy-vsan-witness-host/configure-the-vmkernel-adapters-on-the-vsan-witness-host.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Configure the VMkernel Adapters on the vSAN Witness Host
---

# Configure the VMkernel Adapters on the vSAN Witness Host

To enable vSAN data network communication between the availability zones, configure the witness network on the vSAN witness host.

1. In the inventory panel of the vSphere Client, select vCenterDatacenter.
2. Select the vSAN witness host and click the Configure tab.
3. Remove the dedicated witness traffic VMkernel adapter on the vSAN Witness host.
   1. In the Networking section, click VMkernel adapters.
   2. Select the kernel adapter vmk1 with secondaryPg as Network label and click Remove.
   3. On the Remove VMkernel adapter dialog box, click Remove
4. Remove the secondary switch from the vSAN witness host.
   1. In the left pane, select NetworkingVirtual switches.
   2. Expand the Standard switch: secondary switch section.
   3. Click the vertical ellipsis and from the drop-down menu, select Remove.
   4. On the Remove standard switch dialog box, click Yes.
5. Remove the virtual machine network port group on the vSAN witness host.
   1. Expand the Standard switch: vSwitch0 section.
   2. In the VM Network pane, click the vertical ellipsis and from the drop-down menu, select Remove.
   3. On the Remove port group dialog box, click Yes.
6. Enable witness traffic on the VMkernel adapter for the management network of the vSAN witness host.
   1. On the VMkernel adapters page, select the vmk0 adapter and click Edit.
   2. In the vmk0 - edit settings dialog box, click Port properties, select the vSAN check box, and click OK.