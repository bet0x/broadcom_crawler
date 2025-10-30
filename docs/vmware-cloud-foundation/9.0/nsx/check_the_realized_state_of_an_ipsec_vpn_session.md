---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/check-the-realized-state-of-an-ipsec-vpn-session.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Check the Realized State of an IPSec VPN Session
---

# Check the Realized State of an IPSec VPN Session

After you send a
configuration update request for an IPSec VPN session, you can check to see if
the requested state has been successfully processed in the
NSX local control plane on the transport nodes.

- Familiarize yourself with
  IPSec VPN. See
  [Understanding IPSec VPN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/understanding-ipsec-vpn.html#GUID-f0bb166f-53a6-4307-8fe1-7510b3e7b5cc-en).
- Verify the IPSec VPN is
  configured successfully. See
  [Add an NSX IPSec VPN Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-an-ipsec-vpn-service.html#GUID-fa3387e6-8188-4db8-913c-c1fa71b9db5a-en).
- You must have access to
  the
  NSX Manager
  API.

When you create an IPSec VPN
session, multiple entities are created: IKE profile, DPD profile, tunnel
profile, local endpoint, IPSec VPN service, and IPSec VPN session. These
entities all share the same
IPSecVPNSession span, so you can obtain the
realization state of all the entities of the IPSec VPN session by using the
same
GET
API call. You can check the realization state using only the API.

1. Send a
   POST,
   PUT,
   or
   DELETE request API
   call.

   For example:

   ```
   PUT https://<nsx-mgr>/api/v1/vpn/ipsec/sessions/8dd1c386-9b2c-4448-85b8-51ff649fae4f
   {
      "resource_type": "PolicyBasedIPSecVPNSession",
      "id": "8dd1c386-9b2c-4448-85b8-51ff649fae4f",
      "display_name": "Test RZ_UPDATED",
      "ipsec_vpn_service_id": "7adfa455-a6fc-4934-a919-f5728957364c",
      "peer_endpoint_id":  "17263ca6-dce4-4c29-bd8a-e7d12bd1a82d",
      "local_endpoint_id": "91ebfa0a-820f-41ab-bd87-f0fb1f24e7c8",
      "enabled": true,
      "policy_rules": [
          {
              "id": "1026",
              "sources": [
                  {
                      "subnet": "1.1.1.0/24"
                  }
              ],
              "logged": true,
              "destinations": [
                  {
                      "subnet": "2.1.4..0/24"
                  }
              ],
              "action": "PROTECT",
              "enabled": true,
              "_revision": 1
          }
      ]
   }
   ```
2. Locate and copy the
   value of
   x-nsx-requestid from the response header returned.

   For example:

   ```
   x-nsx-requestid   e550100d-f722-40cc-9de6-cf84d3da3ccb
   ```
3. Request the realization
   state of the IPSec VPN session using the following
   GET
   call.

   ```
               GET https://<nsx-mgr>/api/v1/vpn/ipsec/sessions/<ipsec-vpn-session-id>/state?request_id=<request-id>
   ```

   The following API call
   uses the
   id and
   x-nsx-requestid values in the examples used in the
   previous steps.

   ```
   GET https://<nsx-mgr>/api/v1/vpn/ipsec/sessions/8dd1c386-9b2c-4448-85b8-51ff649fae4f/state?request_id=e550100d-f722-40cc-9de6-cf84d3da3ccb
   ```

   Following is an example of
   a response you receive when the realization state is
   in\_progress.

   ```
   {
     "details": [
       {
         "sub_system_type": "TransportNode",
         "sub_system_id": "fe651e63-04bd-43a4-a8ec-45381a3b71b9",
         "state": "in_progress",
         "failure_message": "CCP Id:ab5958df-d98a-468e-a72b-d89dcdae5346, Message:State realization is in progress at the node."
       },
       {
         "sub_system_type": "TransportNode",
         "sub_system_id": "ebe174ac-e4f1-4135-ba72-3dd2eb7099e3",
         "state": "in_sync"
       }
     ],
     "state": "in_progress",
     "failure_message": "The state realization is in progress at transport nodes."
   }
   ```

   Following is an example of
   a response you receive when the realization state is
   in\_sync.

   ```
   {
       "details": [
           {
               "sub_system_type": "TransportNode",
               "sub_system_id":  "7046e8f4-a680-11e8-9bc3-020020593f59",
               "state": "in_sync"
           }
       ],
       "state": "in_sync"
   }
   ```

   The following are examples
   of possible responses you receive when the realization state is
   unknown.

   ```
   {
       "state": "unknown",
       "failure_message": "Unable to get response from any CCP node. Please retry operation after some time."
   }
   ```

   ```
   {
       "details": [
          {
             "sub_system_type": "TransportNode",
             "sub_system_id": "3e643776-5def-11e8-94ae-020022e7749b",
             "state": "unknown", 
             "failure_message": "CCP Id:ab5958df-d98a-468e-a72b-d89dcdae5346, Message: Unable to get response from the node. Please retry operation after some time."
          },
          {
             "sub_system_type": "TransportNode",
             "sub_system_id": "4784ca0a-5def-11e8-93be-020022f94b73",
             "state": "in_sync"
          }
       ],
       "state": "unknown",
       "failure_message": "The state realization is unknown at transport nodes"
   }
   ```

   After you perform an
   entity
   DELETE operation, you might receive the status of
   NOT\_FOUND, as shown in the following example.

   ```
   {
      "http_status": "NOT_FOUND",
      "error_code": 600, 
      "module_name": "common-services",
      "error_message": "The operation failed because object identifier LogicalRouter/61746f54-7ab8-4702-93fe-6ddeb804 is missing: Object identifiers are case sensitive.."
   }
   ```

   If the IPSec VPN service
   associated with the session is disabled, you receive the
   BAD\_REQUEST response, as shown in the following
   example.

   ```
   {
       "httpStatus": "BAD_REQUEST",
       "error_code": 110199,
       "module_name": "VPN",
       "error_message": "VPN service f9cfe508-05e3-4e1d-b253-fed096bb2b63 associated with the session 8dd1c386-9b2c-4448-85b8-51ff649fae4f is disabled. Can not get the realization status."
   }
   ```