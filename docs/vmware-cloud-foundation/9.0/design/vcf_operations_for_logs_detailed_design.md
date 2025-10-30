---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/vcf-operations-for-logs-deployment-models.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Operations for Logs Detailed Design
---

# VCF Operations for Logs Detailed Design

A VCF fleet can include one or more of the supported for VCF Operations for logs Models. This section describes the options, requirements and recommendations for each VCF Operations for logs Model.

- [Simple VCF Operations for logs Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/vcf-operations-for-logs-deployment-models/simple-vcf-operations-for-logs-model.html)
- [High Availability VCF Operations for logs Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/vcf-operations-for-logs-deployment-models/high-availability-vcf-operations-for-logs-model.html)

## VCF Operations for Logs Deployment Models

Common Design Attributes for the VCF Operations for Logs Deployment Models



| Attribute | Details |
| --- | --- |
| Centralized management | Provides a centralized log management framework for vCenter, ESX, VCF Automation, NSX, and VCF Identity Broker.  The use cases listed are an example, but they are not limited to this subset, for a High Availability / Cluster VCF Operations for logs instance to manage:   - Fleet level deployments - Default deployment model for all management and workload environments - High availability environments   The use cases listed are an example, but they are not limited to this subset, for a Simple / Standard VCF Operations for logs instance to manage:   - Test/Dev Environments Only |
| Initial deployment | Deployed after initial deployment of infrastructure and Ops. It is deployed within the Fleet Management component of VCF Ops. |
| Architecture flexibility | Can be deployed in a Simple or Highly Available Cluster deployment.  Recommended deployment is a HA Cluster deployment and it satisfies most use cases.  Simple deployment is for test/dev environments, it is not for production use cases. |

## 

VCF Fleet Single Site Deployment Design

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/f5cd1d5a-4a8e-47c3-b082-cbaa84fa015d.original.png)

## VCF Operations for logs Sizing Considerations

Log ingestion rates for the Simple / Standard deployment is as follows the storage requirement is 530 GB per node but can support up to 6 TB per volume.

The table below shows examples for simple deployments, to understand the numbers for a clustered deployment simply multiply by 3.

Ex: Medium Node supports 1000 IOPs, a medium cluster deployment has 3 medium sized nodes so it supports 3 x 1000 = 3000 IOPs.

| Node Size | Log Ingest Rate | Virtual CPUs | Memory | IOPs | Syslog Connections (Active TCP Connections) | Events Per Second |
| --- | --- | --- | --- | --- | --- | --- |
| Small | 30 GB/Day | 4 | 8 GB | 500 | 100 | 2000 |
| Medium | 75 GB/Day | 8 | 16 GB | 1000 | 250 | 5000 |
| Large | 225GB/Day | 16 | 32 GB | 1500 | 750 | 15000 |

## Log Retention and Archive Design for VCF Operations for logs

VCF Operations for Logs can allow for archival and retention based upon your organizations requirements. Your organization might require log retention and/or archiving due to compliance, auditing or for troubleshooting purposes and in doing so you will need to configure Operations for Logs to do this. You will need to calculate the sizing by using the [VRLI Sizer.](https://vrlisizer.vmware.com/overview) By default the virtual disk configuration within Operations for Logs is as shown in the table below.

Virtual Disk Configuration on the VCF Operations for logs Appliance



| Hard disk | Size | Usage |
| --- | --- | --- |
| Hard disk 1 | 20 GB | Root file system |
| Hard disk 2 | 510 GB for a medium-size deployment | Contains two partitions:  - /storage/var for system logs - /storage/core for collected logs |

Log Archiving Attributes



| Attribute | Description |
| --- | --- |
| Archiving period | VCF Operations for logs archives log messages as soon as possible. At the same time, the logs are retained on the virtual appliance until the free local space is almost filled. Data exists on both theVMware Aria Operations for Logsappliance and the archive location for most of the retention period. The archiving period must be longer than the retention period. |
| Archive location | The archive location must be on an NFS version 3 (NFSv3) shared storage. The archive location must be available and must have enough capacity to accommodate the archives. |