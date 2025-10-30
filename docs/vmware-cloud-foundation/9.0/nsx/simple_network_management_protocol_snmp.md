---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/simple-network-management-protocol-snmp.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Simple Network Management Protocol (SNMP)
---

# Simple Network Management Protocol (SNMP)

You can use Simple Network Management Protocol (SNMP) to monitor your NSX components. The SNMP service is not started by default after installation.

The SNMP Framework in NSX enables you to monitor various system entities (such as disk on NSX Edge) and logical entities (such as NSX Edge VPN tunnel) using their SNMP managers. This framework enables NSX verticals and platform to define SNMP MIB objects to be monitored and which can be used to enable their SNMP managers to interact with NSX.

To download the SNMP MIB files, see [Knowledge Base article 313538: SNMP MIB module file download](https://knowledge.broadcom.com/external/article?articleNumber=313538). For NSX, download the folder and use the extracted file VMWARE-NSX-MIB.mib.

For SNMP configuration, see Configure SNMP for ESX in the VMware vSphere product documentation.

1. Log in to the NSX Manager CLI or the NSX Edge CLI.
2. Run the following commands

   - For SNMPv1/SNMPv2:

     ```
     set snmp community <community-string>
     start service snmp
     ```

     The maximum character limit for community-string is 64.
   - For SNMPv3

     ```
     set snmp v3-users <user_name> auth-password <auth_password> priv-password <priv_password>

     start service snmp
     ```

     The maximum character limit for user\_name is 32. Ensure that your passwords meet PAM constraints. If you want to change the default engine id, use the following command:

     ```
     set snmp v3-engine-id <v3-engine-id>

     start service snmp
     ```

     v3-engine-id is an even-length hexadecimal string that is 10 to 64 characters long and cannot be all 0s or Fs.

     NSX supports SHA-1, SHA-2, and AES-128 as the authentication and privacy protocols. You can also use API calls to set up SNMPv3. For more information, see the NSX API Guide.
3. To enable the SNMP service to start automatically on reboot on the NSX appliance, run the command: set service snmp start-on-boot.