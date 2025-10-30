---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/transit-gateways/configure-a-transit-gateway.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure a Transit Gateway
---

# Configure a Transit Gateway

Perform the following steps to configure an external connection for a Transit Gateway. Note that in case of a Centralized connection, the Transit Gateway will inherit its HA Mode (Active/Standby or Active/Active) from the Tier-0 gateway to which it is connected. In case of Active-Active mode, it does not support NAT including Default Outbound NAT.

1. From your browser, log in to NSX Manager.
2. From the Project drop-down, select the project for which you want to configure the Transit Gateway.
3. Go to Networking > Transit Gateways.
4. Click the three-dot menu and click Edit.
5. In the Attached External Connection field, select the required connection. You can also create a new connection by clicking the three-dot menu for the default Transit Gateway.
6. In the NAT field, click Set and add a NAT rule for the the IP taken from an External IP Block. Note that NAT is supported for a TGW that has a centralized external connection. For more information about configuring NAT for a TGW, see [Add a NAT Rule for Transit Gateway.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/transit-gateways/add-a-nat-rule-for-transit-gateway.html)
7. Click Save.