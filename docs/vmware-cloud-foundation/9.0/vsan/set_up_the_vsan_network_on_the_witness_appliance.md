---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster/deploying-a-witness-appliance/set-up-the-virtual-san-network-on-the-witness-appliance.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Set Up the vSAN Network on the Witness Appliance
---

# Set Up the vSAN Network on the Witness Appliance

The vSAN witness appliance includes two preconfigured network adapters. You must change the configuration of the second adapter so that the appliance can connect to the vSAN network.

1. Navigate to the virtual appliance that contains the witness host.
2. Right-click the appliance and select Edit Settings.
3. On the Virtual Hardware tab, expand the second Network adapter.
4. From the drop-down menu, select the vSAN port group and click OK.

   You can use the first VMkernel interface for vSAN traffic when using witness traffic separation.