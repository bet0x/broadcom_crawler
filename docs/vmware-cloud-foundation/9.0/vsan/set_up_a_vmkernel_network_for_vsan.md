---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/enabling-virtual-san/set-up-networking-for-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Set Up a VMkernel Network for vSAN
---

# Set Up a VMkernel Network for vSAN

To enable the exchange of data in the vSAN cluster, you must provide a VMkernel network adapter for vSAN traffic on each ESX host.

1. Right-click the host, and select Add Networking.
2. On the Select connection type page, select VMkernel Network Adapter and click Next.
3. On the Select target device page, configure the target switching device.
4. On the Port properties page, select vSAN service. The configuration of vSAN or vSAN witness network interface with vSAN Storage cluster client network interface is not supported.
5. Complete the VMkernel adapter configuration.
6. On the Ready to complete page, verify that vSAN is Enabled in the status for the VMkernel adapter, and click Finish.

vSAN network is enabled for the host.

You can enable vSAN on the host cluster.