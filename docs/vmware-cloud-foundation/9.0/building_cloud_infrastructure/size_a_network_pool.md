---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/about-network-pools/sizing-a-network-pool.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Size a Network Pool
---

# Size a Network Pool

Properly sizing a network pool is critical to prevent future issues in the environment due to insufficient IP addresses. Care must be taken when defining the subnets for a network pool as the subnet cannot be changed after it is deployed. The scope of IP addresses used from the defined subnet can be limited by the definition of one or more inclusion ranges. Thus, it is recommended that you begin with defining a larger subnet than what is initially required and utilize the inclusion ranges to limit use. This will provide you the capability to grow with demand as needed.

You begin sizing a network pool by determining the number of ESX hosts that you will have in each vSphere cluster. The minimum number of ESX hosts varies based on the storage type and deployment model. A vSphere cluster can be expanded to the maximum number of ESX hosts supported by vCenter.

Allocate a minimum of one IP address per ESX host plus enough additional IP addresses to account for growth and expansion of the environment. Ensure that the subnet defined provides enough unused IP addresses and that appropriate inclusion ranges are defined. Note that some of the IP addresses within the subnet will be used for other purposes, such as defining the gateway address, firewalls, or other entities. Use care not to conflict with these addresses.

Here are some important considerations for determining the size of your network pool:

- Type of network architecture.
- Where the default gateway is created.
- Number of hosts that can be placed in each rack or layer-2 network domain.
- Number of hosts required in a vSphere cluster.
- Number of workload domains and cluster you plan on creating.