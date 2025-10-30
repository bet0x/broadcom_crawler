---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/network-latency-statistics/measure-network-latency-statistics.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Measure Network Latency Statistics
---

# Measure Network Latency Statistics

You can configure ESX hosts in your
network to measure: pNIC to vNIC, vNIC to pNIC, vNIC to vNIC, and VTEP to VTEP network
latency statistics.

Both vCenter-managed hosts and standalone ESX hosts that you want to configure for measuring network
latency statistics must be prepared for NSX. That is, NSX components must be installed on all the ESX hosts in your network.

Configuration is supported only using the NSX REST APIs. The steps in the following procedure list the
NSX Policy APIs that
you must run to configure the calculation of various network latency statistics. For
a detailed information about the API schema, example request, example response, and
error messages of all the APIs, you must read the NSX API Guide.

1. To compute vNIC to vNIC, pNIC to
   vNIC, and vNIC to pNIC network latency statistics, do these steps: 
   1. Create a group that
      contains host transport nodes as static members by using the following
      PUT API:

      ```
      PUT https://<nsx-mgr>/policy/api/v1/infra/domains/<domain-id>/groups/<group-id>
      ```

      In the request payload of
      this PUT API, specify the host transport node IDs in the
      expression parameter, as shown in the
      following example:

      Example PUT Request
      :   ```
          PUT https://<nsx-mgr>/policy/api/v1/infra/domains/default/groups/TNGroup

          {
              "expression": [
                  {
                      "paths": [
                          "/infra/sites/default/enforcement-points/default/host-transport-nodes/4efdb573-fcce-43ff-8b35-dac583a86239"
                      ],
                      "resource_type": "PathExpression"
                  }
              ],
              "extended_expression": [],
              "reference": false,
              "group_type": [],
              "resource_type": "Group",
              "id": "TNGroup",
              "display_name": "TNGroup",
              "path": "/infra/domains/default/groups/TNGroup",
              "relative_path": "TNGroup",
              "parent_path": "/infra/domains/default"
          }
          ```

          Observe that in this example request, the
          expression parameter contains a
          single host transport node ID.
   2. Create a latency profile
      with the following PUT API:

      ```
      PUT https://<nsx-mgr>/policy/api/v1/infra/latency-profiles/<profile-id>
      ```

      By default, vNIC to vNIC
      latency is measured for all the vNICs on the host transport
      node.

      In the request body of
      this API, configure the following information:
      - Activate or
        deactivate pNIC latency on the host. When it is activated,
        pNIC to vNIC and vNIC to pNIC latency are calculated for
        each vNIC on the host transport node.
      - Specify
        either the sampling rate or the sampling interval, but not
        both.
      - Specify the path to the group that you created in the
        earlier step.

      Example PUT Request
      :   ```
          PUT https://<nsx-mgr>/policy/api/v1/infra/latency-profiles/profile1
              {
                "sampling_rate": 100,
                "pnic_latency_enabled": false,
                "applied_to_group_path": "/infra/domains/default/groups/TNGroup"
              }
          ```
2. To measure VTEP to VTEP latency
   statistics, enable latency in the BFD health monitoring profile, which is a
   resource type in the transport zone profile. Run the following PUT API:

   ```
   PUT https://<nsx-mgr>/policy/api/v1/infra/transport-zone-profiles/<tz-profile-id>
   ```

Export the statistics to an external
collector for a deeper network insight and troubleshooting network-specific latency
problems.