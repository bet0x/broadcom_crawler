---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/setting-up-load-balancer-components/setting-up-virtual-server-components/add-a-persistence-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Persistence Profile
---

# Add a Persistence Profile

To ensure stability of stateful applications, load balancers implement persistence which directs all related connections to the same server. Different types of persistence are supported to address different types of application needs.

Some applications maintain the server state such as, shopping carts. Such state can be per client and identified by the client IP address. Applications can access or modify this state while processing subsequent related connections from the same client.

The source IP persistence profile tracks sessions based on the source IP address. When a client requests a connection to a virtual server that enables the source address persistence, the load balancer checks if that client was previously connected, and if so, returns the client to the same server. If not, the load balancer selects the server pool member based on the pool load balancing algorithm. Source IP persistence profile is used by Layer 4 virtual servers.

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
4. Select Generic to add a generic persistence profile and enter the profile details. 

   Option | Description || Name and Description | Enter a name and a description for the Source IP persistence profile. |
   | Share Persistence | Toggle the button to share the profile among virtual servers. |
   | Persistence Entry Timeout | Enter the persistence expiration time in seconds. The load balancer persistence table maintains entries to record that client requests are directed to the same server.  The very first connection from new client IP is load balanced to a pool member based on the load balancing algorithm. NSX will store that persistence entry on the LB persistence-table which is viewable on the Edge Node hosting the T1-LB active via the CLI command:get load-balancer <LB-UUID> persistence-tables.  - When there are connections from that client to the VIP, the persistence entry is kept. - When there are no more connections from that client to the VIP, the persistence entry begins the timer count down specified in the "Persistence Entry Timeout" value. If no new connection from that client to the VIP is made before the timer expires, the persistence entry for that client IP is deleted. If that client comes back after the entry is deleted, it will be load balanced again to a pool member based on the load balancing algorithm. |
   | HA Persistence Mirroring | Toggle the button to synchronize persistence entries to the HA peer. |
   | Tags | Enter tags to make searching easier. You can specify a tag to set a scope of the tag. |