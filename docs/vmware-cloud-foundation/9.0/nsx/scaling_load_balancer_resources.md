---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/key-load-balancer-concepts/scaling-load-balancer-resources.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Scaling Load Balancer Resources
---

# Scaling Load Balancer Resources

When you configure a load balancer, you can specify a size (small, medium, large, or extra large). The size determines the number of virtual servers, server pools, and pool members the load balancer can support.

A load balancer runs on a tier-1 gateway, which must be in active-standby mode. The gateway runs on NSX Edge nodes. The form factor of the NSX Edge node (small, medium, large, or extra large) determines the number of load balancers that the NSX Edge node can support.

For more information about what the different load balance sizes and NSX Edge form factors can support, see <https://configmax.broadcom.com>.

Note that using a small NSX Edge node to run a small load balancer is not recommended in a production environment.

You can call an API to get the load balancer usage information of an NSX Edge node:

GET /policy/api/v1/infra/lb-node-usage?node\_path=<node-path>

The usage information includes the number of load balancer objects (such as load balancer services, virtual servers, server pools, and pool members) that are configured on the node. For more information, see the [NSX API Guide](https://developer.broadcom.com/xapis/nsx-t-data-center-rest-api/latest/).