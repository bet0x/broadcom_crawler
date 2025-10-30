---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/setting-up-load-balancer-components/add-load-balancers.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add Load Balancers
---

# Add Load Balancers

Load balancer is created and attached to the tier-1 gateway.

Verify that a tier-1 gateway is configured. See [Tier-1 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-1-gateways.html#GUID-6126710e-8221-4bec-8621-0d406526ebdb-en).

You can configure the level of error messages you want the load balancer to add to the error log.

- Avoid setting the log level to DEBUG on load balancers with a significant traffic due to the number of messages printed to the log that affect performance.
- Load balancer over IPSec VPN is not supported for route-based VPN terminated on Tier-1 gateways.

![The tier-1 gateway contains the load balancer.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/b0c2cc9a-3bf4-4caa-a94d-fbfde542d39f.original.png)

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingLoad BalancingAdd Load Balancer.
3. Enter a name and a description for the load balancer.
4. Select the load balancer size based on your needs of virtual servers and pool members and available resources.
5. Select the already configured tier-1 gateway to attach to this load balancer from the drop-down menu. 

   The tier-1 gateway must be in the Active-Standby mode.
6. Define the severity level of the error log from the drop-down menu. 

   Load balancer collects information about encountered issues of different severity levels to the error log.
7. Enter tags to make searching easier. 

   You can specify a tag to set a scope of the tag.
8. Click Save. 

   The load balancer creation and attaching the load balancer to the tier-1 gateway takes about three minutes and the configuration status to appear green and Up.

   If the status is Down, click the information icon and resolve the error before you proceed.
9. Delete the load balancer. 
   1. Detach the load balancer from the virtual server and tier-1 gateway.
   2. Select the load balancer.
   3. Click the vertical ellipses button.
   4. Select Delete.