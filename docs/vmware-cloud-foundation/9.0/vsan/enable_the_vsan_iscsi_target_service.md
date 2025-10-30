---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/using-the-vsan-iscsi-target-service/enable-the-vsan-iscsi-target-service.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Enable the vSAN iSCSI Target Service
---

# Enable the vSAN iSCSI Target Service

Before you can create iSCSI targets and LUNs and define iSCSI initiator groups, you must enable the iSCSI target service on the vSAN cluster. You must create a VMkernel port on each host to use the vSAN iSCSI default network or select an existing port.

Ensure that you have defined the default network for vSAN iSCSI target service.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN click Services.
4. On the vSAN iSCSI Target Service row, click Enable.

   The Enable vSAN iSCSI Target Service wizard opens.
5. In the Basic tab, you can select the default network, TCP port, and Authentication method at this time. You also can select a vSAN storage policy.
6. In the Virtual IP tab, click the Enable vSAN iSCSI Virtual IP slider to turn it on.
7. Select the network device, IP address, subnet mask, and gateway. When you enable virtual IP, you can use this IP for iSCSI connections. You can disable the virtual IP, as required. If you disable virtual IP, it might cause iSCSI traffic interruptions.

   vSAN stretched cluster does not support vSAN iSCSI virtual IP.
8. Click Enable.

The vSAN iSCSI target service is enabled.

After the iSCSI target service is enabled, you can create iSCSI targets and LUNs, and define iSCSI initiator groups.