---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/distributed-load-balancer/create-and-attach-a-distributed-load-balancer-instance.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create and Attach a Distributed Load Balancer Instance
---

# Create and Attach a Distributed Load Balancer Instance

Unlike a central load balancer, a Distributed Load Balancer (DLB) instance is
attached to virtual interfaces of a VM group.

- Add a policy group consisting
  of VMs. For example, such a VM group can be related to the App tier that
  receives requests from a VM on the Web-tier.

At the end of the procedure a DLB
instance is attached to the virtual interfaces of a VM group. It is only possible to
create and attach a DLB instance through API commands.

1. Run Put
   /policy/api/v1/infra/lb-services/<mydlb>.

   {

   "connectivity\_path" :
   "/infra/domains/default/groups/<clientVMGroup>",

   "enabled" : true,

   "size" : "DLB",

   "error\_log\_level" : "Debug",

   "access\_log\_enabled" :
   false,

   "resource\_type" :
   "LBService",

   "display\_name" : "mydlb"

   }

   Where,
   - connectivity\_path:
     - If the
       connectivity path is set to Null or
       Empty, the DLB instance is not
       applied to any transport nodes.
     - If the
       connectivity path is set ALL, all
       virtual interfaces of all transport nodes are bound to the
       DLB instance. One DLB instance is applied to all the virtual
       interfaces of the policy group.
   - size:
     Set to value DLB. As each application or virtual
     interface gets an instance of DLB, there is just a single size form
     factor of the DLB instance.
   - enabled: By default, the created DLB instance
     is enabled. You cannot disable the DLB instance.
   - error\_log\_level: Supported levels are
     Debug, Error, and
     Info. By default, log level is set to
     Info. To get verbose logs, set the level to
     Debug.

   A DLB instance is created and attached to the VM group. The DLB instance
   created on the Web-tier is attached to all the virtual interfaces of the
   Web-tier VM group.

After creating a DLB instance, log in to
the NSX Manager, go to Networking -> Load Balancing -> Load Balancers. View details of the DLB instance.

Next, [Create a Server Pool for Distributed Load Balancer](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/distributed-load-balancer/create-a-server-pool.html#GUID-219e9fdb-8cdb-4498-9a77-5cf0b50d1500-en).