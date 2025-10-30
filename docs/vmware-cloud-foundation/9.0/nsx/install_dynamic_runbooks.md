---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/install-dynamic-runbooks.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Install Dynamic Runbooks
---

# Install Dynamic Runbooks

In
addition to predefined runbooks, the Online Diagnostic System (ODS) feature also supports
dynamic runbooks to debug NSX at
runtime.

Download
the dynamic package from the VMware site <https://support.broadcom.com/group/ecx/downloads>.

Dynamic runbooks are not dependent on NSX release and
you can install them anytime. Dynamic runbooks address the following issues:

- As development and maintenance of
  predefined runbooks follow the NSX release cycle, it prevents debugging of
  issues emerging at live sites in between release cycles. With dynamic runbooks,
  any debugging requirements can be implemented in between release cycles as
  dynamic runbooks can be developed and installed anytime.
- If you upgrade NSX partially, there
  could be an incompatibility between a runbook and the API that calls it. For
  example, you upgrade the transport node, without upgrading the Unified Appliance
  (UA), and the upgrade installs a new version of runbook on the transport node.
  In this case, UA might not be able to invoke the newer version of the runbook
  with the older API as the API might be outdated.

Only the VMware team can create dynamic
runbooks and you can download them for installing them on your system. Note that
runbooks do not support data backup and restore.

To install the dynamic runbooks, you need
to define a group called the dynamic runbook instance. The dynamic runbook instance
defines all the installation node groups where runbooks are to be installed. If a
new node is added to a group, the runbook will be automatically installed on the new
node.

With NSX 4.2, the following runbook is available for download. For
more informaton about the runbook, download the package from following VMware site
<https://support.broadcom.com/group/ecx/downloads>.

| Runbook | Description |
| --- | --- |
| Hyperbus runbook | The dynamic hyperbus runbook can check for the following hyperbus issues and provide remediation suggestion:   - Hyperbus   connection - Configurations of hyperbus connection - vmknic - Status of   hyperbus connection   This runbook takes vif-id as the input argument. |

To install dynamic runbooks, perform the
following steps:

1. Obtain the path of the transport nodes to be included in the installation node
   group.

   GET
   https://10.180.85.179/policy/api/v1/infra/sites/default/enforcement-points/default/host-transport-nodes
2. Create the installation node group. The group can be a policy group, transport
   node group, or UA node group.

   PATCH
   https://<nsx-mgr>/policy/api/v1/infra/domains/default/groups/<group-name>

   ```
   {
       "expression": 
      [
           {
               "paths": [
                   "/infra/sites/default/enforcement-points/default/host-transport-nodes/TN1"
               ],
               "resource_type": "PathExpression"
           }
       ],
       "extended_expression": [],
       "reference": false,
       "group_type": [],
       "resource_type": "Group"
   }
   ```
3. Create a dynamic runbook instance that includes all the installation node
   groups.

   POST
   https://{{MANAGER\_IP}}/policy/api/v1/infra/sha/dynamic-runbook-instances/<dynamic-instanace-id>

   ```
   {
       "applied_to_group_paths": [
           "/infra/domains/default/groups/TNGroup1"  [Policy Group with node path]
       ],
       "applied_to_nodes": [
           "1e6314a2-a268-4a3a-bcae-4f23b2536ea8"  [The node id can be a host/edge/UA node id]
       ],
       "applied_to_all_appliances": true   [All UA cluster]
   }
   ```
4. Upload the runbook package to the dynamic runbook instance.

   POST
   https://{{MANAGER\_IP}}/policy/api/v1/infra/sha/dynamic-runbook-instances/<dynamic-instanace-id>/file

   The dynamic runbook data is applied to the target nodes specified this
   group.
5. Query the installation state.

   GET
   https://10.180.85.179/policy/api/v1/infra/sha/dynamic-runbook-instances/<dynamic-instanace-id>/state

   ```
   {
       "runbook_name": "Example",
       "management_state": "INSTALL_FINISHED",
       "install_state": [
           {
               "node_id": "084583fa-3ae7-4d0c-98f1-6fc4cb5044b1",
               "node_name": "TN301",
               "version": {
                   "major": 1,
                   "minor": 0
               },
               "status": "INSTALL_FINISHED"
           }
   }
   ```
6. Check the details of the installed runbooks by using the following API.

   GET
   https://{{MANAGER\_IP}}/policy/api/v1/infra/sha/dynamic-runbooks
7. Invoke the runbook by using the steps mentioned in the topic [Debugging NSX at Runtime](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/debugging-nsx-at-runtime.html).

To
extend
a dynamic runbook instance to additional nodes, run the following
API.

PATCH
https://10.180.85.179/policy/api/v1/infra/sha/dynamic-runbook-instances/<dynamic-instanace-id>

```
{
"applied_to_group_paths":["/infra/domains/default/groups/<tn-group-name>"],
"applied_to_nodes":["<target-edge-id>","<target-ua-id>"]
}
```

To uninstall a runbook, run the
following API.

DELETE
https://10.180.85.179/policy/api/v1/infra/sha/dynamic-runbook-instances/<dynamic-instanace-id>/file

To uninstall a dynamic runbook instance,
run the following API .

DELETE
https://10.180.85.179/policy/api/v1/infra/sha/dynamic-runbook-instances/<dynamic-instanace-id>