---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/designing-and-sizing-virtual-san-fault-domains.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Designing and Sizing vSAN Fault Domains 
---

# Designing and Sizing vSAN Fault Domains

vSAN fault domains can spread redundancy components across the servers in separate computing racks. In this way, you can protect the environment from a rack-level failure such as loss of power or connectivity.

## Fault Domain Constructs

vSAN requires at least three fault domains to support Failures to tolerate (FTT) of 1. Each fault domain consists of one or more hosts. Fault domain definitions must acknowledge physical hardware constructs that might represent a potential zone of failure, for example, an individual computing rack enclosure.

If possible, use at least four fault domains. Three fault domains do not support certain data evacuation modes, and vSAN is unable to reprotect data after a failure. In this case, you need an additional fault domain with capacity for rebuilding, which you cannot provide with only three fault domains.

If fault domains are enabled, vSAN applies the active virtual machine storage policy to the fault domains instead of the individual hosts.

Calculate the number of fault domains in a cluster based on the FTT attribute from the storage policies that you plan to assign to virtual machines.

```
number of fault domains = 2 * FTT + 1
```

If a host is not a member of a fault domain, vSAN interprets it as a stand-alone fault domain.

## Using Fault Domains Against Failures of Several Hosts

Consider a cluster that contains four server racks, each with two hosts. If the Failures to tolerate is set to one and fault domains are not enabled, vSAN might store both replicas of an object with hosts in the same rack enclosure. In this way, applications might be exposed to a potential data loss on a rack-level failure. When you configure hosts that could potentially fail together into separate fault domains, vSAN ensures that each protection component (replicas and witnesses) is placed in a separate fault domain.

If you add hosts and capacity, you can use the existing fault domain configuration or you can define fault domains.

For balanced storage load and fault tolerance when using fault domains, consider the following guidelines:

- Provide enough fault domains to satisfy the Failures to tolerate that are configured in the storage policies.

  Define at least three fault domains. Define a minimum of four domains for best protection.
- Assign the same number of hosts to each fault domain.
- Use hosts that have uniform configurations.
- Dedicate one fault domain of free capacity for rebuilding data after a failure, if possible.