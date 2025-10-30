---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/upgrading-the-vsan-cluster/about-vsan-object-format.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > About vSAN Object Format
---

# About vSAN Object Format

The operations space needed by vSAN to perform policy change or other such operations on an object created by vSAN is the space used by a largest object in the cluster.

This is typically difficult to plan for and hence the guidance was to keep 30 percent of free space in the cluster assuming that it is unlikely that the largest object in the cluster consumes more than 25 percent of the space and 5 percent of the space is reserved to make sure cluster does not become full due to policy changes. In vSAN all objects are created in a new format which allows the operations space needed by vSAN to perform policy change on an object if there is 255 GbE per host for objects less than 8 TB and 765 GbE per host for objects 8 TB or larger.

After a cluster is upgraded, the objects greater than 255 GbE created with the older release must be rewritten in the new format before vSAN can provide the benefit of being able to perform operations on an object with the new free space requirements. A new object format health alert is displayed after an upgrade, if there are objects that must be fixed to the new object format and allows the health state to be remediated by starting a relayout task to fix these objects. The health alert provides information on the number of objects that must be fixed and the amount of data that will be rewritten. The cluster might experience a drop of about 20 percent in the performance while the relayout task is in progress. The resync dashboard provides more accurate information about the amount of time this operation takes to complete.