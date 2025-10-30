---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/setting-up-load-balancer-components/setting-up-virtual-server-components/add-a-persistence-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Persistence Profile
---

# Add a Persistence Profile

To ensure stability of stateful applications, load balancers implement persistence which directs all related connections to the same server. Different types of persistence are supported to address different types of application needs.

Some applications maintain the server state such as, shopping carts. Such state can be per client and identified by the client IP address or per HTTP session. Applications can access or modify this state while processing subsequent related connections from the same client or HTTP session.

The source IP persistence profile tracks sessions based on the source IP address. When a client requests a connection to a virtual server that enables the source address persistence, the load balancer checks if that client was previously connected, and if so, returns the client to the same server. If not, the load balancer selects the server pool member based on the pool load balancing algorithm. Source IP persistence profile is used by Layer 4 and Layer 7 virtual servers.

If rule persistence, cookie persistence, and server keep-alive are all configured, the load balancer follows the priority of rule persistence > cookie persistence > server keep-alive.

The Cookie persistence profile offers 3 modes:

- Cookie Insert - the load balance inserts its own cookie with the pool member information (encoded or not) in the server response to the client. The client then forwards the received cookies in subsequent requests (NSX cookie included), and the load balancer uses that information to provide the pool member persistence. The NSX cookie is trimmed from the client request when sent to the pool member.
- Cookie Prefix - the load balancer appends the pool member information (encoded or not) in the server response to the client. The client then forwards the received HTTP cookie in subsequent requests (with the NSX prepended information), and the load balancer uses that information to provide the pool member persistence. The NSX cookie prefix is trimmed from the client request when sent to the pool member.
- Cookie Rewrite - the load balancer replace server cookie value with the pool member information (encoded or not) in the server response to the client. The client then forwards the received HTTP cookie in subsequent requests (with the NSX prepended information), and the load balancer uses that information to provide the pool member persistence. The original server cookie is replaced in the client request when sent to the pool member.

Cookie persistence is available only on L7 virtual servers. Note that a blank space in a cookie name is not supported.

The generic persistence profile supports persistence based on the HTTP header, cookie, or URL in the HTTP request. Therefore, it supports application session persistence when the session ID is part of the URL. This profile is not associated with a virtual server directly. Specify this profile when you configure a load balancer rule for request forwarding and response rewrite.

![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/5c357746-7015-4bcd-be84-694aee0d4ba3.original.png)

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingLoad BalancingProfilesPersistenceAdd Persistence Profiles.
3. Select Source IP to add a source IP persistence profile and enter the profile details. 

   You can also accept the default Source IP profile settings.

   Option | Description || Name and Description | Enter a name and a description for the Source IP persistence profile. |
   | Share Persistence | Toggle the button to share the persistence so that all virtual servers this profile is associated with can share the persistence table. If the persistence sharing is not enabled in the Source IP persistence profile associated to a virtual server, each virtual server that the profile is associated to maintains a private persistence table. |
   | Persistence Entry Timeout | Enter the persistence expiration time in seconds. The load balancer persistence table maintains entries to record that client requests are directed to the same server.  The very first connection from new client IP is load balanced to a pool member based on the load balancing algorithm. NSX will store that persistence entry on the LB persistence-table which is viewable on the Edge Node hosting the T1-LB active via the CLI command:get load-balancer <LB-UUID> persistence-tables.  - When there are connections from that client to the VIP, the persistence entry is kept. - When there are no more connections from that client to the VIP, the persistence entry begins the timer count down specified in the "Persistence Entry Timeout" value. If no new connection from that client to the VIP is made before the timer expires, the persistence entry for that client IP is deleted. If that client comes back after the entry is deleted, it will be load balanced again to a pool member based on the load balancing algorithm. |
   | Purge Entries When Full | A large timeout value can lead to the persistence table quickly filling up when the traffic is heavy. When this option is enabled, the oldest entry is deleted to accept the newest entry.  When this option is disabled, if the source IP persistence table is full, new client connections are rejected. |
   | HA Persistence Mirroring | Toggle the button to synchronize persistence entries to the HA peer. When HA persistence mirroring is enabled, the client IP persistence remains in the case of load balancer failover. |
   | Tags | Enter tags to make searching easier. You can specify a tag to set a scope of the tag. |
