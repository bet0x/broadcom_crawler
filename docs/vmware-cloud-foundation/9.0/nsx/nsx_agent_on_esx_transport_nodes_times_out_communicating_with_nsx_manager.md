---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-host-transport-nodes/nsx-agent-on-esxi-transport-nodes-times-out-communicating-with-nsx-manager.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > NSX Agent on ESX Transport Nodes Times Out Communicating with NSX Manager
---

# NSX Agent on ESX Transport Nodes Times Out Communicating with NSX Manager

In a large-scale environment with many transport nodes and VMs on ESX hosts, NSX agents, which run on ESX hosts, might time out when communicating with NSX Manager.

Some operations, such as when a VM vnic tries to attach to a logical switch, fail. The /var/run/log/nsx-opsagent.log has messages such as:

```
level="ERROR" errorCode="MPA41542"] [MP_AddVnicAttachment] RPC call [0e316296-13-14] to NSX management plane timout
2017-05-15T05:32:13Z nsxa: [nsx@6876 comp="nsx-esx" subcomp="NSXA[VifHandlerThread:-2282640]" tid="1000017079" level="ERROR" errorCode="MPA42003"] [DoMpVifAttachRpc] MP_AddVnicAttachment() failed: RPC call to NSX management plane timout
```

In a large-scale environment, some operations might take longer than usual and fail because the default timeout values are exceeded.

1. Increase the NSX agent timeout (seconds) value. 
   1. On the ESX host, stop the NSX ops agent with the following command:

      On NSX 2.3 or later releases:

      ```
      /etc/init.d/nsx-opsagent stop
      ```

      On NSX 2.1 or previous releases:

      ```
      /etc/init.d/nsxa stop
      ```
   2. Edit the file /etc/vmware/nsx-opsagent/nsxa.json and change the vifOperationTimeout value from 25 seconds to, for example, 55 seconds.

      ```
      "mp" : {
          /* timeout for VIF operation */
          "vifOperationTimeout" : 25,
      ```

      This timeout value must be less than the hostd timeout value that you set in step 2.
   3. Start the NSX ops agent with the following command: 

      ```
      /etc/init.d/nsx-opsagent start
      ```
2. Increase the hostd timeout (seconds) value. 
   1. On the ESX host, stop the hostd agent with the following command:

      ```
      /etc/init.d/hostd stop
      ```
   2. Edit the file /etc/vmware/hostd/config.xml. Under <opaqueNetwork>, uncomment the entry for <taskTimeout> and change the value from 30 seconds to, for example, 60 seconds.

      ```
      <opaqueNetwork>
          <!-- maximum message size allowed in opaque network manager IPC, in bytes. -->
          <!-- <maxMsgSize> 65536 </maxMsgSize> -->
          <!-- maximum wait time for opaque network response -->
          <!-- <taskTimeout> 30 </taskTimeout> -->
      ```
   3. Start the hostd agent with the following command:

      ```
      /etc/init.d/hostd start
      ```