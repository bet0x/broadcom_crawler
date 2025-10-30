---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/configuring-managemnet-appliances/import-and-upgrade-vmware-aria-automation-to-vcf-automation.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Resize Storage
---

# Resize Storage

To increase storage for your VCF management component, you can use the fleet management appliance. The Storage Resize option is supported for VCF Automation and VCF Identity Broker.

Under Fleet ManagementLifecycleComponents, select the integrated component that you want to update.

On the component details screen for VCF Automation or VCF Identity Broker, click Storage Resize. The current storage configuration appears with values displayed for every volume in the cluster:

- Volume Group Name: Name of the volume group.
- Number of Volumes: Number of volumes in the group.
- Volume Group Capacity: Size of each volume in the group.
- Total Used Capacity: Storage capacity used in the group.
- Total Storage Capacity: Number of Volumes times the Volume Group Capacity.

Storage resize only works to extend your storage capacity. To reduce storage, you must redeploy the component.

To resize storage:

1. Enter a larger value for a Volume Group Capacity and click Next.
2. After reviewing the change, click Resize.