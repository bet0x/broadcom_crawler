---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/distributed-load-balancer/create-a-server-pool.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create a Server Pool for Distributed Load Balancer
---

# Create a Server Pool for Distributed Load Balancer

Create a load balancer pool to include virtual machines that consume DLB
services.

- Create a VM group that consumes
  DLB service.
- Create and attach a DLB
  instance to a VM group.

This task can be done both from the NSX
UI and NSX API.

The API command to create a DLB pool is
PUT
https://<NSXManager\_IPaddress>/policy/api/v1/infra/lb-pools/<lb-pool-id>

1. With admin privileges, log in
   to NSX Manager.
2. Go to NetworkingLoad BalancingServer Pools.
3. Click Add Server Pool.
4. Enter values in these fields.

   Field | Description || Name | Enter name of the DLB pool. |
   | Algorithm | Weighted Round Robin, Round Robin, Weighted Least Connection, Least Connection and IP Hash are the supported algorithms. Since Distributed Load Balancer runs locally on each ESX server, these algorithms are local to each ESX server. There is no synchronization of load balancing connection information between different ESX servers of a cluster.  - Weighted   Round Robin: Use this algorithm to send   connections to pool members based on the weights assigned to   each pool member. For example, if you assign pool member A with   weight 3, pool member B with weight 2 and pool member C with   weight 1, then out of a total of 6 client connections, pool   member A receives 3 connections, pool member B receives 2   connections and pool member C receives 1 connection. - Round   Robin: Use this algorithm to send equal number   of connections to each pool member. - Least   Connection: Use this algorithm so that a pool   member with the least number of active connections. Each pool   member is configured to a slow start (Slow Start is set to   True). When it receives connections, the status of the pool   member is set to Slow Start is False. - Weighted   Least Connection: Use this algorithm, to send   connections to pool members based on the weights assigned to   each pool member. - IP Hash: Use this algorithm to send   connections based on the hash of IP addresses. Do not use   IP Hash if you want to persist   connections to the same pool member even after the number of   pool members change. |
   | Members/Group | Click Select Members and on the Configure Server Pool Members window, do one of the following:  - Select   Enter individual members. To add   a new member, click Add Member and   enter values in the mandatory fields. - Select   Select a group and Add   Group or select an existing group. To add a new   group, enter values in these fields.    - Name   - Compute Members: Click     Set Members to add a group     that includes all the pool members.   - IP Revision Filter: Both     IPv4 and IPv6 are supported.   - Port: Default port for all     the dynamic pool members. |
   | SNAT Translation Mode | Set this field to Disabled state. SNAT translation is not supported in a Distributed Load Balancer. |
5. Click Save.

Server pool members are added for the
Distributed Load Balancer.

See [Create a Virtual Server with a Fast TCP or UDP Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/distributed-load-balancer/create-a-virtual-server-with-a-fast-tcp-profile.html#GUID-2ca02fb3-ec04-4d58-bd34-69ea51ce46a8-en).