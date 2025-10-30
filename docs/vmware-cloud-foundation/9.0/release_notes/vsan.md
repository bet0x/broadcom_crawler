---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vsan.html
product: vmware-cloud-foundation
version: 9.0
section: Release Notes
breadcrumb: Release Notes > vSAN
---

# vSAN

This document contains the following sections

- [vSAN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vsan.html#GUID-2ef4ce54-3557-45bb-97d6-f42fc903fd6e-en_id-136c04c8-5115-4eaf-bdb5-ffddd9bf1529)
- [Licensing](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vsan.html#GUID-2ef4ce54-3557-45bb-97d6-f42fc903fd6e-en_id-2808b0f6-f507-4063-a484-e5f086b868cb)

## vSAN

**Disaster Recovery for vSAN clusters using VMware Live Recovery:**

VCF 9.0 now ensures protection of your vSAN clusters by using scalable host-based VM replication to remote vSAN clusters, with an RPO value as low as 1 minute. Additionally, the integration with VMware Live Recovery ensures that vSAN clusters recover quickly from disasters by using enterprise-grade runbook orchestration. For more information, see [What is vSAN Data Protection?](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vlrdp_105&appid=vlrdp-9-0-3&language=&format=rendered).

**vSAN Licensing via VCF Operations:**

VCF 9.0 enables licensing of vSAN clusters and witness hosts through VCF Operations. You can now allocate vSAN TiB entitlements by assigning the VMware vSAN (TiB) license to vCenter. For more information, see [Add-on Licenses](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_874&appid=vcf-9-0&language=&format=rendered).

**Support of Stretched Compute-only Clusters with vSAN storage clusters in VCF 9.0:**

VCF 9.0 now supports stretched compute-only vSphere client clusters connected to a stretched storage cluster deployment. As a result, in VCF, you can configure workload domains that provide site-level resilience for workloads and data. For more information, see [Creating a Stretched Compute Cluster](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsan_109&appid=vcf-9-0&language=&format=rendered).

**Support for client traffic separation with vSAN storage clusters in VCF 9.0:**

VCF 9.0 now supports a more flexible network configuration by separating the external (VM) traffic from the internal (vSAN storage) traffic by utilizing dedicated VMkernel ports for the different traffic types. This provides several benefits including traffic isolation, flexibility in network topologies, and optimization of the network performance**.** For more information, see [Sharing Remote vSAN Datastores](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsan_110&appid=vcf-9-0&language=&format=rendered).

**Support of up to 500 file shares per cluster in vSAN File Services:**

vSAN 9.0 improves the scalability of native File Services in VCF by increasing the maximum number of shares supported per cluster to 500. For more information, see [Configure vSAN File Service](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsan_107&appid=vcf-9-0&language=&format=rendered).

**Dying Disk Handling (DDH) supports Cache Drives:**

VCF 9.0 enhances the ability of vSAN Express Storage Architecture (ESA) to monitor disk latencies and to automatically take corrective actions if the latency exceeds a predefined threshold. It also enables proactive detection and handling of cache drive failures in vSAN Original Storage Architecture (OSA).

## Licensing

## Licensing

**Licensing**

To license your vSAN clusters, assign the VMware vSAN license to your vCenter instance from VCF Operations. All vSAN clusters in that vCenter instance become licensed automatically. A VCF or vSphere Foundation license must first be assigned to the vCenter instance before assigning the VMware vSAN license. Until vSAN is licensed, it can be used for up to 90 days in evaluation mode.