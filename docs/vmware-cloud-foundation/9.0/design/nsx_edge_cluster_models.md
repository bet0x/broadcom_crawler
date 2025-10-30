---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/nsx-edge-cluster-models.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > NSX Edge Cluster Models
---

# NSX Edge Cluster Models

VMware Cloud Foundation supports multiple NSX Edge Cluster Models, you determine the form factor, number of nodes and placement according to the requirements for network services in a workload domain. NSX Edge nodes can be shared across workload domains where such workload domain shares the same NSX Manager cluster.

An NSX Edge node is an appliance that provides centralized networking services which cannot be distributed to hypervisors. Some services, such as Tier-0 gateways, are limited to a single instance per NSX Edge node. However, multiple instances of most services can coexist in these nodes.

## NSX Edge Form Factor

An NSX Edge node can be deployed as a virtual appliance, or installed on bare-metal hardware. The NSX Edge node on bare-metal hardware can have better performance capabilities at the expense of more challenging deployment and limited deployment topology use cases.

NSX Edge Form Factors in VMware Cloud Foundation



| Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| NSX Edge Virtual Appliance | - Can be deployed by using vCenter or NSX Manager. - Lifecycled by using VCF Operations. - Supports four (4) data path virtual NICs. | - Automated password management by using VCF Operations. - Protected by vSphere HA. - Can be recovered across Availability Zones via vSphere HA. - Easy to scale up by modifying the specification of the virtual appliance. - Provides sufficient performance for most scenarios. | Workloads with small packet size might not have the best performance. |
| NSX Edge Bare-Metal Appliance | - Physical server where the NSX Edge software is installed by mounting the installation ISO file or via PXE. - After the image installation, it requires manual registration to NSX Manager. - Workload domain upgrades include NSX Edge bare metal nodes. - Supports up to 16 data path physical interfaces. | - Ability to consume the bandwidth of multiple 100G interfaces. - Workloads with small packet size might have better performance. - Independent from ESX lifecycle management. | - Has hardware compatibility requirements (network interface cards and CPUs). - Requires individual hardware lifecycle management and monitoring of failures, firmware and drivers. - Manual password management. - Must be manually deployed and registered to NSX Manager. |

## NSX Edge Cluster Models

NSX Edge nodes are grouped in one or more NSX Edge clusters, representing a pool of capacity for NSX services.

NSX Edge Cluster Models in VMware Cloud Foundation



| Deployment Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| Host fault tolerant | - Suited to single Availability Zone configurations. - Leverages the Single-Rack Cluster Model. - Supports virtual appliance or bare-metal form factor. | - Allows for the minimal footprint. - Allows for recovery after host failure events. - Supported all workload domains. | - No protection against a rack failure. - North-south throughput limited to physical fabric top of rack switch uplinks in a single rack. |
| Rack fault tolerant | - Suited to single Availability Zone configurations. - Leverages:    - Multiple instances of the Single-Rack Cluster Model (preferred). Or    - Layer 3 or Layer 2 Multi-Rack Cluster Model. - Supports virtual appliance or bare-metal form factor. | - As per cluster model chosen. - Higher north-south throughput scalability across multiple racks. - Independent storage (vSAN) for each rack when using multiple Single-Rack Cluster Models. | - As per Cluster Model chosen. - Requires additional resources to support multiple clusters deployed in or across different racks with independent storage (vSAN). - Physical fabric dependency if using a single Layer 2 Multi-Rack Cluster Model |
| Availability Zone fault tolerant (based on NSX Edge Node High Availability) | - Suited to dual Availability Zone configurations. - Leverages    - Multiple instances of the Single-Rack Cluster Model. or    - Stretched Cluster Model.  - Supports virtual appliance or bare-metal form factor. | - Fast network failover across Availability Zones. - No dependency on physical fabric. - Maintain optimal fault isolation between Availability Zones. | - Dependency on physical fabric, if maintaining symmetric routing is required. - Stretch cluster model usage implies common datastore supporting NSX Edge cluster across Availability Zones. |
| Availability Zone fault tolerant (based on vSphere HA recovery) | - Suited to dual Availability Zone configurations. - Leverages Stretched Cluster Model. - Supports virtual appliance form factor only. | Symmetric routing in and out of the virtual network. | - Slow network failover across Availability Zones. - Dependency on physical fabric to extend uplink VLANs, edge TEP VLAN, and edge Management VLANs. |