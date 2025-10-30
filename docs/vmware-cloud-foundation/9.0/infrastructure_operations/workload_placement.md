---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vrealize-automation-8-x/workload-placement.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Workload Placement
---

# Workload Placement

In VCF Operations , you can configure VCF Automation for VM Apps Organization tenant instances to work with VCF Operations instances. Using VCF Operations you can monitor the placement of existing workloads and optimize the resource usage.

- Verify that the user has privileges of Organizational Owner and Cloud Assembly Administrator set in VCF Automation for VM Apps Organization tenant.
- You must know the vCenter credentials and have the necessary permissions to connect and collect data.
- Verify that VCF Automation for VM Apps Organization tenant is activated from Administration > Integrations in VCF Operations. For more information, see [Configuring the Management Pack for VCF Automation for VM Apps Organization](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vrealize-automation-8-x/configuring-vcf-automation-for-vm-apps-organization.html)VCF Automation for VM Apps Organization.
- VCF Operations must have the same vCenter Cloud Account configured to match with VCF Automation for VM Apps Organization tenant.
- Ensure that integration is activated for VCF Operations and VCF Automation for VM Apps Organization tenant.

1. Click the Workload Placement tab under Capacity > Optimize.
2. Click the View filter drop-down menu and select the VRA Managed objects.

   All the Cloud Zones related to the vCenter are displayed in VCF Operations.
3. Click the Cloud Zone you want to optimize.
4. Based on the operational intent, click Optimize Now.

   The system creates an optimization plan, which depicts BEFORE and (projected) AFTER workload statistics for the optimization action.
5. If you are satisfied with the projected results of the optimization action, click NEXT.
6. Review the optimization moves, then click BEGIN ACTION.

   In the scope of VCF Automation for VM Apps Organization tenant integration, VCF Operations sends a move migration request directly to VCF Automation for VM Apps Organization tenant. In the earlier versions, the migration request was sent to the vCenter.

To verify that the optimization action is complete, select Administration from the left menu, and click Recent Tasks . In the Recent Tasks page, use the Status function on the menu bar to locate your action by its status. You can also search using a range of filters. For example, first filter on Starting Time and scroll to the time when you began the action, then select the Object Name filter. Finally, enter the name of one of the VMs in the rebalance plan.