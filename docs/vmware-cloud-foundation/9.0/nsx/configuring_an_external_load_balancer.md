---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/configuring-an-external-load-balancer.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configuring an External Load Balancer
---

# Configuring an External Load Balancer

You can configure an external load balancer to distribute traffic to the NSX Managers in a manager cluster.

An NSX Manager cluster does not require an external load balancer. The NSX Manager virtual IP (VIP) provides resiliency in the event of a Manager node failure but has the following limitations:

- VIP does not perform load balancing across the NSX Managers.
- VIP requires all the NSX Managers to be in the same subnet.
- VIP recovery takes about 1 - 3 minutes in the event of a Manager node failure.

An external load balancer can provide the following benefits:

- Load balance across the NSX Managers.
- The NSX Managers can be in different subnets.
- Fast recovery time in the event of a Manager node failure.

## Authentication Methods When Accessing NSX Manager

The following authentication methods are supported by NSX Manager. For more information about the authentication methods, see the NSX API Guide.

- HTTP Basic Authentication
- Session-Based Authentication
- Authentication using an X.509 certificate and a Principal Identity
- Authentication in VMware Cloud on AWS

The session-based authentication method (used when you access NSX Manager from a browser) requires source-IP persistence (all requests from the client must go to the same NSX Manager). The other methods do not require source-IP persistence (requests from the client can go to different NSX Managers).

## Recommendations

- Create a single VIP on the load balancer with source-IP persistence configured to handle all the authentication methods.
- If you have applications or scripts that might generate a lot of requests to NSX Manager, create a second VIP without source-IP persistence for these applications or scripts. Use the first VIP for browser access to NSX Manager only.

The VIP must have the following configurations:

- Type: Layer4-TCP
- Port: 443
- Pool: NSX Manager Pool
- Persistence: Source-IP persistence for the first VIP. None for the second VIP (if present).

Example of an external load balancer configuration:

![An example of an external load balancer configuration](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/bf5cfffc-a85e-4a48-8e58-7ec11c8ec2dc.original.png)

## NSX Manager's Certificate

The clients access NSX Manager using FQDN name (for example, nsx.mycompany.com). This FQDN is resolved to the load balancer's VIP. To avoid any certificate mismatch, each NSX Manager must have a certificate that is valid for the VIP's FQDN name. Therefore, you must configure each NSX Manager with a SAN certificate that is valid for its own name (for example, nsxmgr1.mycompany.com) and the VIP's FQDN.

## Monitoring the Health of NSX Managers

The load balancer can check that each NSX Manager is running with the following API:

```
GET /api/v1/reverse-proxy/node/health
```

The request headers are:

- Header 1
  - Name: Content-Type
  - Value: application/json
- Header 2
  - Name: Accept
  - Value: application/json

A response indicating that the NSX Manager is running will be:

```
"healthy" : true
```

Note that the format of the response is “healthy”<space>:<space>true.