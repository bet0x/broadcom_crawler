---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/create-a-workload-domain-by-using-the-vcf-operations-api/deploy-a-l3-multi-rack-vsan-vi-workload-domain/disable-vsan-auto-policy-management.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Deactivate Auto Policy Management for vSAN ESA Cluster
---

# Deactivate Auto Policy Management for vSAN ESA Cluster

You cannot use auto policy management in a multi-rack cluster when using vSAN fault domains. This must be disabled if vSAN fault domains are configured for each rack.

1. In a Web browser, log in to the workload domain vCenter Server at https://<vcenter\_server\_fqdn>/ui as [[email protected]](/cdn-cgi/l/email-protection).
2. In the Hosts and clusters inventory, navigate to the multi-rack vSAN cluster.
3. On the Configure tab for the cluster, select vSANServices.
4. In the vSAN ESA pane, click Edit.
5. Toggle Auto-policy Management off and click Apply.