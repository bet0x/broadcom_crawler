---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/distributed-load-balancer/run-traceflow-on-distributed-load-balancer.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Run Traceflow on Distributed Load Balancer
---

# Run Traceflow on Distributed Load Balancer

Run Traceflow between virtual machines or interfaces where Distributed Load Balancer
is enforced and the Distributed Load Balancer virtual IP address (VIP).

Use Traceflow for debugging purposes, when:

- On a client guest VM, where a
  Distributed Load Balancer service is applied, if the communication is lost
  between the guest VMs to Distributed Load Balancer.
- Or when guest VMs sending
  east-west traffic to another VM in the network drops.

1. With admin privileges, log in
   to NSX Manager.
2. Navigate to the Plan
   & Troubleshoot tab, and click
   Traceflow.
3. Enter source (for example, virtual machine where Distributed Load Balancer is
   enforced) and destination (Distributed Load Balancer VIP).
4. Click
   Trace.

   ![Packet flow between virtual machines where Distributed Load
                                   Balancer is enforced.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/6dd45ffd-807f-4a3a-a5cc-796faca82248.original.png)
5. View results.

   - As DLB is not based on rules, if Distributed Load Balancer drops a
     packet, there are not rule IDs that show up in the traceflow output
     details.
   - If Distributed Load Balancer and DFW services are applied to a client
     virtual machine, a member of a group, first Distributed Load Balancer
     service is applied followed by DFW rules service.