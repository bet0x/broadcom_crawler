---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/load-balancing.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Automation Load Balancing Design
---

# VCF Automation Load Balancing Design

VCF Automation runs within a Kubernetes-based container environment. The native load balancer is the default automatically configured load balancer for both the simple and highly available deployment models.

Note: This section does not cover load balancing for subsidiary functions, such as:

- Workload load balancing
- Load balancing of single sign-on solutions such as VMware Identity Broker
- vSphere Supervisors

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/a0980e9f-3b61-482c-bcee-3929a53105f4.original.png)

If an external load balancer is used, it is an optional post-deployment manual configuration. The external load balancer points to the native load balancer as the ingress point for VCF Automation.

![](/content/dam/broadcom/techdocs/us/en/dita/vmware/vcf/vcf-90/vcf-platform/images/VCFA-SimpleHAcombined-External-LB-v2.png)

| Default Load Balancer | Additional Load Balancer Options |
| --- | --- |
| Native Load Balancer | Can add external, 3rd-party load balancer in front of native load balancer  External, 3rd-party load balancers include VMware Avi Load Balancer |