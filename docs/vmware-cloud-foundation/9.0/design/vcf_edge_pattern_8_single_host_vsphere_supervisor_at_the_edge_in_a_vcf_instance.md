---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-edge(1)/single-host-vsphre-supervisor-at-the-edge-in-a-vcf-instance.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Edge Pattern 8: Single Host vSphere Supervisor at the Edge in a VCF Instance
---

# VCF Edge Pattern 8: Single Host vSphere Supervisor at the Edge in a VCF Instance

VCF Edge Pattern 8: Single Host vSphere Supervisor at the Edge in a VCF Instance

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8537afb0-85ce-46fc-bdb0-b337c3222893.original.png)

This design pattern, focuses on deploying a highly efficient and compact vSphere Supervisor footprint at remote or edge locations. Single host leverages vSphere Supervisor to bring Kubernetes capabilities directly to resource-constrained environments, while maintaining centralized management from a core VCF instance.

| Design Attributes | Details |
| --- | --- |
| Single ESXi Host per Site | Each edge location is built upon a single physical ESXi server. Emphasizing a minimal hardware footprint. |
| vSphere Supervisor | vSphere Supervisor is enabled on the host which enables the deployment and management of Kubernetes workloads directly on the ESXi host. This includes the deployment of a "Control Plane VM" for the Supervisor functionality. |
| Centralized VCF Management | A VCF Fleet (comprising VCF Operation, VCF Automation, vCenter, and NSX) resides at a central data center or management location. Central vCenter instance manages the distributed edge sites. |
| Single Cluster Host Deployment | It is a manual process within the vCenter to create a cluster and add the host. |
| VSphere Supervisor Network | vSphere Distributed Switch (VDS) is used for vSphere Supervisor management and workload network |
| HA Admission control | vSphere HA is enabled on the cluster however, to make vSphere Supervisor to work, we have disabled HA Admission control in the cluster level in vCenter. |
| Storage Options | Only shared storage or local storage supported. |
| Network Connectivity | - Bandwidth**:** Aim for 1 Gbps or higher for efficient VM or container image image transfer. A minimum of 100 Mbps might be acceptable for smaller image s or less frequent deployments, but it will be slow. - Latency: Keep latency below 100 ms for a smooth management experience. While deployments might complete with higher latency, the user experience will degrade. |

To support single node vSphere Supervisor deployment, you must disable HA Admission Control on the vSphere Cluster in vCenter.

| Best Fit Scenarios |
| --- |
| - Numerous Far Edge Locations: Such as retail stores, bank branches, quick-service restaurants, remote industrial sites, or cellular towers, where space and IT staff are limited. - Resource-Constrained Environments: Locations where deploying multiple servers or complex networking is not feasible due to physical limitations or cost. - Applications Requiring Ultra-Low Latency: Workloads like IoT data ingestion and real-time analytics, AI/ML inference at the edge, or local POS systems that demand immediate responses. - High Volume of Small Workloads: Deployments where many small, independent applications need to run close to the data source or end-user. - Simplified Operations for Distributed Deployments: Organizations looking to standardize and automate the deployment and ongoing management of a large fleet of edge sites from a central location. |

| Benefits | Implications |
| --- | --- |
| **Minimized Hardware Footprint:** Significantly reduces the amount of physical hardware needed at each edge site.  **Lowers CapEx** (capital expenditure) for hardware, power, cooling, and space.  **Reduced Operational Overhead:** Simplifies local IT management at the edge due to fewer components. Leverages centralized VCF management for automated lifecycle operations (upgrades, patching), reducing the need for on-site IT staff.  **Optimized for Edge Workloads:** Enables deployment of cloud-native (Kubernetes) and traditional VM workloads directly at the edge. Facilitates ultra-low latency processing and data ingestion close to the source. | **Limited High Availability/Resilience:** A single ESXi host means a single point of failure. If the host goes down, all workloads at that specific edge site become unavailable. Requires robust strategies for application-level resilience or rapid recovery from a central location.  **Resource Constraints:** The single host limits the total compute, memory, and storage capacity available at the edge site. Careful sizing and workload placement are critical to avoid resource contention.  **Storage Dependency:** Reliance on local storage or direct-attached storage means storage failure directly impacts the site.  **Connectivity Criticality:** The WAN link to the central VCF Management Cluster is crucial for management, monitoring, and lifecycle operations. Latency and bandwidth limitations on the WAN as described in the design requirement  **No vMotion for Local HA:** With only one host, vMotion cannot be used for high availability within the edge site itself. If a host fails, VMs cannot automatically migrate to another host. |

For multi-node VKS clusters deployed at the edge, the resilience of even localized workloads is significantly dependent on central vCenter management. Should a Kubernetes pod crash or its VKS worker node fail, the Kubernetes cluster runtime will automatically attempt to restart the pod. However, if that pod utilizes a persistent volume and needs to be restarted on an alternative VKS worker node within the cluster, the underlying vSphere Supervisor, which orchestrates the VKS cluster, must establish communication with vCenter Server to facilitate the necessary volume detach and attach operations between the nodes. **Therefore, maintaining dedicated and stable connectivity to vCenter Server is paramount.** Without this vital connection, the vSphere Supervisor is unable to coordinate with vCenter to provision resources or orchestrate the recovery of the pod, ultimately preventing the affected pod service from coming back online.