4. Select a Cookie persistence profile, and enter the profile details. Cookie persistence is available only on L7 virtual servers. Note that a blank space in a cookie name is not supported. 

   Option | Description || Name and Description | Enter a name and a description for the Cookie persistence profile. |
   | Share Persistence | Toggle the button to share persistence across multiple virtual servers that are associated to the same pool members. The Cookie persistence profile inserts a cookie with the format, <name>.<profile-id>.<pool-id>.  If the persistence shared is not enabled in the Cookie persistence profile associated with a virtual server, the private Cookie persistence for each virtual server is used and is qualified by the pool member. The load balancer inserts a cookie with the format, <name>.<virtual\_server\_id>.<pool\_id>. |
   | Cookie Mode | Select a mode from the drop-down menu. - INSERT - Adds a unique cookie to identify the session. - PREFIX - Appends to the existing HTTP cookie information. - REWRITE - Rewrites the existing HTTP cookie information. |
   | Cookie Name | Enter the cookie name. A blank space in a cookie name is not supported. |
   | Cookie Domain | Enter the domain name. HTTP cookie domain can be configured only in the INSERT mode. |
   | Cookie Fallback | Toggle the button so that the client request is rejected if cookie points to a server that is in a DISABLED or is in a DOWN state. Selects a new server to handle a client request if the cookie points to a server that is in a DISABLED or is in a DOWN state. |
   | Cookie Path | Enter the cookie URL path. HTTP cookie path can be set only in the INSERT mode. |
   | Cookie Garbling | Toggle the button to disable encryption. When garbling is disabled, the cookie server IP address and port information is in a plain text. Encrypt the cookie server IP address and port information. |
   | Cookie Type | Select a cookie type from the drop-down menu. Session Cookie - Not stored. Will be lost when the browser is closed.  Persistence Cookie - Stored by the browser. Not lost when the browser is closed. |
   | HttpOnly Flag | When enabled, this option prevents a script running in the browser from accessing cookies. HttpOnly Flag is only available in the INSERT mode. |
   | Secure Flag | When enabled, this option causes web browsers to send cookies over https only. Secure Flag is only available in the INSERT mode. |
   | Max Idle Time | Enter the time in seconds that the cookie type can be idle before a cookie expires. |
   | Max Cookie Age | For the session cookie type, enter the time in seconds a cookie is available. |
   | Tags | Enter tags to make searching easier. You can specify a tag to set a scope of the tag. |
5. Select Generic to add a generic persistence profile and enter the profile details. 

   Option | Description || Name and Description | Enter a name and a description for the Source IP persistence profile. |
   | Share Persistence | Toggle the button to share the profile among virtual servers. |
   | Persistence Entry Timeout | Enter the persistence expiration time in seconds. The load balancer persistence table maintains entries to record that client requests are directed to the same server.  The very first connection from new client IP is load balanced to a pool member based on the load balancing algorithm. NSX will store that persistence entry on the LB persistence-table which is viewable on the Edge Node hosting the T1-LB active via the CLI command:get load-balancer <LB-UUID> persistence-tables.  - When there are connections from that client to the VIP, the persistence entry is kept. - When there are no more connections from that client to the VIP, the persistence entry begins the timer count down specified in the "Persistence Entry Timeout" value. If no new connection from that client to the VIP is made before the timer expires, the persistence entry for that client IP is deleted. If that client comes back after the entry is deleted, it will be load balanced again to a pool member based on the load balancing algorithm. |
   | HA Persistence Mirroring | Toggle the button to synchronize persistence entries to the HA peer. |
   | Tags | Enter tags to make searching easier. You can specify a tag to set a scope of the tag. |