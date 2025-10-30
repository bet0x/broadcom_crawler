---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service/enable-vsan-file-service.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Enable vSAN File Service
---

# Enable vSAN File Service

You can enable vSAN file services on a vSAN OSA cluster or a vSAN ESA cluster.

Ensure that the following are configured before enabling the vSAN file services:

- The vSAN cluster must be a regular vSAN cluster, a vSAN stretched cluster, or a vSAN ROBO cluster.
- Every ESX host in the vSAN cluster must have minimal hardware requirements such as:

  - Minimum 16 Core CPU
  - Minimum 128 GbE physical memory
  - Minimum 10 GbE network
- You must ensure to prepare the network as vSAN file service network:
  - If using standard switch based network, the Promiscuous Mode and Forged Transmits are enabled as part of the vSAN file services enablement process.
  - If using vSphere Distributed Switch (DVS) based network, vSAN file services are supported on vSphere Distributed Switch (DVS). Create a dedicated distributed port group for vSAN file services in the DVS. MacLearning and Forged Transmits are enabled as part of the vSAN file services enablement process for a provided DVS port group.
  - If using NSX-based network, ensure that MacLearning is enabled for the provided network entity from the NSX admin console, and all the hosts and File Services nodes are connected to the desired NSX network. For more information, see [Create an NSX MAC Discovery Segment Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-mac-discovery-segment-profile/create-an-nsx-mac-discovery-segment-profile.html).

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN click Services.
4. On the File Service row, click Enable.

   The Enable File Service wizard opens.
5. From the Select drop-down, select a network.
6. In the File service agent, select one of the following options to download the OVF file.

   | Option | Description |
   | --- | --- |
   | Automatically load latest OVF | This option lets the system search and download the OVF. - Ensure that you have configured the proxy and firewall so that vCenter can access the following website and download the appropriate JSON file. For more information about configuring the vCenter DNS, IP address, and proxy settings, see the [vCenter Configuration](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_001&appid=vsphere-9-0&language=&format=rendered) guide.  - Use current OVF: Allows you to use the OVF that is already available. - Automatically load latest OVF: Allows the system to search and download the latest OVF. |
   | Manually load OVF | This option allows you to browse and select an OVF that is already available on your local system. If you select this option, you should upload all the following files: - VMware-vSAN-File-Services-Appliance-x.x.x.x-x\_OVF10.mf - VMware-vSAN-File-Services-Appliance-x.x.x.x-x-x\_OVF10.cert - VMware-vSAN-File-Services-Appliance-x.x.x.x-x-x-system.vmdk - VMware-vSAN-File-Services-Appliance-x.x.x.x-x-cloud-components.vmdk - VMware-vSAN-File-Services-Appliance-x.x.x.x-x-log.vmdk - VMware-vSAN-File-Services-Appliance-x.x.x.x-x\_OVF10.ovf |
7. Click Enable.

- The OVF is downloaded and deployed.
- The vSAN file services is enabled.
- A file services VM (FSVM) is placed on each host.

  The FSVMs are managed by the vSAN file services. Do not perform any operation on the FSVMs.