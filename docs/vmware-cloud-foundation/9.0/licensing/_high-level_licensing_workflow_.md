---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/licensing-overview/v9-licensing-overview.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing >   High-Level Licensing Workflow  
---

# **High-Level Licensing Workflow**

1. Install a VCF Operations instance version 9.0, or upgrade your existing Aria Operations instance to VCF Operations 9.0.
2. Register your VCF Operations instance with the VCF Business Services console by using one of the two modes:

   - Disconnected mode - no Internet connection is required. You must manually exchange registration and license file between the VCF Operations instance and the VCF Business Services console.
   - Connected mode - Internet connection is required. You use an activation code from the VCF Business Services console to register your VCF Operations instance.
3. Add licenses to the VCF Operations instance from the VCF Business Services console.
4. Assign licenses to vCenter instances from VCF Operations.

After you add licenses to VCF Operations, you must update the added licenses at least once every 6 months (180 days). If license usage data is not submitted within the required reporting time-frame, and you do not update your licenses, your licenses are treated as expired, your hosts are disconnected from the vCenter instance, and you cannot start any workload operations. Existing workloads are not proactively stopped.

For more information, see [Update Licenses.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/update-licenses/updatelicenses.html)