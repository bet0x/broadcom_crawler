---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/nic-teaming-failover-and-load-balancing/basic-nic-teaming.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Basic NIC Teaming 
---

# Basic NIC Teaming

Basic NIC teaming uses multiple physical uplinks, one vmknic, and a single switch.

vSphere NIC teaming uses multiple uplink adapters, called vmnics, which are associated with a single virtual switch to form a team. This is the most basic option, and you can configure it using a standard vSphere standard switch or a vSphere distributed switch.

![Basic NIC teaming](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/5c1141be-8fbd-4820-a96d-9c60ceff5db1.original.png)

## Failover and Redundancy

vSAN can use the basic NIC teaming and failover policy provided by vSphere.

NIC teaming on a vSwitch can have multiple active uplinks, or an Active/Standby uplink configuration. Basic NIC teaming does not require any special configuration at the physical switch layer.

vSAN does not use NIC teaming for load balancing.

A typical NIC teaming configuration has the following settings. When working on distributed switches, edit the settings of the distributed port group used for vSAN traffic.

- Load balancing: Route based on originating virtual port
- Network failure detection: Link status only
- Notify switches: Yes
- Failback: Yes