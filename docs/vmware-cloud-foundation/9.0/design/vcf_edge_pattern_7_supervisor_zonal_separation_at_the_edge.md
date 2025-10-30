---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-edge(1)/supervisor-zonal-separation-at-the-edge.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Edge Pattern 7: Supervisor Zonal separation at the Edge
---

# VCF Edge Pattern 7: Supervisor Zonal separation at the Edge

Designing edge locations with vSphere Supervisor into distinct logical zones (e.g., Control Plane Zone, Worker Zone) for improved resource isolation, security, and resilience of the workloads.

VCF Edge Pattern 7: Supervisor Zonal separation at the Edge

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ebd2f3d5-1ed8-4d4f-bd93-074afe10a878.original.png)

| Design Attributes | Details |
| --- | --- |
| Management at the Edge Location | VCF Operation, SDDC Manager, vCenter, VCF Automation, and NSX are located within the same physical location as the edge sites.  Provides localized management, reducing latency for management operations and potentially improving resilience against WAN connectivity issues. |
| VCF Instance with single domain and multiple clusters | Both management and edge workload clusters are managed by one VCF domain and one vCenter. |
| Supervisor Cluster | Supervisor is enabled in the vSphere environment at each edge site. Enables the deployment and management of Kubernetes workloads alongside traditional virtual machines (VMs) directly at the edge, supporting modern, containerized applications. |
| Zonal Separation | Each edge site is further divided into Control Plane Zone and Workload Zone. Provides logical isolation and resource separation for critical control plane components and application workloads within each physical site, enhancing stability and security.  The Supervisor's Control Plane VMs reside within the dedicated "Control Plane Zone" at each site. Virtual machines and applications running workloads and acting as Kubernetes worker nodes reside within the dedicated "Worker Zone" at each site. |
| 2 Host Cluster with External Storage | Both Control Plane and Worker Zones at each site running on separate 2-host clusters with external storage. |

| **Best Fit Scenarios** |
| --- |
| **Organizations Requiring Strong Local Control and Security:** Environments where strict local control over the infrastructure and data is paramount, and minimizing external dependencies is a key requirement. |

This design can be implemented with a VCF Instance with single workload domain or multiple domain and clusters inside the workload domain as described in Pattern 6 above.