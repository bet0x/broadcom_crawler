---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-vsan-policies/how-vsan-manages-policy-changes.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > How vSAN Manages Policy Changes
---

# How vSAN Manages Policy Changes

Transient capacity is generated when vSAN reconfigures objects for a policy change. The transient storage activities include vSAN disk rebalancing and object conversions.

When you modify a policy, the change is accepted but not applied immediately. vSAN batches the policy change requests and performs them asynchronously, to maintain a fixed amount of transient space.

Policy changes are rejected immediately due to policy compliance and the underlying capabilities of the storage, such as changing a RAID-5 policy to RAID-6 on a five-host cluster. vSAN storage policy compares the rules associated with the policy and evaluates the underlying storage capabilities to determine whether the vSAN storage is compatible.

You can view transient capacity usage in the vSAN Capacity monitor (Cluster > Monitor > vSAN > Capacity > Capacity Usage > Usage breakdown > System usage). To verify the status of a policy change on an object, use the vSAN health service to check the vSAN object health.