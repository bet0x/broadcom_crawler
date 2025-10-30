---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/configure-an-offline-depot-for-a-vcf-instance.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Connect to an Offline Depot for a VCF Instance
---

# Connect to an Offline Depot for a VCF Instance

Connect to an offline depot for your VCF Instance to access upgrade, patch, and install binaries.

To connect to an offline depot, you must first configure it. See [Set Up an Offline Depot Web Server for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance/connect-to-an-offline-depot-to-download-binaries/set-up-an-offline-depot-web-server-for-vmware-cloud-foundation.html).

SDDC Manager supports two types of software depots:

- Online depot
- Offline depot

You can only connect SDDC Manager to one type of depot. If SDDC Manager is connected to an online depot and you configure a connection to an offline depot, the online depot connection is disabled and deleted.

You can connect multiple VCF Instances to the same offline depot.

To download binaries to an offline depot, see [Download VCF Core Component Binaries to an Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/download-vcf-core-component-binaries-to-an-offline-depot.html).

1. In VCF Operations , click Fleet ManagementLifecycle.
2. Click VCF Instances and click on the name of a VCF Instance.
3. Click Depot Settings.
4. Click Set Up to set up an offline depot.
5. Enter the following information for the offline depot and click Save.

   - Hostname
   - Port
   - Username
   - Password