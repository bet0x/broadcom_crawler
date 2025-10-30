---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/upgrade-sddc-manager-without-upgrading-vcf.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Update or Patch SDDC Manager from VCF Operations
---

# Update or Patch SDDC Manager from VCF Operations

You can update or patch only SDDC Manager without having to upgrade the entire VCF Instance. An independent SDDC Manager patch release includes a change in the fourth group of digits in its version number, for example SDDC Manager 9.0.0.0100.

- Download the SDDC Manager binary.

You can upgrade SDDC Manager without upgrading the VCF Instance when:

- The target version of SDDC Manager is compatible with all the BOM versions running in your VCF Instance (management and workload domains).
- There is a supported upgrade path from your current SDDC Manager version to the target SDDC Manager version.

You can use the SDDC Manager upgrade functionality to upgrade SDDC Manager even when the target version of SDDC Manager is part of a full VCF BOM release, as long as it is compatible.

Updating only SDDC Manager, does not change the version of the management domain.

1. In VCF Operations, browse to Fleet ManagementLifecycle.
2. Select a VCF Instance and click SDDC Manager Updates.

   The UI shows available SDDC Manager updates that are either SDDC Manager-only updates or SDDC Manager updates that are part of a full VCF Instance update.
3. Review and address any compatibility warnings.
4. Click Run Precheck.

   Resolve any precheck issues before proceeding.
5. Schedule the update to run now or at a specific time and click Start Update.