---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/configure-guest-inter-vlan-routing.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure Guest Inter-VLAN Routing
---

# Configure Guest Inter-VLAN Routing

On overlay networks, NSX supports routing of inter-VLAN traffic on an L3 domain. During routing, virtual distributed router (VDR) uses VLAN ID to route packets between VLAN subnets.

- Before you associate a VLAN subinterface to a logical switch, ensure that the logical switch does not have any other associations with another VLAN subinterface. If there is a mismatch, inter-VLAN routing on overlay networks might not work.
- Ensure that hosts run ESX v 6.7 U2 or later versions.

Inter-VLAN routing overcomes the limitation of 10 vNICs that can be used per VM. NSX supporting inter-VLAN routing ensures that many VLAN subinterfaces can be created on the vNIC and consumed for different networking services. For example, one vNIC of a VM can be divided into several subinterfaces. Each subinterface belongs to a subnet, which can host a networking service such as SNMP or DHCP. With Inter-VLAN routing, for example, a subinterface on VLAN-10 can reach a subinterface on VLAN-10 or any other VLAN.

Each vNIC on a VM is connected to a switch through the parent logical port, which manages untagged packets.

To create a subinterface, create a child port on a switch using the API with an associated VIF using the API call described in the procedure. The subinterface tagged with a VLAN ID is associated to a new logical switch, for example, VLAN10 is attached to logical switch LS-VLAN-10. All subinterfaces of VLAN10 have to be attached to LS-VLAN-10. This 1–1 mapping between the VLAN ID of the subinterface and its associated logical switch is an important prerequisite. For example, adding a child port with VLAN20 to logical switch LS-VLAN-10 mapped to VLAN-10 makes routing of packets between VLANs non-functional. Such configuration errors make the inter-VLAN routing non-functional.

Starting from NSX 3.2.2, logical port proton APIs are replaced with the corresponding segment port policy APIs.

1. To create subinterfaces for a vNIC, ensure that the vNIC is updated to a parent port. Make the following REST API call:

   ```
   PATCH https://<nsx-mgr-ip>/policy/api/v1/infra/segments/<Segment to which vNIC is connected>/ports/<Seg-Port-vNIC>
   {
      "attachment": {
        "id": "<Attachment UUID of the vNIC>",
        "type": "PARENT"
     },
      "admin_state": "UP",
      "resource_type": "SegmentPort",
      "display_name": "parentport"
   }
   }
   ```

   If the logical switch does not have a corresponding segment, you can make the following REST API calls (logical port proton API):

   ```
   PUT https://<nsx-mgr-ip>/api/v1/logical-ports/<Logical-Port UUID-of-the-vNIC>
   {
     "resource_type" : "LogicalPort",
     "display_name" : "parentport",
     "attachment" : {
       "attachment_type" : "VIF",
       "context" : {
         "resource_type" : "VifAttachmentContext",
         "vif_type": "PARENT"
       },
       "id" : "<Attachment UUID of the vNIC>"   
     },
     "admin_state" : "UP",
     "logical_switch_id" : "UUID of Logical Switch to which the vNIC is connected",  
     "_revision" : 0
   }
   ```
2. To create child ports for a parent vNIC port on the N-VDS that is associated to the subinterfaces on a VM, make the following API call: 

   Before making the API call, verify that a segment exists to connect child ports with the subinterfaces on the VM.

   ```
   PUT https://<nsx-mgr-ip>/policy/api/v1/infra/segments/<Segment to which child port is connected>/ports/<Child-port>
   {
      "attachment": {
        "id": "<Attachment UUID of the CHILD port>",
        "type": "CHILD",
        "context_id": "<Attachment UUID of the PARENT port from Step 1>",
        "traffic_tag": <VLAN ID>,
        "app_id": "<ID of the attachment>", ==> display id(can be any string). Must be unique.
     },
      "address_bindings": [
       {
          "ip_address": "<IP address to the corresponding VLAN>",
          "mac_address": "<vNIC MAC Address>",
          "vlan_id": <VLAN ID>
       }
     ],
      "admin_state": "UP",
      "resource_type": "SegmentPort",
      "display_name": "<Name of the Child PORT>"
   }
   ```

   If the logical switch does not have a corresponding segment, you can make the following REST API calls (logical port proton API):

   ```
   POST https://<nsx-mgr-ip>/api/v1/logical-ports/
   {
     "resource_type" : "LogicalPort",
     "display_name" : "<Name of the Child PORT>",   
     "attachment" : {
       "attachment_type" : "VIF",
       "context" : {
         "resource_type" : "VifAttachmentContext",
         "parent_vif_id" : "<UUID of the PARENT port from Step 1>",     
         "traffic_tag" : <VLAN ID>,    
         "app_id" : "<ID of the attachment>",  ==> display id(can give any string). Must be unique.
         "vif_type" : "CHILD"
       },
      "id" : "<ID of the CHILD port>"  
     },
     
     "logical_switch_id" : "<UUID of the Logical switch(not the PARENT PORT's logical switch) to which Child port would be connected to>",         
     "address_bindings" : [ { "mac_address" : "<vNIC MAC address>", "ip_address" : "<IP address to the corresponding VLAN>", "vlan" : <VLAN ID> } ],       
     "admin_state" : "UP"
   }
   ```

NSX creates subinterfaces on VMs.